#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        """
        Initialize the Cash Register.
        :param discount: Discount percentage applied at checkout.
        """
        self.total = 0
        self.discount = discount
        self.items = []
        self.last_transaction_amount = 0
        self.last_transaction_items = []

    def add_item(self, title, price, quantity=1):
        """
        Add an item to the cart.
        :param title: Name of the item.
        :param price: Price per unit.
        :param quantity: Number of units.
        """
        transaction_total = price * quantity
        self.total += transaction_total

        # Add multiple items
        new_items = [title for _ in range(quantity)]
        self.items.extend(new_items)

        # Track last transaction
        self.last_transaction_amount = transaction_total
        self.last_transaction_items = new_items

    def apply_discount(self):
        if self.discount > 0:
            discount_amount = self.total * (self.discount / 100)
            self.total = int(self.total - discount_amount)
            print(f"After the discount, the total comes to ${self.total}.")
        else:
            print("There is no discount to apply.")

    def get_items(self):
        """
        Return the list of items currently in the cart.
        """
        return self.items

    def void_last_transaction(self):
        """
        Void (remove) the last transaction.
        """
        if self.last_transaction_amount > 0:
            self.total -= self.last_transaction_amount
            for item in self.last_transaction_items:
                if item in self.items:
                    self.items.remove(item)
            self.last_transaction_amount = 0
            self.last_transaction_items = []


# Example usage
if __name__ == "__main__":
    register = CashRegister(discount=20)

    register.add_item("Shoes", 50, 2)
    register.add_item("Hat", 25, 1)
    print("Items:", register.get_items())
    print("Total before discount:", register.total)

    print(register.apply_discount())
    print("Total after discount:", register.total)

    register.void_last_transaction()
    print("Items after void:", register.get_items())
    print("Total after void:", register.total)
    print("Last transaction amount:", register.last_transaction_amount)