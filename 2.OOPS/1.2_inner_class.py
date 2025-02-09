'''
Explains the python inner class concept
'''

class Outerclass:
    ''' Example for Outer - Inner class architecture '''

    def __init__(self):
        self.name = "Outerclass"
        self.inner = self.Innerclass() # attribute to the Inner class

    def show(self):
        print(f'It is: {self.name} ')

    # Inner class
    class Innerclass:
        def __init__(self):
            self.name = "Innerclass"

        def show(self):
            print(f'It is: {self.name}')

outerclass = Outerclass()
outerclass.show()
innerclass = outerclass.inner
innerclass.show()


