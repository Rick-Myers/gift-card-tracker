class GiftCardModel(object):

    def __init__(self):
        self.mainMenu = ["List Cards", "Add Card", "Update Balance", "Exit"]
        self.dummyList = {"Subway": 20.00, "Target": 10.00, "Five Guys": 5.34}

    def get_main_menu(self):
        return self.mainMenu

    def get_all_cards(self):
        return self.dummyList
