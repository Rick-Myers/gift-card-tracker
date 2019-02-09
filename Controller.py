from View import GiftCardView
from Model import GiftCardModel


class GiftCardController(object):

    def __init__(self):
        self.model = GiftCardModel()
        self.view = GiftCardView()

    def handle(self, request=None):
        if request is None:
            menu = self.model.get_main_menu()
            self.view.generate_main_menu(menu)


def main():
    request_handler = GiftCardController()
    request_handler.handle()


if __name__ == "__main__":
    main()
