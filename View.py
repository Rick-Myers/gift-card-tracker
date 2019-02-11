__author__ = "Rick Myers"


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
        # prompt for a card
        # turn user input into 'card,balance' format
        # return card
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
        while 1 > int(user_choice) or int(user_choice) > len(menu):
            user_choice = self.input_validation("Choose from menu - [1-{}]: ".format(len(menu)))
        return menu[user_choice-1]

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

