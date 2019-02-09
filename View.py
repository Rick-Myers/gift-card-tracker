class GiftCardView(object):

    def __init__(self):
        pass

    def list_all_cards(self):
        print("list all cards")

    def add_a_card(self):
        print("add a card")

    def update_balance(self):
        print("update balance")

    def exit(self):
        print("Exiting")

    def generate_main_menu(self):
        #todo move to model, retrieve through controller
        testList = [
            {"List Cards":self.list_all_cards},
            {"Add Card":self.add_a_card},
            {"Update Balance":self.update_balance},
            {"Exit":self.exit}
        ]

        print("**Gift Card Tracker**")
        for index, value in enumerate(testList, 1):
            print ("[" + str(index) + "] " + str(list(value.keys())[0]))

#testA = GiftCardView()
#testA.generate_main_menu()
