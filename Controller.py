__author__ = "Rick Myers"


from View import GiftCardView
from Model import GiftCardModel
import sys


class GiftCardController(object):

    def __init__(self):
        self.model = GiftCardModel()
        self.view = GiftCardView()

    def handle(self, request=None):
        # todo just show the main menu at start
        if request is None:
            self.main_menu()
        elif request == "List Cards":
            cards = self.model.get_card_list()
            self.view.list_all_cards(cards)
            self.main_menu()
        elif request == "Add Card":
            self.model.add_card(self.view.add_a_card())
            self.main_menu()
        elif request == "Update Balance":
            self.model.update_balance(self.view.update_balance(self.model.get_card_list()))
            self.main_menu()
        elif request == "Exit":
            self.view.exit()
            sys.exit()

    def view_event(self, event):
        if event == "List Cards":
            request = event
        elif event == "Exit":
            request = event
        elif event == "Add Card":
            request = event
        elif event == "Update Balance":
            request = event
        self.handle(request)

    def main_menu(self):
        menu = self.model.get_main_menu()
        event = self.view.generate_main_menu(menu)
        self.view_event(event)


def main():
    request_handler = GiftCardController()
    request_handler.handle()


if __name__ == "__main__":
    main()
