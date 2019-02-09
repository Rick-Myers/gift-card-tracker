from View import GiftCardView


class GiftCardModel(object):

    def __init__(self):
        self.mainMenu = [
            {"List Cards": GiftCardView.list_all_cards},
            {"Add Card": GiftCardView.add_a_card},
            {"Update Balance": GiftCardView.update_balance},
            {"Exit": GiftCardView.exit}
        ]

    def get_main_menu(self):
        return self.mainMenu
