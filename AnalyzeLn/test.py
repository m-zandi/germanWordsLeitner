import sys
sys.path.append( "../")

from main.base.Buttons import ButtonPer as Btn
from main.base.ButtonsA import ButtonAdmiPer as BtnA 



print(Btn().aboutBot)

class inherTest(Btn):
    def __init__(self):
        self.some = "hi"
        super().__init__()
        self.thisOne = self.beforeWordLeitBP
        # pass
    def someFunc(self):
        # print(self.this)
        print(self.thisOne)


class getValue(inherTest):
    def __init__(self):
        super().__init__()
        self.this = self.some
        self.this2 = self.yesDot
    def someFunc(self):
        # print(self.this)
        print(self.this2)
# getValue().someFunc()
# inherTest().someFunc()