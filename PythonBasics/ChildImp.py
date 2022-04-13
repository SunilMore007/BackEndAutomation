from OopsDemo import Calculator


class ChildImplementation(Calculator):
    num2 = 100
    def __init__(self):
        Calculator.__init__(self, 1, 2)

    def getCompleteData(self):
        return self.num2 + self.num + self.sumation()

obj=ChildImplementation()
print(obj.getCompleteData())