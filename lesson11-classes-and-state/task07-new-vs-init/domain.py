"""MiniERP domain layer: real classes for the catalog.

Earlier phases carried a product as a bare tuple or a dict and passed it to free
functions. This phase makes it an object: a class that bundles the data (sku, name,
price) with the behavior that belongs to it (labels, display, validation,
construction). Prices stay integer cents, never float -- the representation the
catalog and pricing engine already use.
"""


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
