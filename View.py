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

    def generate_main_menu(self, menu):
        print("**Gift Card Tracker**")
        for index, value in enumerate(menu, 1):
            print("[" + str(index) + "] " + str(list(value.keys())[0]))
        # Alert the controller to prompt for a menu choice

# testA = GiftCardView()
# testA.generate_main_menu()
