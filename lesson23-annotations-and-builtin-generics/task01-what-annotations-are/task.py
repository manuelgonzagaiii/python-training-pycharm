"""What Annotations Really Are

MiniERP guided project — stage stub.

TODO(author): implement this stage.
Starter idea: # theory page only — shows live examples against existing MiniERP classes
class Product:  # already built in an earlier phase (Rich OOP)
    def __init__(self, sku, name, price):
        self.sku = sku
        self.name = name
        self.price = price

# At runtime Python ignores annotations; they live in __annotations__.
x: int = 5
print(__annotations__)        # {'x': <class 'int'>}
print(Product.__init__.__annotations__)  # {} — nothing yet to annotate
# A checker (mypy/pyright) is what turns annotations into errors.
"""

# Your code here.
