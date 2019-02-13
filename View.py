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
        card_name = self._not_empty()
        card_balance = self.input_validation("Enter balance: ",
                                             self._float_input,
                                             "Not an number! Try again.")
        card = GiftCard(card_name, card_balance)
        return card

    def delete_a_card(self, cards):
        if len(cards) > 0:
            os.system('cls')
            title = "**Gift Card Tracker - Add Card**"
            print(title + "\n" + "-" * len(title))
            x = [y for y in cards.keys()]
            for index, value in enumerate(x, 1):
                print("[" + str(index) + "] " + value)
            card_choice = self.menu_choice(x)
            return card_choice
        else:
            print("You need to add some cards first!")
            return False

    def update_balance(self, cards):
        if len(cards) > 0:
            # todo implement 3 letter search after 10 cards instead of listing all?
            title = "**Gift Card Tracker - Update balance**"
            print(title + "\n" + "-" * len(title))
            x = [y for y in cards.keys()]
            for index, value in enumerate(x, 1):
                print("[" + str(index) + "] " + value)
            card_choice = self.menu_choice(x)
            money_spent = self.input_validation("Enter money spent: ",
                                                self._float_input,
                                                "Not an number! Try again.")
            return card_choice, money_spent
        else:
            print("You need to add some cards first!")
            return False

    def exit(self):
        print("Exiting")
        os.system('cls')

    def generate_main_menu(self, menu):
        title = "**Gift Card Tracker - Main Menu**"
        print("\n" + title + "\n" + "-" * len(title))
        for index, value in enumerate(menu, 1):
            print("[" + str(index) + "] " + value)
        view_event = self.menu_choice(menu)
        return view_event

    def menu_choice(self, menu):
        user_choice = self.input_validation("Choose an option: ",
                                            self._int_input,
                                            "Not an integer! Try again.")
        while 1 > int(user_choice) or int(user_choice) > len(menu):
            user_choice = self.input_validation("Choose from menu - [1-{}]: ".format(len(menu)),
                                                self._int_input,
                                                "Not an integer! Try again.")
        return menu[user_choice-1]

    def input_validation(self, message, type_check, error):
        while True:
            try:
                user_input = type_check(message)
            except ValueError:
                print(error)
                continue
            else:
                return user_input
                break

    def _float_input(self, message):
        return float(input(message))

    def _int_input(self, message):
        return int(input(message))

    def _not_empty(self):
        while True:
            try:
                user_input = input("Enter a card name: ")
            except SyntaxError:
                print("Enter a name for your card.")
                continue
            else:
                return user_input
                break


