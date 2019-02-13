__author__ = "Rick Myers"


import os
from GiftCard import GiftCard


class GiftCardView(object):

    def __init__(self):
        pass

    def list_all_cards(self, cards):
        os.system('cls')
        title = "**Gift Card Tracker - All Cards**"
        print(title + "\n" + "-" * len(title))
        if len(cards) > 0:
            for card in cards.values():
                card.print()
        else:
            print("Gift Card queue is empty!")

    def add_a_card(self):
        os.system('cls')
        title = "**Gift Card Tracker - Add Card**"
        print(title + "\n" + "-" * len(title))
        card_name = input("Enter a card name: ")
        card_balance = input("Enter balance: ")
        card = GiftCard(card_name, card_balance)
        return card

    def update_balance(self, cards):
        if len(cards) > 0:
            os.system('cls')
            title = "**Gift Card Tracker - Update balance**"
            print(title + "\n" + "-" * len(title))
            x = [y for y in cards.keys()]
            for index, value in enumerate(x, 1):
                print("[" + str(index) + "] " + value)
            card_choice = self.menu_choice(x)
            money_spent = self.currency_validation("Enter money spent: ")
            return card_choice, money_spent
        else:
            print("You need to add some cards first!")
            return False

    def exit(self):
        print("Exiting")

    def generate_main_menu(self, menu):
        title = "**Gift Card Tracker - Main Menu**"
        print("\n" + title + "\n" + "-" * len(title))
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

    def currency_validation(self, message):
        while True:
            try:
                user_input = float(input(message))
            except ValueError:
                print("Not an number! Try again.")
                continue
            else:
                return user_input
                break


