import os

class GiftCardView(object):

    def __init__(self):
        pass

    def list_all_cards(self, cards):
        os.system('cls')
        print("All Cards: ")
        for name, balance in cards.items():
            formatted_balance = '${:,.2f}'.format(balance)
            print(name + ": " + str(formatted_balance))

    def add_a_card(self):
        print("add a card")

    def update_balance(self):
        print("update balance")

    def exit(self):
        print("Exiting")

    def generate_main_menu(self, menu):
        print("**Gift Card Tracker**")
        for index, value in enumerate(menu, 1):
            print("[" + str(index) + "] " + value)
        view_event = self.menu_choice(menu)
        return view_event

    def menu_choice(self, menu):
        user_choice = self.input_validation("Choose an option: ")
        while 1 > user_choice > len(menu):
            user_choice = self.input_validation("Choose an option: ")
        return menu[user_choice-1]
        # print('You chose: {}'.format(user_choice))

    def input_validation(self, message):
        while True:
            try:
                user_input = int(input(message))
            except ValueError:
                print("Not an integer! Try again.")
                continue
            else:
                return user_input
                break

            # testA = GiftCardView()
# testA.generate_main_menu()
