class Silly:

    @property
    def silly(self):
        "This is a silly property"
        print("You are getting silly")
        return self._silly

    @silly.setter
    def silly(self, value):
        print("You are making silly {}".format(value))
        self._silly = value

    @silly.deleter
    def silly(self):
        print("Whoah, you killed silly!")
        del self._silly


class AverageList(list):
    @property
    def average(self):
        return sum(self) / len(self)

a = AverageList([1,2,3,4])
print(a.average)
