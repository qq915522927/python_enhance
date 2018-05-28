
quotes = ('A man is not complete until he is married. Then he is'
 'finished.', 'As I said before, I never repeat myself.',
 'Behind a successful man is an exhausted woman.', 
 'Black holes really suck...', 'Facts are stubborn'
 'things.')

class QuoteModel:
 def get_quote(self, n):
     try:
         value = quotes[n]
     except IndexError as err:
         value = 'Not found!'
     return value

class QuoteTerminalView:
    def show(self, quote):
        print(quote)


    def error(self, msg):
        print(msg)

    def select_quote(self):
        return input('quote index?')

class QuoteTerminalController:
    def __init__(self):
        self.model = QuoteModel()
        self.view = QuoteTerminalView()

    def run(self):
        valid_input = False
        while not valid_input:
            n = self.view.select_quote()
            try:
                n = int(n)

            except ValueError as err:
                self.view.error("Incorrect index")
            else:
                valid_input = True
        quote = self.model.get_quote(n)
        self.view.show(quote)


def main():
    controller = QuoteTerminalController()
    while True:
        controller.run()

if __name__ == '__main__':
    main()