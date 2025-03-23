#1
class ManipulateString:
    def __init__(self):
        self.text = ""

    def getString(self):
        self.text = input("введи строку: ")

    def printString(self):
        print(self.text.upper())


obj= ManipulateString()
obj.getString()
obj.printString()



