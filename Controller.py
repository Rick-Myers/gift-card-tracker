__author__ = "Rick Myers"


from View import GiftCardView
from Model import GiftCardModel
import sys


class GiftCardController(object):
    """The GiftCardController displays the main menu and then receives
       user events from the view and updates the model. The main menu function
       names, and method to complete the request are stored in a dictionary.
       The GiftCardModel also holds a reference to the GiftCardModel and GiftCardView."""

    def __init__(self):
        """Initialize model, view and request main menu request dictionary."""
        self.model = GiftCardModel()
        self.view = GiftCardView()
        self.requests = {"List Cards": self._list_cards_request,
                         "Add Card": self._add_card_request,
                         "Delete Card": self._delete_card_request,
                         "Update Balance": self._update_balance_request,
                         "Exit": self._exit_request}

    def _list_cards_request(self):
        """Passes a list of all gift cards to the view."""
        cards = self.model.get_card_list()
        self.view.list_all_cards(cards)

    def _add_card_request(self):
        """Adds a card created in the view to the model and saves.."""
        self.model.add_card(self.view.add_a_card())

    def _delete_card_request(self):
        """Passes a list of all cards to the view to print a list for the user to
           choose a card to delete. That card is passed back to the model to be
           delete."""
        self.model.delete_card(self.view.delete_a_card(self.model.get_card_list()))

    def _update_balance_request(self):
        """Passes a list of all cards to the view to print a list for the user to
           choose a card to update its balance. It prompts for the amount that was
           spent and then passes that to the model. The model deducts the spent
           money and saves."""
        self.model.update_balance(self.view.update_balance(self.model.get_card_list()))

    def _exit_request(self):
        """Exits the app."""
        self.model.save_cards()
        self.view.exit()
        sys.exit()

    def handle(self, request=None):
        """Handles events that are passed back from the View."""
        if request is None:
            self.main_menu()
        else:
            self.requests[request]()
        self.main_menu()

    def view_event(self, event):
        """Listens for view events and passes those to the event handler handle()."""
        self.handle(event)

    def main_menu(self):
        """Creates the main menu by requesting it from the model and passing it
           to the view to be viewed. It then collects the user event and passes
           it to the controller handler handle()."""
        menu = self.model.get_main_menu()
        event = self.view.generate_main_menu(menu)
        self.view_event(event)


def main():
    request_handler = GiftCardController()
    request_handler.handle()


if __name__ == "__main__":
    main()
