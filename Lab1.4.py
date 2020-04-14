class ProgressBar:
    def __init__(self, value, max=100):
        self.value = value
        self.max = max
    def addValue(self, value):
        self.value += value
        return value
    def subValue(self, value):
        self.value -= value
        return value
    def show(self):
        print(self.value, '/', self.max)

pb = ProgressBar(3)
while pb.max > pb.value:
    pb.show()
    pb.addValue(5)
pb = ProgressBar(100)

print()

while  pb.value > 0:
    pb.show()
    pb.subValue(10)
