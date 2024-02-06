class String:
    def __init__(self):
        self.input_string = ""

    def getString(self):
        self.input_string = input()

    def printString(self):
        print(self.input_string.upper())


if __name__ == "__main__":
    string = String()
    string.getString()
    string.printString()
