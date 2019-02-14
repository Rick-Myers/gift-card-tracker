__author__ = "Rick Myers"


class GiftCard(object):
    """A gift card. For now it only stores the name of the card
       and the balance. It provides a function to update the balance
       if supplied with an amount of money to deduct from its current
       balance."""

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def get_name(self):
        return self.name

    def get_balance(self):
        return self.balance

    def update_balance(self, deduction):
        """Updates the balance by reducing the deduction from the current balance."""
        self.balance = float(self.balance) - deduction

    def print(self):
        """Prints the current balance in a money format."""
        formatted_balance = '${:,.2f}'.format(float(self.balance))
        print(self.name + ": " + str(formatted_balance))

