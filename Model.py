__author__ = "Rick Myers"


import os
from GiftCard import GiftCard


class GiftCardModel(object):

    def __init__(self):
        self.mainMenu = ["List Cards", "Add Card", "Update Balance", "Exit"]
        # todo rethink data structure? a list of cards to allow dupes?
        # todo fill list from file on init
        self.card_list = {"Subway": GiftCard("Subway", 20.00)}
        self.filename = 'cards.dat'

    def get_main_menu(self):
        return self.mainMenu

    def _get_append_write(self):
        if os.path.exists(self.filename):
            return 'a'
        return 'w'

    def get_card_list(self):
        if len(self.card_list) > 0:
            gift_cards = self.card_list
        else:
            if not os.path.exists(self.filename):
                return False

            with open(self.filename, 'r') as data_file:
                gift_cards = filter(lambda x: len(x) > 0, data_file.read().split('\n'))
            gift_cards = {x.split(',')[0]: GiftCard(x.split(',')[0], x.split(',')[1]) for x in list(gift_cards)}

        return gift_cards

    def save_cards(self):
        with open(self.filename, self._get_append_write()) as data_file:
            for card_name, balance in self.card_list.items():
                data_file.write("{},{}\n".format(card_name, balance.get_balance()))

    def add_card(self, card):
        self.card_list[card.get_name()] = GiftCard(card.get_name(), card.get_balance())
    # todo validate cards for any add failures and re-prompt through controller.
