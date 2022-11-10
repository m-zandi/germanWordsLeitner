import pytest
import random
import PIL
from PIL import Image, ImageDraw , ImageFont
import langdetect
from langdetect import detect
import math 
from io import BytesIO
import scipy
from imutils import perspective
from imutils import contours
import numpy 
import threading

import imutils
from cv2 import cv2
import datetime
#font fix for persian
import arabic_reshaper
from bidi.algorithm import get_display
#
from . import VidSet as VS

import sys
sys.path.append( "../")
# import os 
# sys.path.append(os.path.realpath(r"D:\project\WoerterbuchProject\mainV2"))

from mainV2.base.Txt import MessageNVarPer as MsgPer
from mainV2.base.Txt import MessageNVarDe as MsgDe
from mainV2.base.Txt import MessageNVarEn as MsgEn
from mainV2.set.dbContact import DateArrange as DA 

# from ..base.Txt import MessageNVarPer as MsgPer
# from ..base.Txt import MessageNVarDe as MsgDe
# from ..base.Txt import MessageNVarEn as MsgEn
# from ..set.dbContact import DateArrange as DA 

@pytest.fixture
def going():
    going = VS.Going()
    yield going

class Testgoing:

    def parameters(self):
        importCardLimitation,cardLimitation = 5,20
        return importCardLimitation,cardLimitation
    def test_makeFirstLastList(self):
        importCardLimitation,cardLimitation = self.parameters()
        first , last = self.makeFirstLastList(importCardLimitation,cardLimitation)
        diference = []
        for i in range(len(last)):
           diference.append(last[i]-first[i])
        print(f"{first     = }\n{last      = }\n{diference = }\n\ns{sum(first) = }\n{sum(last)   = }")
        #correction condition
        for i in range(2,len(last)-1):
            equation = (last[i]-first[i])-(last[i+1]-first[i+1])
            if last[i+1]>first[i+1] :
                assert  equation<=0
                limitUpNum = (first[i]-(last[i+1]-first[i+1]))
                assert limitUpNum>=0 
                # print(f"{limitUpNum = }")
                # assert last[i]==0 or last[i] == limitUpNum or  last[i] < limitUpNum
        assert len(first) == 8
        assert len(last) == 8
        assert sum(first)==sum(last)
        assert last[0]==0
        assert last[7] ==first[7] or (last[7]>first[7] and last[7]<(first[7]+first[6])) or last[7]==(first[7]+first[6])
        # print(f"{first = }\n{last  = }")
        for i in range(2,7):
                # print(f"{i = }")
                assert last[i] == 0 or last[i]==first[i]+first[i-1] or last[i]<first[i]+first[i-1]
                if last[i]<first[i]:
                    assert last[1]>first[1]
                assert (last[i+1]-first[i+1])== first[i] or (last[i+1]-first[i+1])< first[i]
 
        # print(f"{sum(first) = } , {sum(last) = }\n{first = } \n{last = }")
        # print(f"{first = }\n{last = }\n{diference = }\n\ns{sum(first) = }\n{sum(last) = }")

    

    def makeFirstLastList(self,importCardLimitation,cardLimitation):    
        first = []
        for i in range(8):
            if i ==0:
                first.append(random.randrange(1,importCardLimitation))
            else:
                first.append(random.randrange(0,cardLimitation))
        firstSum =sum(first)
        blankListPure = [0,0,0,0,0,0,0,0]
        last = blankListPure.copy()
        if first[6]==0:
            last[7]=first[7]
        else:
            last[7]=random.randrange(first[7],first[7]+first[6])
        if first[6]-(last[7]-first[7]) != 0:
            last[6]=random.randrange(0,first[6]-(last[7]-first[7]))
        # elif last[]
        else:
            last[6]=first[6]

        for i in range(1,6):
          if i ==1:
            if first[0]!=first[i-1]+first[i]:
                last[i]=random.randrange(first[0],first[i-1]+first[i])
            else:
                last[i]==first[i-1]+first[i]
            # last[i]=last[i]+((first[6]-(last[7]-first[7]))-last[6])
            last[i]=last[i]+(last[6]-first[6])-(last[7]-first[7])
          elif (first[i-1] + first[i]) != 0:
            last[i]=random.randrange(0,first[i-1]+first[i])
          else:
            last[i]=first[i]
        # for i in range(2,7):
        #     if last[i]<first[i] :
                

        ##correction two index beside 
        for i in range(2,7):
            equation = (last[i]-first[i])+(last[i+1]-first[i+1])
            if last[i+1]>first[i+1] and equation>0:
                #FIXME limitUpNum -1
                limitUpNum = (first[i]-(last[i+1]-first[i+1]))
                # print(f"{limitUpNum = }")
                last[i]=random.randrange(0,limitUpNum)

        #####
        lastSum =sum(last)
        if firstSum == lastSum:
            pass
        elif lastSum<firstSum:
            subtraction = firstSum-lastSum
            last[1]=last[1]+subtraction
        elif lastSum>firstSum:
            plus = lastSum-firstSum
            # subtraction = 0
            for i in reversed(range(2,7)):
                if firstSum!=sum(last) and plus !=0:
                    if last[i]>first[i]:
                        if plus > (last[i]-first[i]) or plus == (last[i]-first[i]):
                            plus=plus - (last[i]-first[i])
                            last[i]=first[i]
                        else:
                            last[i]=  last[i]-plus
                            plus = 0

                        
                elif firstSum ==sum(last):
                    break



        # print(f"first = {first}\nlast  = {last}\n\nsum(first) = {sum(first)}\n sum(last)  = {sum(last)}")
        return first ,last

    # def test_get_xYAxises(self):
    #     l = ["Per","En","De"]
    #     lan = random.choice(l)
    #     xYAxis = self.get_xYAxises(lan)
    #     assert len(xYAxis) == 8
    #     for i in range(len(xYAxis)):
    #         assert len(i) == 2

    # @pytest.fixture()
    def get_xYAxises(self,lan):
        if lan == "Per":
            xYAxis = [(1146, 598),(933, 598), (760, 598), (599, 598), (435, 598), (269, 598), (109, 598), (185, 234)]
        else:
            xYAxis = [(50, 598),(295, 598), (462, 598), (622, 598), (787, 598), (955, 598), (1118, 598), (1021, 235)]
        return xYAxis
    # @pytest.fixture()
    def test_firstNLastTupleList8ElementList3ElementTuple(self):
        
        importCardLimitation,cardLimitation = self.parameters()
        first,last = self.makeFirstLastList(importCardLimitation,cardLimitation)
        l= ["Per","En","De"]
        lan = random.choice(l)
        xYAxis = self.get_xYAxises(lan)
        firstTupleList,lastTupleLIst = self.firstNLastTupleList8ElementList3ElementTuple(first,last,xYAxis)
        assert len(firstTupleList) == 8
        assert len(lastTupleLIst) == 8
        for i in range(len(firstTupleList)):
            assert len(firstTupleList[i])==3
            assert len(lastTupleLIst[i])==3


    def checkLastAndFirst(self,first,last):
        assert len(first) == 8
        assert len(last) == 8
        for i in range(len(first)):
            assert len(first[i])==3
            assert len(last[i])==3

    def firstNLastTupleList8ElementList3ElementTuple(self,first,last,xYAxis):

        e8First = first
        e8Last = last
        firstTupleList = []
        lastTupleLIst = []
        for i in range(len(xYAxis)):
            oneList = []
            oneList.append(e8First[i])
            oneList.append(xYAxis[i][0])
            oneList.append(xYAxis[i][1])
            firstTupleList.append(tuple(oneList))

            secondList = []
            secondList.append(e8Last[i])
            secondList.append(xYAxis[i][0])
            secondList.append(xYAxis[i][1])
            lastTupleLIst.append(tuple(secondList))

        return firstTupleList,lastTupleLIst
    






    @pytest.mark.parametrize("goingOneFrame",[
        ("goingOneFrame_1"),
        ("goingOneFrame_2"),
        ("goingOneFrame_3"),
        ("goingOneFrame_4")
        
        ])


    def test_GoingOneFrameIndex0(self,goingOneFrame,goingOneFrameValues,going):

        for i in range(len(goingOneFrame)):
                # return firstName,lan,countOfFrameGoing,countOfFrameReturning,verticalGoing,verticalReturning,first,last
                _,_,countOfFrameGoing,_,verticalGoing,_,first,last = goingOneFrameValues[goingOneFrame]   
                blankList = going.makeBlankList(first)
                frame = blankList.copy()  
                stayBoxArray = first.copy() 
                verticalArray = []    
                firstVerticalArray = []
                secondVerticalArray = []
                for i in range(len(first)-1):
                    for j in range(countOfFrameGoing):
                        # def get_stayBoxArrayNFrameGo(self,i,j,countOfFrame,first,last,stayBoxArray,frame,vertical = 100,verticalArray=[],firstVerticalArray=[],secondVerticalArray=[])
                        frame,stayBoxArray,verticalArray,firstVerticalArray,secondVerticalArray = going.get_stayBoxArrayNFrameGo(i,j,countOfFrameGoing,first,last,stayBoxArray,frame,verticalGoing,verticalArray,firstVerticalArray,secondVerticalArray)

                        print(f"{first        = }\n{stayBoxArray = }\n{last       = }")
                        if i == 0:
                            if j==0:
                                # print(f"stayBoxArray (j==0)  = {stayBoxArray}")
                                assert stayBoxArray[i][0]!=0 
                                assert frame[i][0]==0                     

                            elif j> (countOfFrameGoing/10) and j < (4*countOfFrameGoing/5) :
                                assert stayBoxArray[i][0]==0
                                assert frame[i][0]!= 0
                            elif j> (4*countOfFrameGoing/5) :
                                # FIXME stayBoxArray[i+1] [0] i==0
                            #    if (i+1)!=1:
                            #         assert stayBoxArray[i+1][0] ==  first[i+1][0]+first[i][0]
                               assert frame[i][0] == 0
                               assert frame[i+1][0] ==  0
                            if frame[i][0] != 0:
                                assert stayBoxArray[i][0]==0


                        else:
                            if  last[i+1][0] > first[i+1][0]:

                                if j==0 :
                                    assert frame[i][0] == 0     
                                elif j> (countOfFrameGoing/10) and j < (4*countOfFrameGoing/5) :
                                    assert frame[i][0] == last[i+1][0] - first[i+1][0]
                                    if i == 1:
                                        assert stayBoxArray[i][0] == first[0][0] + first[1][0] or  stayBoxArray[i][0] == (first[0][0] + first[1][0])-(last[i+1][0]-first[i+1][0])
                                    else:
                                        assert stayBoxArray[i][0] == first[i][0] - (last[i+1][0] - first[i+1][0])   
                                elif j> (4*countOfFrameGoing/5) :
                                    assert frame[i][0] == 0
                                    assert frame[i+1][0] == 0
                                    # FIXME stayBoxArray[i+1] [0] i !=1
                                    # if (i+1)!=1:
                                    #     assert stayBoxArray[i+1] [0] == first[i][0] + first[i+1][0]  

    @pytest.mark.parametrize("goingOneFrame",[
        ("goingOneFrame_1"),
        ("goingOneFrame_2"),
        ("goingOneFrame_3"),
        ("goingOneFrame_4")
        
        ])
    def test_GoingOneFrameIndex1(self,goingOneFrame,goingOneFrameValues,going):
        # i,j=self.getINJ()
        for i in range(len(goingOneFrame)):   
   
                # return firstName,lan,countOfFrameGoing,countOfFrameReturning,verticalGoing,verticalReturning,first,last
                _,lan,countOfFrameGoing,_,verticalGoing,_,first,last = goingOneFrameValues[goingOneFrame] 
                blankList = going.makeBlankList(first)
                frame = blankList.copy()  
                stayBoxArray = first.copy()
                verticalArray = []  
                firstVerticalArray = []
                secondVerticalArray = []
                for i in range(len(first)-1):
                    for j in range(countOfFrameGoing):
                        # def get_stayBoxArrayNFrameGo(self,i,j,countOfFrame,first,last,stayBoxArray,frame,vertical = 100,verticalArray=[],firstVerticalArray=[],secondVerticalArray=[])
                        
                        frame,stayBoxArray,verticalArray,firstVerticalArray,secondVerticalArray = going.get_stayBoxArrayNFrameGo(i,j,countOfFrameGoing,first,last,stayBoxArray,frame,verticalGoing,verticalArray,firstVerticalArray,secondVerticalArray)
                        if i == 0:
                            if lan == "Per":
                                assert first[i][1]>frame[i][1]
                            else:
                                assert first[i][1]<frame[i][1] 
                        elif i ==6:
                            if  last[i+1][0] > first[i+1][0]:
                                if lan == "Per":
                                    assert first[i][1]<frame[i][1]
                                else:
                                    assert first[i][1]>frame[i][1] 
                        else:
                            if  last[i+1][0] > first[i+1][0]:
                                if lan == "Per":
                                    assert first[i][1]>frame[i][1]
                                else:
                                    assert first[i][1]<frame[i][1]  

    @pytest.mark.parametrize("goingOneFrame",[
        ("goingOneFrame_1"),
        ("goingOneFrame_2"),
        ("goingOneFrame_3"),
        ("goingOneFrame_4")
        
        ])                          
    def test_GoingOneFrameIndex2(self,goingOneFrame,goingOneFrameValues,going):
        for i in range(len(goingOneFrame)):
                # return firstName,lan,countOfFrameGoing,countOfFrameReturning,verticalGoing,verticalReturning,first,last
                _,_,countOfFrameGoing,_,verticalGoing,_,first,last = goingOneFrameValues[goingOneFrame]  

                blankList = going.makeBlankList(first)
                frame = blankList.copy()  
                stayBoxArray = first.copy()
                verticalArray = []   
                # firstVerticalArray = []
                # secondVerticalArray = []
                for i in range(len(first)-1):
                    verticalArray = []   
                    firstVerticalArray = []
                    secondVerticalArray = []
                    for j in range(countOfFrameGoing):
                        # def get_stayBoxArrayNFrameGo(self,i,j,countOfFrame,first,last,stayBoxArray,frame,vertical = 100,verticalArray=[],firstVerticalArray=[],secondVerticalArray=[])
                        frame,stayBoxArray,verticalArray,firstVerticalArray,secondVerticalArray = going.get_stayBoxArrayNFrameGo(i,j,countOfFrameGoing,first,last,stayBoxArray,frame,verticalGoing,verticalArray,firstVerticalArray,secondVerticalArray)
                        # inputAddcard(firstName,lan,frame,stayBoxArray)
                        # verticalGoing = 100
                        halfCount = int(countOfFrameGoing/2)
                        section = verticalGoing/halfCount
                        if i == 0:
                            
                            if j == 0 :
                               
                                assert frame[i][2] == blankList[i][2] - (section*j)
                                assert blankList[i][2] == frame[i][2]
                            elif j<halfCount and j!=0 :
                                assert frame[i][2] == verticalArray[j-1] - (section*j)
                                assert verticalArray [j-1] > verticalArray [j]
                            elif j == halfCount:
                                assert frame[i][2] == verticalArray[j]
                                assert frame[i][2] == verticalArray [j-1]
                            else :
                                assert verticalArray [j-1] < verticalArray [j]
                                assert verticalArray[j-1] < frame[i][2]  
                                if j ==(countOfFrameGoing-1):
                                    assert frame[i][2] == blankList[i][2]
                            assert frame[i][2] == verticalArray[j] 
                        else:
                            if  last[i+1][0] > first[i+1][0]:
                                
                                # #FIXed movement learnet words    
                                # # vertically movement
                                section6N7 = (first[6][2]-first[7][2])/countOfFrameGoing
                                plusVertical = (first[6][2]-first[7][2])/15
                                # for first half monhani
                                firstCount = int(3*countOfFrameGoing/5)
                                #for full second monhani
                                secondCount = int((2*countOfFrameGoing/5)/2)
                                verticalDistance = False
                                if i+1 ==7:
                                    verticalDistance = True
                                if j<0 and verticalDistance is False:
                                    assert len(verticalArray) == j-1
                                elif j == 0 and verticalDistance is False:
                                    #FIXed elif j == 0   len(verticalArray) == 1
                                    # print(f"{verticalDistance = }\n{firstCount =}")
                                    # print(f"\n\n{i=}\n{j=}\n{frame = } \n{verticalArray = }\n {frame[i][2] = }\n\n")
                                    # print(f"\n{verticalArray[j] =} ")
                                    assert len(verticalArray) == 1
                                if j==0 :
                                    # assert frame[i][2] == blankList[i][2] - (section*j)
                                    # assert blankList[i][2] == frame[i][2]
                                    if verticalDistance is True and j<firstCount:
                                        assert frame[i][2] == first[6][2]-(section6N7*j)
                                        assert frame[i][2] == firstVerticalArray[j]
                                    else:
                                        
                                        assert frame[i][2] == blankList[i][2] - (section*j)
                                        assert blankList[i][2] == frame[i][2]
                                        # print(f"\n\n{i=}\n{j=}\n{frame = } \n{verticalArray = }\n\n")
                                        # print(f"\n\n{i=}\n{j=}\n{frame = } \n{verticalArray = }\n {frame[i][2] = }\n\n")
                                        # print(f"{verticalArray[j] =}")
                                        # assert frame[i][2] == verticalArray[j]

                                if j<halfCount and j !=0 :
                                    if verticalDistance is True and j<firstCount:
                                        assert frame[i][2] == first[6][2]-(section6N7*j)
                                        assert frame[i][2] == firstVerticalArray[j]
                                        assert firstVerticalArray [j-1] > firstVerticalArray [j]    
                                    else:
                                        #FIXed j<halfCount and j !=0 else
                                        
                                        # print(f"\n\n{i=}\n{j=}\n{frame = } \n{verticalArray = }\n {frame[i][2] = }\n\n")
                                        # print(f"\n{verticalArray[j] =} ")
                                        assert frame[i][2] == verticalArray[j-1] - (section*j)
                                        assert verticalArray [j-1] > verticalArray [j]
                                        # assert frame[i][2] == verticalArray[j]

                                elif j == halfCount:
                                    if verticalDistance is True and j<firstCount:
                                        assert frame[i][2] == first[6][2]-(section6N7*j)
                                        assert frame[i][2] == firstVerticalArray[j]
                                        # print(f"\n\n{i=}\n{j=}\n{frame = } \n{firstVerticalArray = }\n {frame[i][2] = }\n\n")
                                        

                                    else:

                                        assert frame[i][2] == verticalArray [j-1]
                                        assert frame[i][2] == verticalArray[j]
                                elif j> halfCount :
                                    if verticalDistance is True and j<firstCount:
                                        assert frame[i][2] == first[6][2]-(section6N7*j)
                                        assert frame[i][2] == firstVerticalArray[j]
                                    elif verticalDistance is True and  j==firstCount:
                                        #EDIT zero point

                                        assert frame[i][2]== first[7][2]-(plusVertical*(j-firstCount))
                                        assert frame[i][2] == secondVerticalArray[j-firstCount]
                                    elif verticalDistance is True and j<firstCount+secondCount and j>firstCount  :
                                        #EDit between zero and middle
                                        assert frame[i][2]== first[7][2]-(plusVertical*(j-firstCount))
                                        # print(f"{i = }\n{j = }\n{secondVerticalArray = }\n{halfCount =}\n{firstCount =}\n{plusVertical = }\n{secondCount =}")
                                        assert frame[i][2] == secondVerticalArray[j-firstCount]
                                        assert secondVerticalArray [(j-(firstCount+1))] > secondVerticalArray [j-firstCount]
                                    elif verticalDistance is True and j==(firstCount+secondCount) :
                                        #Edit middle 
                                        assert frame[i][2] == firstVerticalArray [j-1]
                                        assert frame[i][2] == firstVerticalArray[j]
                                        assert frame[i][2]== firstVerticalArray[j]
                                    elif verticalDistance is True and j<(firstCount+(2*secondCount)) :
                                        #EDIT more than middle
                                        assert firstVerticalArray [j-1] < firstVerticalArray [j]
                                        assert firstVerticalArray[j-1] < frame[i][2] 
                                        assert frame[i][2]== firstVerticalArray[j]
                                    else:
                                        # print(f"\n\n{i=}\n{j=}\n{frame = } \n{verticalArray = }\n {frame[i][2] = }\n\n")
                                        # print(f"{halfCount =}")
                                        # print(f"\n\n{verticalArray[j] =} \n\n")
                                        assert verticalArray [j-1] < verticalArray [j]
                                        assert verticalArray[j-1] < frame[i][2] 
                                        assert frame[i][2]== verticalArray[j]
                                # print(f"{frame = }")


    @pytest.mark.parametrize("first,indexList,countOfFrame",[
        ([(0, 1146, 598), (0, 933, 598), (0, 760, 598), (0, 599, 598), (0, 435, 598), (0, 269, 598), (0, 109, 598), (0, 185, 234)],0,20),
        ([(0, 1146, 598), (0, 933, 598), (0, 760, 598), (0, 599, 598), (0, 435, 598), (0, 269, 598), (0, 109, 598), (0, 185, 234)],1,20),
        ([(0, 1146, 598), (0, 933, 598), (0, 760, 598), (0, 599, 598), (0, 435, 598), (0, 269, 598), (0, 109, 598), (0, 185, 234)],2,20),
        ([(0, 1146, 598), (0, 933, 598), (0, 760, 598), (0, 599, 598), (0, 435, 598), (0, 269, 598), (0, 109, 598), (0, 185, 234)],3,20),
        ([(0, 1146, 598), (0, 933, 598), (0, 760, 598), (0, 599, 598), (0, 435, 598), (0, 269, 598), (0, 109, 598), (0, 185, 234)],4,20),
        ([(0, 1146, 598), (0, 933, 598), (0, 760, 598), (0, 599, 598), (0, 435, 598), (0, 269, 598), (0, 109, 598), (0, 185, 234)],5,20),
        ([(0, 1146, 598), (0, 933, 598), (0, 760, 598), (0, 599, 598), (0, 435, 598), (0, 269, 598), (0, 109, 598), (0, 185, 234)],6,20)

    ])
    def test_horizentalDistance(self,first,indexList,countOfFrame,going):
        partSize, horizentalDistance =  going.horizentalDistanceFunc(first,indexList,countOfFrame)
        for _ in range(len(first)):
            assert horizentalDistance == first[indexList][1]-first[indexList+1][1]
            assert partSize == horizentalDistance/countOfFrame



    # def test_GoingOneFrameIndex2(firstName,lan,first,last):
    #     firstName,lan,first,frame,stayBoxArray,horizentalDistance = goingOneFrame(firstName,lan,first,last)
    #     for i in range(len(first)):
    #         pass



    # @pytest.mark.parametrize("firstName,lan,first,last,countOfFrame,vertical",[
    #     ("khafan","Per",[(3,1146, 598),(6,933, 598), (9,760, 598), (5,599, 598), (2,435, 598), (8,269, 598), (9,109, 598), (2,185, 234)],[(0,1146, 598),(66,933, 598), (4,760, 598), (423,599, 598), (0,435, 598), (6,269, 598), (0,109, 598), (5,185, 234)],10,100)
    # ])
    # def test_going(firstName,lan,first,last,countOfFrame,vertical):
    #     lan = get_lan(lan)
    #     stayBoxList = going(firstName,lan,first,last,countOfFrame,vertical)
    #     assert len(stayBoxList)==8
    #     for i in range(len(stayBoxList)):
    #         assert len(stayBoxList[i])==3
    #         # if i == 0:
    #         #     assert stayBoxList[i][0]==0
    #     assert lan == "Per" or lan == "De" or lan == "En"


    def get_lan(self,lan):
        return lan
    @pytest.mark.parametrize("countOfFrame,vertical",[
        (10,100),
        (20,150),

    ])
    def test_getValues(self,countOfFrame,vertical,going):
        halfCount,section = going.getValues(countOfFrame,vertical)
        assert halfCount*2 == countOfFrame
        assert section == vertical/halfCount


    @pytest.mark.parametrize("first",[
        ([(3,1146, 598),(6,933, 598), (9,760, 598), (5,599, 598), (2,435, 598), (8,269, 598), (9,109, 598), (2,185, 234)]),
        ([(1,50, 598),(4,295, 598), (7,462, 598), (8,622, 598), (2,787, 598), (0,955, 598), (33,1118, 598), (44,1021, 235)])
    ])
    def test_makeBlankList(self,first,going):
        blankList = going.makeBlankList(first)
        assert len(blankList) == 8
        for i in range(len(blankList)):
            assert blankList[i][0] == 0
            assert len(blankList[i]) ==3


    @pytest.mark.parametrize("arrayOneElement,indexArrToChange,valueToChange",[
        ((1,4,6),2,9),
        ((0,0,0),0,0)
    ])
    def test_tupleChange(self,arrayOneElement,indexArrToChange,valueToChange,going):
        el3tuple = going.tupleChange(arrayOneElement,indexArrToChange,valueToChange)
        assert len(el3tuple)==len(arrayOneElement)
        assert el3tuple[indexArrToChange] == valueToChange
        assert isinstance(el3tuple,tuple)
        


    @pytest.mark.parametrize("aL,bL,num,xYAxis,",[
        ([1,3,6,9,1,5,3],[8,4,8,3,2,6,9],3,[(1146, 598),(933, 598), (760, 598), (599, 598), (435, 598), (269, 598), (109, 598), (185, 234)]),
        ([0,42,1,3,5,7,8],[4,6,8,3,1,4,3],2,[(50, 598),(295, 598), (462, 598), (622, 598), (787, 598), (955, 598), (1118, 598), (1021, 235)])
    ])
    def test_add1elementInFirstOfTwoListN8elemetsForEachOThem(self,aL,bL,num,xYAxis,going):
        assert isinstance(num,int)
        listA,listB = going.firstNLastTupleList8ElementList3ElementTuple(aL,bL,num,xYAxis)  
        # listA,listB =LP().firstNLastTupleList8ElementList3ElementTuple(aL,bL,num,xYAxis)  
        assert isinstance(listA,list)
        assert isinstance(listB,list)
        assert len(listA)==8
        assert len(listB)==8
        assert listA[0][0] == num
        assert listB[0][0] == 0

    @pytest.fixture
    def xYAxis_1(self):
        lan = "Per"
        xYAxis = [(1146, 598),(933, 598), (760, 598), (599, 598), (435, 598), (269, 598), (109, 598), (185, 234)]
        return xYAxis,lan

    @pytest.fixture
    def xYAxis_2(self):
        lan = "En"
        xYAxis = [(50, 598),(295, 598), (462, 598), (622, 598), (787, 598), (955, 598), (1118, 598), (1021, 235)]
        return  xYAxis ,lan
    @pytest.fixture
    def xYAxis_3(self):
        lan = "De"
        xYAxis = [(50, 598),(295, 598), (462, 598), (622, 598), (787, 598), (955, 598), (1118, 598), (1021, 235)]
        return xYAxis ,lan

    @pytest.fixture
    def xYAxisValues(self,xYAxis_1,xYAxis_2,xYAxis_3):
        return {"xYAxis_1":xYAxis_1,"xYAxis_2":xYAxis_2,"xYAxis_3":xYAxis_3}

    # @pytest.mark.parametrize("xYAxisLangs,lan",[
    #     ("xYAxis_1","Per"),
    #     ("xYAxis_2","En"),
    #     ("xYAxis_3","De")
    # ])
    @pytest.mark.parametrize("xYAxisLangs",[
        ("xYAxis_1"),
        ("xYAxis_2"),
        ("xYAxis_3")
    ])
    #FIXed test_get_xYAxises
    def test_get_xYAxises(self,xYAxisLangs,xYAxisValues,going):
        for i in range(len(xYAxisLangs)):
            xYAxisesT,lan=xYAxisValues[xYAxisLangs]
            xYAxises = going.get_xYAxises(lan)
            assert xYAxises[i]==xYAxisesT[i]
            assert len(xYAxises[i]) == 2
            assert len(xYAxisesT) == 8


    @pytest.fixture
    def addCard_shapeFrame_1(self):
        firstName = "hi baby, you never going see me again"
        lan = "En"
        frame = [(0, 62.25, 598.0), (0, 295, 598), (0, 462, 598), (0, 622, 598), (0, 787, 598), (0, 955, 598), (0, 1118, 598), (0, 1021, 235)]
        stayBoxArray =[(3, 50, 598), (2, 295, 598), (3, 462, 598), (6, 622, 598), (3, 787, 598), (8, 955, 598), (5, 1118, 598), (2, 1021, 235)]
        frameType = ""
        yield firstName,lan,frame,stayBoxArray,frameType
    
    @pytest.fixture
    def addCard_shapeFrame_2(self):
        firstName = "خان چلی اصل مکزیکی فر پنهان گون اندک مجال"
        lan = "En"
        frame = [(3, 258.25, 538.0), (0, 295, 598), (0, 462, 598), (0, 622, 598), (0, 787, 598), (0, 955, 598), (0, 1118, 598), (0, 1021, 235)]
        stayBoxArray =[(0, 50, 598), (2, 295, 598), (16, 462, 598), (0, 622, 598), (19, 787, 598), (18, 955, 598), (13, 1118, 598), (0, 1021, 235)]
        frameType = "Going"
        yield firstName,lan,frame,stayBoxArray,frameType

    @pytest.fixture
    def addCard_shapeFrame_3(self):
        firstName = "حافظ تو خود حجاب خودی از میان برخیز"
        lan = "Per"
        frame = [(0, 1135.35, 598.0), (0, 933, 598), (0, 760, 598), (0, 599, 598), (0, 435, 598), (0, 269, 598), (0, 109, 598), (0, 185, 234)]
        stayBoxArray =[(3, 1146, 598), (1, 933, 598), (18, 760, 598), (8, 599, 598), (7, 435, 598), (17, 269, 598), (10, 109, 598), (1, 185, 234)]
        frameType = "Returning"
        yield firstName,lan,frame,stayBoxArray,frameType

    @pytest.fixture
    def addCard_shapeFrame_4(self):
        firstName = "Astalavista baby"
        lan = "Per"
        frame = [(3, 1071.4499999999994, 388.0), (0, 933, 598), (0, 760, 598), (0, 599, 598), (0, 435, 598), (0, 269, 598), (0, 109, 598), (0, 185, 234)]
        stayBoxArray =[(0, 1146, 598), (1, 933, 598), (18, 760, 598), (8, 599, 598), (7, 435, 598), (17, 269, 598), (10, 109, 598), (1, 185, 234)]
        frameType = "Going"
        yield firstName,lan,frame,stayBoxArray,frameType    

    @pytest.fixture
    def addCard_shapeFrame_5(self):
        firstName = "Alison"
        lan = "De"
        frame = [(0, 295.0, 598.0), (0, 295, 598), (0, 462, 598), (0, 622, 598), (0, 787, 598), (0, 955, 598), (0, 1118, 598), (0, 1021, 235)]
        stayBoxArray =[(0, 50, 598), (4, 295, 598), (15, 462, 598), (8, 622, 598), (6, 787, 598), (16, 955, 598), (12, 1118, 598), (16, 1021, 235)]
        frameType = "Returning"
        yield firstName,lan,frame,stayBoxArray,frameType    

    @pytest.fixture
    def addCard_shapeFrame_6(self):
        firstName = "Röpke"
        lan = "De"
        frame = [(3, 209.25, 318.0), (0, 295, 598), (0, 462, 598), (0, 622, 598), (0, 787, 598), (0, 955, 598), (0, 1118, 598), (0, 1021, 235)]
        stayBoxArray =[(0, 50, 598), (1, 295, 598), (15, 462, 598), (8, 622, 598), (6, 787, 598), (16, 955, 598), (12, 1118, 598), (16, 1021, 235)]
        frameType = "Going"
        yield firstName,lan,frame,stayBoxArray,frameType   

    #firstName,lan,countOfFrame,first,last
    @pytest.fixture
    def addCard_shapeFrameValues(self,addCard_shapeFrame_1,addCard_shapeFrame_2,addCard_shapeFrame_3,addCard_shapeFrame_4,addCard_shapeFrame_5,addCard_shapeFrame_6):
        return {"addCard_shapeFrame_1":addCard_shapeFrame_1,"addCard_shapeFrame_2":addCard_shapeFrame_2,"addCard_shapeFrame_3":addCard_shapeFrame_3,"addCard_shapeFrame_4":addCard_shapeFrame_4,"addCard_shapeFrame_5":addCard_shapeFrame_5,"addCard_shapeFrame_6":addCard_shapeFrame_6}
    @pytest.mark.parametrize("addCard_shapeFrame",[
    ("addCard_shapeFrame_1"),
    ("addCard_shapeFrame_2"),
    ("addCard_shapeFrame_3"),
    ("addCard_shapeFrame_4"),
    ("addCard_shapeFrame_5"),
    ("addCard_shapeFrame_6")
    
    ]) 
    def test_addCard_shape(self,addCard_shapeFrame,addCard_shapeFrameValues,going):
        _,lan,frame,stayBoxArray,_ =addCard_shapeFrameValues[addCard_shapeFrame]
        alfa,beta = 70,102
        num = 10
        lastNum = num*3
        for y in range(len(stayBoxArray)):
            
            cardNumFrame = frame[y][0]
            pointLeftFrame = frame[y][1]
            pointUperFrame = frame[y][2]
            # size of card
            # distanceFrame = lastNum /cardNumFrame
            try:
                distanceFrame = lastNum /cardNumFrame
            except:
                distanceFrame =0  
            ######
            cardNumStayBox = stayBoxArray[y][0]
            pointLeftStayBox = stayBoxArray[y][1]
            pointUperStayBox = stayBoxArray[y][2]
            # size of card
            # distanceStayBox = lastNum /cardNumStayBox
            try:
                distanceStayBox = lastNum /cardNumStayBox
            except:
                distanceStayBox = 0
            for x in reversed(range(cardNumFrame)):
                shapeFrame = going.addCard_shapeFrame(lan,distanceFrame,pointLeftFrame,pointUperFrame,x,alfa,beta)
                shapeStayBox = going.addCard_shapeStayBox(lan,distanceStayBox,pointLeftStayBox,pointUperStayBox,x,alfa,beta)
                assert len(shapeFrame) == 2
                assert len(shapeFrame[0]) == 2
                assert len(shapeFrame[1]) == 2
                assert len(shapeStayBox) == 2
                assert len(shapeStayBox[0]) == 2
                assert len(shapeStayBox[1]) == 2

                if lan == "Per":
                    assert shapeFrame[0][0]==pointLeftFrame+distanceFrame*x
                    assert shapeFrame[0][1]==pointUperFrame-distanceFrame*x
                    assert shapeFrame[1][0]==pointLeftFrame+alfa+distanceFrame*x
                    assert shapeFrame[1][1]==pointUperFrame+beta-distanceFrame*x
                    assert shapeStayBox [0][0] == pointLeftStayBox+distanceStayBox*x
                    assert shapeStayBox [0][1] == pointUperStayBox-distanceStayBox*x
                    assert shapeStayBox [1][0] == pointLeftStayBox+alfa+distanceStayBox*x
                    assert shapeStayBox [1][1] == pointUperStayBox+beta-distanceStayBox*x

                else:
                    assert shapeFrame[0][0]==pointLeftFrame-distanceFrame*x     
                    assert shapeFrame[0][1]==pointUperFrame-distanceFrame*x
                    assert shapeFrame[1][0]==pointLeftFrame+alfa-distanceFrame*x
                    assert shapeFrame[1][1]==pointUperFrame+beta-distanceFrame*x
                    assert shapeStayBox [0][0] == pointLeftStayBox-distanceStayBox*x
                    assert shapeStayBox [0][1] == pointUperStayBox-distanceStayBox*x
                    assert shapeStayBox [1][0] == pointLeftStayBox+alfa-distanceStayBox*x
                    assert shapeStayBox [1][1] == pointUperStayBox+beta-distanceStayBox*x


 


    @pytest.mark.parametrize("aL,bL,num,lan,",[
        ([1,3,6,9,1,5,3],[8,4,8,3,2,6,9],3,"Per"),
        ([0,42,1,3,5,7,8],[4,6,8,3,1,4,3],2,"En")
    ])
    def test_2listAddeachElementXYAxisTuplePosition1N2(self,aL,bL,num,lan,going):
        xYAxis = going.get_xYAxises(lan)
        # xYAxis = LP().get_xYAxises(lan)
        assert len(xYAxis)==8
        for i in range(len(xYAxis)):
            assert len(xYAxis[i])==2
            assert isinstance(xYAxis[i],tuple)
        listAoutPut,listBoutPut = going.firstNLastTupleList8ElementList3ElementTuple(aL,bL,num,xYAxis)
        # listAoutPut,listBoutPut = LP().firstNLastTupleList8ElementList3ElementTuple(aL,bL,num,xYAxis)
        for i in range(len(listAoutPut)):
            assert len(listAoutPut[i])==3
            assert isinstance(listAoutPut[i],tuple)
        for i in range(len(listBoutPut)):
            assert len(listAoutPut[i])==3
            assert isinstance(listBoutPut[i],tuple)
        for i in range(len(xYAxis)):

            if i == 0:
                assert num == listAoutPut[i][0]
            else:
                assert aL[i-1] == listAoutPut[i][0]
            assert xYAxis[i][0] == listAoutPut[i][1]
            assert xYAxis[i][1] == listAoutPut[i][2]
        for i in range(len(xYAxis)):
            if i == 0:
                assert 0 == listBoutPut[i][0]
            else:
                assert bL[i-1] == listBoutPut[i][0]
            assert xYAxis[i][0] == listBoutPut[i][1]
            assert xYAxis[i][1] == listBoutPut[i][2]
    
    
    @pytest.fixture
    def test_addNumber_1(self):
        lan = "Per"
        firstName = "خفن خان"
        cardNum = 5
        pointLeft = 760
        pointUper = 598
        frameType = "Going"
        # img,imgDraw,dearPosition,dearText,firstNamePosition,announcementText,announcementPosition,font_type_announcement,todayNDate,datePosition,font_type_date,fontPos,font_type,font_type_firstName,botAddressPosition,botAddressFont,telIcon
        _,imgDraw,_,_,_,_,_,_,_,_,_,fontPos,font_type,_,_,_,_ = VS.Going().lanOutputs(lan,firstName)
        yield imgDraw,lan,cardNum,pointLeft,pointUper,font_type,fontPos,frameType

    @pytest.fixture
    def test_addNumber_2(self):
        lan = "Per"
        firstName = "Refigh"
        cardNum = 8
        pointLeft = 269
        pointUper = 598
        frameType = ""
        # img,imgDraw,dearPosition,dearText,firstNamePosition,announcementText,announcementPosition,font_type_announcement,todayNDate,datePosition,font_type_date,fontPos,font_type,font_type_firstName,botAddressPosition,botAddressFont,telIcon
        _,imgDraw,_,_,_,_,_,_,_,_,_,fontPos,font_type,_,_,_,_ = VS.Going().lanOutputs(lan,firstName)
        yield imgDraw,lan,cardNum,pointLeft,pointUper,font_type,fontPos,frameType

    @pytest.fixture
    def test_addNumber_3(self):
        lan = "En"
        firstName = "Peter Fando terapatoni"
        cardNum = 3
        pointLeft = 787
        pointUper = 598
        frameType = "Going"
        # img,imgDraw,dearPosition,dearText,firstNamePosition,announcementText,announcementPosition,font_type_announcement,todayNDate,datePosition,font_type_date,fontPos,font_type,font_type_firstName,botAddressPosition,botAddressFont,telIcon
        _,imgDraw,_,_,_,_,_,_,_,_,_,fontPos,font_type,_,_,_,_ = VS.Going().lanOutputs(lan,firstName)
        yield imgDraw,lan,cardNum,pointLeft,pointUper,font_type,fontPos,frameType

    @pytest.fixture
    def test_addNumber_4(self):
        lan = "En"
        firstName = "پوپک خان منوچهری منش چهره آزاد"
        cardNum = 2
        pointLeft = 1021
        pointUper = 235
        frameType = ""
        # img,imgDraw,dearPosition,dearText,firstNamePosition,announcementText,announcementPosition,font_type_announcement,todayNDate,datePosition,font_type_date,fontPos,font_type,font_type_firstName,botAddressPosition,botAddressFont,telIcon
        _,imgDraw,_,_,_,_,_,_,_,_,_,fontPos,font_type,_,_,_,_ = VS.Going().lanOutputs(lan,firstName)
        yield imgDraw,lan,cardNum,pointLeft,pointUper,font_type,fontPos,frameType

    @pytest.fixture
    def test_addNumber_5(self):
        lan = "De"
        firstName = "Julian Repke"
        cardNum = 13
        pointLeft = 1118
        pointUper = 598
        frameType = "Returning"
        # img,imgDraw,dearPosition,dearText,firstNamePosition,announcementText,announcementPosition,font_type_announcement,todayNDate,datePosition,font_type_date,fontPos,font_type,font_type_firstName,botAddressPosition,botAddressFont,telIcon
        _,imgDraw,_,_,_,_,_,_,_,_,_,fontPos,font_type,_,_,_,_ = VS.Going().lanOutputs(lan,firstName)
        yield imgDraw,lan,cardNum,pointLeft,pointUper,font_type,fontPos,frameType

    @pytest.fixture
    def test_addNumber_6(self):
        lan = "De"
        firstName = "پوپک خان منوچهری منش چهره آزاد"
        cardNum = 3
        pointLeft = 160.25
        pointUper = 238
        frameType = "Going"
        # img,imgDraw,dearPosition,dearText,firstNamePosition,announcementText,announcementPosition,font_type_announcement,todayNDate,datePosition,font_type_date,fontPos,font_type,font_type_firstName,botAddressPosition,botAddressFont,telIcon
        _,imgDraw,_,_,_,_,_,_,_,_,_,fontPos,font_type,_,_,_,_ = VS.Going().lanOutputs(lan,firstName)
        yield imgDraw,lan,cardNum,pointLeft,pointUper,font_type,fontPos,frameType

    @pytest.fixture    
    def test_AddNumberValues(self,test_addNumber_1,test_addNumber_2,test_addNumber_3,test_addNumber_4,test_addNumber_5,test_addNumber_6):
        return {"test_addNumber_1":test_addNumber_1,"test_addNumber_2":test_addNumber_2,"test_addNumber_3":test_addNumber_3,"test_addNumber_4":test_addNumber_4,"test_addNumber_5":test_addNumber_5,"test_addNumber_6":test_addNumber_6}
    @pytest.mark.parametrize("test_addNumber",[
    ("test_addNumber_1"),
    ("test_addNumber_2"),
    ("test_addNumber_3"),
    ("test_addNumber_4"),
    ("test_addNumber_5"),
    ("test_addNumber_6")
    ])
    def test_addNumber(self,test_addNumber,test_AddNumberValues,going):
        plus =0
        imgDraw,lan,cardNum,pointLeft,pointUper,font_type,fontPos,frameType = test_AddNumberValues[test_addNumber]
        shapeText = going.addNumber(frameType,imgDraw,lan,cardNum,pointLeft,pointUper,font_type,fontPos)
        if lan == "Per":
            if cardNum >100 :
                space = 300
            elif cardNum >10 and cardNum< 100:
                space = 8
            else:
                space =4 
        else:
            if cardNum>999:
                space = 300
                plus = -40
            elif cardNum >100  and cardNum >999:
                space = 300
                plus = 300*3
            elif cardNum >10 and cardNum< 100:
                space = 200
                plus = -20
            else:
                space =12 
        assert len(shapeText) == 2
        assert isinstance(shapeText,tuple)
        assert shapeText[0] == pointLeft+fontPos/space+plus
        assert shapeText[1] == pointUper-fontPos


    #TODO_done test_lanOutputs(self,lan,firstName,going)
    @pytest.mark.parametrize("lan,firstName",[
        ("Per","خفن خان"),
        ("En","میثم"),
        ("De","Röpke"),
        ("En","Alison"),
        ("De","Youri"),
        ("Per","Julian")
    ])
    def test_lanOutputs(self,lan,firstName,going):
        #img,imgDraw,dearPosition,dearText,firstNamePosition,announcementText,announcementPosition,font_type_announcement,todayNDate,datePosition,font_type_date,fontPos,font_type,font_type_firstName,botAddressPosition,botAddressFont,telIcon
        img,imgDraw,dearPosition,dearText,firstNamePosition,announcementText,announcementPosition,font_type_announcement,todayNDate,datePosition,font_type_date,fontPos,font_type,font_type_firstName,botAddressPosition,botAddressFont,telIcon = going.lanOutputs(lan,firstName)
        ## position
        if lan == "Per":
            assert len(dearPosition) == 2
            assert isinstance(dearPosition,tuple)
        else:
            assert dearPosition == None
            assert dearText == None
        assert len(firstNamePosition)==2
        assert isinstance(firstNamePosition,tuple)
        assert len(announcementPosition) == 2
        assert isinstance(announcementPosition,tuple)
        assert len(datePosition) == 2
        assert isinstance(datePosition,tuple)
        assert isinstance(fontPos,int)
        assert isinstance(announcementText,str)
        assert isinstance(todayNDate,str)
        assert isinstance(img,PIL.PngImagePlugin.PngImageFile)
        assert isinstance(imgDraw,PIL.ImageDraw.ImageDraw)
        assert isinstance(font_type_date,PIL.ImageFont.FreeTypeFont)
        assert isinstance(font_type_announcement,PIL.ImageFont.FreeTypeFont)
        assert isinstance(font_type,PIL.ImageFont.FreeTypeFont)
        assert isinstance(font_type_firstName,PIL.ImageFont.FreeTypeFont)
        assert isinstance(botAddressPosition,tuple)
        assert len(botAddressPosition)==2
        assert isinstance(botAddressFont,str)
        assert isinstance(telIcon,PIL.PngImagePlugin.PngImageFile )
    
    @pytest.mark.parametrize("lan,firstName",[
        ("Per","خفن خان اصل مکزیکی فرد بلا منش فرفری پور مزدک مرام خفن خان اصل مکزیکی فرد بلا منش فرفری پور مزدک مرام"),
        ("En","میثم"),
        ("De","Röpke juliani Berlin Bayern muich stutgard losangles heideger Röpke juliani Berlin Bayern muich stutgard losangles heideger"),
        ("En","Alison where do you live, what color do you like when you r going to sleep at night? "),
        ("De","خفن خان اصل مکزیکی فرد بلا منش فرفری پور مزدک مرام خفن خان اصل مکزیکی فرد بلا منش فرفری پور مزدک مرام"),
        ("Per","Röpke juliani Berlin Bayern muich stutgard losangles heideger Röpke juliani Berlin Bayern muich stutgard losangles heideger"),
        ("En","میثم  خفن خان اصل مکزیکی فرد بلا منش فرفری پور مزدک مرام خفن خان اصل مکزیکی فرد بلا منش فرفری پور مزدک مرام")

    ])
    #TODO_done test_correctFirstName(self,lan,firstName,going):
    def test_correctFirstName(self,lan,firstName,going):
        firstNameOutPut = going.correctFirstName(firstName,lan)
        assert isinstance(firstNameOutPut,str)
        assert len(firstNameOutPut)<26
        if lan != "Per":
            listFirstname = list(firstNameOutPut)
            count = len(listFirstname)
            assert firstNameOutPut[count-1] ==  ","
            assert firstNameOutPut[count-2] ==  " "
        else:
            listFirstname = list(firstNameOutPut)
            count = len(listFirstname)
            assert firstNameOutPut[count-1] !=  " "
        langFirstName = detect(firstName)
        if  langFirstName == "fa" or langFirstName == "ar" or langFirstName == "ur":
            reshape_textFirstName = arabic_reshaper.reshape(firstName)
            if len(firstName)>25:
                assert len(firstName)-2 == len(reshape_textFirstName)
            else:
                assert len(firstName) == len(reshape_textFirstName)

            with pytest.raises(langdetect.lang_detect_exception.LangDetectException) as exp:
                detect(firstNameOutPut)
            assert str(exp.value)== 'No features in text.'

    @pytest.mark.parametrize("mergeCard",[
    ("addCard_shapeFrame_1"),
    ("addCard_shapeFrame_2"),
    ("addCard_shapeFrame_3"),
    ("addCard_shapeFrame_4"),
    ("addCard_shapeFrame_5"),
    ("addCard_shapeFrame_6")
    ])
    #TODO_done test_mergeAdding
    def test_mergeAdding(self,mergeCard,addCard_shapeFrameValues,going):
        firstName,lan,frame,stayBoxArray,frameType = addCard_shapeFrameValues[mergeCard]
        img,imgDraw = going.mergeAdding(firstName,lan,frame,stayBoxArray,frameType)
        assert isinstance(img,PIL.PngImagePlugin.PngImageFile)
        assert isinstance(imgDraw,PIL.ImageDraw.ImageDraw)

    @pytest.mark.parametrize("goingOneFrame",[
    ("goingOneFrame_1"),
    ("goingOneFrame_2"),
    ("goingOneFrame_3"),
    ("goingOneFrame_4")
    ]) 
    #TODO_done test_goingList(self,firstName,lan,countOfFrame,first,last)
    def test_goingList(self,goingOneFrame,goingOneFrameValues,going):
        # return firstName,lan,countOfFrameGoing,countOfFrameReturning,verticalGoing,verticalReturning,first,last
        firstName,lan,countOfFrameGoing,_,verticalGoing,_,first,last = goingOneFrameValues[goingOneFrame]
        goingPics,lastStayBoxArray,stayBoxArray = going.goingList(firstName,lan,countOfFrameGoing,verticalGoing,first,last)
        
        
        assert isinstance(goingPics,list)
        for i in range(len(goingPics)):
            assert isinstance(goingPics[i],PIL.PngImagePlugin.PngImageFile)
        assert isinstance(lastStayBoxArray,list)
        assert len(lastStayBoxArray) == 8
        assert lastStayBoxArray[0][0] == 0
        assert lastStayBoxArray==stayBoxArray
        lba = 0
        l = 0
        print(f"{first            = }\n{lastStayBoxArray = }\n{last             = }\n\n")
        for i in range(len(last)):
            l = l +last[i][0]
            lba = lba + lastStayBoxArray[i][0]

        assert l == lba
        print(f"{l = }\n{lba = }")
        
        #FIXME lastStayBoxArray[7][0]
        # assert lastStayBoxArray[7][0]== last[7][0]
        for i in range(len(last)-1):
            print(f"{i = }")
            if i != 1:
                assert last[i][0]<lastStayBoxArray[i][0] or last[i][0]==lastStayBoxArray[i][0]

@pytest.fixture
def returning():
    returning = VS.Returning()
    yield returning

class TestReturning:

    @pytest.mark.parametrize("returningOneFrame",[
    ("goingOneFrame_1"),
    ("goingOneFrame_2"),
    ("goingOneFrame_3"),
    ("goingOneFrame_4")
    ]) 
    #TODO_done test_ReturningOneFrameIndex0
    def test_ReturningOneFrameIndex0(self,returningOneFrame,goingOneFrameValues,going,returning):
        # firstName,lan,countOfFrameGoing,countOfFrameReturning,verticalGoing,verticalReturning,first,last
        firstName,lan,countOfFrameGoing,countOfFrameReturning,verticalGoing,verticalReturning,first,last = goingOneFrameValues[returningOneFrame]
        
        _,lastStayBoxGoing,_ =going.goingList(firstName,lan,countOfFrameGoing,verticalGoing,first,last)
        
        stayBoxArray = lastStayBoxGoing.copy()
        frame = going.makeBlankList(last)
        verticalArray = []
        
        for i in range(len(last)-1):
            if last[i][0]<lastStayBoxGoing[i][0]:
                subtraction = lastStayBoxGoing[i][0] - last[i][0] 
                # verticalArray = []
                for j in range(countOfFrameReturning) :
                    stayTemp = stayBoxArray.copy()
                    stayBoxArray,frame,verticalArray = returning.get_stayBoxArrayNFrameRe(i,j,countOfFrameReturning,last,stayBoxArray,frame,lastStayBoxGoing,verticalReturning,verticalArray)
                    print(f"{lastStayBoxGoing = }\n{stayBoxArray     = }\n{last             = }\n\n")

                    if j == 0:
                        assert frame[i][0] == 0 
                        assert stayBoxArray[i][0] != 0
                    elif j>(countOfFrameReturning/10) and j < (4*countOfFrameReturning/5):
                        #  if i+1 == 7 :
                        #      assert stayBoxArray[7][0] == last[7][0]
                        #  else:
                         assert stayBoxArray[i][0] == last[i][0]
                         assert frame[i][0] == subtraction
                         assert frame[i][0] != 0
                    elif j> (9*countOfFrameReturning/10):
                         assert   frame[i][0] == 0

                         assert stayBoxArray[1][0] == stayTemp[1][0] + (lastStayBoxGoing[i][0]-last[i][0])   
                        #  assert stayBoxArray[i+1][0] == last[i+1][0]
                        #  assert stayBoxArray[i][0]==subtraction+lastStayBoxGoing[i][0]
                        #  assert stayBoxArray[i][0]==lastStayBoxGoing[i][0]-subtraction
        for i in range(len(last)):
            # print(f"{last = }\n{stayBoxArray = }\n{lastStayBoxGoing = }")
            print(f"{lastStayBoxGoing = }\n{stayBoxArray     = }\n{last             = }\n\n")
            assert stayBoxArray[i][0] == last[i][0]

    @pytest.mark.parametrize("returningOneFrame",[
    ("goingOneFrame_1"),
    ("goingOneFrame_2"),
    ("goingOneFrame_3"),
    ("goingOneFrame_4")
    ]) 
    #TODO_done test_ReturningOneFrameIndex1
    def test_ReturningOneFrameIndex1(self,returningOneFrame,goingOneFrameValues,going,returning):
        # firstName,lan,countOfFrameGoing,countOfFrameReturning,verticalGoing,verticalReturning,first,last
        firstName,lan,countOfFrameGoing,countOfFrameReturning,verticalGoing,verticalReturning,first,last = goingOneFrameValues[returningOneFrame]
        # return goingPics,lastStayBoxArray,stayBoxArray
        _,lastStayBoxGoing,_ =going.goingList(firstName,lan,countOfFrameGoing,verticalGoing,first,last)
        stayBoxArray = lastStayBoxGoing.copy()
        # frame = going.makeBlankList(last)
        verticalArray = []
        for i in range(len(last)-1):
            frame = going.makeBlankList(last)
            if last[i][0]<lastStayBoxGoing[i][0]:
                # horizentalDistance =   last[i][1]-last[1][1]
                partSize,_ = returning.horizentalDistanceFuncRe(last,i,countOfFrameReturning)
                for j in range(countOfFrameReturning) :
                    if last[i][0]<lastStayBoxGoing[i][0]:
                        tempFrameInx1 = frame[i][1]    
                        # partSize,_ = self.returning.horizentalDistanceFuncRe(last,i,countOfFrame)
                        stayBoxArray,frame,verticalArray = returning.get_stayBoxArrayNFrameRe(i,j,countOfFrameReturning,last,stayBoxArray,frame,lastStayBoxGoing,verticalReturning,verticalArray)
                        # print(f"{frame = }")
                        # assert frame[i][1]== frame[i][1] - horizentalDistance/countOfFrame
                        if lan == "Per":
                            assert first[i][1]<frame[i][1]
                        else:

                            assert first[i][1]>frame[i][1]
                                    # partSize,_ = self.horizentalDistanceFuncRe(last,i,countOfFrame)
                        
                        assert frame[i][1] == tempFrameInx1-partSize
                        # if (j+1) == countOfFrame:

                        #     if lan == "Per":
                        #         assert frame[i][1] <first[1][1] and frame[i][1] >first[2][1]
                        #     else:
                        #         assert frame[i][1] >first[1][1] and frame[i][1] <first[2][1]
        # if lan = "Per":      
        #     xYAxis = [(1146, 598),(933, 598), (760, 598), (599, 598), (435, 598), (269, 598), (109, 598), (185, 234)]
        # else:
        #     xYAxis = [(50, 598),(295, 598), (462, 598), (622, 598), (787, 598), (955, 598), (1118, 598), (1021, 235)]
        # return xYAxis


    @pytest.mark.parametrize("returningOneFrame",[
    ("goingOneFrame_1"),
    ("goingOneFrame_2"),
    ("goingOneFrame_3"),
    ("goingOneFrame_4")
    ]) 
    #TODO_done test_ReturningOneFrameIndex2
    def test_ReturningOneFrameIndex2(self,returningOneFrame,goingOneFrameValues,going,returning):
        #     return firstName,lan,countOfFrameGoing,countOfFrameReturning,verticalGoing,verticalReturning,first,last
        firstName,lan,countOfFrameGoing,countOfFrameReturning,verticalGoing,verticalReturning,first,last = goingOneFrameValues[returningOneFrame]

        _,lastStayBoxGoing,_ =going.goingList(firstName,lan,countOfFrameGoing,verticalGoing,first,last)
        stayBoxArray = lastStayBoxGoing.copy()
        frame = going.makeBlankList(last)
        blankList = going.makeBlankList(last)
        halfCount = int(countOfFrameReturning/2)
        # vertical = verticalReturning
        section = verticalReturning/halfCount
        for i in range(len(last)-1):
            if last[i][0]<lastStayBoxGoing[i][0]:
                verticalArray=[]
                for j in range(countOfFrameReturning) :
                    stayBoxArray,frame,verticalArray = returning.get_stayBoxArrayNFrameRe(i,j,countOfFrameReturning,last,stayBoxArray,frame,lastStayBoxGoing,verticalReturning,verticalArray)
                    assert frame[i][2] == verticalArray[j]
                    if j == 0:
                        assert frame[i][2] ==blankList[i][2] - (section*j)
                        assert frame[i][2] == blankList[i][2]
                        
                    elif j<halfCount and j !=0:
                        # print(f"{i = },{j = },{frame = }\n{verticalArray =}\n{verticalArray[j-1] = }- {(section*j) = }\n{verticalArray[j-1] - (section*j) = }\n{frame[i][2] = }\n\n")
                        assert frame[i][2]== verticalArray[j-1] - (section*j)
                        assert verticalArray [j-1] > verticalArray [j]
                        
                    elif j == halfCount:
                        assert frame[i][2] == verticalArray [j-1]
                    else:
                        assert verticalArray [j-1] < verticalArray [j]
                        assert verticalArray[j-1] < frame[i][2] 


    @pytest.mark.parametrize("goingOneFrame",[
    ("goingOneFrame_1"),
    ("goingOneFrame_2"),
    ("goingOneFrame_3"),
    ("goingOneFrame_4")
    ])                
    #TODO_done test_returningList
    def test_returningList(self,goingOneFrame,goingOneFrameValues,going,returning):
        # firstName,lan,countOfFrameGoing,countOfFrameReturning,verticalGoing,verticalReturning,first,last
        firstName,lan,countOfFrameGoing,countOfFrameReturning,verticalGoing,verticalReturning,first,last=goingOneFrameValues[goingOneFrame]       
        _,lastStayBoxGoing,stayBoxArrayGoing = going.goingList(firstName,lan,countOfFrameGoing,verticalGoing,first,last)
        assert isinstance(lastStayBoxGoing,list)
        assert len(lastStayBoxGoing) == 8
        assert lastStayBoxGoing[0][0] == 0
        assert lastStayBoxGoing==stayBoxArrayGoing
         #def returningList(self,firstName,lan,countOfFrame,verticalReturning,lastStayBoxGoing,last):
        returningPics,img,imgDraw,lastStayBoxArrayReturning  = returning.returningList(firstName,lan,countOfFrameReturning,verticalReturning,lastStayBoxGoing,last)
        assert isinstance(returningPics,list)
        for i in range(len(returningPics)):
            assert isinstance(returningPics[i],PIL.PngImagePlugin.PngImageFile)
        # print(f"{type(imgDraw)}")
        
        assert isinstance(imgDraw,PIL.ImageDraw.ImageDraw)
        assert isinstance(img,PIL.PngImagePlugin.PngImageFile)
        print(f"{lastStayBoxGoing          = }\n{lastStayBoxArrayReturning = }\n{last                      = }\n\n")
        for i in range(len(last)):
            assert last[i][0]==lastStayBoxArrayReturning[i][0]

    @pytest.mark.parametrize("lan,firstName,goingOneFrame",[
    ("Per","خفن خان","goingOneFrame_1"),
    ("En","میثم","goingOneFrame_2"),
    ("De","Röpke","goingOneFrame_3"),
    ("En","Alison","goingOneFrame_4")
    ])
    #TODO test_botAdressframe(self)
    def test_botAdressframe(self,lan,firstName,goingOneFrame,goingOneFrameValues,going,returning):
        # firstName,lan,countOfFrameGoing,countOfFrameReturning,verticalGoing,verticalReturning,first,last
        firstName,lan,countOfFrameGoing,countOfFrameReturning,verticalGoing,verticalReturning,first,last=goingOneFrameValues[goingOneFrame]
        _,lastStayBoxGoing,_ = going.goingList(firstName,lan,countOfFrameGoing,verticalGoing,first,last)
        _,_,_,lastStayBoxArrayReturning = returning.returningList(firstName,lan,countOfFrameReturning,verticalReturning,lastStayBoxGoing,last)
        countOfFrameBot = 40
        bAframe,fontSizeList = returning.botAddressframe(lan,firstName,lastStayBoxArrayReturning)
        # bAframe,fontSizeList = returning.botAddressframe(img,imgDraw,lan,firstName)
        assert isinstance(bAframe,list)
        assert len(bAframe)==countOfFrameBot
        assert isinstance(fontSizeList,list)
        assert len(fontSizeList)==countOfFrameBot

        for i in range(countOfFrameBot):
            assert isinstance(bAframe[i],PIL.PngImagePlugin.PngImageFile)
            assert isinstance(fontSizeList[i],int)
            if i<19:
                assert fontSizeList[i]+2==fontSizeList[i+1]
            elif i==19:
                assert fontSizeList[i]-2 ==fontSizeList[i-1]
            elif i ==39:
                assert fontSizeList[i]+2==fontSizeList[i-1]
            else:
                assert fontSizeList[i]==fontSizeList[i+1]+2

@pytest.fixture
def video():
    video = VS.Video()
    yield video


class TestVideo:
    # def __init__(self):
    #     self.frameArray=[]
    #     self.idArray=[]
    @pytest.mark.parametrize("lists",[
        (([1,5,6],[9,939,2923,23,4],[0,3,5,66,2,456,867,234,645])),
        (([0,9,2,3,5],[2,3]))

    ])
    def test_MergeAllList_1(self,lists,video):
        output = video.mergeAllList(*lists)
        sum = []
        for i in range(len(lists)):
            sum = sum + lists[i]
        assert len(output) == len(sum) 
        assert isinstance(output,list)
      
        for i in lists:
            assert isinstance(i,list)

        indx = 0 
        for oneList in lists:
            for i in range(len(oneList)):
                assert oneList[i]==output[i+indx]
            indx = indx + len(oneList)

        for i in range(len(sum)):
                assert sum[i] == output[i]  
                

    @pytest.mark.parametrize("goingOneFrame",[
    ("goingOneFrame_1"),
    ("goingOneFrame_2"),
    ("goingOneFrame_3"),
    ("goingOneFrame_4")
    ]) 
    def test_MergeAllList_2(self,goingOneFrame,goingOneFrameValues,video,going,returning):
        # return firstName,lan,countOfFrameGoing,countOfFrameReturning,verticalGoing,verticalReturning,first,last
        firstName,lan,countOfFrameGoing,countOfFrameReturning,verticalGoing,verticalReturning,first,last=goingOneFrameValues[goingOneFrame]
        goingPics,lastStayBoxGoing,_ = going.goingList(firstName,lan,countOfFrameGoing,verticalGoing,first,last)
        returningPics,_,_,lastStayBoxArrayReturning  = returning.returningList(firstName,lan,countOfFrameReturning,verticalReturning,lastStayBoxGoing,last)
        bAPics,_ = returning.botAddressframe(lan,firstName,lastStayBoxArrayReturning)

        output = video.mergeAllList(goingPics,returningPics,bAPics)
        lists = (goingPics,returningPics,bAPics)
        sum = []
        for i in range(len(lists)):
            sum = sum + lists[i]
        assert len(output) == len(sum)
        assert isinstance(output,list)
      
        for i in lists:
            assert isinstance(i,list)

        indx = 0 
        for oneList in lists:
            for i in range(len(oneList)):
                assert oneList[i]==output[i+indx]
            indx = indx + len(oneList)

        for i in range(len(sum)):
                assert sum[i] == output[i]  
                assert isinstance(sum[i],PIL.PngImagePlugin.PngImageFile) 
        # print(f"{first = } \n{last = }")
        return output


    # @pytest.mark.parametrize("goingOneFrame,id",[
    # ("goingOneFrame_1",12344),
    # ("goingOneFrame_2",1245234),
    # ("goingOneFrame_3",989758),
    # ("goingOneFrame_4",9345765)
    # ]) 
    def test_thread_frame(self,frameArr):  

        # frame = self.test_MergeAllList_2(goingOneFrame,goingOneFrameValues,video,going,returning)
        # path=video.dRAdrs
        # self.frameArray.append(frame)
        # self.idArray.append(id)
        idArr = [12344,1245234]
        # numpy_image,img,size,pathNFile,out = video.videoOutput(frame,id)
        if len(frameArr)==2:
            for i in range(len(frameArr)):
                threading.Thread(target=video.videoOutput(frameArr[i],idArr[i]))


    @pytest.mark.parametrize("goingOneFrame,id",[
    ("goingOneFrame_1",12344),
    ("goingOneFrame_2",1245234),
    ("goingOneFrame_3",989758),
    ("goingOneFrame_4",9345765)
    ]) 
    # def test_videoOutput(self,goingOneFrame,goingOneFrameValues,video):
        # fps =10
    def test_videoOutput(self,id,goingOneFrame,goingOneFrameValues,video,going,returning):    
        frame = self.test_MergeAllList_2(goingOneFrame,goingOneFrameValues,video,going,returning)
        print(f"frame = {frame}")
        # path=video.dRAdrs
        # numpy_image,img,size,pathNFile,out = video.videoOutput(frame,id)
        # print(f"{type(numpy_image) = }")
        # assert isinstance(numpy_image,numpy.ndarray)
        # # print(f"{type(img) = }")
        # assert isinstance(img,numpy.ndarray)
        # assert len(size)==2
        # assert isinstance(size,tuple)
        # # print(f"{type(out) = }")
        # assert isinstance(out,cv2.VideoWriter)
        # # print(f"{type(pathNFile) = }")
        # assert isinstance(pathNFile,str)


@pytest.fixture
def releaseVideo():
    releaseVideo = VS.ReleaseVideo()
    yield releaseVideo

class TestReleaseVideo:
    # releaseVideo(self,id,firstName,lanuage,first,last)
    @pytest.mark.parametrize("goingOneFrame",[
    ("goingOneFrame_1"),
    ("goingOneFrame_2"),
    ("goingOneFrame_3"),
    ("goingOneFrame_4")
    ]) 
    def test_releaseVideo(self,goingOneFrame,goingOneFrameValues,going,returning,video,releaseVideo):
        firstName,lan,_,_,_,_,first,last=goingOneFrameValues[goingOneFrame]
        id = 000000
        # TestVideo
        # frames = TestVideo().test_MergeAllList_2(goingOneFrame,goingOneFrameValues,video,going,returning)

        pathNFile = releaseVideo.releaseVideo(id,firstName,lan,first,last)
        assert isinstance(pathNFile,str)
