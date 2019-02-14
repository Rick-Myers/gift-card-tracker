__author__ = "Rick Myers"


import os
from GiftCard import GiftCard


class GiftCardModel(object):
    """The GiftCardModel holds the state of the stored gift card list,
       the main menu, and the file name used for saving. The data structure
       used to store the gift card list looks like {"Subway": GiftCard("Subway", 20.00)}.
       The GiftCardModel is also responsible for persistence."""

    def __init__(self):
        self.mainMenu = ["List Cards", "Add Card", "Delete Card", "Update Balance", "Exit"]
        self.filename = 'cards.dat'
        self.card_list = self._load_cards()

    def get_main_menu(self):
        return self.mainMenu

    def update_balance(self, spent):
        """Updates the card balance if there are actually cards to be updated."""
        if spent is not False:
            self.card_list[spent[0]].update_balance(spent[1])
            self.card_list[spent[0]].print()
            self.save_cards()

    def _load_cards(self):
        """Helper function to create an empty dictionary or reads in a file as
           a dictionary. This dictionary is the main list of all gift cards."""
        if not os.path.exists(self.filename):
            return {}
        else:
            with open(self.filename, 'r') as data_file:
                gift_cards = filter(lambda x: len(x) > 0, data_file.read().split('\n'))
            gift_cards = {x.split(',')[0]: GiftCard(x.split(',')[0], x.split(',')[1]) for x in list(gift_cards)}

        return gift_cards

    def get_card_list(self):
        """Returns the gift card list."""
        return self.card_list

    def save_cards(self):
        """Opens file self.filename and saves the file to the disk. The file is saved
           in a csv format."""
        with open(self.filename, 'w') as data_file:
            for card_name, balance in self.card_list.items():
                data_file.write("{},{}\n".format(card_name, balance.get_balance()))

    def add_card(self, card):
        """Adds a card to the card list. Makes sure there are no duplicates by adding
           a unique number to the card name."""
        count = 0
        temp = card.get_name()
        while temp in self.card_list.keys():
            count = count + 1
            temp = card.get_name() + "({})".format(str(count))
        card.name = temp
        self.card_list[card.get_name()] = GiftCard(card.get_name(), card.get_balance())
        self.save_cards()

    def delete_card(self, key):
        """Deletes the card from the card list if the key passed is valid."""
        if key is not False:
            del self.card_list[key]
            self.save_cards()
