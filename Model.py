__author__ = "Rick Myers"


import os
from GiftCard import GiftCard


class GiftCardModel(object):

    def __init__(self):
        self.mainMenu = ["List Cards", "Add Card", "Update Balance", "Exit"]
        # todo rethink data structure? a list of cards to allow dupes?
        self.card_list = {}
        self.filename = 'cards.dat'
        self.card_list = self.get_card_list()

    def get_main_menu(self):
        return self.mainMenu

    def _get_append_write(self):
        if os.path.exists(self.filename):
            return 'a'
        return 'w'

    def _get_read_write(self):
        if os.path.exists(self.filename):
            return 'r'
        return 'w'

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
        self.card_list[card.get_name()] = GiftCard(card.get_name(), card.get_balance())
        self.save_cards()
    # todo validate cards for any add failures and re-prompt through controller.

# example of current data structure
# self.card_list = {"Subway": GiftCard("Subway", 20.00)}


#Check if the current card list is empty or not.
    #if its empty, then we need to read from a file
        #check if a file exists
            #if the file exists, read in the contents
            #if it doesn't exist, create an empty file and make sure card list is set to empty dict