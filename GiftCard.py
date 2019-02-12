__author__ = "Rick Myers"


class GiftCard(object):

    # Maybe the cards are json?

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def get_name(self):
        return self.name

    def get_balance(self):
        return self.balance

    def update_balance(self, deduction):
        self.balance -= deduction

    def print(self):
        formatted_balance = '${:,.2f}'.format(float(self.balance))
        print(self.name + ": " + str(formatted_balance))


#card = GiftCard("Five Guys", 10.00)
#card_list = {"Subway": GiftCard("Subway", 20.00)}
#card_list["Subway"].print()
#card_list[card.get_name()] = GiftCard(card.get_name(), card.get_balance)
#print(card_list)
