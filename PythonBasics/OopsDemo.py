class Calculator:
    num = 200  # class Variables

    def __init__(self, a, b):  # Syntax to create constructor

        self.firstNumber = a
        self.secondNumber = b
        print("i am under constructor")

    def GetData(self):
        print("Getdata Method")

    def sumation(self):
        return self.firstNumber + self.secondNumber


obj = Calculator(3, 4)  # Syntax to create object of the class
obj.GetData()
print(obj.num)
print(obj.sumation())
