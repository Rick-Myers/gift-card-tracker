__author__ = "Rick Myers"


import os
from GiftCard import GiftCard


class GiftCardModel(object):

    def __init__(self):
        self.mainMenu = ["List Cards", "Add Card", "Delete Card", "Update Balance", "Exit"]
        self.card_list = {}
        self.filename = 'cards.dat'
        # todo create a helper function for this instead of using the model function
        self.card_list = self.get_card_list()

    def get_main_menu(self):
        return self.mainMenu

    def update_balance(self, x):
        if x is not False:
            self.card_list[x[0]].update_balance(x[1])
            self.card_list[x[0]].print()
            self.save_cards()

    def get_card_list(self):
        if len(self.card_list) > 0:
            gift_cards = self.card_list
        else:
            if not os.path.exists(self.filename):
                return {}

            with open(self.filename, 'r') as data_file:
                gift_cards = filter(lambda x: len(x) > 0, data_file.read().split('\n'))
            gift_cards = {x.split(',')[0]: GiftCard(x.split(',')[0], x.split(',')[1]) for x in list(gift_cards)}

        return gift_cards

    def save_cards(self):
        with open(self.filename, 'w') as data_file:
            for card_name, balance in self.card_list.items():
                data_file.write("{},{}\n".format(card_name, balance.get_balance()))

    def add_card(self, card):
        count = 0
        temp = card.get_name()
        while temp in self.card_list.keys():
            count = count + 1
            temp = card.get_name() + "({})".format(str(count))
        card.name = temp
        self.card_list[card.get_name()] = GiftCard(card.get_name(), card.get_balance())
        self.save_cards()

    def delete_card(self, key):
        del self.card_list[key]
        self.save_cards()

# example of current data structure
# self.card_list = {"Subway": GiftCard("Subway", 20.00)}
