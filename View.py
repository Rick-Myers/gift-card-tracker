__author__ = "Rick Myers"


import os
from GiftCard import GiftCard


class GiftCardView(object):
    """The GiftCardView is responsible for displaying the data that is held
       in the GiftCardModel. This was a first attempt at following the MVC
       model. The view will do some processing by taking user input throughout
       the app and validating it before sending it back to the GiftCardModel."""

    def __init__(self):
        pass

    @staticmethod
    def list_all_cards(cards):
        """Takes a list of GiftCards and displays them to the screen."""
        os.system('cls')
        title = "**Gift Card Tracker - All Cards**"
        print(title + "\n" + "-" * len(title))
        if len(cards) > 0:
            for card in cards.values():
                card.print()
        else:
            print("Gift Card queue is empty!")

    def add_a_card(self):
        """Prompts the user for a GiftCard() to be added to the list.
           Returns a card to be added to the GiftCardModel."""
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
        """Prompts the user to delete a card from the gift card list.
           The card that is chosen is deleted. If this option is chosen,
           a card must be delete."""
        if len(cards) > 0:
            os.system('cls')
            title = "**Gift Card Tracker - Delete Card**"
            print(title + "\n" + "-" * len(title))
            card_names = [y for y in cards.keys()]
            for index, value in enumerate(card_names, 1):
                print("[" + str(index) + "] " + value)
            card_choice = self.menu_choice(card_names)
            return card_choice
        else:
            print("You need to add some cards first!")
            return False

    def update_balance(self, cards):
        """Prompts the user for a card and then passes that card back to
           the GiftCardModel with the amount of money spent. The model will
           then deduct the money spent from the card and update the model."""
        if len(cards) > 0:
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

    @staticmethod
    def exit():
        print("Exiting")
        os.system('cls')

    def generate_main_menu(self, menu):
        """Prints the Main Menu. Returns the user's choice."""
        title = "**Gift Card Tracker - Main Menu**"
        print("\n" + title + "\n" + "-" * len(title))
        for index, value in enumerate(menu, 1):
            print("[" + str(index) + "] " + value)
        view_event = self.menu_choice(menu)
        return view_event

    def menu_choice(self, menu):
        """Validates menu choices to insure and integer is entered
           and that integer is between the range of the menu list.
           It then returns the user choice as a string."""
        user_choice = self.input_validation("Choose an option: ",
                                            self._int_input,
                                            "Not an integer! Try again.")
        while 1 > int(user_choice) or int(user_choice) > len(menu):
            user_choice = self.input_validation("Choose from menu - [1-{}]: ".format(len(menu)),
                                                self._int_input,
                                                "Not an integer! Try again.")
        return menu[user_choice-1]

    @staticmethod
    def input_validation(message, type_check, error):
        """Helper function that can validate both float and int based
           user inputs. It returns clean user input as user_input."""
        while True:
            try:
                user_input = type_check(message)
            except ValueError:
                print(error)
                continue
            else:
                return user_input

    @staticmethod
    def _float_input(message):
        """Validates input to be sure its a float."""
        return float(input(message))

    @staticmethod
    def _int_input(message):
        """Validates input to be sure its an int."""
        return int(input(message))

    @staticmethod
    def _not_empty():
        """Validates input to be sure something was actually entered."""
        while True:
            try:
                user_input = input("Enter a card name: ")
            except SyntaxError:
                print("Enter a name for your card.")
                continue
            else:
                return user_input



