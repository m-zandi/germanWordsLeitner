import pytest
import locale
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
import numpy as np
import imutils
from cv2 import cv2
import datetime
#font fix for persian
import arabic_reshaper
from bidi.algorithm import get_display
#
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

class Going:
    def __init__(self):
        #pc
        self.font_path = "./font"
        self.basePic_path = "./picLeitner"

        #server
        # self.font_path = r"C:\Users\Administrator\Downloads\j\w\mainV2\font"
        # self.basePic_path = r"C:\Users\Administrator\Downloads\j\w\mainV2\picLeitner"



    #TODO_done  goingList(self,firstName,lan,countOfFrame,first,last)
    #FIXed goingList
    def goingList(self,firstName,lan,countOfFrame,verticalGoing,first,last):
        blankList = self.makeBlankList(first)
        frame = blankList.copy()  
        stayBoxArray = first.copy()
        goingPics = []

        for i in range(len(first)-1):
            verticalArray = []   
            firstVerticalArray = []
            secondVerticalArray = []
            frame = blankList.copy() 
            for j in range(countOfFrame):
                # frame,stayBoxArray,verticalArray,firstVerticalArray,secondVerticalArray = self.get_stayBoxArrayNFrameGo(i,j,countOfFrame,first,last,stayBoxArray,frame,verticalArray,firstVerticalArray,secondVerticalArray)
                if  last[i+1][0] > first[i+1][0] or i ==0:
                    frame,stayBoxArray,verticalArray,firstVerticalArray,secondVerticalArray = self.get_stayBoxArrayNFrameGo(i,j,countOfFrame,first,last,stayBoxArray,frame,verticalGoing,verticalArray,firstVerticalArray,secondVerticalArray)
                    img,_=self.mergeAdding(firstName,lan,frame,stayBoxArray,frameType="Going")
                    goingPics.append(img)
                else:
                    pass
        lastStayBoxArray = stayBoxArray.copy()
        return goingPics,lastStayBoxArray,stayBoxArray

    #TODO_done mergeAdding merge all here
    #FIX mergeAdding      firstName,lan,frame,stayBoxArray,frameType
    def mergeAdding(self,firstName,lan,frame,stayBoxArray,frameType,fontSizeBot=None):
        #img,imgDraw,dearPosition,dearText,firstNamePosition,announcementText,announcementPosition,font_type_announcement,todayNDate,datePosition,font_type_date,fontPos,font_type,font_type_firstName,botAddressPosition
        img,imgDraw,dearPosition,dearText,firstNamePosition,announcementText,announcementPosition,font_type_announcement,todayNDate,datePosition,font_type_date,fontPos,font_type,font_type_firstName,botAddressPosition,botAddressFont,telIcon = self.lanOutputs(lan,firstName)
        self.addText(imgDraw,lan,firstName,firstNamePosition,font_type_firstName,announcementPosition,announcementText,font_type_announcement,dearText,dearPosition)  
        self.addDate(imgDraw,todayNDate,datePosition,font_type_date)
        self.addCard(firstName,lan,frame,frameType,stayBoxArray,imgDraw,fontPos,font_type)
        if fontSizeBot is not None:
            self.addBotAddress(img,imgDraw,fontSizeBot,botAddressPosition,botAddressFont)
            self.addIconTelegram(img,telIcon,fontSizeBot,botAddressPosition)
        # img.show() 
        return img,imgDraw
    # def addBotAddress(self,imgDraw,fontSize,botAddressPosition):
    #     fillPurple=(108,105,237,255)
    #     fillPink = (255,123,172,255)
    #     botAddress = "@gudwbot"
    #     with open(self.font_path+"\\"+"BAUHS93.TTF", "rb") as f:
    #         bytes_font_botAddress = BytesIO(f.read())
    #     font_type_botAddress = ImageFont.truetype(bytes_font_botAddress,fontSize)
    #     imgDraw.text(xy=botAddressPosition,text=str(botAddress),fill=fillPink,font=font_type_botAddress,stroke_fill=fillPurple,stroke_width=4)
    def addBotAddress(self,img,imgDraw,fontSize,botAddressPosition,botAddressFont):
        alfa = int(fontSize)
        x = botAddressPosition[0]+int(9*alfa/10)
        y = botAddressPosition[1]
        botAddressPosition=(x,y) 
        fillPurple=(108,105,237,255)
        fillPink = (255,123,172,255)
        botAddress = "gudwbot"
        with open(botAddressFont, "rb") as f:
            bytes_font_botAddress = BytesIO(f.read())
        font_type_botAddress = ImageFont.truetype(bytes_font_botAddress,fontSize)
        imgDraw.text(xy=botAddressPosition,text=str(botAddress),fill=fillPink,font=font_type_botAddress,stroke_fill=fillPurple,stroke_width=4)  
    
    def addIconTelegram(self,img,telIcon,fontSize,botAddressPosition):
        # tel = Image.open(r"D:\project\WoerterbuchProject\mainV2\picLeitner\tel~2_short.png")
        alfa = int(fontSize)
        x = (botAddressPosition[0]+int(9*alfa/10))-alfa
        y = botAddressPosition[1]+25
        telAddressPosition =(x,y)
        telResize = telIcon.resize((alfa,alfa))
        img.paste(telResize,telAddressPosition)
    
    #TODO_done addCard(self,firstName,lan,frame,stayBoxArray)
    def addCard(self,firstName,lan,frame,frameType,stayBoxArray,imgDraw,fontPos,font_type):
        alfa,beta = 70,102
        num = 10
        lastNum = num*3
        ###
        for y in range(len(stayBoxArray)):
                try:
                    cardNumStayBox = stayBoxArray[y][0]
                    pointLeftStayBox = stayBoxArray[y][1]
                    pointUperStayBox = stayBoxArray[y][2]
                    # size of card
                    distanceStayBox = lastNum /cardNumStayBox
                    for x in reversed(range(cardNumStayBox)):
                        shapeStayBox=self.addCard_shapeStayBox(lan,distanceStayBox,pointLeftStayBox,pointUperStayBox,x,alfa,beta)
                        imgDraw.rectangle(shapeStayBox,fill="white",outline="black",width = 1)
                    frameStayType = "StayType"
                    self.addNumber(frameStayType,imgDraw,lan,cardNumStayBox,pointLeftStayBox,pointUperStayBox,font_type,fontPos)

                except:
                    pass
            
                try:
                    cardNumFrame = frame[y][0]
                    pointLeftFrame = frame[y][1]
                    pointUperFrame = frame[y][2]
                    # size of card
                    distanceFrame = lastNum /cardNumFrame
                    for x in reversed(range(cardNumFrame)):
                        shapeFrame = self.addCard_shapeFrame(lan,distanceFrame,pointLeftFrame,pointUperFrame,x,alfa,beta)
                        imgDraw.rectangle(shapeFrame,fill="white",outline="black",width = 1)
                    self.addNumber(frameType,imgDraw,lan,cardNumFrame,pointLeftFrame,pointUperFrame,font_type,fontPos)
                except:
                    pass
        # img.show() 
        # return img


    def addCard_shapeStayBox(self,lan,distanceStayBox,pointLeftStayBox,pointUperStayBox,x,alfa,beta):
        if lan == "Per":
            shapeStayBox = [(pointLeftStayBox+distanceStayBox*x, pointUperStayBox-distanceStayBox*x), (pointLeftStayBox+alfa+distanceStayBox*x,  pointUperStayBox+beta-distanceStayBox*x)]    
        else:
            shapeStayBox = [(pointLeftStayBox-distanceStayBox*x, pointUperStayBox-distanceStayBox*x), (pointLeftStayBox+alfa-distanceStayBox*x,  pointUperStayBox+beta-distanceStayBox*x)]
        return shapeStayBox

    def addCard_shapeFrame(self,lan,distanceFrame,pointLeftFrame,pointUperFrame,x,alfa,beta):
        if lan == "Per":
            shapeFrame = [(pointLeftFrame+distanceFrame*x, pointUperFrame-distanceFrame*x), (pointLeftFrame+alfa+distanceFrame*x,  pointUperFrame+beta-distanceFrame*x)]
        else:
            shapeFrame = [(pointLeftFrame-distanceFrame*x, pointUperFrame-distanceFrame*x), (pointLeftFrame+alfa-distanceFrame*x,  pointUperFrame+beta-distanceFrame*x)]
        return shapeFrame
    def addNumber(self,frameType,imgDraw,lan,cardNum,pointLeft,pointUper,font_type,fontPos):
        if frameType == "Going":
            fillColor = (57,255,20,255)
            cardNumStr = str(cardNum)
            cardNumOut =  "+"+cardNumStr
        elif frameType == "Returning":
            #other
            fillColor = (181,179,92,255)
            #brown
            # fillColor = (129,63,11,255)
            cardNumStr = str(cardNum)
            cardNumOut = "-" + cardNumStr
        else:
            fillColor = "blue"
            cardNumOut = str(cardNum)
        plus = 0
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

        shapeText = (pointLeft+fontPos/space+plus, pointUper-fontPos)
        # print(f"{shapeText =}")
        imgDraw.text(xy=shapeText,text=cardNumOut,fill=fillColor,font=font_type)
        return shapeText


    def addText(self,imgDraw,lan,firstName,firstNamePosition,font_type_firstName,announcementPosition,announcementText,font_type_announcement,dearText,dearPosition):
        # fillPink = (255,123,172,255)
        fillPink = "pink"
        ###firstName###
        firstName = self.correctFirstName(firstName,lan)
        imgDraw.text(xy=firstNamePosition,text=str(firstName),fill=fillPink,font=font_type_firstName,stroke_fill = (108,105,237,255),stroke_width=2)
        ## dear in persian ##
        if lan == "Per":
            imgDraw.text(xy=dearPosition,text=str(dearText),fill=fillPink,font=font_type_announcement,stroke_fill = (108,105,237,255),stroke_width=2)
        ### announcementText ###
        imgDraw.text(xy=announcementPosition,text=str(announcementText),fill=fillPink,font=font_type_announcement,stroke_fill = (108,105,237,255),stroke_width=2)
    
    def addDate(self,imgDraw,todayNDate,datePosition,font_type_date):
        imgDraw.text(xy=datePosition,text=str(todayNDate),fill=(108,105,237,255),font=font_type_date)
        

    #TODO_done  correctFirstName(self,firstName,lan)
    def correctFirstName(self,firstName,lan):
        langFirstName = detect(firstName)
        # print(f"{langFirstName}")
        firstNameOut = ""
        # fnList = list(firstName)
        if len(firstName)>20:
            firstNameOut = firstName[:20-len(firstName)]+"..."
        else:
            firstNameOut = firstName
        if  langFirstName == "fa" or langFirstName == "ar" or langFirstName == "ur":
            ## make persian text firstName correct
            # print(f"{firstNameOut = }")
            reshape_textFirstName = arabic_reshaper.reshape(firstNameOut)
            firstNameOut = get_display(reshape_textFirstName)
            # print(f"{firstNameOut = }")
            # firstNameOutPut = firstNameOut
        if lan == "De" or lan== "En":
            firstNameOutPut = firstNameOut + " ,"
        else:
            firstNameOutPut = firstNameOut
        
        return firstNameOutPut

    #TODO_done lanOutputs(self,lan,firstName)
    def lanOutputs(self,lan,firstName):
        # with open(self.font_path+"\\"+"BAUHS93.TTF", "rb") as f:
        #     bytes_font_botAddress = BytesIO(f.read()) 
        # font_type_botAddress = ImageFont.truetype(bytes_font_botAddress,fontSize)
        botAddressFont = self.font_path+"\\"+"BAUHS93.TTF"
        telIcon = Image.open(self.basePic_path +"\\"+"tel.png")
        with open(self.font_path+"\\"+"arialbd.ttf", "rb") as f:
            firstName_Size = 50
            bytes_font_firstName = BytesIO(f.read())
        font_type_firstName = ImageFont.truetype(bytes_font_firstName,firstName_Size)
        now = datetime.datetime.now()
        dearPosition,dearText = None,None
        if lan == "Per":
            guideLineXPer = 1240
            # address = self.basePic_path +"\\"+ "Per_leitner Box‍.png"
            adrs = self.basePic_path +"\\"+ "PerLeitnerBox‍.png"
            
            img = Image.open(adrs)
            imgDraw = ImageDraw.Draw(img)
            fontPos = 140
            
            with open(self.font_path+"\\"+"TRAFFIC.TTF", "rb") as f:
                bytes_font = BytesIO(f.read())
            font_type = ImageFont.truetype(bytes_font,80)
            #FIXedME
            with open(self.font_path+"\\"+"Siavash.TTF", "rb") as f:
                fontSize_announcement =60
                bytes_font_announcement = BytesIO(f.read())
            font_type_announcement = ImageFont.truetype(bytes_font_announcement,fontSize_announcement)



            ## Date
            with open(self.font_path+"\\"+"TRAFFIC.ttf", "rb") as f:
                fontSize_date = 43
                bytes_font_date = BytesIO(f.read())
            font_type_date = ImageFont.truetype(bytes_font_date,fontSize_date)

            #### date
            #FIXME date per
            todayNDateSplit  = MsgPer().todayDate(now)
            ## make persian text today correct
            reshape_textDate = arabic_reshaper.reshape(todayNDateSplit)
            todayNDate = get_display(reshape_textDate)
            ##
            yDate = 79
            wDate, _ = imgDraw.textsize(todayNDate,font_type_date) #877 , 1240 = 369 #right number 778
            plusWDate = 12
            # print(f"{guideLineXPer} - {wDate}  = {guideLineXPer - wDate }")
            datePosition = (guideLineXPer -wDate +plusWDate ,yDate)
            ####
            #### announcement
            announcementTextSplit = MsgPer(firstName).leitnerChanges()
            ## make persian text announcement correct
            reshape_textAnnouncement = arabic_reshaper.reshape(announcementTextSplit)
            announcementText = get_display(reshape_textAnnouncement)
            ##
            wAnnouncement, _ = imgDraw.textsize(announcementText,font_type_announcement)
            announcementPosition = (guideLineXPer - wAnnouncement,196)
            #####
            #### first name
            
            # x_Axis_one_letter = 1230
            y_Axis = 135
            # firstName = self.correctFirstName(firstName)
            w, _ = imgDraw.textsize(firstName,font_type_firstName)
            # print(f"w = {w}")
            # (5*(wPage-w)/6,yDate)
            # x_Axis = 5*(wPage-w)/8
            
            x_Axis = guideLineXPer - w
            firstNamePosition = (x_Axis,y_Axis)
            #### dear
            # dear = MsgPer().dear()
            ## make persian text dear correct
            dearTextSplit = MsgPer(firstName).dear()
            reshape_textDear = arabic_reshaper.reshape(dearTextSplit)
            dearText = get_display(reshape_textDear)
            ##
            dearPosition = (x_Axis - 130 ,130)
            ## bot Address 
            botAddressPosition = (670,250)

            #output dearPosition,dearText,firstNamePosition,announcementPosition,announcementText,datePosition,todayNDate,fontPos,font_type
        elif lan == "En":
            adrs = self.basePic_path +"\\"+"EnLeitnerBox‍.png"
            img = Image.open(adrs)
            imgDraw = ImageDraw.Draw(img)
            fontPos = 140
            with open(self.font_path+"\\"+"BERNHC.TTF", "rb") as f:
                bytes_font = BytesIO(f.read())
            font_type = ImageFont.truetype(bytes_font,70)

            with open(self.font_path+"\\"+"GILSANUB.TTF", "rb") as f:
                bytes_font_announcement = BytesIO(f.read())
            font_type_announcement = ImageFont.truetype(bytes_font_announcement,40)
            with open(self.font_path+"\\"+"ELEPHNT.TTF", "rb") as f:
                bytes_font_date = BytesIO(f.read())
            font_type_date = ImageFont.truetype(bytes_font_date,33)
            # now = datetime.datetime.now()
            x_Axis = 160
            ## Date 
            try:
                locale.setlocale(locale.LC_TIME, ('en', 'UTF-8'))
            except:
                locale.setlocale(locale.LC_TIME, (""))
            todayNDate = now.strftime("%A, %B %d, %Y")
            datePosition = (x_Axis,44)
            ##
            #FIXedME datePosition en
            announcementText = MsgEn(firstName).leitnerChanges()
            announcementPosition = (20,106)
            ###
            firstNamePosition = (x_Axis,100)
            ## bot Address 
            botAddressPosition = (20,250)
            

            #output dearPosition,dearText,firstNamePosition,announcementPosition,announcementText,datePosition,todayNDate,fontPos
        elif lan == "De":
            adrs = self.basePic_path +"\\"+"DeLeitnerBox‍.png"
            img = Image.open(adrs)
            imgDraw = ImageDraw.Draw(img)
            fontPos = 140
            with open(self.font_path+"\\"+"BERNHC.TTF", "rb") as f:
                bytes_font = BytesIO(f.read())
            font_type = ImageFont.truetype(bytes_font,80)
            with open(self.font_path+"\\"+"GILSANUB.TTF", "rb") as f:
                bytes_font_announcement = BytesIO(f.read())
            font_type_announcement = ImageFont.truetype(bytes_font_announcement,40)
            with open(self.font_path+"\\"+"DSWallau.ttf", "rb") as f:
                bytes_font_date = BytesIO(f.read())
            font_type_date = ImageFont.truetype(bytes_font_date,36)
            # now = datetime.datetime.now()
            x_Axis = 140
            ## Date
            # weekDay = now.strftime("%A")
            # dictDay = {"Sunday":"Sontag","Monday":"Montag","Tuesday":"Dienstag","Wednesday":"Mittwoch","Thursday":"Donnerstag","Friday":"Freitag","Saturday":"Samstag"}
            # weekDayDe = dictDay[weekDay]
            # print(f"weekDayDe = {weekDayDe}")
            
            # todayNDateHalf = now.strftime("A%, %B %d, %Y")
            # todayNDate = weekDayDe+todayNDateHalf
            try:
                locale.setlocale(locale.LC_TIME, ('de', 'UTF-8'))
            except:
                locale.setlocale(locale.LC_TIME, 'deu_deu')
            todayNDate = now.strftime("%A, %B %d, %Y")
            try:
                locale.setlocale(locale.LC_TIME, ('en', 'UTF-8'))
            except:
                locale.setlocale(locale.LC_TIME, '')
            # print(f"todayNDate = {todayNDate}")
            datePosition = (x_Axis,44)
            
            ##
            announcementText = MsgDe(firstName).leitnerChanges()
            # userTest = announcementTextSplit.decode('utf-8') announcementTextSplit
            announcementPosition = (20,106)
            ###
            #FIXMEd firstNamePosition de
            firstNamePosition = (x_Axis+200,100)
            ## bot Address 
            botAddressPosition = (20,250)

        return img,imgDraw,dearPosition,dearText,firstNamePosition,announcementText,announcementPosition,font_type_announcement,todayNDate,datePosition,font_type_date,fontPos,font_type,font_type_firstName,botAddressPosition,botAddressFont,telIcon
    
   #TODO_done get_stayBoxArrayNFrameGo general test
    def get_stayBoxArrayNFrameGo(self,i,j,countOfFrame,first,last,stayBoxArray,frame,vertical = 100,verticalArray=[],firstVerticalArray=[],secondVerticalArray=[]):
        partSize,_ = self.horizentalDistanceFunc(first,i,countOfFrame)
        ## vertical variables
        # vertical = 100

        halfCount = int(countOfFrame/2)
        print(f"{halfCount = }\n{vertical = }\n\n")
        section = vertical/halfCount
        if i == 0:
            if j ==0:
            #     
                stayBoxArray[i] = self.tupleChange(first[i],0,first[i][0])
                frame[i] = self.tupleChange(frame[i],0,0)
            elif j> (countOfFrame/10) and j < (4*countOfFrame/5):

                stayBoxArray[i] = self.tupleChange(stayBoxArray[i],0,0)
                frame[i] = self.tupleChange(frame[i],0,first[i][0])
            elif j> (4*countOfFrame/5) :
                
                # stayBoxArray[i+1] = self.tupleChange(first[i+1],0,first[i][0] + first[i+1][0])
                stayBoxArray[1] = self.tupleChange(first[1],0,first[0][0] + first[1][0])
                frame[i] = self.tupleChange(frame[i],0,0)
                frame[i+1] = self.tupleChange(frame[i+1],0,0)
            # index one movement horizentally i = 0
            frame[i] = self.tupleChange(frame[i],1,frame[i][1]-partSize)


              
            
            ## vertical
            
            if j == 0 :
                frame[i] = self.tupleChange(frame[i],2,frame[i][2] - (section*j))
                verticalArray.append(frame[i][2])
            elif j<halfCount and j!=0 :
                frame[i] = self.tupleChange(frame[i],2,frame[i][2] - (section*j))
                verticalArray.append(frame[i][2])
            elif j == halfCount:
                reverseVerticalArray = []
                reverseVerticalArray = verticalArray.copy()
                reverseVerticalArray.reverse()
                verticalArray = verticalArray + reverseVerticalArray
                frame[i] = self.tupleChange(frame[i],2,verticalArray[j])
            else :
                frame[i] = self.tupleChange(frame[i],2,verticalArray[j])


        else:
            verticalDistance = False
            if  last[i+1][0] > first[i+1][0]:
                if j== 0:
                    frame[i] = self.tupleChange(frame[i],0,0)                
             
                elif j> (countOfFrame/15) and j < (4*countOfFrame/5): 
                    
                        frame[i] = self.tupleChange(frame[i],0,last[i+1][0] - first[i+1][0])
                        # stayBoxArray[i] = self.tupleChange(first[i+1],0,)
                        if i == 1:
                            stayBoxArray[i] = self.tupleChange(stayBoxArray[i],0,(first[0][0]+first[1][0]) - (last[i+1][0] - first[i+1][0]))
                        else:
                            stayBoxArray[i] = self.tupleChange(stayBoxArray[i],0,first[i][0] - (last[i+1][0] - first[i+1][0]))
                elif j> (4*countOfFrame/5) :
                    #i is 0 and i+1 is 1 it means from new words and first box we add them together
                    #FIXME stayBoxArray[i+1]
                    if i+1 ==7:
                        stayBoxArray[7] = self.tupleChange(first[7],0,last[7][0])
                
                        # stayBoxArray[i+1] = self.tupleChange(first[i+1],0,first[i][0] + first[i+1][0])
                    else:
                        stayBoxArray[i+1] = self.tupleChange(first[i+1],0,last[i+1][0])
                    frame[i] = self.tupleChange(frame[i],0,0)
                    frame[i+1] =  self.tupleChange(frame[i+1],0,0)

                if i+1==7:
                    verticalDistance =True 
                #index one movement  horizentally else
                frame[i] = self.tupleChange(frame[i],1,frame[i][1]-partSize)
                
                #FIXed index two else
                #FIXed movement learnet words    
                ### vertically movement
                section6N7 = (first[6][2]-first[7][2])/countOfFrame
                plusVertical = (first[6][2]-first[7][2])/15
                # for first half monhani
                firstCount = int(3*countOfFrame/5)
                #for full second monhani
                secondCount = int((2*countOfFrame/5)/2)

                if j==0:
                    if verticalDistance is True and j<firstCount:
                        firstVerticalArray = []
                        frame[i]=self.tupleChange(frame[i],2,first[6][2]-(section6N7*j))
                        firstVerticalArray.append(frame[i][2])

                    else:
                        # verticalArray = []
                        frame[i]=self.tupleChange(frame[i],2,frame[i][2]-(section*j))
                        verticalArray.append(frame[i][2])
                if j<halfCount and  j !=0:
                    #FIXed def get_stayBoxArrayNFrameGo() if j<halfCount and  j !=0: index2
                    if verticalDistance is True and j<firstCount:
                        
                        frame[i]=self.tupleChange(frame[i],2,first[6][2]-(section6N7*j))
                        firstVerticalArray.append(frame[i][2])

                    else:
                        frame[i]=self.tupleChange(frame[i],2,frame[i][2]-(section*j))
                        verticalArray.append(frame[i][2])

                elif j == halfCount:
                    if verticalDistance is True and j<firstCount:
                        
                        frame[i]=self.tupleChange(frame[i],2,first[6][2]-(section6N7*j))
                        firstVerticalArray.append(frame[i][2]) 

                    else:
                        reverseVerticalArray = verticalArray.copy()
                        reverseVerticalArray.reverse()
                        verticalArray = verticalArray + reverseVerticalArray
                        
                        frame[i] = self.tupleChange(frame[i],2,verticalArray[j])
                elif j>halfCount :
                    if verticalDistance is True and j<firstCount:
                        
                        frame[i]=self.tupleChange(frame[i],2,first[6][2]-(section6N7*j))
                        firstVerticalArray.append(frame[i][2])
                    
                    elif verticalDistance is True and ((j<firstCount+secondCount and j>firstCount)  or j==firstCount):
                        
                        frame[i]=self.tupleChange(frame[i],2,first[7][2]-(plusVertical*(j-firstCount)))
                        secondVerticalArray.append(frame[i][2])

                    elif verticalDistance is True and j==(firstCount+secondCount) :
                        reverseVerticalArray6N7 = secondVerticalArray.copy()
                        reverseVerticalArray6N7.reverse()
                        firstVerticalArray = firstVerticalArray + secondVerticalArray + reverseVerticalArray6N7
                        # print(f"firstVerticalArray = {firstVerticalArray} , j = {j}")
                        frame[i] = self.tupleChange(frame[i],2,firstVerticalArray[j])
                    elif verticalDistance is True and j<(firstCount+(2*secondCount)) :
                        # print(f"firstVerticalArray = {firstVerticalArray} , j = {j}")
                        frame[i] = self.tupleChange(frame[i],2,firstVerticalArray[j])
                    else:
                        # print(f"{frame[i] = }\n{verticalArray = }\n{firstVerticalArray = }\n{len(verticalArray) = }\n{j = }\n\n")
                        if len(verticalArray) !=0:
                            frame[i] = self.tupleChange(frame[i],2,verticalArray[j])
                        else:
                            pass
                        # pass1
        
        # print(f"frame[{i}] = {frame[i]}\nfirst[{i}] = {first[i]}")
    
        return frame,stayBoxArray,verticalArray,firstVerticalArray,secondVerticalArray





    def horizentalDistanceFunc(self,first,indexList,countOfFrame):
        horizentalDistance = first[indexList][1]-first[indexList+1][1]
        partSize = horizentalDistance/countOfFrame
        return  partSize,horizentalDistance

    def getValues(self,countOfFrame,vertical):
        halfCount = int(countOfFrame/2)
        section = vertical/halfCount
        return halfCount,section

    def makeBlankList(self,aList):
        blankList = aList.copy()
        for i in range(len(blankList)):
            blankList[i]=self.tupleChange(blankList[i],0,0)
        return blankList

    def get_xYAxises(self,lan):
        if lan == "Per":
            xYAxis = [(1146, 598),(933, 598), (760, 598), (599, 598), (435, 598), (269, 598), (109, 598), (185, 234)]
        else:
            xYAxis = [(50, 598),(295, 598), (462, 598), (622, 598), (787, 598), (955, 598), (1118, 598), (1021, 235)]
        return xYAxis
    def firstNLastTupleList8ElementList3ElementTuple(self,first,last,num,xYAxis):
        numList = [num]
        e8First = numList +first
        e8Last = [0] +last
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

    def tupleChange(self,arrayOneTupleElement,indexArrToChange,valueToChange):
        convTupToList = list(arrayOneTupleElement)
        convTupToList[indexArrToChange]=valueToChange
        convListToTuple = tuple(convTupToList)
        return convListToTuple

class Returning:
    def __init__(self):
        self.obj_Going = Going()
        # self.font_path = r"D:\project\WoerterbuchProject\mainV2\font"
        # self.basePic_path = r"D:\project\WoerterbuchProject\mainV2\picLeitner"
        self.font_path =  self.obj_Going.font_path
        self.basePic_path =  self.obj_Going.basePic_path
    # #TODO_done get_stayBoxArrayNFrameReReturn
    #FIXedME get_stayBoxArrayNFrameReReturn
    #FIXed get_stayBoxArrayNFrameRe
    def horizentalDistanceFuncRe(self,last,indexList,countOfFrame):
        horizentalDistance = last[indexList][1]-last[1][1]
        partSize = horizentalDistance/countOfFrame
        return  partSize,horizentalDistance

        
    def get_stayBoxArrayNFrameRe(self,i,j,countOfFrame,last,stayBoxArray,frame,lastStayBoxGoing,vertical = 40,verticalArray=[]):
        # vertical = 40
        halfCount = int(countOfFrame/2)
        section = vertical/halfCount
        # stayBoxTemp = 0
        # print(f"i = {i} , j = {j} , lastStayBoxGoing = {lastStayBoxGoing} , last = {last}")
        if last[i][0]<lastStayBoxGoing[i][0]:
            # horizentalDistance =   last[i][1]-last[0][1]
            # horizentalDistance =   stayBoxArray[i][1]-stayBoxArray[0][1]
            partSize,_ = self.horizentalDistanceFuncRe(last,i,countOfFrame)
            subtraction = lastStayBoxGoing[i][0]-last[i][0]
            if j == 0:
                frame[i] = self.obj_Going.tupleChange(frame[i],0,0)
            elif j>(countOfFrame/10) and j < (4*countOfFrame/5):
                frame[i] = self.obj_Going.tupleChange(frame[i],0,subtraction)
                stayBoxArray[i]=self.obj_Going.tupleChange(last[i],0,last[i][0])
                # stayBoxTemp = stayBoxArray[1][0]
            elif j> (9*countOfFrame/10):
                frame[i] = self.obj_Going.tupleChange(frame[i],0,0)
                # stayBoxArray[i]=self.obj_Going.tupleChange(last[i],0,lastStayBoxGoing[i][0]-subtraction) 
                #FIXME returning stayBoxArray
                # stayBoxArray[i]=self.obj_Going.tupleChange(last[i],0,last[i][0]) 
                # stayBoxArray[1] = self.obj_Going.tupleChange(last[1],0,lastStayBoxGoing[1][0] + (lastStayBoxGoing[i][0]-last[i][0]))
                stayBoxArray[1] = self.obj_Going.tupleChange(last[1],0,stayBoxArray[1][0] + (lastStayBoxGoing[i][0]-last[i][0]))
            #TODO horizental Index1    
            #   
            # frame[i]=self.obj_Going.tupleChange(frame[i],1,frame[i][1]-(horizentalDistance/countOfFrame)) 
            # frame[i]=self.obj_Going.tupleChange(frame[i],1,last[i][1]-((int(horizentalDistance/countOfFrame))*(j+1)))
            # partSize,_ = self.horizentalDistanceFuncRe(last,i,countOfFrame)
            frame[i] = self.obj_Going.tupleChange(frame[i],1,frame[i][1]-partSize)
            #FIXME horizental Index1 returning
            # frame[i] = self.obj_Going.tupleChange(frame[i],1,last[1][1])
            #TODO_doen vertical Index2
            if j == 0:
                frame[i]=self.obj_Going.tupleChange(frame[i],2,frame[i][2] - (section*j))
                verticalArray.append(frame[i][2])
            elif j<halfCount and j !=0:
                print(f"{i = },{j = },{frame = }\n{verticalArray =}\n{verticalArray[j-1] = }- {(section*j) = }\n{verticalArray[j-1] - (section*j) = }\n{frame[i][2] = }before\n\n")
                frame[i] = self.obj_Going.tupleChange(frame[i],2,frame[i][2] - (section*j))
                verticalArray.append(frame[i][2])
                print(f"{i = },{j = },{frame = }\n{verticalArray =}\n{verticalArray[j-1] = }- {(section*j) = }\n{verticalArray[j-1] - (section*j) = }\n{frame[i][2] = }after\n\n")
            elif j == halfCount:
                reverseVerticalArray = []
                reverseVerticalArray = verticalArray.copy()
                reverseVerticalArray.reverse()
                verticalArray = verticalArray + reverseVerticalArray
                frame[i] = self.obj_Going.tupleChange(frame[i],2,verticalArray[j])
            else:
                frame[i] = self.obj_Going.tupleChange(frame[i],2,verticalArray[j])
        # stayBoxArray = [(0, 50, 598), (4, 295, 598), (5, 462, 598), (10, 622, 598), (4, 787, 598), (5, 955, 598), (9, 1118, 598), (2, 1021, 235)]
        return stayBoxArray,frame,verticalArray

    #TODO_done returningList
    #FIX returningList
    def returningList(self,firstName,lan,countOfFrame,verticalReturning,lastStayBoxGoing,last):
        blankList = self.obj_Going.makeBlankList(last)
        # print(f"{last = }")
        """
            xYAxis = [(1146, 598),(933, 598), (760, 598), (599, 598), (435, 598), (269, 598), (109, 598), (185, 234)]
        else:
            xYAxis = [(50, 598),(295, 598), (462, 598), (622, 598), (787, 598), (955, 598), (1118, 598), (1021, 235)]
        """
        # countOfFrame = 20
        frame = blankList.copy()  
        stayBoxArray = lastStayBoxGoing.copy()
        returningPics = []
        img,imgDraw="",""
        for i in range(len(last)-1):
            verticalArray = []
            frame = blankList.copy()     
            for j in range(countOfFrame):
                #FIX_done returningList self.get_stayBoxArrayNFrameRe
                if last[i][0]<lastStayBoxGoing[i][0]:
                    # def get_stayBoxArrayNFrameRe(self,i,j,countOfFrame,last,stayBoxArray,frame,lastStayBoxGoing,vertical = 40,verticalArray=[]):

                    stayBoxArray,frame,verticalArray = self.get_stayBoxArrayNFrameRe(i,j,countOfFrame,last,stayBoxArray,frame,lastStayBoxGoing,verticalReturning,verticalArray)
                    img,imgDraw=self.obj_Going.mergeAdding(firstName,lan,frame,stayBoxArray,frameType="Returning")
                    returningPics.append(img)
                else:
                    pass
        # lastStayBoxArray = stayBoxArray.copy()
        # return returningPics,lastStayBoxArray,stayBoxArray
        # lastFrame = returningPics[countOfFrame-1]
        lastStayBoxArrayReturning = stayBoxArray.copy()
        return returningPics,img,imgDraw ,lastStayBoxArrayReturning  
    #TODO botAddressframe
    def botAddressframe(self,lan,firstName,lastStayBoxArrayReturning):
        self.font_path
        # open(self.font_path+"\\"+"BAUHS93.TTF", "rb") 
        # def makeBlankList(self,aList):
        frame = self.obj_Going.makeBlankList(lastStayBoxArrayReturning)
        # font_type_botAddress = ImageFont.truetype(bytes_font_botAddress,fontSize)
        # _,_,_,lastStayBoxArrayReturning=self.returningList()
        # _,_,_,_,_,_,_,_,_,_,_,_,_,_,botAddressPosition = self.obj_Going.lanOutputs(lan,firstName)
        countOfFrame = 40
        fontSize = 83
        # fillPurple=(108,105,237,255)
        # fillPink = (255,123,172,255)
        bAframe = []
        fontSizeList = []
        # botAddress = "@gudwbot"
        for i in range(countOfFrame):
            # imgDraw = ImageDraw.Draw(img)
            if i<(countOfFrame/2): 
                fontSize = fontSize + 2
            else:
                fontSize = fontSize - 2
            fontSizeList.append(fontSize)
            # mergeAdding(self,firstName,lan,frame,stayBoxArray,fontSizeBot=None):
            frameType = ""
            img,_=self.obj_Going.mergeAdding(firstName,lan,frame,lastStayBoxArrayReturning,frameType,fontSize)
            # addBotAddress(self,imgDraw,fontSize,botAddressPosition):
            # going.mergeAdding()
            # with open(self.font_path+"\\"+"BAUHS93.TTF", "rb") as f:
            #     bytes_font_botAddress = BytesIO(f.read())
            # font_type_botAddress = ImageFont.truetype(bytes_font_botAddress,fontSize)
            # imgDraw.text(xy=botAddressPosition,text=str(botAddress),fill=fillPink,font=font_type_botAddress,stroke_fill=fillPurple,stroke_width=4)
            bAframe.append(img)
        return bAframe,fontSizeList

class Video:
    def __init__(self):
        # pass
        #pc
        # self.dRAdrs = r"D:\project\WoerterbuchProject\mainV2\dailyReport"
        self.dRAdrs="./dailyReport"

        #server
        # self.dRAdrs = r"C:\Users\Administrator\Downloads\j\w\mainV2\dailyReport"
    def mergeAllList(self,*args):
        sum =[]
        for i in args:
            sum = sum +i
        return sum
    def videoOutput(self,frame_array,id):
    # def videoOutput(self,frame_array,pathOut= r'E:\tutorial\python\gif\video\newMethodVideo.mp4'):
        pathNFile = self.dRAdrs+"\\"+f"dR_{id}.mp4"
        fps = 10
        for i in range(len(frame_array)):

            #reading each files
            numpy_image=np.array(frame_array[i]) 


            # convert to a openCV2 image, notice the COLOR_RGB2BGR which means that 
            # the color is converted from RGB to BGR format
            img=cv2.cvtColor(numpy_image, cv2.COLOR_RGB2BGR) 

            height, width, _ = img.shape
            size = (width,height)
            
            #inserting the frame into an image array
            out = cv2.VideoWriter(pathNFile,cv2.VideoWriter_fourcc(*'DIVX'), fps, size)
        for i in range(len(frame_array)):
            # writing to a image array
            numpy_image=np.array(frame_array[i]) 
            img=cv2.cvtColor(numpy_image, cv2.COLOR_RGB2BGR)
            out.write(img)
        out.release()
        return numpy_image,img,size,pathNFile,out
class ReleaseVideo:
    def __init__(self):
        self.obj_Going= Going()
        self.obj_Returning = Returning()
        self.obj_Video = Video()
        # pass
    def mergeCardNumWFirstNLast(self,cardNum,first,last):
        cardNumList = [cardNum]
        firstOut = cardNumList+first
        lastOut = [0]+last
        return firstOut,lastOut
    def get_xYAxises(self,lan):
        if lan == "Per":
            xYAxis = [(1146, 598),(933, 598), (760, 598), (599, 598), (435, 598), (269, 598), (109, 598), (185, 234)]
        else:
            xYAxis = [(50, 598),(295, 598), (462, 598), (622, 598), (787, 598), (955, 598), (1118, 598), (1021, 235)]
        return xYAxis

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
    def releaseVideo(self,id,cardNum,firstName,language,firstIndex0,lastIndex0):
        verticalGoing = 40
        verticalReturning = 40
        countOfFrameGoing = 18
        countOfFrameReturning = 20
        # _,_,_,_,_,_,_,_=goingOneFrameValues[goingOneFrame]
        cardFirstIndex0,cardLastIndex0 = self.mergeCardNumWFirstNLast(cardNum,firstIndex0,lastIndex0)
        xYAxis = self.get_xYAxises(language)
        first,last =self.firstNLastTupleList8ElementList3ElementTuple(cardFirstIndex0,cardLastIndex0,xYAxis)


        goingPics,lastStayBoxGoing,_ = self.obj_Going.goingList(firstName,language,countOfFrameGoing,verticalGoing,first,last)
        returningPics,_,_,lastStayBoxArrayReturning  = self.obj_Returning.returningList(firstName,language,countOfFrameReturning,verticalReturning,lastStayBoxGoing,last)
        bAPics,_ = self.obj_Returning.botAddressframe(language,firstName,lastStayBoxArrayReturning)

        outputFrames = self.obj_Video.mergeAllList(goingPics,returningPics,bAPics)
        #numpy_image,img,size,pathNFile,out
        _,_,_,pathNFile,_ = self.obj_Video.videoOutput(outputFrames,id)
        return pathNFile