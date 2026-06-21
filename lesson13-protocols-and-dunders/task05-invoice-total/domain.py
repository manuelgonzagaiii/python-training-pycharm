"""MiniERP domain layer: real classes for the catalog.

Earlier phases carried a product as a bare tuple or a dict and passed it to free
functions. This phase makes it an object: a class that bundles the data (sku, name,
price) with the behavior that belongs to it (labels, display, validation,
construction). Prices stay integer cents, never float -- the representation the
catalog and pricing engine already use.
"""
from decimal import Decimal
from functools import total_ordering


class Product:
    """A product in the catalog: a SKU, a display name, and a price in cents.

    Bundling data with behavior is the whole point of a class. Where a tuple needed
    a free function like label(product), a Product carries label() on itself, so the
    data and the code that understands it travel together.
    """

    def __init__(self, sku: str, name: str, price_cents: int) -> None:
        """Initialize a new product. `self` is the fresh instance; each assignment
        stores one argument as an attribute that lives on that specific object.
        """
        self.sku = sku
        self.name = name
        self.price_cents = price_cents

    def label(self) -> str:
        """A short human label, e.g. 'A-001 - Widget'."""
        return f"{self.sku} - {self.name}"

    # Class attributes: one shared copy for every Product, not stored per instance.
    CURRENCY = "USD"
    DEFAULT_TAX_RATE_BPS = 0  # basis points (1 bp = 0.01%); overridden per sale later

    def price_display(self) -> str:
        """The price as a currency string, e.g. 1500 -> '$15.00'.

        A method reaches the object's own data through self -- self.price_cents and
        the shared self.CURRENCY -- so the behavior lives on the product itself.
        """
        symbol = "$" if self.CURRENCY == "USD" else f"{self.CURRENCY} "
        return f"{symbol}{self.price_cents // 100}.{self.price_cents % 100:02d}"

    @classmethod
    def from_row(cls, row: tuple) -> "Product":
        """Alternate constructor: build a Product from a (sku, name, price_cents) row.

        A classmethod receives the class as `cls`, so calling cls(...) builds an
        instance of whatever class the method was called on -- the Pythonic way to
        offer more than one way to construct an object.
        """
        sku, name, price_cents = row
        return cls(sku, name, price_cents)

    @classmethod
    def from_dict(cls, data: dict) -> "Product":
        """Alternate constructor: build a Product from a mapping with sku/name/price_cents."""
        return cls(data["sku"], data["name"], data["price_cents"])

    @staticmethod
    def is_valid_sku(value: str) -> bool:
        """True if value is a non-empty SKU of letters, digits, and hyphens.

        A staticmethod takes neither self nor cls: it is a plain function namespaced
        on the class because it belongs there conceptually, but it needs no instance.
        """
        return bool(value) and all(ch.isalnum() or ch == "-" for ch in value)

    # SKU interning cache: one canonical instance per SKU (a later lesson swaps this
    # strong dict for a weakref registry so dropped products can be collected).
    _instances: dict[str, "Product"] = {}

    def __new__(cls, sku: str, name: str, price_cents: int) -> "Product":
        """Allocate the instance. __new__ runs BEFORE __init__ and decides which
        object to return; here it returns the existing object for a known SKU so the
        catalog never holds two different Products for the same SKU. __init__ then
        still runs and sets the fields.
        """
        if sku in cls._instances:
            return cls._instances[sku]
        instance = super().__new__(cls)
        cls._instances[sku] = instance
        return instance

    @property
    def price_dollars(self) -> Decimal:
        """The price as an exact Decimal number of dollars, computed from price_cents.

        A computed (read-only) property looks like an attribute -- callers write
        product.price_dollars, no parentheses -- but runs code each time, so it can
        never drift out of step with price_cents. Decimal keeps it exact; float would
        not.
        """
        return Decimal(self.price_cents) / 100

    @property
    def price_cents(self) -> int:
        """The price in cents. Reading goes through this getter; writing goes through
        the setter below, so the stored value is always validated."""
        return self._price_cents

    @price_cents.setter
    def price_cents(self, value: int) -> None:
        if value < 0:
            raise ValueError("price must not be negative")
        self._price_cents = value

    @property
    def discount_cents(self) -> int | None:
        """An optional per-product discount in cents, or None when unset."""
        return getattr(self, "_discount_cents", None)

    @discount_cents.setter
    def discount_cents(self, value: int) -> None:
        if value < 0:
            raise ValueError("discount must not be negative")
        self._discount_cents = value

    @discount_cents.deleter
    def discount_cents(self) -> None:
        """Clear the discount back to None (del product.discount_cents)."""
        self._discount_cents = None

    def __repr__(self) -> str:
        return f"Product(sku={self.sku!r}, name={self.name!r}, price_cents={self.price_cents})"

    def __str__(self) -> str:
        return self.label()

    def __eq__(self, other) -> bool:
        """Two products are equal when their SKUs match (the identifying field)."""
        if not isinstance(other, Product):
            return NotImplemented
        return self.sku == other.sku

    def __hash__(self) -> int:
        # Define __hash__ alongside __eq__: a class that overrides __eq__ but not
        # __hash__ becomes unhashable. Hash on the same field equality uses.
        return hash(self.sku)

    def __lt__(self, other) -> bool:
        """Order products by price, so sorted(products) ranks them cheapest first."""
        if not isinstance(other, Product):
            return NotImplemented
        return self.price_cents < other.price_cents


@total_ordering
class Money:
    """A monetary amount: integer minor units (cents) plus a currency code.

    Storing cents as an int keeps money exact -- no binary-float drift, the same rule
    the whole course follows. This is the plain-class version of Money; a later lesson
    re-expresses the identical idea as a frozen dataclass, but the representation
    (integer cents) never changes.
    """

    def __init__(self, cents: int, currency: str = "USD") -> None:
        self.cents = cents
        self.currency = currency

    @classmethod
    def from_dollars(cls, dollars, currency: str = "USD") -> "Money":
        """Build Money from a dollar amount given as a string or Decimal (never a
        float, so the cents are exact), e.g. Money.from_dollars("15.99")."""
        return cls(int(Decimal(str(dollars)) * 100), currency)

    @property
    def dollars(self) -> Decimal:
        """The amount as an exact Decimal number of dollars (1599 cents -> 15.99)."""
        return Decimal(self.cents) / 100

    def __repr__(self) -> str:
        return f"Money(cents={self.cents}, currency={self.currency!r})"

    def __str__(self) -> str:
        symbol = "$" if self.currency == "USD" else f"{self.currency} "
        sign = "-" if self.cents < 0 else ""
        whole, rem = divmod(abs(self.cents), 100)
        return f"{sign}{symbol}{whole}.{rem:02d}"

    def __format__(self, spec: str) -> str:
        """Render under format()/f-strings. Supported specs: '' or 'money' -> '$15.00',
        'full' -> '15.00 USD', 'cents' -> '1500'."""
        if spec in ("", "money"):
            return str(self)
        if spec == "full":
            sign = "-" if self.cents < 0 else ""
            whole, rem = divmod(abs(self.cents), 100)
            return f"{sign}{whole}.{rem:02d} {self.currency}"
        if spec == "cents":
            return str(self.cents)
        raise ValueError(f"unknown Money format spec: {spec!r}")

    def __eq__(self, other) -> bool:
        if not isinstance(other, Money):
            return NotImplemented
        return (self.cents, self.currency) == (other.cents, other.currency)

    def __hash__(self) -> int:
        """Hash on the same fields __eq__ compares, so equal Money hash equally and can
        be set members or dict keys. (Treat Money as immutable once created.)"""
        return hash((self.cents, self.currency))

    def __lt__(self, other) -> bool:
        if not isinstance(other, Money):
            return NotImplemented
        if self.currency != other.currency:
            raise ValueError("cannot compare Money of different currencies")
        return self.cents < other.cents

    def __add__(self, other) -> "Money":
        if not isinstance(other, Money):
            return NotImplemented
        if self.currency != other.currency:
            raise ValueError("cannot add Money of different currencies")
        return Money(self.cents + other.cents, self.currency)

    def __sub__(self, other) -> "Money":
        if not isinstance(other, Money):
            return NotImplemented
        if self.currency != other.currency:
            raise ValueError("cannot subtract Money of different currencies")
        return Money(self.cents - other.cents, self.currency)

    def __mul__(self, n: int) -> "Money":
        if not isinstance(n, int):
            return NotImplemented
        return Money(self.cents * n, self.currency)

    def __radd__(self, other) -> "Money":
        # Enables sum([...]) of Money, which starts from the int 0.
        if other == 0:
            return self
        return NotImplemented


class LineItem:
    """One line of an invoice: a product and a quantity. Its line_total is Money,
    composed from the product's price and the quantity."""

    def __init__(self, product: Product, quantity: int) -> None:
        self.product = product
        self.quantity = quantity

    @property
    def line_total(self) -> Money:
        """The line's money total: unit price times quantity, as Money."""
        return Money(self.product.price_cents) * self.quantity


class Invoice:
    """An invoice is a container of LineItems. Implementing the container dunders lets
    it behave like a built-in collection: len(), iteration, indexing, and `in`."""

    def __init__(self, lines: list[LineItem] | None = None) -> None:
        self.lines = list(lines) if lines else []

    def __len__(self) -> int:
        return len(self.lines)

    def __bool__(self) -> bool:
        # Without this, truthiness would fall back to __len__; defined explicitly here.
        return len(self.lines) > 0

    def __getitem__(self, index):
        return self.lines[index]

    def __iter__(self):
        return iter(self.lines)

    def __contains__(self, product) -> bool:
        """Support `product in invoice` by checking the lines' products."""
        return any(line.product == product for line in self.lines)

    @property
    def total(self) -> Money:
        """The grand total: every line_total summed, as Money. Starting the sum from
        Money(0) (not the default int 0) keeps an empty invoice's total a Money too."""
        return sum((line.line_total for line in self.lines), Money(0))

    def __str__(self) -> str:
        rendered = "\n".join(
            f"  {line.product.label()} x{line.quantity}  {line.line_total}"
            for line in self.lines
        )
        return f"Invoice:\n{rendered}\n  Total: {self.total}"
