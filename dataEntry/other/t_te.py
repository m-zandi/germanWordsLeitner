import pytest
from itertools import product
import itertools
from itertools import chain,repeat,islice,count
from collections import Counter
from test_entering import Db as db
# a = True
# b = 44
# x = a if False else b
# print(x)
# #44
# # x = len(a) if a<b else len(b)
# b = []
# if len(b) == 0:
#     print("b has no element")

# a = [1,2,4,5,6,7,8]
# b = [22,55,4,24,235,1,3,2,5,7,8]
# c = set(b)-set(a)
# print(f"{c = }")
# print(type(c))
# import openpyxl
# path = r"D:\project\WoerterbuchProject\mainV2\dataEntry\words.xlsx" 
# sheet = "orginal"
# wb = openpyxl.load_workbook(filename=path)
# # print(f"{wb.sheetnames}")
# # ws = wb.worksheets[0]
# # print(f"{ws}")
# mySheet = wb.get_sheet_by_name(sheet)
# print(mySheet.cell(3,2).value)
class Input:
    def __init__(self):
        pass
    def sth(self,a,b,c=None,f=None):
        output = 0
        if c == None and f==None:
            output = a+b
        elif f==None and c!=None:
            output = (a+b)*c
        elif c==None and f!=None:
            output = (a+b)-f
        elif c!=None and f!=None:
            output = (a+b)*(c*f)
        return output
    def tenNumberNNone(self,num):
        a=["deuName10","deuTelegramLink10","engName10","engTelegramLink10","synName10","synTelegramLink10","perName10","perTelegramLink10"]
        print(len(a))
        output = []
        temp = []
        for i in range(0,10):
            for h in range(len(num)):
                temp = []
                for j in range(0,9):
                    if i>j:
                        temp.append(num[h])
                    else:
                        temp.append(None)
                output.append(temp)
                if i == 0:
                        break
        return output
    def some(self,value):
        if value is True:
            return 10,20,30,40
        else:
            return False
    def kwargsMyFunc(self,**kwargs):
        # print(f"{kwargs = }")
        fields = []
        values = []
        for field,val in kwargs.items():
            fields.append(field)
            values.append(val)
        print(f"{fields = }\n{values = }")
        print(f"{len(kwargs) = }")

        return kwargs

@pytest.fixture
def input():
    input = Input()
    return input

class Test_Input:
    @pytest.mark.parametrize("a,b,c,f",[
        (5,6,None,None),
        (5,6,"c=2",None),
        (5,6,"f=3",None),
        (5,6,2,3)
    ])
    def test_sth(self,a,b,c,f,input):
        # a,b=5,6
        if c == "c=2":
            c=2
        elif c=="f=3":
            f=3
        if c==None and f==None:
            output1 =input.sth(a,b)
            assert output1 ==a+b
        # c=2
        elif c!=None and f==None:
            output2 = input.sth(a,b,c=c)
            assert output2 ==(a+b)*c
        # f=3
        elif c==None and f!=None:
            output3 = input.sth(a,b,f=f)
            assert output3 == (a+b)-f
        elif c!=None and f!=None:
            output4 = input.sth(a,b,c,f)
            assert output4 == (a+b)*(c*f)
    def test_TenNumberNNone(self,input):
        # deuName,deuTelegramLink,engName,engTelegramLink,synName,synTelegramLink,perName,perTelegramLink
        num = [0,1,2,3,4,5,6]
        # num = 0
        output = input.tenNumberNNone(num)
        print(f"{output = }")
        assert len(output)==10
        assert isinstance(output,list)
        for i in  range(len(output)):
            assert isinstance(output[i],list)
            assert len(output[i])==9
            numTemp = 0
            for j in range(len(output[i])):
                for h in range(len(num)):
                    for k in range(0,i):
                        if i>j:
                            
                            assert output[i][j]==num[h]
                        elif i == 0:
                            assert output[i][j]==None
                            
                        else:
                            # print(f"{i = },{j =}")
                            # print(f"{output[i][j] = }")
                            assert output[i][j]==None
                

            

    def test_PermutationWRepeated(self,input):
        a=[0,1,2]
        # a=["deuName10","deuTelegramLink10","engName10","engTelegramLink10","synName10","synTelegramLink10","perName10","perTelegramLink10"]
        permutaionList = []
        # output = input.permutationWRepeated(a)
        # assert isinstance(output,list)
        # for i in range(len(a)):
        #     assert out
# import itertools
        x = [0,1, 2, 3, 4, 5, 6]
        # d=[p for p in product(x, repeat=6)]
        # print(f"{d = }")
        t = [1,2,2,2,4]
        c = list(itertools.combinations(t, 6))
        print(f"{c = }")
        # print(f"{set(c) = }")
        # h = list(itertools.permutations(set(a)))
        # print(f"{h = }")
        # f = list(itertools.combinations(x,1))
        # print(f"{f = }")

# a,b=5,6
# c=2
# c=None
# f=3
# f=None
# print(sth(a,b,c=c))
# print(sth(a,b,f=f))
# print(sth(a,b))


    def combinations_without_repetition(self,r, iterable=None, values=None, counts=None):
        if iterable:
            values, counts = zip(*Counter(iterable).items())

        f = lambda i,c: chain.from_iterable(map(repeat, i, c))
        n = len(counts)
        indices = list(islice(f(count(),counts), r))
        if len(indices) < r:
            return
        while True:
            yield tuple(values[i] for i in indices)
            for i,j in zip(reversed(range(r)), f(reversed(range(n)), reversed(counts))):
                if indices[i] != j:
                    break
            else:
                return
            j = indices[i]+1
            for i,j in zip(range(i,r), f(count(j), islice(counts, j, None))):
                indices[i] = j
    
    def test_combinations_without_repetition(self):
        n = list(self.combinations_without_repetition(3, values=[0,1,2], counts=[1,2,3]))
        print(f"{n = }")
    
    def test_doubleCot(self):
        wordType = ""
        wordTypeVerList = ["","Verb","Adverb","Adjektiv","Nomen","Possessivpronomen","Interjektion"]
        assert wordType in  wordTypeVerList
    @pytest.mark.parametrize("value",[
        (False),
        (True),
        (False),
        (True),
        (True)
    ])     
    def test_some(self,input,value):
        # a,b,c,d=False,False,False,False
        # a,b,c,d = input.some(value)
        # if (a,b,c,d):
        a,b,c,d = None,None,None,None
        if (a,b,c,d := input.some(value)):   
            print(f"a,b,c,d = {a,b,c,d}")
            return a,b,c,d
        else:
            return False
    @pytest.mark.parametrize("kwargs",[
        ({"word id":"asdfagsdfg","word Type":"Verb","article":"___","name_wort_file_Audio":"sich.mp3"}),
        ({"greeting":"hi","where":"here"})
    ])
    def test_kwargsMyFunc(self,kwargs,input):
        output = input.kwargsMyFunc(**kwargs)
        assert isinstance(output,dict) 

    def test_update(self):
        fiNVal = {"khooneh":"hi"}
        cond = {"_id":"5dc5c380ec972f0ee087361d"}
        outputMongo = {"_id":0,"deuVoice":1}
        output = None
        for col in db().testMeaningCollection.find(cond,outputMongo):
            for keys in col.keys():
                output = col[keys]
        updateV = {"khooneh":"hi"}
        output.update(updateV)
        updateFNV = {"deuVoice":output}
        db().testMeaningCollection.update_many({"_id":"5dc5c380ec972f0ee087361d"},{"$set":updateFNV})

