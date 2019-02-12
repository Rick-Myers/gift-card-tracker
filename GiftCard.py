__author__ = "Rick Myers"


class GiftCard(object):

    # todo Maybe the cards are json?

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def get_name(self):
        return self.name

    def get_balance(self):
        return self.balance

    def update_balance(self, deduction):
        self.balance = float(self.balance) - deduction

    def print(self):
        formatted_balance = '${:,.2f}'.format(float(self.balance))
        print(self.name + ": " + str(formatted_balance))

