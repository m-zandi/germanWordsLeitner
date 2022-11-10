class father:
    def __init__(self):
        pass
    def fatherFoot(self):
        print("father foot")
class son(father):
    # def __init__(self):
    #     pass
    def sonFoot(self):
        print(super().fatherFoot())
    
# print(son.sonFoot())
son().sonFoot()