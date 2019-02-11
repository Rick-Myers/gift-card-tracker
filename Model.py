__author__ = "Rick Myers"


import os


class GiftCardModel(object):

    # todo create a Card object, then store a list of Cards? Maybe the cards are json?
    def __init__(self):
        self.mainMenu = ["List Cards", "Add Card", "Update Balance", "Exit"]
        self.dummyList = {"Subway": 20.00, "Target": 10.00, "Five Guys": 5.34}
        self.filename = 'cards.dat'

    def get_main_menu(self):
        return self.mainMenu

    def _get_append_write(self):
        if os.path.exists(self.filename):
            return 'a'
        return 'w'

    def get_card_list(self):
        if not os.path.exists(self.filename):
            return False

        with open(self.filename, 'r') as data_file:
            gift_cards = filter(lambda x: len(x) > 0, data_file.read().split('\n'))
        gift_cards = {x.split(',')[0]: float(x.split(',')[1]) for x in list(gift_cards)}

        return gift_cards

    def save_cards(self, gift_cards):
        with open(self.filename, self._get_append_write()) as data_file:
            for card_name, balance in gift_cards.items():
                data_file.write("{},{}\n".format(card_name, balance))

    def add_card(self, card):
        with open(self.filename, self._get_append_write()) as data_file:
            data_file.write(card)
    # todo Instead of immediately saving the card to file, store in memory (add to dictionary) and write out on exit.
