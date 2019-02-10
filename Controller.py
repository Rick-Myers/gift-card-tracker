from View import GiftCardView
from Model import GiftCardModel


class GiftCardController(object):

    def __init__(self):
        self.model = GiftCardModel()
        self.view = GiftCardView()

    def handle(self, request=None):
        if request is None:
            menu = self.model.get_main_menu()
            event = self.view.generate_main_menu(menu)
            self.view_event(event)
        elif request == "List Cards":
            cards = self.model.get_all_cards()
            self.view.list_all_cards(cards)

    def view_event(self, event):
        if event == "List Cards":
            request = event
            self.handle(request)


def main():
    request_handler = GiftCardController()
    request_handler.handle()


if __name__ == "__main__":
    main()
