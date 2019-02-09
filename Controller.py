import sys
from View import GiftCardView
from Model import GiftCardModel

class GiftCardController(object):

	def __init__(self):
		self.model = GiftCardModel()
		self.view = GiftCardView()
	
	def handle(self, request):
		if (request == 'start'):
			self.view.generate_main_menu()
	
	
	

def main():
	request_handler = GiftCardController()
	request_handler.handle('start')

if __name__ == "__main__":
	main()