__author__ = "Rick Myers"
import os


class GiftCardModel(object):

    def __init__(self):
        self.mainMenu = ["List Cards", "Add Card", "Update Balance", "Exit"]
        self.dummyList = {"Subway": 20.00, "Target": 10.00, "Five Guys": 5.34}
        self.filename = 'cards.dat'

    def get_main_menu(self):
        return self.mainMenu

    # todo replace with persistence
    def get_all_cards(self):
        return self.dummyList

    def _get_append_write(self):
        if os.path.exists(self.filename):
            return 'a'
        return 'w'

    def get_card_list(self):
        if not os.path.exists(self.filename):
            return False

        with open(self.filename, 'r') as data_file:
            cards = data_file.read().split('\n')

        return cards
