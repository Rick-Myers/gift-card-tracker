__author__ = "Rick Myers"


from View import GiftCardView
from Model import GiftCardModel
import sys


class GiftCardController(object):

    def __init__(self):
        self.model = GiftCardModel()
        self.view = GiftCardView()
        self.requests = {"List Cards": self._list_cards_request,
                         "Add Card": self._add_card_request,
                         "Delete Card": self._delete_card_request,
                         "Update Balance": self._update_balance_request,
                         "Exit": self._exit_request}

    def _list_cards_request(self):
        cards = self.model.get_card_list()
        self.view.list_all_cards(cards)

    def _add_card_request(self):
        self.model.add_card(self.view.add_a_card())

    def _delete_card_request(self):
        self.model.delete_card(self.view.delete_a_card(self.model.get_card_list()))

    def _update_balance_request(self):
        self.model.update_balance(self.view.update_balance(self.model.get_card_list()))

    def _exit_request(self):
        self.model.save_cards()
        self.view.exit()
        sys.exit()

    def handle(self, request=None):
        if request is None:
            self.main_menu()
        else:
            self.requests[request]()
        self.main_menu()

    def view_event(self, event):
        self.handle(event)

    def main_menu(self):
        menu = self.model.get_main_menu()
        event = self.view.generate_main_menu(menu)
        self.view_event(event)


def main():
    request_handler = GiftCardController()
    request_handler.handle()


if __name__ == "__main__":
    main()
