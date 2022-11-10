# برای استفاده از این کلاس ابتدا سرور یا پی سی ام اس ای بودن  را برای مقدار کایند(به انگلیسی)مشخص کنید
# ExportDb()exportCollectionSJson()
 # ExportDb()makeCollectionsZip()
#
#email
import sys
sys.path.append( "../")

from mainV2.base.ButtonsA import ButtonSame as ABtnS

from mainV2.base.Buttons import ButtonEn as EnBtn
from mainV2.base.ButtonsA import ButtonAdminEn as EnBtnA 
from mainV2.base.Buttons import ButtonDe as DeBtn
from mainV2.base.ButtonsA import ButtonAdminDe as DeBtnA 
from mainV2.base.Buttons import ButtonPer as PerBtn
from mainV2.base.ButtonsA import ButtonAdminPer as PerBtnA 
from mainV2.base.Buttons import ButtonSame as BtnS

import random

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

#telegram

from mainV2 import pybotc 
import requests
import pymongo


import simplejson as json
import codecs
from bson import json_util

# from bson.json_util import dumps
# import json
import zipfile
import os.path
import operator
import numpy as np 
import datetime
from datetime import timedelta
import calendar 
import convertdate
from convertdate import persian
from dateutil.relativedelta import relativedelta

class Db:
    def __init__(self):
            self.connection = pymongo.MongoClient("localhost",27017)
            self.database=self.connection["woerterbuch"]
            self.userCollection = self.database["user"]
            self.wordCollection = self.database["word"]
            self.meaningCollection = self.database["meaning"]
            self.bookCollection = self.database["book"]
            self.sectionCollection =  self.database["section"]
            self.settingCollection = self.database["setting"]
            self.backupCollection = self.database["backup"]
            # self.test2Collection = self.database["test2"]

    # def addCollection(self,colName,data):


    

    def addCollection(self,input):    
        # self.database[colName]
        client = pymongo.MongoClient("localhost",27017)
        # cars = [ {'name': 'Audi', 'price': 52642},
        #         {'name': 'Mercedes', 'price': 57127},
        #         {'name': 'Skoda', 'price': 9000},
        #         {'name': 'Volvo', 'price': 29000},
        #         {'name': 'Bentley', 'price': 350000},
        #         {'name': 'Citroen', 'price': 21000},
        #         {'name': 'Hummer', 'price': 41400},
        #         {'name': 'Volkswagen', 'price': 21600} ]
        

        with client:

            db = client.testdb

            # db = client.woerterbuch
            
            db.newone.insert_many(input)

#کلاس نام نویسی کاربر
class User:
        def __init__(self,id,firstName,last_Name=None,username=None):
            self.id = int(id)
            self.firstName = firstName
            self.lastName = last_Name
            self.username = username
            self.obj_RaveshYadgiri = RaveshYadgiri(self.id)
            self.obj_ShomarVazhgan = ShomarVazhgan(self.id)
            self.obj_Db = Db()
            # self.obj_lookingForUser = LookingForUser(self.id)

            #نام نویسی کاربر در پایگاه داده
        def registerGuest(self):
            #planA
            #FIXMEfixed "way":{"deutsch":False ,"english":False ,"synonym":False,"پارسی":False}
            userInfo = {"userId":self.id,"username":self.username,"firstName":self.firstName,"lastName":self.lastName,"deletedTimes":"","guestStartDay":datetime.datetime.now(),"userStartDay":"","nextTrainingDate":"","way":["persian","deutsch","english","synonym"],"temporary":{"rightWrongLampFlag":True,"automateMsgFlag":False},"todayWordsCorrection":"","report":False,"uILanguage":"Per","wordNumPerDay":0,"reportNum":0,"todayWordsNAnswer":"","reviewWords":"","plan":"Trial","userType":"guest","counter":0,"msgs":"","opinion":""}


            #planB
            #FIXMEfixed "way":{"deutsch":False ,"english":False ,"synonym":False,"پارسی":False}
            # userInfo = {"userId":self.id,"username":self.username,"firstName":self.firstName,"lastName":self.lastName,"guestStartDay":datetime.datetime.now(),"userStartDay":"","nextTrainingDate":"","way":{"deutsch":False ,"english":False ,"synonym":False,"پارسی":False},"temporary":{"rightWrongLampFlag":True,"automateMsgFlag":False},"todayWordsCorrection":"","report":False,"uILanguage":"","wordNumPerDay":0,"reportNum":0,"todayWordsNAnswer":"","reviewWords":"","plan":"","userType":"guest","counter":0,"msgs":""}

            self.obj_Db.userCollection.insert_one(userInfo)




        # update user or none user identity put it in analayze
        def updateIdentity(self):
            update = {"username":self.username,"firstName":self.firstName,"lastName":self.lastName}
            self.obj_Db.userCollection.update_many({"userId":self.id},{"$set":update})
        
       
        def updateNoneUserToSimple(self):
            update = {"userStartDay":datetime.datetime.now(),"userType":"user"}
            condition = {"userId":self.id,"$or":[{"userType":"guest"},{"userType":"deleted"}]}
            self.obj_Db.userCollection.update_many(condition,{"$set":update})


        def updateLastActiveDateNNum(self):
            numberOfActiveDays=0
            condition = {"userId":self.id}
            for col in self.obj_Db.userCollection.find(condition,{"numberOfActiveDays":1,"_id":0}):
                for keys in col.keys():
                        numberOfActiveDays = col[keys]
            numberOfActiveDays +=1
            update = {"activeDate":datetime.datetime.now(),"numberOfActiveDays":numberOfActiveDays}
            self.obj_Db.userCollection.update_many({"userId":self.id},{"$set":update})




        # if output is true we have this user otherwise we don't  
        def userIdentify(self):
            output = ""
            condition = {"userId":self.id,"userType":"user"}
            find = {"userId":1,"_id":0} 
            for col in self.obj_Db.userCollection.find(condition,find):
                    for keys in col.keys():
                        if self.id == col[keys]:
                            # print("this one is user")
                            output = True
            
            if output is True:
                self.updateIdentity()
            if output =="":
                self.guestIdentify()
                # print("this one is new guest" )
                output = False
            return output      


        
        def guestIdentify(self):
            condition = {"userId":self.id,"userType":"guest"} 
            find = {"userId":1,"_id":0}
            output = ""
            for col in self.obj_Db.userCollection.find(condition,find):
                    for keys in col.keys():
                        if self.id == col[keys]:
                            print(f"this one with id = {self.id} is geust")
                            output = True 
            if output is True:
                self.updateIdentity()
            elif output is not True:
                self.registerGuest()
                print(f"this one with id = {self.id} is new and visitor")
                output = False
            return output



class Admin:
        def __init__(self,id,firstName=None,last_Name=None,username=None):
            self.id = id
            self.firstName = firstName
            self.last_Name = last_Name
            self.username = username
            self.obj_Db = Db()
            self.obj_Msgs = Msg()
            self.obj_DateArrange = DateArrange()
        
        def changeAWordSection(self):
            self.obj_Db.sectionCollection.update_many({"word":"freuen [vr]"},{"$set":{"word":"sich freuen [vr]"}})


        ########ورزانش و اعمال تغییرات و دگرگونی ها به صورت کلی  ########
        ####past changed
        def changeNoneUserKindToUser(self):
            condition = {"userType":{"$eq":""}}
            find = {"userId":1,"firstName":1,"_id":0}
            beforArr = [col[keys] for col in self.obj_Db.userCollection.find(condition,find)for keys in col.keys()]
            self.obj_Db.userCollection.update_many(condition,{"$set":{"userType":"user"}})
            afterArr = [col[keys] for col in self.obj_Db.userCollection.find(condition,find)for keys in col.keys()]
            output = f"changeNoneUserKindToUser \nbeforArr = {beforArr}\n afterArr = {afterArr}"
            return output

        def makeFieldGuestStartDayToOldUsers(self): 
            condition = {"guestStartDay":{"$exists":False},"userType":"user"}
            find2 = {"userId":1,"firstName":1,"_id":0}
            beforArr = [col[keys] for col in self.obj_Db.userCollection.find(condition,find2)for keys in col.keys()]


            find = {"userId":1,"userStartDay":1,"_id":0}
            for col in self.obj_Db.userCollection.find(condition,find):
                id = 0
                userStartDay = ""
                for keys in col.keys():
                    if keys == "userId":
                        id = col[keys]
                    if keys == "userStartDay":
                        userStartDay = col[keys]
                    self.obj_Db.userCollection.update_many({"userId":id},{"$set":{"guestStartDay":userStartDay}})
            afterArr = [col[keys] for col in self.obj_Db.userCollection.find(condition,find2)for keys in col.keys()]
            output = f"makeFieldGuestStartDayToOldUsers \nbeforArr = {beforArr}\n afterArr = {afterArr}"
            return output

        def covertUserToGuestHasntStartDay(self):
            condition = {"userStartDay":{"$eq":""},"userType":"user"}
            find2 = {"userId":1,"firstName":1,"_id":0}
            beforArr = [col[keys] for col in self.obj_Db.userCollection.find(condition,find2)for keys in col.keys()]


            find = {"userId":1,"_id":0}
            for col in self.obj_Db.userCollection.find(condition,find):
                id = 0
                for keys in col.keys():
                    if keys == "userId":
                        id = col[keys]
                    self.obj_Db.userCollection.update_many({"userId":id},{"$set":{"userType":"guest"}})
            afterArr = [col[keys] for col in self.obj_Db.userCollection.find(condition,find2)for keys in col.keys()]
            output = f"covertUserToGuestHasntStartDay \nbeforArr = {beforArr}\n afterArr = {afterArr}"
            return output
       

        def deleteRepeatedRecord(self):
            find2 = {"userId":1,"_id":0}
            beforArr = []
            for col in self.obj_Db.userCollection.find({},find2):
                id = 0
                # i=0
                for keys in col.keys():
                    i=0
                    id = col[keys]
                    for col2 in self.obj_Db.userCollection.find({},find2):
                        id2 = 0
                        # i=0 #output empty
                        for keys in col2.keys():
                            id2 = col2[keys]
                            # i=0 #output empty
                            if id == id2:
                                i+=1
                                if 2 <=i:
                                    print(f"i = {i}")
                                    print(f"id  = {id} \nid2 = {id2}")
                                    if id not in beforArr:
                                        beforArr.append(id)


            for col in beforArr:
                self.obj_Db.userCollection.delete_one({"userId":col})


            afterArr = []
            for col in self.obj_Db.userCollection.find({},find2):
                id = 0
                # i=0
                for keys in col.keys():
                    i=0
                    id = col[keys]
                    for col2 in self.obj_Db.userCollection.find({},find2):
                        id2 = 0
                        # i=0 #output empty
                        for keys in col2.keys():
                            id2 = col2[keys]
                            # i=0 #output empty
                            if id == id2:
                                i+=1
                                if 2 <=i:
                                    print(f"i = {i}")
                                    print(f"id  = {id} \nid2 = {id2}")
                                    if id not in beforArr:
                                        afterArr.append(id)


            output = f"deleteRepeatedRecord \nbeforArr = {beforArr}\nafterArr = {afterArr}"
            # print(output)

            return output
        ####################################################

        # guestsNum
        def usersNum(self):
            condition = {"userType":"user"}
            users = []
            for col in self.obj_Db.userCollection.find(condition,{"userId":1,"_id":0}):
                for keys in col.keys():
                    users.append(col[keys])
            usersNum = len(users)
            print(f"usersNum = {usersNum}")
            return usersNum

        def guestsNum(self):
            condition = {"userType":"guest"}
            users = []
            for col in self.obj_Db.userCollection.find(condition,{"userId":1,"_id":0}):
                for keys in col.keys():
                    users.append(col[keys])
            usersNum = len(users)
            print(f"usersNum = {usersNum}")
            return usersNum

        
        #برای گزارش فراگیر از کاربران و میهمانان گرفتن نام ونام خانوادگی و نام کاربری و شماره چت  و تعداد روز استفاده از ربات به عنوان کاربر
        def getAllUsersInfoNuserStartDay(self):
            conditionUser = {"userType":"user"}
            outputArray = []
            output=""
            for col in self.obj_Db.userCollection.find(conditionUser,{"userId":1,"firstName":1,"lastName":1,"username":1,"userStartDay":1,"_id":0}):
                usersInfo = []
                for keys in col.keys():
                        if keys == "userStartDay":
                            tilNow = datetime.datetime.now() - col[keys]
                            # print(f"tilNow = {tilNow}")
                            usersInfo.append(tilNow.days)
                            # print(f"tilNow.days = {tilNow.days}")
                            usersInfo.append(f"Days={tilNow.days}")
                        elif keys == "userId":
                            usersInfo.append(f"Id={col[keys]}")                      
                        elif keys == "username":
                            # print(f"username = {col[keys]}")
                            if col[keys]=="":
                                usersInfo.append("UN = _____ ")
                            else:
                                usersInfo.append(f"UN=@{col[keys]}")
                        elif keys == "firstName":
                            # print(f"firstName = {col[keys]}")
                            usersInfo.append(f"FN={col[keys]}")
                        elif keys == "lastName":
                            if col[keys]=="":
                                usersInfo.append(":LN =")
                            else:
                                # print(f"lastName = {col[keys]}")
                                usersInfo.append(f"LN={col[keys]}")                        
                        else:
                            usersInfo.append(col[keys])

                        usersInfoTuple = tuple(usersInfo)

                # print(f"userInfo = {usersInfo}")              
                
                outputArray.append(usersInfoTuple)
            if len(outputArray) == 0:
                output = "هیچ کاربری تا این دم و لحظه ثبت نام نکرده است."
            else: 
                # print(f"output without sort= {output}")
                outputArray.sort(key = operator.itemgetter(4), reverse = True)
                ouputSeprarated = '\n'.join('{}'.format(item) for item in outputArray) 
                print(f"ouputSeprarated = {ouputSeprarated}")
                output = ouputSeprarated
            return output

        def getAllGuestsInfoNguestStartDay(self):
            conditionUser = {"userType":"guest"}
            outputArray = []
            output=""
            for col in self.obj_Db.userCollection.find(conditionUser,{"userId":1,"firstName":1,"lastName":1,"username":1,"guestStartDay":1,"_id":0}):
                guestsInfo = []
                for keys in col.keys():
                        if keys == "guestStartDay":
                            tilNow = datetime.datetime.now() - col[keys]
                            # print(f"tilNow = {tilNow}")
                            guestsInfo.append(tilNow.days)
                            # print(f"tilNow.days = {tilNow.days}")
                            guestsInfo.append(f"Days={tilNow.days}")
                        elif keys == "userId":
                            guestsInfo.append(f"Id={col[keys]}")                      
                        elif keys == "username":
                            # print(f"username = {col[keys]}")
                            if col[keys]=="":
                                guestsInfo.append("UN = _____ ")
                            else:
                                guestsInfo.append(f"UN=@{col[keys]}")
                        elif keys == "firstName":
                            # print(f"firstName = {col[keys]}")
                            guestsInfo.append(f"FN={col[keys]}")
                        elif keys == "lastName":
                            if col[keys]=="":
                                guestsInfo.append(":LN =")
                            else:
                                # print(f"lastName = {col[keys]}")
                                guestsInfo.append(f"LN={col[keys]}")                        
                        else:
                            guestsInfo.append(col[keys])

                        guestsInfoTuple = tuple(guestsInfo)

                # print(f"userInfo = {guestsInfo}")              
                
                outputArray.append(guestsInfoTuple)
            if len(outputArray) == 0:
                output = "هیچ میهمانی تا این دم و لحظه ثبت نام نکرده است."
            else: 
                # print(f"output without sort= {output}")
                outputArray.sort(key = operator.itemgetter(4), reverse = True)
                ouputSeprarated = '\n'.join('{}'.format(item) for item in outputArray) 
                print(f"ouputSeprarated = {ouputSeprarated}")
                output = ouputSeprarated
            return output

         #گرفتن نظرات براساس کاربر
        def takeOpinionsBaseOnEachUser(self):
            suggestersNum = 0
            opinionsNum = 0

            find = {"userId":1,"firstName":1,"opinion":1,"lastName":1,"username":1,"_id":0}
            condition = {"$and":[{"opinion":{ "$exists": True }},{"opinion":{ "$ne": "" }}]}
            # find2 = {"userId":1,"opinion":1,"_id":0}
            outputArray = []
            for col in self.obj_Db.userCollection.find(condition,find):

                usersInfo = []
                
                # print(f"col = {col}")
                for keys in col.keys():
                    # print(f"keys = {keys}")
                    if keys == "userId":
                        usersInfo.append(f"^^^ userId = {col[keys]}")
                        suggestersNum = suggestersNum +1
                    elif keys == "firstName":
                        usersInfo.append(f"FN = {col[keys]}")
                    elif keys == "lastName":
                        usersInfo.append(f"LN = {col[keys]}")
                    elif keys == "username":
                        usersInfo.append(f"UN = {col[keys]}")
                    elif keys == "opinion" :

                        print(f"col[keys] = {col[keys]}")
                        for alpha,yArray in col[keys].items():
                            # usersInfo.append(f"$$ Date = {alpha}")
                            dateGrigori = datetime.datetime.strptime(alpha,"%B_%d_%Y")
                            print(dateGrigori)
                            weakDay = dateGrigori.strftime("%A")
                            # monthAlpha,year,month,day,monthAlphaFinglish,weekDayPer,weekDayFinglish
                            _,year,month,day,_,_,_ = self.obj_DateArrange.convertToKhorshidi(dateGrigori)
                            print(year,month,day)        
                            dateKhorshid = f"{year}-{month}-{day}"
                            print(dateKhorshid)
                            usersInfo.append(f"$$ Date = {weakDay} # {alpha} ## {dateKhorshid}")

                            print(f"alpha = {alpha}")
                            print(f"yArray = {yArray}")
                            # print(f"yArray[0] = {yArray[0]}")
                            # print(f"yArray[1] = {yArray[1]}")
                            for xDict in yArray:
                                print(f"xDict = {xDict}")
                                for field,value in xDict.items():
                                    print(f"field = {field}")
                                    print(f"value = {value}")
                                    # if field =="timedate":
                                    #     # usersInfo.append(f"time = {value}")
                                    #     pass

                                    if field == "oPMsg":
                                        opinionsNum = opinionsNum +1
                                        usersInfo.append(f"& Opinion = {value}")
                                    elif field == "oPId":
                                        usersInfo.append(f"Opinion ID = {value}")

                                    
                                    usersInfoTuple = tuple(usersInfo)  
                                    print(f"usersInfoTuple = {usersInfoTuple}")

                          
                    # userinfoTuple = tuple(usersInfo)
                outputArray.append(usersInfoTuple)
            print(f"outputArray = {outputArray}")
            ouputSeprarated = str(outputArray)
            print(f"ouputSeprarated = {ouputSeprarated}")

            ouputSeprarated=ouputSeprarated.replace("^^^","\n\n")
            # print(f"ouputSeprarated = {ouputSeprarated}")
            ouputSeprarated=ouputSeprarated.replace("$$","\n   ")
            # print(f"ouputSeprarated = {ouputSeprarated}")
            ouputSeprarated=ouputSeprarated.replace("&","\n      ")   
            ouputSeprarated=ouputSeprarated.replace("[","")       
            ouputSeprarated=ouputSeprarated.replace("]","")
            ouputSeprarated=ouputSeprarated.replace("(","")
            ouputSeprarated=ouputSeprarated.replace(")","") 
            ouputSeprarated=ouputSeprarated.replace("'","")      
            print(f"ouputSeprarated = {ouputSeprarated}")
            return suggestersNum,opinionsNum,ouputSeprarated





    
        #گرفتن تعداد افراد کنشگر امروز
        def getTodayActivesNum(self):
            users = []
            # titr = self.msgsDateAlpha()
            titr = self.obj_Msgs.msgsDateAlpha()
            for col in self.obj_Db.userCollection.find({f"msgs.{titr}":{"$exists":"true"}},{"userId":1,"_id":0}):
                for keys in col.keys():
                    users.append(col[keys])
            usersNum = len(users)
            return usersNum

        #گرفتن تعداد کاربران کنشگر امروز
        def getTodayActiveUsersNum(self):
            titr = self.obj_Msgs.msgsDateAlpha()
            condition = {f"msgs.{titr}":{"$exists":"true"},"userType":"user"}
            users = []
            # titr = self.msgsDateAlpha()

            for col in self.obj_Db.userCollection.find(condition,{"userId":1,"_id":0}):
                for keys in col.keys():
                    users.append(col[keys])
            usersNum = len(users)
            return usersNum

        #گرفتن تعداد میهمانان کنشگر امروز
        def getTodayActiveGuestsNum(self):
            titr = self.obj_Msgs.msgsDateAlpha()
            condition = {f"msgs.{titr}":{"$exists":"true"},"userType":"guest"}
            guests = []
            # titr = self.msgsDateAlpha()
            for col in self.obj_Db.userCollection.find(condition,{"userId":1,"_id":0}):
                for keys in col.keys():
                    guests.append(col[keys])
            guestsNum = len(guests)
            return guestsNum    

        # get messages today of all users
        def getMessagesTodayOfAll(self):
            now = datetime.datetime.now()
            # print(now)
            field = now.strftime("%B_%d_%Y")
            print(field)
            allTodayMsgs = []
            try:
                for col in self.obj_Db.userCollection.find({f"msgs.{field}":{"$exists":"true"}},{f"msgs.{field}":1,"_id":0}):
                    # print(f"col = {col}")
                    for keys in col:
                        # print(f"col[keys][field] = {col[keys][field]}")
                        for middleCol in col[keys][field]:
                            # print(f"middleCol = {middleCol}")
                            for filedL,valueL in middleCol.items():
                                if filedL == "msg":
                                    allTodayMsgs.append(valueL)
                                # print(f"fieldL = {filedL} \n valueL = {valueL}")
                        
            except:
                print("today we don't have msgs")       
            # print(f"allTodayMsgs = {allTodayMsgs}")
            return allTodayMsgs
    

     
        # گرفتن نام و نام خانواردگی نام کاربری شماره چت افراد کنشگر امروز
        def getActiveUsersInfo(self):
            titr = self.obj_Msgs.msgsDateAlpha()
            # titr = self.msgsDateAlpha()
            condition = {f"msgs.{titr}":{"$exists":"true"},"userType":"user"}
            find = {"userId":1,"firstName":1,"lastName":1,"username":1,"userStartDay":1,"_id":0}
            output=""
            outputArray = []
            for col in self.obj_Db.userCollection.find(condition,find):
                usersInfo = []
                #   print(f"col = {col}")
                for keys in col.keys():
                        # print(f"col.keys() = {col.keys()}")
                        # print(f"keys = {keys}")
                        # print(f"col[keys] = {col[keys]}")
                        # getUserTrasNum
                        if keys == "userId":
                            numTrans = self.getUserTrasNum(col[keys])
                            usersInfo.append(numTrans)
                            usersInfo.append(f"NT={numTrans}")
                            usersInfo.append(f"Id={col[keys]}")
                            
                        elif keys == "username":
                            if col[keys]=="":
                                usersInfo.append("UN = _____ ")
                            else:
                                usersInfo.append(f"UN=@{col[keys]}")   
                        elif keys == "firstName":
                            usersInfo.append(f"FN={col[keys]}")
                        elif keys == "lastName":
                            usersInfo.append(f"LN={col[keys]}")
                        # elif type(col[keys]) is datetime.datetime:
                        elif keys == "userStartDay":
                            tilNow = datetime.datetime.now() - col[keys]
                            usersInfo.append(f"days={tilNow.days}")


                        else:
                            usersInfo.append(col[keys])
                        # usersInfo.append("\n")
                        usersInfoTuple = tuple(usersInfo)
                #   usersInfo.append("\n")
                #   print(f"userInfo = {usersInfo}")
                #   output.append("\n")
                outputArray.append(usersInfoTuple)
                #   print(f"output = {output}")
                #   output = "\n".join(output)
            if len(outputArray)==0:
                output = "هیچ کاربر کنشگری امروز تا این دم و لحظه وجود ندارد."
            else:
                outputArray.sort(key = operator.itemgetter(0), reverse = True)
                #   output = str(output)
                #   print(f"usersInfoTuple = {usersInfoTuple}")
                #   print(f"output = {output}")
                ouputSeprarated = '\n'.join('{}'.format(item) for item in outputArray)
                #   print("\n".join(output))  
                print(f"ouputSeprarated = {ouputSeprarated}")
                output = ouputSeprarated
            return output



     
        # گرفتن نام و نام خانواردگی نام کاربری شماره چت افراد کنشگر امروز
        def getActiveGuestsInfo(self):
            # titr = self.msgsDateAlpha()
            titr = self.obj_Msgs.msgsDateAlpha()
            condition = {f"msgs.{titr}":{"$exists":"true"},"userType":"guest"}
            find = {"userId":1,"firstName":1,"lastName":1,"username":1,"userStartDay":1,"_id":0}
            output=""
            outputArray = []
            for col in self.obj_Db.userCollection.find(condition,find):
                guestsInfo = []
                #   print(f"col = {col}")
                for keys in col.keys():
                        # print(f"col.keys() = {col.keys()}")
                        # print(f"keys = {keys}")
                        # print(f"col[keys] = {col[keys]}")
                        # getUserTrasNum
                        if keys == "userId":
                            numTrans = self.getUserTrasNum(col[keys])
                            guestsInfo.append(numTrans)
                            guestsInfo.append(f"NT={numTrans}")
                            guestsInfo.append(f"Id={col[keys]}")
                            
                        elif keys == "username":
                            if col[keys]=="":
                                guestsInfo.append("UN = _____ ")
                            else:
                                guestsInfo.append(f"UN=@{col[keys]}")   
                        elif keys == "firstName":
                            guestsInfo.append(f"FN={col[keys]}")
                        elif keys == "lastName":
                                guestsInfo.append(f"LN={col[keys]}")
                        elif keys == "guestStartDay":
                            tilNow = datetime.datetime.now() - col[keys]
                            guestsInfo.append(f"days={tilNow.days}")
                        else:
                            guestsInfo.append(col[keys])
                        # usersInfo.append("\n")
                        # print(f"guestsInfo = {guestsInfo}")
                        guestsInfoTuple = tuple(guestsInfo)
                        # print(f"guestsInfoTuple = {guestsInfoTuple}")
                #   usersInfo.append("\n")
                #   print(f"userInfo = {usersInfo}")
                #   output.append("\n")
                outputArray.append(guestsInfoTuple)
                #   print(f"output = {output}")
                #   output = "\n".join(output)
            if len(outputArray)==0:
                output = "هیچ میهمان کنشگری امروز تا این دم و لحظه وجود ندارد."
            else:

                outputArray.sort(key = operator.itemgetter(0), reverse = True)
                #   output = str(output)
                #   print(f"guestsInfoTuple = {guestsInfoTuple}")
                #   print(f"output = {output}")
                ouputSeprarated = '\n'.join('{}'.format(item) for item in outputArray)
                #   print("\n".join(output))  
                print(f"ouputSeprarated = {ouputSeprarated}")
                output = ouputSeprarated
            return output


         # گرفتن  شمار تراکنش های یک یوزر در امروز
       
        def getUserTrasNum(self,id):
                withdraw =""
                length = 0
                # titr = self.msgsDateAlpha()
                titr = self.obj_Msgs.msgsDateAlpha()
                for col in self.obj_Db.userCollection.find({f"msgs.{titr}":{"$exists":"true"},"userId":id},{f"msgs.{titr}":1,"_id":0}):
                    # print(f"col = {col}")
                    for keys in col.keys():
                        # print(f"keys = {keys}")
                        # print(f"col[keys] = {col[keys]}")
                        withdraw = col[keys]
                        for _,y in withdraw.items():
                            # print(f"x = {x}")
                            # print(f"y = {y}")
                            length = len(y)+length
                print(f"length = {length}")
                return length

        #ذخیره پیام فرستاده شده توسط ادمین در پایگاه داده
        def saveTempSendToAll(self,msg):
            # msgSendToAll = 
            self.obj_Db.userCollection.update_many({"userId":self.id},{"$set":{"temporary.tempSendToAll":msg}})

        # گرفتن پیام ذخیره شده برای فرستادن به هم از پایگاه داده
        def getTempSendToAll(self):
            msgDict = ""
            for col in self.obj_Db.userCollection.find({"userId":self.id},{"temporary.tempSendToAll":1,"_id":0}):
                for keys in col.keys():
                    print(f"col[keys] = {col[keys]}")
                    msgDict = col[keys]
                    print(f" msgDict['tempSendToAll'] = {msgDict['tempSendToAll']}")           
            return msgDict['tempSendToAll']

        # گرفتن تمامی چت ادی های کاربران به جز ادمین
        def getUserIds(self):
            ids = []
            for col in self.obj_Db.userCollection.find({},{"userId":1,"_id":0}):
                for keys in col.keys():
                    if self.id != col[keys]:
                        ids.append(col[keys]) 
            print(f"ids = {ids}")
            return ids

        #گرفتن تمامی پیام های امروز
        def getTodaysMsgs(self):
            msgsDict = ""
            msgs = ""
            # length = 0
            titr = self.obj_Msgs.msgsDateAlpha()
            for col in self.obj_Db.userCollection.find({"userId":self.id},{f"msgs.{titr}":1,"_id":0}):
                for keys in col.keys():
                    msgsDict=col[keys] 
            for _,y in msgsDict.items():
                msgs = y
                
            # length = len(msgs)
            # print(f"length = {length}")
            # print(f"msgs = {msgs}")
            # print(f"msgs[length-1] = {msgs[length-1]}")
            return msgs 
                
                

        #FIXME یکی مونده و دوتا مونده به آخر اگر پیام به همه بود با کیبورد مقایسه نشود در هر سه زبان
        #راستی آزمایی پیام یکی مانده به آخر اگر برابر با  <<پیام به همه>> باشد درست است در غیراینصورت اشتباه است
        def verifySendToAllMsg(self):
            try:
                    msgs = self.getTodaysMsgs()
                    length = len(msgs)
                    oneNextToTheLastDict = msgs[length -2]
                    # print(f"oneNextToTheLastDict = {oneNextToTheLastDict}")
                    for x,y in oneNextToTheLastDict.items():
                        # print(f"x = {x}")
                        # print(f"y = {y}")
                        if x == "msg" and ( y == PerBtnA().sendToAll or y == DeBtnA().sendToAll or y == EnBtnA().sendToAll):
                            # print(f"y = {y}")
                            return True
                        else:
                            pass
            except:
                pass
        # if Admin(self.id).verifySendToAllMsg() and Admin(self.id).msgKeyBotComparison(msg):
        
        # پیام چیزی جز تمامی دکمه های کیبورد ربات باشد جواب درست درغیر اینصورت اشتباه است
        def msgKeyBotComparison(self,msg):
            counter = 0
            # "Deutsche Tastatur und Nachricht⌨️💬"],["English Keyboard and Message⌨️💬"],["کیبورد و پیام پارسی⌨️💬"
            
            keyBotsArray = PerBtn().arrButtonPer + BtnS().arrButtonSame + PerBtnA().arrButtonAdminPer
            length = len(keyBotsArray)
            for col in keyBotsArray:
                if msg != col:
                    counter +=1
                    print(f"counter = {counter}")
                    # return True
            print(f"length = {length}")
            print(f"counter out last = {counter}")
            if length == counter:
                return True
            else:
                pass

        # پیام چیزی جز تمامی دکمه های کیبورد ربات باشد جواب درست درغیر اینصورت اشتباه است
        def msgKeyBotComparisonDe(self,msg):
            counter = 0
            # "Deutsche Tastatur und Nachricht⌨️💬"],["English Keyboard and Message⌨️💬"],["کیبورد و پیام پارسی⌨️💬"
            
            keyBotsArray =  DeBtn().arrButtonDe + BtnS().arrButtonSame + DeBtnA().arrButtonAdminDe
            length = len(keyBotsArray)
            for col in keyBotsArray:
                if msg != col:
                    counter +=1
                    print(f"counter = {counter}")
                    # return True
            print(f"length = {length}")
            print(f"counter out last = {counter}")
            if length == counter:
                return True
            else:
                pass
                  
        # پیام چیزی جز تمامی دکمه های کیبورد ربات باشد جواب درست درغیر اینصورت اشتباه است
        def msgKeyBotComparisonEn(self,msg):
            counter = 0
            # "Deutsche Tastatur und Nachricht⌨️💬"],["English Keyboard and Message⌨️💬"],["کیبورد و پیام پارسی⌨️💬"
            
            keyBotsArray =  EnBtn().arrButtonEn + BtnS().arrButtonSame + EnBtnA().arrButtonAdminEn
            length = len(keyBotsArray)
            for col in keyBotsArray:
                if msg != col:
                    counter +=1
                    print(f"counter = {counter}")
                    # return True
            print(f"length = {length}")
            print(f"counter out last = {counter}")
            if length == counter:
                return True
            else:
                pass





        def afterOneMinNexTrain(self,id):
            now = datetime.datetime.now()
            min = now.minute +1
            nextTraining = now+ relativedelta(minute=min) 
            self.obj_Db.userCollection.update_many({"userId":id},{"$set":{"nextTrainingDate":nextTraining}})
            output = self.obj_DateArrange.getTomorrowNextTraining(id)
            # output = f"output1 = {output1}\n consideredNextTraining = {nextTraining}"
            return output



 #کلاس برای گرفتن خروجی از پایگاه داده   
 # برای استفاده از این کلاس ابتدا سرور یا پی سی ام اس ای بودن  را برای مقدار کایند(به انگلیسی)مشخص کنید
 #  # ExportDb()exportCollectionSJson(kind)
 # ExportDb()makeCollectionsZip(kind)

class ExportDb:
    def __init__(self,kind):
        self.obj_Db = Db()
        inp= "config.cfg"
        self.bot = pybotc.Bot(inp) 
        self.pack = pybotc.mail(inp)
        self.kind = kind
        self.obj_DateArrange = DateArrange()


    def pathIdentifier(self):
        # create a ZipFile object
        now = datetime.datetime.now()
        dirNameToday = datetime.datetime.strftime(now,'%Y-(%B-%m)-%d')
        yesterday = now -datetime.timedelta(days=1)
        dirNameYesterday = datetime.datetime.strftime(yesterday,'%Y-(%B-%m)-%d')
        
        ## pc
        if self.kind == "pcmsi":
            dir = os.path.dirname(os.path.realpath("__file__"))
            path = os.path.join(dir,r'.\dbEx')
            # path = "D:\\project\\WoerterbuchProject\\main\\db server"
            destinationZip = os.path.join(dir,r'.\zipDailyDb')
            # destinationZip = r'D:\project\WoerterbuchProject\main\zipDailyDb'
            todayDirectory = f"{path}\\{dirNameToday}"
            yesterdayDirectory = f"{path}\\{dirNameYesterday}"
            if os.path.exists(todayDirectory):
                pass
            else:
                os.mkdir(f"{path}\\{dirNameToday}")
                todayDirectory = f"{path}\\{dirNameToday}"

            if os.path.exists(yesterdayDirectory):
                pass
            else:
                os.mkdir(f"{path}\\{dirNameYesterday}")
                yesterdayDirectory = f"{path}\\{dirNameYesterday}"


        ## server
        elif self.kind == "server":
            dir = os.path.dirname(os.path.realpath("__file__"))
            path = os.path.join(dir,r'.\dbEx')
            # path = "C:\\Users\\Administrator\\Downloads\\j\\w\\main\\dbEx"
            destinationZip = os.path.join(dir,r'.\zipDailyDb')
            # destinationZip = r'C:\Users\Administrator\Downloads\j\w\main\zipDailyDb'
                                
            todayDirectory = f"{path}\\{dirNameToday}"
            yesterdayDirectory = f"{path}\\{dirNameYesterday}"
            if os.path.exists(todayDirectory):
                pass
            else:
                os.mkdir(f"{path}\\{dirNameToday}")
                todayDirectory = f"{path}\\{dirNameToday}"  

            if os.path.exists(yesterdayDirectory):
                pass
            else:
                os.mkdir(f"{path}\\{dirNameYesterday}")
                yesterdayDirectory = f"{path}\\{dirNameYesterday}"  

            
        return yesterday,yesterdayDirectory,todayDirectory,destinationZip







    def testImport(self):
        arr = []
        for col in self.obj_Db.userCollection.find():
            arr.append(col)
        self.obj_Db.addCollection(arr)


# dump and export collections (user,setting,section) as json
    def exportCollectionSJson(self,endOFDay=None): 
        # pathIdentifier()-->yesterday,yesterdayDirectory,todayDirectory,destinationZip  
        _,yesterdayDirectory,save_path,_ = self.pathIdentifier()
        if endOFDay is True :
            save_path = yesterdayDirectory
        nowTimeDate = datetime.datetime.now()
        ##file name
        nowStr = str(nowTimeDate)
        now = nowStr.replace(":","_")
        print(f"now = {now}")
        ###### WOKED!!!!###### userCollection
        name_of_file_user = f"{now}~userCollection"
        completeNameUser = os.path.join(save_path,name_of_file_user+".json")
        with codecs.open(completeNameUser, 'w',encoding='utf8') as file:
            arr = []
            for col in self.obj_Db.userCollection.find():
                arr.append(json.dumps(col,ensure_ascii=False,default=json_util.default,encoding='utf8'))
            file.writelines("%s\n" % place for place in arr)
            file.close()
        ###### WOKED!!!!###### sectionCollection
        name_of_file_section = f"{now}~sectionCollection"
        completeNameSection = os.path.join(save_path,name_of_file_section+".json")
        with codecs.open(completeNameSection, 'w',encoding='utf8') as file:
            arr = []
            for col in self.obj_Db.sectionCollection.find():
                arr.append(json.dumps(col,ensure_ascii=False,default=json_util.default,encoding='utf8'))
            file.writelines("%s\n" % place for place in arr)
            file.close()
        ###### WOKED!!!!###### settingCollection
        name_of_file_setting = f"{now}~settingCollection"
        completeNameSetting = os.path.join(save_path,name_of_file_setting+".json")
        with codecs.open(completeNameSetting, 'w',encoding='utf8') as file:
            arr = []
            for col in self.obj_Db.settingCollection.find():
                arr.append(json.dumps(col,ensure_ascii=False,default=json_util.default,encoding='utf8'))
            file.writelines("%s\n" % place for place in arr)
            file.close()
        ###### WOKED!!!!###### backupCollection
        name_of_file_setting = f"{now}~backupCollection"
        completeNameSetting = os.path.join(save_path,name_of_file_setting+".json")
        with codecs.open(completeNameSetting, 'w',encoding='utf8') as file:
            arr = []
            for col in self.obj_Db.settingCollection.find():
                arr.append(json.dumps(col,ensure_ascii=False,default=json_util.default,encoding='utf8'))
            file.writelines("%s\n" % place for place in arr)
            file.close()





    #make one zip file from all collections backup in 'db server' of yesterday
    def makeCollectionsZip(self):
        #pathIdentifier()-->yesterday,yesterdayDirectory,todayDirectory,destination
        yesterday,directory,_,destination = self.pathIdentifier()
      # create a ZipFile object
        zipFileName = f"{datetime.datetime.strftime(yesterday,'%Y-(%B-%m)-%d_%H')}.zip"
        pathZipFileName = f"{destination}\\{zipFileName}"
        #zipfile.ZIP_DEFLATED... compressor

        if self.findZippedPack(zipFileName) is False and self.backupPackCondition() is not False:
            id = self.backupPackCondition()
            with zipfile.ZipFile(pathZipFileName, 'w',zipfile.ZIP_DEFLATED) as zipObj:
                #avoid directory structure zip
                rootdir = os.path.basename(destination)
                # Iterate over all the files in directory
                for dirpath, _, filenames in os.walk(directory):
                    # print(f"dirpath = {dirpath} \n dirnames = {dirnames} \n filenames = {filenames}")
                    for filename in filenames:
                            # create complete filepath of file in directory
                            filePath = os.path.join(dirpath, filename)
                            #avoid directory structure zip
                            parentpath = os.path.relpath(filePath, directory)
                            arcname    = os.path.join(rootdir, parentpath)
                            # Add file to zip
                            zipObj.write(filePath,arcname)
                zipObj.close()
                # return pathZipFileName 
            print(f"file backup zipped right here -->{pathZipFileName}")
            self.obj_Db.backupCollection.update_many({"_id":id},{"$set":{"zipBackups.zipped":True}})
            m,p = self.pack.email()
            try:
                self.emailBackup(pathZipFileName,id,m,p)
                self.telegramBackup(pathZipFileName,id)
            except:
                pass
        elif self.findZippedPack(zipFileName) is True and self.backupPackConditionEmailNTelegram() is not False:
            id = self.backupPackConditionEmailNTelegram()
            # print(f"self.backupPackConditionEmailNTelegram() id = {id}")
            m,p = self.pack.email()
            try:
                self.emailBackup(pathZipFileName,id,m,p)
                self.telegramBackup(pathZipFileName,id)
            except:
                pass
        else:
            pass


        






    def makeBackupRecord(self,zipBackupsTimeDate):
        now=datetime.datetime.now()
        backupRecord = {"today":datetime.datetime.now(),"backupTimes":{"h1":{"nextBackup":now.replace(hour=1,minute=0),"situation":False},"h3":{"nextBackup":now.replace(hour=3,minute=0),"situation":False},"h5":{"nextBackup":now.replace(hour=5,minute=0),"situation":False},"h7":{"nextBackup":now.replace(hour=7,minute=0),"situation":False},"h9":{"nextBackup":now.replace(hour=9,minute=0),"situation":False},"h11":{"nextBackup":now.replace(hour=11,minute=0),"situation":False},"h13":{"nextBackup":now.replace(hour=13,minute=0),"situation":False},"h15":{"nextBackup":now.replace(hour=15,minute=0),"situation":False},"h17":{"nextBackup":now.replace(hour=17,minute=0),"situation":False},"h19":{"nextBackup":now.replace(hour=19,minute=0),"situation":False},"h21":{"nextBackup":now.replace(hour=21,minute=0),"situation":False},"h23":{"nextBackup":now.replace(hour=23,minute=0),"situation":False},"h24":{"nextBackup":now.replace(hour=0,minute=0)+relativedelta(days=1),"situation":False}},"backups":False,"zipBackups":{"timeDate": zipBackupsTimeDate,"zipped":False,"emailSent":False,"telegramSent":False},"backupSent":False}

        self.obj_Db.backupCollection.insert_one(backupRecord)




    def findBackup(self):
        
        now = datetime.datetime.now()
        todayZero = now.replace(hour=0,minute=0,second=0,microsecond=0)
        # print(f"now = {now}")
        todayOneHourLater = now.replace(hour=1,minute=0,second=0,microsecond=0)
        # print(f"todayOneHourLater = {todayOneHourLater}")
        endOfToday = now.replace(hour=23,minute=59,second=59,microsecond=999999)
        # print(f"endOfToday = {endOfToday}")
        tomorrowZipBackupsTimeDate = now.replace(hour=1,minute=0) + relativedelta(days=1)
        yesterdayOnehourlater = todayOneHourLater - relativedelta(days=1)
        #شرطهابی برای ساعت صفر تا یک 
        condition1_1 ={"today": {"$lt" : todayOneHourLater,"$gt":todayZero},"backupSent":False,"zipBackups.timeDate":{"$lt" : todayOneHourLater,"$gt":todayZero}}
        condition1_2 ={"today": {"$lt" : todayOneHourLater,"$gt":todayZero},"backupSent":True}
        condition1_3 = {"today": {"$lt" : todayOneHourLater,"$gt":yesterdayOnehourlater}}
        condition1_mix = {"$or":[condition1_1,condition1_2,condition1_3]}

        condition2 ={"today": {"$lt" : endOfToday,"$gt":todayOneHourLater},"backupSent":False,"zipBackups.timeDate":{"$lt" : tomorrowZipBackupsTimeDate,"$gt":todayOneHourLater}}
        condition = ""

        zipBackupsTimeDate = ""
        ## اگر الان بین ساعت صفر تا یک باشد
        if now < todayOneHourLater and todayZero <now:
            zipBackupsTimeDate = now.replace(hour=0,minute=0,second=1,microsecond=1)
            condition = condition1_mix
        # اگر الان بین یک تا آخر امروز باشد
        elif now < endOfToday and todayOneHourLater < now:
            zipBackupsTimeDate = now.replace(hour=1,minute=0,second=0,microsecond=1) + relativedelta(days=1)
            condition = condition2

        # condition = {"enterDatatime":{"$lte":now,"$gte":timePast}}
        # timPast.replace(hour=23)
        idAutomate = ""
        for col in self.obj_Db.backupCollection.find(condition,{"_id":1}):
            for keys in col.keys():
                    idAutomate = col[keys]
                    # print(f"idAutomate = {idAutomate}")
                    return idAutomate
        
        if idAutomate == "":
            self.makeBackupRecord(zipBackupsTimeDate)
            print("make record")
            return False
            
    def isMadeBackup(self,record_id , backupTimesField):
        output = ""
        if record_id != "" and backupTimesField != "":
            for col in self.obj_Db.backupCollection.find({"_id":record_id,f"backupTimes.{backupTimesField}.situation":False},{f"backupTimes.{backupTimesField}.nextBackup":1,"_id":0}):
                for keys in col.keys():
                    output = col[keys]
                    return output
        #backup already made
        if output == "":
            return False

    def hourlyBackup(self):
        now = datetime.datetime.now()
        hour=now.hour
        record_id = ""
        backupTimesField = ""
        dict ={"h1":1,"h3":3,"h5":5,"h7":7,"h9":9,"h11":11,"h13":13,"h15":15,"h17":17,"h19":19,"h21":21,"h23":23,"h24":0}
        dictMiddle ={"h1":2,"h3":4,"h5":6,"h7":8,"h9":10,"h11":12,"h13":14,"h15":16,"h17":18,"h19":20,"h21":22}
        if self.findBackup()  is not False:
            record_id = self.findBackup()
            for field,value in dict.items():
                # print(f"hour = {hour} \nvalue = {value}")
                if value == hour:
                    backupTimesField = field
            for field,value in dictMiddle.items():
                # print(f"hour = {hour} \nvalue = {value}")
                if value == hour:
                    backupTimesField = field
        isMadeBackup = self.isMadeBackup(record_id , backupTimesField)
        # print(f"hour = {hour} \nbackupTimesField = {backupTimesField}")
        # print(f"isMadeBackup = {isMadeBackup}")


        if backupTimesField == "h24" and isMadeBackup is not False:
            self.exportCollectionSJson(True)
            self.obj_Db.backupCollection.update_many({"_id":record_id,f"backupTimes.{backupTimesField}.situation":False},{"$set":{f"backupTimes.{backupTimesField}.situation":True}})

        elif isMadeBackup is not False:
            self.exportCollectionSJson()
            self.obj_Db.backupCollection.update_many({"_id":record_id,f"backupTimes.{backupTimesField}.situation":False},{"$set":{f"backupTimes.{backupTimesField}.situation":True}})
        self.backupFCheckNDone(record_id)



        

    def backupPackConditionEmailNTelegram(self):
        id = ""
        # now = datetime.datetime.now()
        # print(f"now = {now}")
        # timePass= now.replace(hour=0,minute=0)
        # print(f"timePass = {timePass}")
        condition={"backups":True,"backupSent":False,"zipBackups.zipped":True}

        # condition={"zipBackups.timeDate":{"$lt":now,"$gt":timePass},"backups":True,"backupSent":False,"zipBackups.zipped":False}
        for col in self.obj_Db.backupCollection.find(condition,{"_id":1}):
            for keys in col.keys():
                id = col[keys] 
        if id != "":
            # print(f"backupPackConditionEmailNTelegram id = {id}")
            return id
        #در صورت پیدا نکردن
        else:
            return False
    


    def backupPackCondition(self):
        id = ""
        # now = datetime.datetime.now()
        # print(f"now = {now}")
        # timePass= now.replace(hour=0,minute=0)
        # print(f"timePass = {timePass}")
        condition={"backups":True,"backupSent":False,"zipBackups.zipped":False}

        # condition={"zipBackups.timeDate":{"$lt":now,"$gt":timePass},"backups":True,"backupSent":False,"zipBackups.zipped":False}
        for col in self.obj_Db.backupCollection.find(condition,{"_id":1}):
            for keys in col.keys():
                id = col[keys] 
        if id != "":
            return id
        #در صورت پیدا نکردن
        else:
            return False
        
    # پیدا کردن پکیج زیپ شده
    def findZippedPack(self,name):
        #pathIdentifier()-->yesterday,yesterdayDirectory,todayDirectory,destination
        _,_,_,path = self.pathIdentifier()
        a = ""
        # print(f"name = {name}")
        for root, _, files in os.walk(path):
            if name in files:
                a = os.path.join(root, name)
                # print(a)
        if a != "":
            # print(f"we have this file here it is ---> {a}")
            return True
        else:
            # print("there's no such a file!")
            return False


    def backupFCheckNDone(self,id):
        condition={"$or":[{"_id":id,"backupTimes.h1.situation":True,"backupTimes.h3.situation":True,"backupTimes.h5.situation":True,"backupTimes.h7.situation":True,"backupTimes.h9.situation":True,"backupTimes.h11.situation":True,"backupTimes.h13.situation":True,"backupTimes.h15.situation":True,"backupTimes.h17.situation":True,"backupTimes.h19.situation":True,"backupTimes.h21.situation":True,"backupTimes.h23.situation":True,"backupTimes.h24.situation":True},{"_id":id,"backupTimes.h24.situation":True}]}   
        self.obj_Db.backupCollection.update_many(condition,{"$set":{"backups":True}})



    def convertPathToGregorian(self,path):
        # path = r"D:\project\WoerterbuchProject\main\zipDailyDb\2020-(January-01)-11_00.zip"
        listPath = path.split("\\")
        # print(listPath)
        nameStringWithHour = listPath[len(listPath)-1]
        # print(nameStringWithHour)
        listPath2 = nameStringWithHour.split("_")
        # print(listPath2)
        nameString = listPath2[0]
        convertedDate = datetime.datetime.strptime(nameString,"%Y-(%B-%m)-%d").date()
        # print(f"convertedDate = {convertedDate}")
        return convertedDate
        
    #تبدیل تاریخ فایلی که فرستاده می شود به خورشیدی
    #TODO می بایست پاک شود و با convertToKhorshidi ادغام شود
    def dateFileKhorshidi(self,dateGregorian):
        # monthAlpha,year,month,day,monthAlphaFinglish,weekDay,weekDayFinglish
        monthAlpha,year,_,day,_,_,_ = self.obj_DateArrange.convertToKhorshidi(dateGregorian)    
        # گرفتن نام روز در هفته به پارسی
        # print(dateGregorian)
        weakDayNum = dateGregorian.weekday()
        # print(weakDayNum)
        weeDayKhorshidiDict = {0:"دوشنبه",1:"سه شنبه",2:"چهارشنبه",3:"پنج شنبه",4:"جمعه",5:"شنبه",6:"یکشنبه"}
        weekDay = weeDayKhorshidiDict[weakDayNum]
        # print(f"weekDay = {weekDay} , day = {day},monthAlpha = {monthAlpha},year = {year}")
        return weekDay,day,monthAlpha,year




    def emailBackup(self,path,_id,email=None,password=None,send_to_email=None,subject=None,message=None,file_location=None):
        if self.emailSendingCheck(_id) is not False: 

            send_to_email = 'first.backup.com@gmail.com'
            grigorianDate = self.convertPathToGregorian(path)
            weekDay,day,monthAlpha,year = self.dateFileKhorshidi(grigorianDate)
            subject = f'{grigorianDate} -{weekDay} {year} {monthAlpha} {day}  Backup @GUEWortschatzbot'
            message = f'check atachment! \n file date {grigorianDate} \n {weekDay} {year} {monthAlpha} {day} '
            file_location = path
            msg = MIMEMultipart()
            msg['From'] = email
            msg['To'] = send_to_email
            msg['Subject'] = subject

            msg.attach(MIMEText(message, 'plain'))

            # Setup the attachment
            filename = os.path.basename(file_location)
            attachment = open(file_location, "rb")
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(attachment.read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', "attachment; filename= %s" % filename)

            # Attach the attachment to the MIMEMultipart object
            msg.attach(part)

            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(email, password)
            text = msg.as_string()
            server.sendmail(email, send_to_email, text)
            server.quit()
            self.obj_Db.backupCollection.update_many({"_id":_id},{"$set":{"zipBackups.emailSent":True}})
        else:
            pass


    def emailSendingCheck(self,_id):
        # print(f"_id = {_id}")
        output = ""
        for col in self.obj_Db.backupCollection.find({"_id":_id,"backupSent":False,"zipBackups.zipped":True,"zipBackups.emailSent":False},{"_id":1}):
            for keys in col.keys():
                output = col[keys]
        if output != "":
            return output
        #برقرار نبودن شرط که یا عدم فرستاده شدن ایمیل بوده یا عدم زیپ شدن فایل بوده یا عدم وجود چنین ایدی بوده
        else:
            return False


    def telegramBackup(self,document_path,_id):
        if self.telegramSendingCheck(_id) is not False:
            chat_id = -1001137567001

            grigorianDate = self.convertPathToGregorian(document_path)
            weekDay,day,monthAlpha,year = self.dateFileKhorshidi(grigorianDate)
            caption = f'{grigorianDate} -{weekDay} {year} {monthAlpha} {day} -  Backup @GUEWortschatzbot'
            files = {'document': open(document_path, 'rb')}
            requests.post(self.bot.base+f'sendDocument?chat_id={chat_id}&caption={caption}', files=files)
            self.obj_Db.backupCollection.update_many({"_id":_id},{"$set":{"zipBackups.telegramSent":True}})
        else:
            pass


    def telegramSendingCheck(self,_id):
        output = ""
        # print (_id)
        for col in self.obj_Db.backupCollection.find({"_id":_id,"backupSent":False,"zipBackups.zipped":True,"zipBackups.telegramSent":False},{"_id":1}):
            for keys in col.keys():
                output = col[keys]
        if output != "":
            return output
        #برقرار نبودن شرط که یا عدم فرستاده شدن فایل در تلگرام بوده یا عدم زیپ شدن فایل بوده یا عدم وجود چنین ایدی بوده
        else:
            return False

    
    def checkFullBackupSentNUpdate(self):
        condition = {"zipBackups.zipped":True,"zipBackups.emailSent":True,"zipBackups.telegramSent":True,"backupSent":False}
        self.obj_Db.backupCollection.update_many(condition,{"$set":{"backupSent":True}})




#این کلاس کمک می کند مطمین و استیگان شویم از وجود کاربر در پایگاه داده
class LookingForUser:
      def __init__(self,id):
          self.id = id
          self.obj_Db = Db()

      def lookingForUser(self):
            m = [col for col in self.obj_Db.userCollection.find({"userId":self.id},{"_id":0,"userId":1})]
            # print(m)
            if len(m) !=0 :
                #we have this user
                # print("we have this user")
                return True
            else :
                #there is no such a user
                # print("there is no such a user")
                return False

      
# شمار واژگان در پایگاه داده
class ShomarVazhgan:
     def __init__(self,id):
         self.id = int(id)
         self.obj_Db = Db()

         #به روز رسانی و ذخیره شمار واژگان روزانه در پایگاه داده
     def saveWordNum(self,wordsNum):
         self.obj_Db.userCollection.update_many({"userId":self.id},{"$set":{"wordNumPerDay":wordsNum}})
        
        #گرفتن شمار و تعداد واژگان ورودی روزانه
     def getWordNum(self):
         shomarVazhegan = 0
         for col in self.obj_Db.userCollection.find({"userId":self.id},{"_id":0,"wordNumPerDay":1}):
             for keys in col.keys():
                #  print(f"col = {col[keys]}")
                 shomarVazhegan = int(col[keys]) 

        #  print(f"shomarVazhegan = {shomarVazhegan}")
         return shomarVazhegan
            
# ه«روش یادگیری و تمرین» در پایگاه داده
class RaveshYadgiri:
    def __init__(self,id,way=None):
        self.id = int(id)
        self.way = way
        self.obj_Db = Db()

 

       #به روز رسانی و ذخیره روش یادگیری و تمرین در پایگاه داده
    def saveWay(self,way):
        if isinstance(way,list):
            arrayWay = []
            for item in way:
                if item in arrayWay:
                    arrayWay.append(item)
            if len(arrayWay) != 0:
                way = arrayWay
        self.obj_Db.userCollection.update_many({"userId":self.id},{"$set":{"way":way}}) 
    
    
    def changeWay(self,data):
        print(f"data = {data}")
        allChangeKeys = BtnS().allChangeKeys
        for z in allChangeKeys:
            if data == z[0]:
                subtract = z[1]
                add = z[2]
                # if z[1] in way:
                #     keysArray.append({'text': z[0], 'callback_data':z[0]})
        print(f"add = {add} \nsubtract = {subtract}")
        way = self.getWay()
        print(way)
        wayOut = []
        if not isinstance(way,list):
            wayOut.append(way)
        
        wayOut = [n for n in way if n != subtract]
        wayOut.append(add)
        print(wayOut)
        self.saveWay(wayOut)
        if add == BtnS().persianTextEn:
            add = BtnS().persianText
        elif subtract == BtnS().persianTextEn:
            subtract = BtnS().persianText
        print(subtract)
        return add,subtract



    
           #به روز رسانی و ذخیره روش یادگیری و تمرین  در پایگاه داده
    def saveWayBool(self,wayField):
        self.obj_Db.userCollection.update_many({"userId":self.id},{"$set":{f"way.{wayField}":True}}) 
    
    #planB
    #FIXMEfixed output array getWayBool apply to getWay
      #گرفتن روش یادگیری وتمرین با توجه به ایدی کاربر از پایگاه داده
    def getWayBool(self):
        way=""
        arrayWays = []
        # print(f"id = {id}")
        for col in self.obj_Db.userCollection.find({"userId":self.id},{"_id":0,"way":1}):
            for keys in col.keys():
                # print("col = {col[keys]}")
                way = col[keys]
                for field,value in way.itmes():
                    if value == True:
                        arrayWays.append(field)
 
        # print(f"arrayWays = {arrayWays}")
        return arrayWays  

    #planA ... planB getWayBool()
      #گرفتن روش یادگیری وتمرین با توجه به ایدی کاربر از پایگاه داده
    def getWay(self):
        way = ''
        for col in self.obj_Db.userCollection.find({"userId":self.id},{"_id":0,"way":1}):
            for keys in col.keys():
                way = col[keys]
        # self.saveWay(way)
        print(way)
        return way  

    def addWay(self,data):
        allWaysWithAdd = [{BtnS().addEnglish :BtnS().englishText},{BtnS().addDeutsch:BtnS().deutschText},{BtnS().addPersian:BtnS().persianTextEn},{BtnS().addSynonym:BtnS().synonymText}]
        addingWay = ""
        for z in allWaysWithAdd:
            for x,y in z.items():
                if x == data:
                    addingWay = y
        way = self.getWay()
        if isinstance(way,list):
            way.append(addingWay)
            wayOutput = [n for n in way if n != ""]
            # wayOutput = way
        else:
            wayOutput = []
            wayOutput.append(way)
            wayOutput.append(addingWay)
        print(wayOutput)
        self.saveWay(wayOutput)
        if addingWay == BtnS().persianTextEn:
            addingWay = BtnS().persianText
        return addingWay

    def subtractWay(self,data):
        allWaysWithAdd = [{BtnS().subtractPersian :BtnS().persianTextEn},{BtnS().subtractDeutsch:BtnS().deutschText},{BtnS().subtractEnglish:BtnS().englishText},{BtnS().subtractSynonym:BtnS().synonymText}]
        subtractingWay = ""
        for z in allWaysWithAdd:
            for x,y in z.items():
                if x == data:
                    subtractingWay = y
        way = self.getWay()


        wayOutput = [n for n in way if n !=subtractingWay]
        # print(f"wayOUtput = {wayOutput}")
        self.saveWay(wayOutput)
        if subtractingWay == BtnS().persianTextEn:
            subtractingWay = BtnS().persianText
        return subtractingWay


    # آماده سازی روش ها و تبدیل به واژه هایی پشت سر هم بدون کاما و براکت 
    def wayOrWaysString(self,way):
        # 📒📕📘📔
        wayArrString = str(way)
        wayArrString = wayArrString.replace("[","")
        wayArrString = wayArrString.replace("]","")
        wayArrString = wayArrString.replace("'","")
        wayArrString = wayArrString.replace("deutsch","📒deutsch")
        wayArrString = wayArrString.replace("english","📕english")
        wayArrString = wayArrString.replace("synonym","📘synonym")
        wayArrString = wayArrString.replace("persian","📔persian")
        return wayArrString


     #📒📕📘📔 بعد از گرفتن روش دادن رنگ به کتاب با ایکن
    def getIconBook(self,way):
        output = ""
        if way == BtnS().deutschText:
            output = "📒"
        elif way == BtnS().persianTextEn:
            output = "📔"
        elif way == BtnS().englishText:
            output = "📕"
        elif way == BtnS().synonymText:
            output = "📘"
        elif way == "all together":
            output = "📒📕📘📔"
        else:
            pass
        return output
    

        #save Temporary way
    def saveTemportyWay(self):
        wayTemp={"wayTemp":self.way}
        self.obj_Db.userCollection.update_many({"userId": self.id},{"$set": {"temporary": wayTemp}})
    
    # get Temporary way value
    def getTemporaryWay(self):
        dict = ""
        for col in self.obj_Db.userCollection.find({"userId":self.id},{"temporary":1}):
            for keys in col.keys():
               dict = col[keys]
        # print(f"dict = {dict}")
        return dict["wayTemp"] 

    #get Temporary way Value and put in way
    def saveWayByTemporary(self):
        # print(self.getTemporaryWay())
        self.obj_Db.userCollection.update_many({"userId":self.id},{"$set":{"way":self.getTemporaryWay()}})




# ه«دگرسانی زبان» در پایگاه داده
class UILanguage:
    def __init__(self,id=None):
        self.id = id
        self.obj_Db = Db()

    #ذخیره زبان پوسته در پایگاه داده
    def saveUIL(self,uILanguage):
        ln = ""
        
        if uILanguage == BtnS().keyNMsgDe:
           ln = "De"
        elif uILanguage == BtnS().keyNMsgPer:
           ln = "Per"
        elif uILanguage == BtnS().keyNMsgEn:
            ln = "En"

        self.obj_Db.userCollection.update_many({"userId": self.id},{"$set": {"uILanguage": ln}})

    #پاک کردن زبان پیام و کیبورد برای همه
    def erase(self):
        self.obj_Db.userCollection.update_many({},{"$set": {"uILanguage": ""}})

    #گرفتن پوسته زبان از پایگاه داده
    def getUIL(self):
        ln = ""
        # print(id = {self.id})
        for col in self.obj_Db.userCollection.find({"userId":self.id},{"_id":0,"uILanguage":1}):
            for keys in col.keys():
                # print(f"col = {col[keys]}")
                ln = col[keys]
        # print(f"ln = {ln}")
        if ln == "":
            self.obj_Db.userCollection.update_many({"userId":self.id},{"$set":{"uILanguage":"Per"}})
            for col in self.obj_Db.userCollection.find({"userId":self.id},{"_id":0,"uILanguage" : 1}):
                for keys in col.keys():
                    # print(f"col = {col[keys]}")
                    ln = col[keys] 
        # print(ln)
        return ln




# UILanguage(id,uILanguage).saveTemportyUI()


#کلاس  حذف ربات 🗑 از پایگاه داده
class DeleteBot:
    def __init__(self,id):
        self.id = int(id)
        self.obj_Db = Db()
        

      # حذف ربات 🗑
    def deleteBot(self):
        self.addDeletedTime()
        userInfo = {"userStartDay":"","nextTrainingDate":"","way":"","temporary":{"rightWrongLampFlag":True,"automateMsgFlag":False},"todayWordsCorrection":"","report":False,"wordNumPerDay":0,"reportNum":0,"todayWordsNAnswer":"","reviewWords":"","plan":"","userType":"guest","counter":0,"msgs":""}
        self.obj_Db.userCollection.update_many({"userId":self.id},{"$set": userInfo})
        # self.obj_Db.userCollection.insert_one(userInfo)
        # self.obj_Db.userCollection.delete_many({"userId":self.id})
        self.obj_Db.sectionCollection.delete_many({"userId":self.id})

        #add field deletedTimes to record 
    def deleteUser(self):
        self.obj_Db.sectionCollection.delete_many({"userId":self.id})
        self.obj_Db.userCollection.delete_many({"userId":self.id})





    def addDeletedTime(self):
        condition = {"userId":self.id,"userType":"deleted"}
        find = {"deletedTimes":1,"_id":0}
        output = ""
        condition = {"userId":self.id}
        find = {"_id":0,"deletedTimes":1}

        for col in self.obj_Db.userCollection.find(condition,find):
            for keys in col.keys():
                output = col[keys]

        arrayToday =[datetime.datetime.now()]
        add1 = {"deletedTimes":[datetime.datetime.now()]}
        # add2 = {"deleted":arrayAdd.append(output)}
        
        if output == "":
            self.obj_Db.userCollection.update_many(condition,{"$set":add1})
        elif  len(output) == 1 or len(output) > 1:
            add2 = {"deletedTimes":output + arrayToday}
            self.obj_Db.userCollection.update_many(condition,{"$set":add2})    



class Vazhegan:
    def __init__(self,id,msg=None):
        self.id = int(id)
        self.msg = msg
        self.obj_Db = Db()
        self.obj_Book = Book(id)
        
        
        # self.obj_IdentifyWordsSection = IdentifyWordsSection(id)
        # self.obj_Counter = Counter(id)
        # self.colWord = Db().wordCollection
        # self.colSection = Db().sectionCollection
        # self.colMeaning = Db().meaningCollection
        # self.colUser = Db().userCollection
        self.obj_ShomarVazhgan = ShomarVazhgan(id)
        self.obj_RaveshYadgiri = RaveshYadgiri(id,msg)
        self.obj_Sections = Sections(id)
        self.obj_DateArrange = DateArrange(id)
        self.obj_UILanguage = UILanguage(id)
        
        


        #گرفتن واژگان نو
    def getNewWords(self):
        # print(self.obj_ShomarVazhgan)
        newWords2dimention = []
        # print(f"self.getAllWordsSection() = {self.getAllWordsSection()}")
        for col in self.obj_Db.wordCollection.find({"word":{"$nin":self.getAllWordsSection()}},{"word":1,"_id":0}).limit(self.obj_ShomarVazhgan.getWordNum()):
            for keys in col.keys():
               newWords2dimention.append(col[keys])
        oneDimentionNewWords = np.array(newWords2dimention)
        noKommaNewWords = oneDimentionNewWords.flatten()
        oneDimentionNewArray = list(noKommaNewWords)
        # print(f"newWords = {oneDimentionNewArray}")
        return oneDimentionNewArray
 
        #گرفتن واژگان قدیمی موجود در section
    def getAllWordsSection(self):
        oldWord=[]
        for col in self.obj_Db.sectionCollection.find({"userId":self.id,"section":{"$ne":7}},{"word":1,"_id":0}):
            for keys in col.keys():
                oldWord.append(col[keys])
        oldWord2 = np.array(oldWord)
        result = oldWord2.flatten()
        result = list(result)
        # print(f"old words = {result}")
        return result

     # گرفتن واژگان قدیمی و پیشین در سکشن ها براساس روز ۱و۲و۴و۷و۱۴و۲۸
    def getOldWords(self):

        distance = self.obj_DateArrange.firstDateTillNow()
        if distance == False:
            oldWordsArray = []
            return oldWordsArray
        else:
            oldWordsArray = []
            #get first section
            firstSection = self.obj_Sections.getSectionOne()
            oldWordsArray = firstSection

            #get section 2 , two days
            if distance % 2 == 0:
                secondSection = self.obj_Sections.getSectionTwo()
                oldWordsArray = oldWordsArray + secondSection
            
            #get section 3 , four days
            if distance % 4 == 0:
                thirdSection = self.obj_Sections.getSectionThree()
                oldWordsArray = oldWordsArray + thirdSection

            #get section 4 , seven days
            if distance % 7 == 0:
                fourthSection = self.obj_Sections.getSectionFour()
                oldWordsArray = oldWordsArray + fourthSection

            #get section 5 , fourtheen days
            if distance % 14 == 0:
                fifthSection = self.obj_Sections.getSectionFive()
                oldWordsArray = oldWordsArray + fifthSection        

            #get section 6 , twenty eight days
            if distance % 30 == 0:
            # else:
                sixthSection = self.obj_Sections.getSectionSix()
                oldWordsArray = oldWordsArray + sixthSection
            # print(f"oldWordsArray = {oldWordsArray}")
            return oldWordsArray        



        # آمیزش و همبندی واژگان
    def mixWords(self):
        mix = self.getNewWords() + self.getOldWords()
        a = tuple(mix)
        #ساختن یک دیکشنری برای استفاده زمان انتخاب درستی و نادرستی واژگان
        b = {t:"" for t in a }
        # print(f"b = {b}")
        self.obj_Db.userCollection.update_many({"userId":self.id},{"$set": {"todayWordsCorrection":b}})
        self.obj_Db.userCollection.update_many({"userId":self.id},{"$set": {"todayWordsNAnswer":b}})
        # print(f"mix = {mix}")
        return mix

    # add this length = len(self.getTodayWords())
    #گرفتن شمار و تعداد تمامی واژگان گذشته و تازه امروز
    def getWordsLength(self,wordsArray):
        length = len(wordsArray)
        # print(f"getWordsLength = {length}" )
        return length
    
    # دریافت واژگان امیزش شده 
    def getTodayWords(self):
        wordsDictionary =""
        for col in self.obj_Db.userCollection.find({"userId":self.id},{"todayWordsCorrection":1,"_id":0}):
            for keys in col.keys():
                wordsDictionary = col[keys]
        # print(f"wordsDictionary = {wordsDictionary}")
        words = []
        for x in wordsDictionary:
            words.append(x)
        # print(f"getTodayWords() = {words}")
        return words
    
    # پاک کردن فیلد todayWordsCorrection
    def eraseTodayWords(self):
        self.obj_Db.userCollection.update_many({"userId":self.id},{"$set":{"todayWordsCorrection":""}})
    #useless
    #FIXMEfixed getWay makeTodayWordsNAswers
    # ساختن یک دیکشنری از واژه و پاسخ نخستین بر طبق لانگنشایت روز
    # def makeTodayWordsNAswers(self):
    #     words = self.getTodayWords()
    #     answers = []
    #     for col in self.obj_Db.meaningCollection.find({"word":{"$in":words}},{self.obj_RaveshYadgiri.getWay():1,"_id":0}):
    #         for keys in col.keys():
    #             answers.append(col[keys])
    #     wordsNAnswers = dict(zip(words,answers))
    #     print(f"wordsNAnswers = {wordsNAnswers}")
    #     return wordsNAnswers
    
    # پاک کردن فیلد todayWordsNAnswer
    def eraseTodayWordsNAnswer(self):
        self.obj_Db.userCollection.update_many({"userId":self.id},{"$set":{"todayWordsNAnswer":""}})

    def getOneRightWordBehind(self,one):
        a = self.getTodayWords()
        # print(f"a = {a}")
        counter = Counter(self.id).getCounter()-one
        # print(counter)
        # print(f"getOneRightWordBehind = {a[counter]}")
        return a[counter]  
    
    # add this a = self.getTodayWords()
    #در این متد واژه مشخص با توجه به کانتر و شمارنده را می خواهیم
    def getOneRightWord(self,wordsArray):
        # a = self.getTodayWords()
        # a = wordsArray
        # print(f"wordsArray = {wordsArray}")
        counter = Counter(self.id).getCounter()
        # print(f"getOneRightWord = {wordsArray[counter]}")
        return wordsArray[counter]
    
 






    #حذف مدت زمان و ففط گرفتن واژه
    def getOneRightWordWithoutDuration(self,wordsArray):
        # print(f"wordsArray = {wordsArray}")
        counter = Counter(self.id).getCounter()
        # print(f"getOneRightWordWithoutDuration = {wordsArray[counter][0]}")
        return wordsArray[counter][0]

    #add this word = self.getOneRightWord()    
    #گونه و نوع واژه
    
    def kindOfWord(self,word):
        # word = self.getOneRightWord()
        wArray = []
        for col in self.obj_Db.sectionCollection.find({"userId":self.id,"word":word},{"_id":0,"word":1}):
            for keys in col.keys():
                wArray.append(col[keys])

        languageIn =self.obj_UILanguage.getUIL()
        # print(f"languageIn = {languageIn}")
        if languageIn == "De":
            if len(wArray) == 0:
                output = "neues Wort"
            else:
                output = "altes Wort"
        elif languageIn == "En":
            if len(wArray) == 0:
                output = "new word"
            else:
                output = "old word"
        elif languageIn == "Per":
            if len(wArray) == 0:
                output = "واژه نو"
            else:
                output = "واژه دیرین"
        else:
            if len(wArray) == 0:
                output = "واژه نو"
            else:
                output = "واژه دیرین"
        return output
        # if len(wArray) == 0:
        #     return "واژه نو"
        # else:
        #     return "واژه دیرین"


    # get answer word
    def getAnswer(self,word,way):
        answer = ""
        for col in self.obj_Db.meaningCollection.find({"word":word},{way:1,"_id":0}):
            for keys in col.keys():
                # print(f"getAnswer = {col[keys]}")
                answer = col[keys]  
        return answer
    
    #planB
    #FIXMEfixed just change it with getOneAnswerPure(self,word)
    #add this for col in self.obj_Db.meaningCollection.find({"word":self.getOneRightWord()},{self.obj_RaveshYadgiri.getWay():1,"_id":0}):
    def getOneAnswerPureNew(self,word):
        answer =""
        dash = "___________________________________"
        wayArray = self.obj_RaveshYadgiri.getWayBool()
        article = {"deutsch":"📒 deutsch 📒", "english":"📕 english 📕", "synonym":"📘 synonym 📘", "persian": "📔 persian 📔"}
        if len(wayArray)==1:
            answerUnique = self.getAnswer(word,wayArray[0])
            answer = f"<b>{article[wayArray[0]]}</b> \n {answerUnique}"
        elif len(wayArray)==2:
            firstAnswer = self.getAnswer(word,wayArray[0])
            secondAnswer = self.getAnswer(word,wayArray[1])
            answer = f"<b>{article[wayArray[0]]}</b> \n {firstAnswer} \n {dash} \n <b> {article[wayArray[1]]}</b>  \n {secondAnswer}"
        elif len(wayArray)==3:
            firstAnswer = self.getAnswer(word,wayArray[0])
            secondAnswer = self.getAnswer(word,wayArray[1])
            thirdAnswer = self.getAnswer(word,wayArray[2])
            answer = f"<b>{article[wayArray[0]]}</b> \n {firstAnswer} \n {dash} \n <b> {article[wayArray[1]]}</b>  \n {secondAnswer} \n {dash} \n <b> {article[wayArray[2]]}</b>  \n {thirdAnswer}"
        elif len(wayArray)==4:
            firstAnswer = self.getAnswer(word,wayArray[0])
            secondAnswer = self.getAnswer(word,wayArray[1])
            thirdAnswer = self.getAnswer(word,wayArray[2])
            fourthAnswer = self.getAnswer(word,wayArray[3])
            answer = f"<b>{article[wayArray[0]]}</b> \n {firstAnswer} \n {dash} \n <b> {article[wayArray[1]]}</b>  \n {secondAnswer} \n {dash} \n <b> {article[wayArray[2]]}</b>  \n {thirdAnswer} \n {dash} \n <b> {article[wayArray[3]]}</b>  \n {fourthAnswer}"
            return answer



    #planA ... planB getOneAnswerPureNew(self,word)
    #add this for col in self.obj_Db.meaningCollection.find({"word":self.getOneRightWord()},{self.obj_RaveshYadgiri.getWay():1,"_id":0}):
    def getOneAnswerPure(self,word,data):
        way = self.obj_RaveshYadgiri.getWay()
        # if data == 
        if way != "all together":
            answer = self.getAnswer(word,data)
            return answer
        elif way == "all together":
            dash = "___________________________________"
            deutsch = self.getAnswer(word,"deutsch")
            english = self.getAnswer(word,"english")
            synonym = self.getAnswer(word,"synonym")
            persian = self.getAnswer(word,"persian")
            answer = f"📒 deutsch 📒 \n {deutsch} \n {dash} \n 📕 english 📕 \n {english} \n {dash} \n 📘 synonym 📘 \n {synonym} \n {dash} \n 📔 persian 📔 \n {persian}"
            return answer
 

    #در این متد پاسخ واژه مشخص با توجه به کانتر و شمارنده را می خواهیم    
    def getOneAnswer(self,oneAnswerPure):
        # answer = self.getOneAnswerPure()
        answer = oneAnswerPure
        #replace < to (
        answer = answer.replace("<","(")
        answer = answer.replace(">",")") 
          
        return answer


   # استاندارد کردن واژه در قالب صفحه مبایل تلگرام 
    def standardizeWordReview(self,word,type):
        # standard full answer with guide is 662 English / 704 فارسی
        # standard line  english 38 / persian 40 
        print(f"type = {type}")
        # print(f"len(answer) = {len(word)}")
        enterBeforeWord = ""
        enterAfterWord = ""
        wordLength = len(word)
        ##test 12 + 23 + 7
        # "Entschuldigung die;-,en" length = 23 center(50) // test 12 + 23 + 7 = 
        # "Ihr" length = 3 center(72) // test  33 + 3 + 27
        # "grüß Gott"  = 9 center (63) 
        centerAlign = 75- wordLength
        word = word.center(centerAlign)
        # reportNum = 6
        chapNSection=[PerBtn().chapterNSection,PerBtn().nextWordChapNS,PerBtn().beforeWordChapNS,DeBtn().chapterNSection,DeBtn().nextWordChapNS,DeBtn().beforeWordChapNS,EnBtn().chapterNSection,EnBtn().nextWordChapNS,EnBtn().beforeWordChapNS,BtnS().wordChapNSCB]
        # print(chapNSection)
        leitnerBox = [PerBtn().leitnerBoxParts,PerBtn().beforeWordLeitBP,PerBtn().nextWordLeitBP,DeBtn().leitnerBoxParts,DeBtn().nextWordLeitBP,DeBtn().beforeWordLeitBP,EnBtn().leitnerBoxParts,EnBtn().nextWordLeitBP,EnBtn().beforeWordLeitBP,BtnS().wordLeitBPCB]
        # print(leitnerBox)
        weakWord = [PerBtn().weakWords,PerBtn().nextWordWW,PerBtn().beforeWordWW,DeBtn().weakWords,DeBtn().nextWordWW,DeBtn().beforeWordWW,EnBtn().weakWords,EnBtn().nextWordWW,EnBtn().beforeWordWW,BtnS().wordWWCB]
        # print(weakWord)
        chapNSectionNum = 330
        leitnerBoxNum = 300
        weakWordNum = 300
        while True:
            if  type in chapNSection: 
                    # 662
                    if chapNSectionNum<=wordLength:
                        break
                    elif wordLength<chapNSectionNum:
                        enterBeforeWord = enterBeforeWord +"\n"
                        enterAfterWord = enterAfterWord +"\n"
                        wordLength = wordLength + 76 +20
              # without guide line          
            elif type in leitnerBox:
                    
                    #764
                    if leitnerBoxNum<=wordLength:
                        break
                    elif wordLength<leitnerBoxNum:
                        enterBeforeWord = enterBeforeWord +"\n"
                        enterAfterWord = enterAfterWord +"\n"
                        wordLength = wordLength + 76 +20
            elif type in weakWord:
                    #764
                    
                    if weakWordNum<=wordLength:
                        break
                    elif wordLength<weakWordNum:
                        enterBeforeWord = enterBeforeWord +"\n"
                        enterAfterWord = enterAfterWord +"\n"
                        wordLength = wordLength + 76 +20
        standardizedWord = enterBeforeWord + word + enterAfterWord
        return standardizedWord

   # استاندارد کردن واژه در قالب صفحه مبایل تلگرام 
    def standardizeWord(self,word,reportNum):
        # standard full answer with guide is 662 English / 704 فارسی
        # standard line  english 38 / persian 40 
        # print(f"len(answer) = {len(word)}")
        enterBeforeWord = ""
        enterAfterWord = ""
        wordLength = len(word)
        ##test 12 + 23 + 7
        # "Entschuldigung die;-,en" length = 23 center(50) // test 12 + 23 + 7 = 
        # "Ihr" length = 3 center(72) // test  33 + 3 + 27
        # "grüß Gott"  = 9 center (63) 
        centerAlign = 75- wordLength
        word = word.center(centerAlign)
        # reportNum = 6
        while True:
            if  reportNum <= 5:   
                    # 662
                    if 200<=wordLength:
                        break
                    elif wordLength<200:
                        enterBeforeWord = enterBeforeWord +"\n"
                        enterAfterWord = enterAfterWord +"\n"
                        wordLength = wordLength + 76 +20
              # without guide line          
            elif 5<reportNum:
                    #764
                    if 450<=wordLength:
                        break
                    elif wordLength<450:
                        enterBeforeWord = enterBeforeWord +"\n"
                        enterAfterWord = enterAfterWord +"\n"
                        wordLength = wordLength + 76 +20

        standardizedWord = enterBeforeWord + word + enterAfterWord
        return standardizedWord

    
    # استاندارد سازی پاسخ در قالب تلگرام 
    def standardizeAnswer(self,way,answer,reportNum):
        # standard full answer with guide is 662 English / 704 فارسی
        # standard line  english 38 / persian 40 
        # print(f"way = {way}")
        # print(f"len(answer) = {len(answer)}")
        enterBeforeAnswer = ""
        enterAfterAnswer = ""
        answerLength = len(answer)
        # reportNum = 6
        while True:
            if  reportNum <= 5:   
                #FIXME persian standard answer
                if way == BtnS().persianTextEn:
                    if 250<=answerLength:
                        break
                    elif answerLength<250:
                        enterBeforeAnswer = enterBeforeAnswer +"\n"
                        enterAfterAnswer = enterAfterAnswer +"\n"
                        answerLength = answerLength + 76 +20
                else:
                    # 662
                    if 300<=answerLength:
                        break
                    elif answerLength<300:
                        enterBeforeAnswer = enterBeforeAnswer +"\n"
                        enterAfterAnswer = enterAfterAnswer +"\n"
                        answerLength = answerLength + 76 +40
              # without guide line          
            elif 5<reportNum:
                if way == BtnS().persianTextEn:
                    #804
                    if 500<=answerLength:
                        break
                    elif answerLength<500:
                        enterBeforeAnswer = enterBeforeAnswer +"\n"
                        enterAfterAnswer = enterAfterAnswer +"\n"
                        answerLength = answerLength + 76 +20
                else:
                    #764
                    if 450<=answerLength:
                        break
                    elif answerLength<450:
                        enterBeforeAnswer = enterBeforeAnswer +"\n"
                        enterAfterAnswer = enterAfterAnswer +"\n"
                        answerLength = answerLength + 76 +20

        answer = enterBeforeAnswer + answer + enterAfterAnswer
        return answer

    # add this  for col in self.obj_Db.meaningCollection.find({"word":self.getOneRightWord()},{"_id":0}):
    def getMeaningId(self,word):
        id = ""
        # for col in self.obj_Db.meaningCollection.find({"word":self.getOneRightWord()},{"_id":0}):
        for col in self.obj_Db.meaningCollection.find({"word":word},{"_id":0}):
            for keys in col.keys():
                # print(f"getOneAswer = {col[keys]}")
                id = col[keys]  
        return id
    ######
    #make package words 
    # self.obj_DbC.Vazhegan(self.id,self.msg).mixWords()
    # self.obj_Vazhegan.mixWords()
    #get word num
    def wordNdetails(self):
        obj_Counter = Counter(self.id)
        numW = obj_Counter.getCounter() + 1 
        # numW = self.Counter(self.id).getCounter() + 1 
        todayWords = self.getTodayWords()
        #get number of all words
        numAll = self.getWordsLength(todayWords)
        #get word
        word =  self.getOneRightWord(todayWords)
        way = self.obj_RaveshYadgiri.getWay()
        # print(f'way = {way}')
        linkWord =  self.audioWord(word)
        # print(f'link word = {linkWord}')
        #kind of word
        wKind = self.kindOfWord(word)
        #get words page
        # self.obj_Book =Book()
        wordsPage = self.obj_Book.getOnePage(word)
        #get content and chapter abbrevation
        content,chapter = self.obj_Book.makeMixAbbContentChap(word)
        # cotentNChap = f"{content}-{chapter}"
        return way,wKind,numW,numAll,word,content,chapter,wordsPage,linkWord


    def audioWord(self,word):
        link=""
        for col in self.obj_Db.wordCollection.find({"word":word},{"_id":0,"voice.telegramLink":1}):
            for keys in col.keys():
                for _,y in col[keys].items():
                    link = y
        output = f"<a href='{link}'> </a>"
        return output
    
    def audioAnswer(self,word,way):
        link = ""
        # print(f'way = {way},word = {word}')
        if way == "deutsch":
            for col in self.obj_Db.meaningCollection.find({"word":word},{"_id":0,"deuVoice.deuTelegramLink":1}):
                # print(col)
                for keys in col.keys():
                    # print(keys)
                    for _,y in col[keys].items():
                        link = y    
        elif way == "synonym":
            for col in self.obj_Db.meaningCollection.find({"word":word},{"_id":0,"synVoice.synTelegramLink":1}):
                for keys in col.keys():
                    for _,y in col[keys].items():
                        link = y  
        elif way == "persian":
            for col in self.obj_Db.meaningCollection.find({"word":word},{"_id":0,"perVoice.perTelegramLink":1}):
                for keys in col.keys():
                    for _,y in col[keys].items():
                        link = y 
        elif way == "english":
            for col in self.obj_Db.meaningCollection.find({"word":word},{"_id":0,"engVoice.engTelegramLink":1}):
                for keys in col.keys():
                    for _,y in col[keys].items():
                        link = y   
        elif way == "all together":
            for col in self.obj_Db.meaningCollection.find({"word":word},{"_id":0,"allVoice.allTelegramLink":1}):
                # print(col)
                for keys in col.keys():
                    for _,y in col[keys].items():
                        link = y           
        else:
            pass
        # print(f"link = {link}")
        output = f"<a href='{link}'> </a>"
        return output 



    


    #قرار دادن مقدار درون هر فیلد دیکشنری
    def updateValueKey(self,input):
        s =self.getTodayWordsCorrections()
        todayWords = self.getTodayWords()
        s[self.getOneRightWord(todayWords)]=input
        # print(f"new dictionary with key and values ={s}")
        self.obj_Db.userCollection.update_many({"userId":self.id},{"$set":{"todayWordsCorrection":s}})

    #قرار دادن مقدار درون هر فیلد دیکشنری
    def updateValueKeyAnswer(self,input):
        s =self.getTodayWordsNAnswer()
        todayWords = self.getTodayWords()
        s[self.getOneRightWord(todayWords)]=input
        
        # print(f"new dictionary with key and values ={s}")
        self.obj_Db.userCollection.update_many({"userId":self.id},{"$set":{"todayWordsNAnswer":s}})




    #todayWordsCorrection پیدا کردن  دیکشنری 
    def getTodayWordsCorrections(self):
        one =""
        for col in self.obj_Db.userCollection.find({"userId":self.id},{"todayWordsCorrection":1,"_id":0}):
            for keys in col.keys():
                one = col[keys]
        # print(f"todayWordsCorrection = {one}")
        return one



    # todayWordsNAnswer گرفتن مقدار فیلد 
    def getTodayWordsNAnswer(self):
        one =""
        for col in self.obj_Db.userCollection.find({"userId":self.id},{"todayWordsNAnswer":1,"_id":0}):
            for keys in col.keys():
                one = col[keys]
        # print(f"todayWordsNAnswer = {one}")
        return one


# Review().reviewWeakWordsNDetails()
# مرور واژه ها
class Review:
        def __init__(self,id):
            self.id = id
            self.obj_Db = Db()
            self.obj_Vazhegan = Vazhegan(id)
            self.obj_Report = Report (id)
            self.obj_Counter = Counter(id)
            self.obj_Book = Book(id)
            self.obj_IdentifyWordsSection = IdentifyWordsSection(id)
            self.obj_RaveshYadgiri = RaveshYadgiri(id)
            self.obj_UILanguage = UILanguage(id)

        
        # واژگان ناتوان با جزییات برگ،فصل و سرفصل،پاسخ،شمارند،شمار واژگان ناتوان،بخش
        def reviewWeakWordsNDetails(self):
            weakWords = self.getReviewWords()
            if len(weakWords) != 0 :  
                # print(f"weakWords = {weakWords}")
                word = self.obj_Vazhegan.getOneRightWordWithoutDuration(weakWords)
                # print(f"word = {word}")

                #FIXMEfixed fixed audio answer
                way = self.obj_RaveshYadgiri.getWay()
                link = self.obj_Vazhegan.audioWord(word)

                durationDays = self.getDuration(word)
                section = self.obj_IdentifyWordsSection.identifyOneWordSection(word)
                length = len(weakWords)
                counter = self.obj_Counter.getCounter()
                # answerPure = self.obj_Vazhegan.getOneAnswerPure(word)
                # answer = self.obj_Vazhegan.getOneAnswer(answerPure)
                chapter = self.obj_Book.getChapter(word)
                content = self.obj_Book.getContent(word)
                page = self.obj_Book.getOnePage(word)
                # print (f"word = {word} \n durationDays = {durationDays} \n section = {section} \n length = {length} \n counter = {counter}  \n answer = {answer} \n content = {content} \n chapter = {chapter} \n page = {page} \n link = {link}")
                return way,durationDays,counter,length,section,word,content,chapter,page,link
            else :
                # print("there is no weak words, not even single one")
                return False
         
        def getDuration(self,word):
            weakWords = self.getReviewWords()
            duration = ""
            for _,x in enumerate(weakWords):
                if word == x[0]:
                    duration = x[1]
                ###to ignore warning
                # print(index)
            return duration




        # واژگان موجود در بخش ها، با جزییات برگ،فصل و سرفصل،پاسخ،شمارند،شمار واژگان ،بخش
        def reviewBakhshhaWordsNDetails(self):
            words = self.getReviewWords()
            # print(f"words = {words}")
            word = self.obj_Vazhegan.getOneRightWord(words)
            # print(f"word = {word}")

            #FIXMEfixed audio answer
            way = self.obj_RaveshYadgiri.getWay()
            link = self.obj_Vazhegan.audioWord(word)

            section = self.obj_IdentifyWordsSection.identifyOneWordSection(word)
            length = len(words)
            counter = self.obj_Counter.getCounter()
            # answerPure = self.obj_Vazhegan.getOneAnswerPure(word)
            # answer = self.obj_Vazhegan.getOneAnswer(answerPure)
            chapter = self.obj_Book.getChapter(word)
            content = self.obj_Book.getContent(word)
            page = self.obj_Book.getOnePage(word)
            # print (f"word = {word} \n section = {section} \n length = {length} \n counter = {counter}   \n content = {content} \n chapter = {chapter} \n page = {page} \n link = {link}")
            return way,counter,length,section,word,page,content,chapter,link


        # واژگان براساس موضوع و زمینه، با جزییات برگ،فصل و سرفصل،پاسخ،شمارند،شمار ،بخش
        def reviewChapterContentWordsNDetails(self):
            words = self.getReviewWords()     
            # print(f"words = {words}")
            word = self.obj_Vazhegan.getOneRightWord(words)
            # print(f"word = {word}")

            #FIXMEfixed fixed audio answer
            way = self.obj_RaveshYadgiri.getWay()
            link = self.obj_Vazhegan.audioWord(word)
            # print(f"link = {link}")
            section = self.obj_IdentifyWordsSection.identifyOneWordSection(word)
            length = len(words)
            counter = self.obj_Counter.getCounter()
            # answerPure = self.obj_Vazhegan.getOneAnswerPure(word)
            # answer = self.obj_Vazhegan.getOneAnswer(answerPure)
            chapter = self.obj_Book.getChapter(word)
            content = self.obj_Book.getContent(word)
            page = self.obj_Book.getOnePage(word)
            
            # print (f"word = {word} \n section = {section} \n length = {length} \n counter = {counter}  \n answer = {answer} \n content = {content} \n chapter = {chapter} \n page = {page} \n link = {link}")
            # return way,content,chapter,word,answer,counter,length,section,page,link
            return way,content,chapter,word,counter,length,section,page,link

        # واژگان براساس موضوع و زمینه، با جزییات برگ،فصل و سرفصل،پاسخ،شمارند،شمار ،بخش
        def reviewANSWERChapterContentNDetails(self,answerWay):
            words = self.getReviewWords()     
            # print(f"words in reviewANSWERChapterContentNDetails = {words}")
            word = self.obj_Vazhegan.getOneRightWord(words)
            # print(f"word before = {word}")
            if isinstance(word,list) and isinstance(word[1],int):
                word = word[0]
            # print(f"word = {word}")
            # print(f"answerWay = {answerWay}")
            #FIXMEfixed fixed audio answer
            way = self.obj_RaveshYadgiri.getWay()
            link = self.obj_Vazhegan.audioAnswer(word,answerWay)
            # print(f"link = {link}")
            # section = self.obj_IdentifyWordsSection.identifyOneWordSection(word)[
            length = len(words)
            counter = self.obj_Counter.getCounter()
            # answerPure = self.obj_Vazhegan.getOneAnswerPure(word)
            answerPure = self.obj_Vazhegan.getAnswer(word,answerWay)
            answer = self.obj_Vazhegan.getOneAnswer(answerPure)
            # print(f'answerPure = {answerPure}\nanswer= {answer}')
            # chapter = self.obj_Book.getChapter(word)
            # content = self.obj_Book.getContent(word)
            # page = self.obj_Book.getOnePage(word)
            
            # print (f"word = {word} \n section = {section} \n length = {length} \n counter = {counter}  \n answer = {answer} \n content = {content} \n chapter = {chapter} \n page = {page} \n link = {link}")
            # return way,content,chapter,word,answer,counter,length,section,page,link
            return way,answer,counter,length,link

        # words = Review(self.id).sortChapterContentBase()
        # Review(self.id).saveReviewWords(words)
        # Review(self.id).reviewChapterContentWordsNDetails()

        #واژگان به ترتیب موضوع و زمینه
        def sortChapterContentBase(self):
            words = self.obj_Vazhegan.getAllWordsSection()
            wordNChapNContArray = []
            output = []
            # chapNCont = []
            for x in words :
                for col in self.obj_Db.bookCollection.find({"word":x},{"_id":0,"content":1,"chapter":1}):
                    chapNCont = []
                    for keys in col.keys():
                        chapNCont.append(col[keys])
                        # print(f"chapNCont = {chapNCont}")
                # chapNCont = chapNCont
                chapNCont = tuple(chapNCont)
                # chapNCont = chapNCont.replace("[","")
                # chapNCont = chapNCont.replace("]","")
                a = []
                a.append((x,chapNCont))
                # print(f"a = {a}")
                # print(f"a[0][0] = {a[0][0]}")
                # print(f"a[0][1][0] = {a[0][1][0]}")
                # print(f"a[0][1][1] = {a[0][1][1]}")
                a = (a[0][0],a[0][1][1], a[0][1][0])
                # print(f" a = {a}")
                wordNChapNContArray.append(a)
            # print(f"wordNChapNContArray = {wordNChapNContArray}")
            sortWCHCA = sorted(wordNChapNContArray,key = lambda x: str(x[1]), reverse = True)
            
            for x in sortWCHCA:
                output.append(x[0])
            output = tuple(output)
            # print(f"output = {output}")
            return output


        #واژگان به ترتیب بخش 
        def sortSectionBase(self):
            words = self.obj_Vazhegan.getAllWordsSection()
            wordNSectionArray = []
            output = []
            for x in words :
                for col in self.obj_Db.sectionCollection.find({"word":x},{"_id":0,"section":1}):
                    section = ""
                    for keys in col.keys():
                        section = int(col[keys])
                        # print(f"section = {section}")
                wordNSectionArray.append((x,section))
            # print(f"wordNChapNContArray = {wordNSectionArray}")
            sortWSec = sorted(wordNSectionArray,key = lambda x: str(x[1]), reverse = False)
            # print(f"sortWSec = {sortWSec}")
            for x in sortWSec:
                output.append(x[0])
            output = tuple(output)
            # print(f"output = {output}")
            return output








            ######گرفتن واژگان ناتوان به همراه مدت زمان  اقامت در جعبه لایتنر
        def weakWordsNDuraionSorted(self):
                outputList = []
                dict = self.obj_Report.weakWordDateEnterBoxSection()
                # print(f"dict = {dict}")
                for i in range(len(dict)):
                    a = str(datetime.datetime.now() - dict[i]["dateEnterTorBox"])
                    # print(f"a = {a}")
                    word = str(dict [i]["word"])
                    # print(f"word = {word}")
                    # word = wordIn.replace(","," _")
                    a = a.split(" ")
                    # print(f"a split = {a}")
                    try:
                        lengthDay = int(a[0])
                        # print(f"lengthDay = {lengthDay}")
                        if  lengthDay >30:
                            oneRec = (word,lengthDay)
                            # print(f"oneRec = {oneRec}")
                            outputList.append(oneRec)
                        # print(f"outputList = {outputList}")
                        
                    except:
                        pass
                # try:
                languageIn =self.obj_UILanguage.getUIL()
                # print(f"languageIn = {languageIn}")
                if outputList != []:
                    outputSorted = sorted(outputList, key = lambda x: float(x[1]), reverse = True)
                    # print(f"outputSorted = {outputSorted}")
                    return outputSorted
                else :
                    
                    if languageIn == "De":
                        output = "Es gibt noch keinen schwachen Wortschatz"
                    elif languageIn == "En":
                        output = "There is no weak vocabulary yet"
                    elif languageIn == "Per":
                        output = "واژگان ناتوان تا کنون وجود ندارد"
                    else:
                        output = "واژگان ناتوان تا کنون وجود ندارد"
                    print (f"output = {output}")
                    return False







           # واژه های ناتوان
        def sortedWeakWords(self):
            outputList = []
            dict = self.obj_Report.weakWordDateEnterBoxSection()
            # print(f"dict = {dict}")
            for i in range(len(dict)):
                a = str(datetime.datetime.now() - dict[i]["dateEnterTorBox"])
                a = a.split(" ")
                try:
                    lengthDay = int(a[0])
                    if  lengthDay >30:
                        word = dict [i]["word"]
                        outputList.append(word)
                except:
                    pass
            # print(f"outputList = {outputList}")
            # self.obj_Db.userCollection.update_many({"userId":self.id},{"$set":{"reviewWords":outputList}})
            return outputList
            ####

        # ذخیره واژه ها مرتب شده در پایگاه داده
        def saveReviewWords(self,words):
            self.obj_Db.userCollection.update_many({"userId":self.id},{"$set":{"reviewWords":words}})
        
        # گرفتن واژگان مرتب شده  برای مرور
        def getReviewWords(self):
            words = ""
            for col in self.obj_Db.userCollection.find({"userId":self.id},{"reviewWords":1,"_id":0}):
                for keys in col.keys():
                    words = col[keys]
            # print(f"words = {words}")
            return  words


            # def IdentifyWordsSection
            # گرفتن واژگان ناتوان از پایگاه داده
        def getWeakWords(self):
            weakWords = ""
            for col in self.obj_Db.userCollection.find({"userId":self.id},{"_id":0,"reviewWords":1}):
                for keys in col.keys():
                    weakWords = col[keys]
            # print( f"getWeakWords() = {weakWords}")
            return weakWords



        



class Counter:
    def __init__(self,id):
        self.id = int(id)
        self.obj_Db = Db()
        # self.colUser = Db().userCollection
        self.Vazhegan = Vazhegan(id)
        # self.getingCounter = self.getCounter()

    def putZeroToCounter(self):
        self.obj_Db.userCollection.update_many({"userId":self.id},{"$set":{"counter":0}})
    
    def putValueToCounter(self,val):
        self.obj_Db.userCollection.update_many({"userId":self.id},{"$set":{"counter":val}})

    def getCounter(self):
        for col in self.obj_Db.userCollection.find({"userId":self.id},{"counter":1,"_id":0}):
            for keys in col.keys():
                # print(f"counter = {col[keys]}")
                return col[keys]

    def addOneToCounter(self):
        addOneToCounter = int(self.getCounter()) +1
        # print(f"addOneToCounter = {addOneToCounter}")
        self.obj_Db.userCollection.update_many({"userId":self.id},{"$set":{"counter":addOneToCounter}}) 

    def subtractOneToCounter(self):
        subtractOneToCounter = int(self.getCounter()) -1
        if subtractOneToCounter < 0 :
            subtractOneToCounter = 0
        # print(f"subtractOneToCounter = {subtractOneToCounter}")
        self.obj_Db.userCollection.update_many({"userId":self.id},{"$set":{"counter":subtractOneToCounter}})    

    def lastWordVerification(self):
        lengthIndexes = len(self.Vazhegan.getTodayWords()) -1
        # print(f"lengthIndexes = {lengthIndexes}")
        counter = self.getCounter()
        # print(f"counter = {counter}")
        if lengthIndexes < counter:
            return False
        else:
            return True        

class Msg:
        def __init__(self,id=None,msg=None):
            if id is not None:
                    self.id = int(id)
            self.msg = msg
            self.obj_Db = Db()
            
        #FIXME پیام قبلی اگر پیشنهادات و انتقادات هست به پیامش ایراد کیبورد نگیرد
        def noneKeyboardMsgs(self,msg,userKind):
            # print(self.id)

            try:
                msgsToday = self.getMessagesToday(self.id)
                length = len(msgsToday)
                secondToLastMsg = msgsToday[length-2]
                # print(f"secondToLastMsg = {secondToLastMsg}")
                thirdToLastMsg = msgsToday[length-3]
                # print(f"thirdToLastMsg = {thirdToLastMsg}")
                fourthToLastMsg = msgsToday[length-4]
                # print(f"fourthToLastMsg = {fourthToLastMsg}")
                # userOpinionLangKeys = [PerBtn().opinion,DeBtn().opinion,EnBtn().opinion]
                output= ""
                if userKind == "Admin":
                    
                    msgsNotAvoid =  PerBtn().arrButtonPer + BtnS().arrButtonSame + PerBtnA().arrButtonAdminPer + ABtnS().avoidMsgs
                elif userKind == "User":
                    
                    msgsNotAvoid =  PerBtn().arrButtonPer + BtnS().arrButtonSame 
                # print(f"msg = {msg}")
                # print(f"msgsNotAvoid = {msgsNotAvoid}")
                if msg in msgsNotAvoid :
                    output = False
                elif secondToLastMsg == PerBtn().opinion or thirdToLastMsg == PerBtn().opinion  :
                    output = False
                elif secondToLastMsg == PerBtnA().sendToAll or thirdToLastMsg == PerBtnA().sendToAll or fourthToLastMsg == PerBtnA().sendToAll:
                    output = False
                else:
                    output = True
            
                return output

            except:
                return False

        #FIXME پیام قبلی اگر پیشنهادات و انتقادات هست به پیامش ایراد کیبورد نگیرد
        def noneKeyboardMsgsDe(self,msg,userKind):
            # print(self.id)
            try:
                msgsToday = self.getMessagesToday(self.id)
                length = len(msgsToday)

                secondToLastMsg = msgsToday[length-2]
                # print(f"secondToLastMsg = {secondToLastMsg}")
                thirdToLastMsg = msgsToday[length-3]
                # print(f"thirdToLastMsg = {thirdToLastMsg}")
                fourthToLastMsg = msgsToday[length-4]
                # print(f"fourthToLastMsg = {fourthToLastMsg}")
                output= ""
                if userKind == "Admin":
                    
                    msgsNotAvoid =  DeBtn().arrButtonDe + BtnS().arrButtonSame + DeBtnA().arrButtonAdminDe + ABtnS().avoidMsgs

                elif userKind == "User":
                    
                    msgsNotAvoid =  DeBtn().arrButtonDe + BtnS().arrButtonSame 

                # print(f"msg = {msg}")
                # print(f"msgsNotAvoid = {msgsNotAvoid}")
                if msg in msgsNotAvoid :
                    output = False
                elif secondToLastMsg == DeBtn().opinion or thirdToLastMsg == DeBtn().opinion  :
                    output = False
                elif secondToLastMsg == DeBtnA().sendToAll or thirdToLastMsg == DeBtnA().sendToAll or fourthToLastMsg == DeBtnA().sendToAll:
                    output = False
                else:
                    output = True

                return output

            except:
                return False
            #verification for nonkeyboard input if false means it's from bot keyboard and if true it come from main keyboard
           
           #FIXME پیام قبلی اگر پیشنهادات و انتقادات هست به پیامش ایراد کیبورد نگیرد
            #FIXME پیام به همه تنظیم برای فرستادن پیام و خارج از کیبورد بودن
        def noneKeyboardMsgsEn(self,msg,userKind):
            # print(self.id)
            try:
                msgsToday = self.getMessagesToday(self.id)
                length = len(msgsToday)
                secondToLastMsg = msgsToday[length-2]
                # print(f"secondToLastMsg = {secondToLastMsg}")
                thirdToLastMsg = msgsToday[length-3]
                # print(f"thirdToLastMsg = {thirdToLastMsg}")
                fourthToLastMsg = msgsToday[length-4]
                # print(f"fourthToLastMsg = {fourthToLastMsg}")
                output= ""
                if userKind == "Admin":
                    
                    msgsNotAvoid =  EnBtn().arrButtonEn + BtnS().arrButtonSame + EnBtnA().arrButtonAdminEn + ABtnS().avoidMsgs
                elif userKind == "User":
                    
                    msgsNotAvoid =  EnBtn().arrButtonEn + BtnS().arrButtonSame 
                # print(f"msg = {msg}")
                # print(f"msgsNotAvoid = {msgsNotAvoid}")
                if msg in msgsNotAvoid :
                    output = False
                elif secondToLastMsg == EnBtn().opinion or thirdToLastMsg == EnBtn().opinion  :
                    output = False
                elif secondToLastMsg == EnBtnA().sendToAll or thirdToLastMsg == EnBtnA().sendToAll or fourthToLastMsg == EnBtnA().sendToAll:
                    output = False
                else:
                    output = True

                return output
            except:
                return False


        # get message one user from    msgs.date->January_17_2020.[{msg}] 
        def getMessagesToday(self,id):
            now = datetime.datetime.now()
            # print(now)
            field = now.strftime("%B_%d_%Y")
            # print(field)
            msgsDateField = ""
            for col in self.obj_Db.userCollection.find({"userId":id},{f"msgs.{field}":1,"_id":0}):
                for keys in col.keys():
                    msgsDateField = col[keys][field]
            msgs=[]
            for col in msgsDateField :
                for key,value in col.items():
                    if key == "msg":
                       msgs.append(value)
            # print(f"msgs = {msgs}")         
            return msgs 
        

        # آیا پیام آخری ثبت شده امروز تکراری بود کاری است که این متد انجام می دهد در صورت ترو بودن به معنای تکرای بودن پیام می باشد
        def isTheLastOneRepeatedMsg(self,id,userKind):
            msgs = self.getMessagesToday(id)
            length = len(msgs)
            outputAvoidMsgs = ""
            output = ""
            
            language = UILanguage(id).getUIL()
            # if language == "En":
            #     msgsAvoid = EnBtn().avoidMsgs + EnBtnA().avoidMsgs
            # elif language == "De":
            #     msgsAvoid = DeBtn().avoidMsgs + DeBtnA().avoidMsgs
            # elif language == "Per" or language == "":
            #     msgsAvoid = PerBtn().avoidMsgs + PerBtnA().avoidMsgs

            if userKind == "Admin" :
                if language == "En":
                    msgsAvoid = EnBtnA().avoidMsgs + EnBtn().avoidMsgs 
                elif language == "De":
                    msgsAvoid = DeBtnA().avoidMsgs + DeBtn().avoidMsgs
                elif language == "Per" or language == "":
                    msgsAvoid = PerBtnA().avoidMsgs + PerBtn().avoidMsgs 

            elif userKind == "User":
                if language == "En":
                    msgsAvoid = EnBtn().avoidMsgs 
                elif language == "De":
                    msgsAvoid = DeBtn().avoidMsgs
                elif language == "Per" or language == "":
                    msgsAvoid = PerBtn().avoidMsgs           
           
            for col in msgsAvoid:  
                # print(f"col = {col}")
                # print(f"msgs[length-1] = {msgs[length-1]}")
                if msgs[length-1] == col:
                    outputAvoidMsgs = True
            try:
                # print(msgs[length-1])
                # print(f"msgsAvoid = {msgsAvoid}")
                if msgs[length-1] in msgsAvoid :
                    output = False 
                elif msgs[length-1] == msgs[length-2] and msgs[length-1] == msgs[length-3] and outputAvoidMsgs is not True:
                        # print(f"msgs[length-2] = {msgs[length-2]}")
                        # print(f"msgs[length-2] = {msgs[length-2]}")
                        output = True
            except:
                pass
            if output == "" or length == 1:
                output = False
            # print(f"isTheLastOneRepeatedMsg() output = {output}")
            return output


        #گرفتن پیام های ثبت شده بدست کاربر    
        def getMsgs(self):
            withdraw =""
            for col in self.obj_Db.userCollection.find({"userId":self.id},{"msgs":1,"_id":0}):
            # for col in self.obj_Db.userCollection.find({"userId":self.id},{"msgs":{ "$elemMatch":{"December_26_2019":1,"_id":0}}}):    
                # { viewData: { $elemMatch : { "widgetData.widget.title": "England" } } }
                # print(f"col = {col}")
                for keys in col.keys():
                    # print(f"keys = {keys}")
                    # print(f"col[keys] = {col[keys]}")
                    withdraw = col[keys]
            # print(f"withdraw = {withdraw}")
            return withdraw

        #December_26_2019 تبدیل تاریخ امروز به حروف در غالب استرینگ مانند 
        def msgsDateAlpha(self):
            now = datetime.datetime.now()
            output = now.strftime("%B_%d_%Y")   
            return output 

        #FIXMEfixed اشکال به تعداد تیترهای موجود در ام اس جی اس پیام اول را تکراری می زند
        # افزودن پیام تازه به پیام های قدیمی
        def addMsgs(self,msg):
            msgs = self.getMsgs()
            # print(f"msgs = {msgs}")
            titr = self.msgsDateAlpha()
            # print(f"titr = {titr}")
            arr = []
            #it needs update or assign
            assigning = ""
            if msgs != "":
                newEntry = {"timedate":datetime.datetime.now(),"msg":msg}
                for x,y in msgs.items():
                    if x == titr:
                        arr = y
                        # print(f"arr = {arr}")
                        arr.append(newEntry)
                        self.obj_Db.userCollection.update_many({"userId":self.id},{"$set":{f"msgs.{titr}":arr}})
                        assigning = False

                if assigning is not False:
                    arr.append(newEntry)
                    self.obj_Db.userCollection.update_many({"userId":self.id},{"$set":{f"msgs.{titr}":arr}})
            else:
                newEntry = {titr:[{"timedate":datetime.datetime.now(),"msg":msg}]}
                self.obj_Db.userCollection.update_many({"userId":self.id},{"$set":{f"msgs":newEntry}})
        
        def getOpMsgs(self):
            withdraw =""
            for col in self.obj_Db.userCollection.find({"userId":self.id},{"opinion":1,"_id":0}):
            # for col in self.obj_Db.userCollection.find({"userId":self.id},{"msgs":{ "$elemMatch":{"December_26_2019":1,"_id":0}}}):    
                # { viewData: { $elemMatch : { "widgetData.widget.title": "England" } } }
                # print(f"col = {col}")
                for keys in col.keys():
                    # print(f"keys = {keys}")
                    # print(f"col[keys] = {col[keys]}")
                    withdraw = col[keys]
            # print(f"withdraw = {withdraw}")
            return withdraw

        #FIXME isSecondTodEndMsg or isThirdTodEndMsg ?
        def isSecondTodEndMsg(self):
            msgs = self.getMessagesToday(self.id)
            # print(msgs)
            length = len(msgs)
            # print(length)
            # thirdToEnd = msgs[length-3]
            # print(f"thirdToEnd = {thirdToEnd}")
            secondToEnd = msgs[length-2]
            # print(f"secondToEnd = {secondToEnd}")
            # firstToEnd = msgs[length-2]
            # print(f"firstToEnd = {firstToEnd}")
            if secondToEnd == PerBtn().opinion or secondToEnd == DeBtn().opinion or secondToEnd == EnBtn().opinion:
                return True
            else:
                return False


        #FIXME Opinion
        def saveOpinion(self,msg):
            length = len(msg)
            # print(f"length msg = {length}")
            msgs = self.getOpMsgs()
            # print(f"msgs = {msgs}")
            titr = self.msgsDateAlpha()
            # print(f"titr = {titr}")
            arr = []
            #it needs update or assign
            now = datetime.datetime.today()
            year = now.year
            month = now.month
            day = now.day
            hour = now.hour
            minute = now.minute
            second = now.second
            rndNum = random.randint(0,10000)
            opId = f"{rndNum}{year}{month}{day}{hour}{minute}{second}"
            print(opId)
            msgsAvoidhere = EnBtn().arrButtonEn + BtnS().arrButtonSame + EnBtnA().arrButtonAdminEn + DeBtn().arrButtonDe +  DeBtnA().arrButtonAdminDe + PerBtn().arrButtonPer + PerBtnA().arrButtonAdminPer
            msgsGetBack = EnBtn().getBack + DeBtn().getBack + PerBtn().getBack
            msgsAvoid = list(set(msgsAvoidhere) - set(msgsGetBack))
            # opId = uuid.uuid4().hex
            output = ""
            if length < 4050: 
                if msg not in msgsAvoid:
                    assigning = ""
                    if msgs != "":
                        newEntry = {"timedate":datetime.datetime.now(),"oPMsg":msg,"oPId":opId}
                        for x,y in msgs.items():
                            if x == titr:
                                arr = y
                                # print(f"arr = {arr}")
                                arr.append(newEntry)
                                self.obj_Db.userCollection.update_many({"userId":self.id},{"$set":{f"opinion.{titr}":arr}})
                                assigning = False

                        if assigning is not False:
                            arr.append(newEntry)
                            self.obj_Db.userCollection.update_many({"userId":self.id},{"$set":{f"opinion.{titr}":arr}})
                    else:
                        newEntry = {titr:[{"timedate":datetime.datetime.now(),"oPMsg":msg,"oPId":opId}]}
                        self.obj_Db.userCollection.update_many({"userId":self.id},{"$set":{f"opinion":newEntry}})
                    output = True
                    return output,opId
                #clicked getBack
                elif msg in msgsGetBack:
                    output = False
                    opId = "getBack"
                    return output,opId
                #bot keyboard Clicked
                else:
                    output = False
                    opId = "botKeyboard"
                    return output,opId
            else:
                output = False
                opId = "outOfRange"
                return output,opId
                
            






class Book:
    def __init__(self,id):
        self.id = int(id)
        # self.word = word
        self.obj_Db = Db()
        # self.colBook = Db().bookCollection

    def getChapter(self,word):
        chapter = ""
        for col in self.obj_Db.bookCollection.find({"word":word},{"chapter":1,"_id":0}):
                for keys in col.keys():
                    chapter = (col[keys])
        # print(f"chapter = {chapter}")
        return chapter

    def getContent(self,word):
        content = ""
        for col in self.obj_Db.bookCollection.find({"word":word},{"content":1,"_id":0}):
            for keys in col.keys():
                content = (col[keys])
        # print(f"content = {content}")
        return content
   
    def getPages(self,word):
        pages = []
        for col in self.obj_Db.bookCollection.find({"word":{"$in":word}},{"page":1,"_id":0}
        ):
                for keys in col.keys():
                    pages.append(col[keys])
                
        # print(f"pages = {pages}")
        return pages
    
    def getOnePage(self,word):
        page = ""
        for col in self.obj_Db.bookCollection.find({"word":word},{"page":1,"_id":0}):
                for keys in col.keys():
                    page =(col[keys])
        page = page.replace("&","-")                
        # print(f"page = {page}")
        return page

    def makeMixAbbContentChap(self,word):
        contentArray = self.getContent(word).split("-")
        content = contentArray[0]
        # print(f"content = {content}")
        # A-Kontakte, Informationen zur Person
        chapterArray = self.getChapter(word).split(" ")
        
        chapter = chapterArray[0]
        # print(f"chapter = {chapter}")
        # 1 sich vorstellen
        # output = f"{content}-{chapter}"
        # print(f"output = {output}")
        return content,chapter

  #مرور واژگان گذشته      
class MorurVazhehayeGozashteh:
    def __init__(self,id):
        self.id = int(id)
        self.obj_Vazhegan = Vazhegan(id)
        self.obj_Db = Db()
   


# نمایان کردن واژگان در هر بخش
class IdentifyWordsSection:
    def __init__(self,id,msg=None):
        self.id = id
        self.msg = msg
        self.obj_Db = Db()
        # self.obj_Correction = Correction(id)
        self.obj_Vazhegan = Vazhegan(id)
        self.obj_RaveshYadgiri = RaveshYadgiri(id,msg)
        self.obj_UILanguage = UILanguage(id)
        
    #planA
#باتوجه به پاسخ واژه پیدا کردن
    def meaningIdIdentify(self):
        id = ""
        todayWordsNAnswer = self.obj_Vazhegan.getTodayWordsNAnswer()
        word = self.obj_Vazhegan.getOneRightWordBehind(1)
        answer = todayWordsNAnswer[word]

        way = self.obj_RaveshYadgiri.getWay()
        if way == "all together":
            answerArray = answer.split(" ")
            way = answerArray[1]
            answerArray2 = answer.split(f" \n ")
            # print(f"answerArray2 = {answerArray2}")
            meaning = answerArray2[1]
            answer = meaning
            # print( f"answer = {answer}")
        for col in self.obj_Db.meaningCollection.find({"word":word,self.msg:answer},{"_id":1}):
            for keys in col.keys():
                id = col[keys]
        return id

    #planB
    #FIXMEfixed just change it with meaningIdIdentify()
#باتوجه به پاسخ واژه پیدا کردن
    def meaningIdIdentifyNew(self):
        id = ""
        todayWordsNAnswer = self.obj_Vazhegan.getTodayWordsNAnswer()
        word = self.obj_Vazhegan.getOneRightWordBehind(1)
        answer = todayWordsNAnswer[word]
        answerArray = answer.split(" ")
        way = answerArray[1]
        # print(f"way = {way}")
        answerArray2 = answer.split(f" \n ")
        # print(f"answerArray2 = {answerArray2}")
        meaning = answerArray2[1]
        # print( f"answer = {answer}")
        # print(meaning)
        #####
        for col in self.obj_Db.meaningCollection.find({"word":word,way:meaning},{"_id":1}):
            for keys in col.keys():
                id = col[keys]
        return id


    def makeWordSection(self,one):
        wordsDic =self.obj_Vazhegan.getOneRightWordBehind(1)
        #planB
        #FIXMEfixed just change getWay() to getWayBool() or delete oldest and put newest by name of getWay()
        # way = self.obj_RaveshYadgiri.getWayBool()
        #planA
        way = self.obj_RaveshYadgiri.getWay()
        # for col in wordsDic:
        newSection = {"section":1,"way":way,"dateEnterTorBox":datetime.datetime.now(),"dateTimeEnterToSection":datetime.datetime.now(),"dateTimeOutput":"","userId":self.id,"word":wordsDic,"meaningId":self.meaningIdIdentify()}
        self.obj_Db.sectionCollection.insert_one(newSection)

    def moveToNextLevel(self,one):
        section = 0
        wordDic = self.obj_Vazhegan.getOneRightWordBehind(one)
        dic= self.obj_Vazhegan.getTodayWordsCorrections()
        # print(f"wordDic= {wordDic}") 
        # print(f"dic[wordDic]= {dic[wordDic]}")
        if dic[wordDic] == True:
            # print(f"dic[wordDic] = {dic[wordDic]}")      
            for coli in self.obj_Db.sectionCollection.find({"userId":self.id,"word":wordDic},{"section":1,"_id":0}):
                for keys in coli.keys():
                    section = coli[keys]
            section +=1
            # section = 1
            # print(section)
            self.obj_Db.sectionCollection.update_many({"userId":self.id,"word":wordDic},{"$set":{"section":section,"dateTimeEnterToSection":datetime.datetime.now()}})
        elif dic[wordDic] == False:
            self.obj_Db.sectionCollection.update_many({"userId":self.id,"word":wordDic},{"$set":{"section":1,"dateTimeEnterToSection":datetime.datetime.now()}})


    def findUserNWord(self):
        a = []
        one = 1
        word=self.obj_Vazhegan.getOneRightWordBehind(one)
        for col in self.obj_Db.sectionCollection.find({"userId":self.id,"word":word},{"_id":0,"section":1,"word":1}):
            a.append(col)
        have_list = True if len(list(a)) else False
        # print(have_list)
        return have_list

    def deleteAllSections(self):
        self.obj_Db.sectionCollection.delete_many({"userId":self.id})
    
    def identifyOneWordSection(self,word):
        languageIn =self.obj_UILanguage.getUIL()
        # print(f"languageIn = {languageIn}")
        if languageIn == "De":
            sectionDictDe = {"1":"1. Partition","2":"2. Partition","3":"3. Partition","4":"4. Partition","5":"5. Partition","6":"6. Partition"}
            sectionDict = sectionDictDe
        elif languageIn == "En":
            sectionDictEn = {"1":"1Th partition","2":"2Th partition","3":"3Th partition","4":"4Th partition","5":"5Th partition","6":"6Th partition"}
            sectionDict = sectionDictEn
        elif languageIn == "Per":
            sectionDictPer = {"1":"بخش نخست","2":"بخش دوم","3":"بخش سوم","4":"بخش چهارم","5":"بخش پنجم","6":"بخش ششم"}
            sectionDict = sectionDictPer
        # sectionDict = {"1":"بخش نخست","2":"بخش دوم","3":"بخش سوم","4":"بخش چهارم","5":"بخش پنجم","6":"بخش ششم"}
        section = "" 
        sectionNum = ""
        for col in self.obj_Db.sectionCollection.find({"userId":self.id,"word":word},{"section":1,"_id":0}):
            for keys in col.keys():
                # print(f"col[keys] = {col[keys]}")
                sectionNum = str(col[keys])
        for col in sectionDict:
                if  col == sectionNum:
                    section = sectionDict[col]
        # print(f"section = {section}")           
        return section

#کلاس گزارش ها
class Report:
    def __init__(self,id):
        self.id = id
        self.obj_Db = Db()
        # self.obj_Correction = Correction(id)
        self.obj_Percentage = Percentage()
        self.obj_Graph = Graph()
        self.obj_Vazhegan = Vazhegan(id)
        self.obj_DateArrange = DateArrange(id)
        self.obj_RaveshYadgiri = RaveshYadgiri(id)
        self.obj_ShomarVazhgan = ShomarVazhgan(id)
        self.obj_UILanguage = UILanguage(id)
        self.obj_Counter = Counter(id)
        inp= "config.cfg"
        self.bot = pybotc.Bot(inp) 

    #FIXME leitnerBoxStatistics
    def firstLeitnerBoxStatistics(self,key):
        pattitionsWordNumNLearnedNum = self.wordsSectionPosition()
        # firstLevelKey = [EnBtn().startLearning,EnBtn().dailyLearnWords,DeBtn().startLearning,DeBtn().dailyLearnWords,PerBtn().startLearning,PerBtn().dailyLearnWords]
        # structLast = {"temporary.lastWordsPartion":pattitionsWordNumNLearnedNum}
        # if key in firstLevelKey:
        structFirst = {"temporary.firstWordsPartion":pattitionsWordNumNLearnedNum}
        self.obj_Db.userCollection.update_many({"userId":self.id},{"$set":structFirst})
        # else:
        #     structLast = {"temporary.lastWordsPartion":pattitionsWordNumNLearnedNum}
        #     self.obj_Db.userCollection.update_many({"userId":self.id},{"$set":structLast})
        
    def lastLeitnerBoxStatistics(self,key):
        pattitionsWordNumNLearnedNum = self.wordsSectionPosition()
        structLast = {"temporary.lastWordsPartion":pattitionsWordNumNLearnedNum}
        self.obj_Db.userCollection.update_many({"userId":self.id},{"$set":structLast})

    def getLeitnerBoxStatistics(self):
        # firstName,language
        firstPattitionsWordNumNLearnedNum = ""
        for col in self.obj_Db.userCollection.find({"userId":self.id},{"_id":0,"temporary.firstWordsPartion":1}):
            for keys in col.keys():
                for _,y in col[keys].items():
                        firstPattitionsWordNumNLearnedNum = y  
                # firstPattitionsWordNumNLearnedNum = col[key]
        lastPattitionsWordNumNLearnedNum = ""
        for col in self.obj_Db.userCollection.find({"userId":self.id},{"_id":0,"temporary.lastWordsPartion":1}):
            for keys in col.keys():
                for _,z in col[keys].items():
                        lastPattitionsWordNumNLearnedNum = z
        return firstPattitionsWordNumNLearnedNum, lastPattitionsWordNumNLearnedNum

    def channelMemberVerification(self,chat_id):
        reportNum = self.getReportNum()
        if reportNum != 0:
            channelVerified,out = self.bot.getChatMember(chat_id,self.id)
            print(f"channelVerified= {channelVerified}")
            print(f"out = {out}")
            # print(f'reportNum = {self.getReportNum()}')
            if  reportNum > 0 and channelVerified is True:

                return True
            else:
                return False
        elif reportNum == 0:
            return 0


    
    def dailyReport(self):
        self.obj_DateArrange.saveFalseRightWrongLampFlag(self.id)
        self.obj_DateArrange.saveFalseAutomateMsgFlag(self.id)
        all = self.allWordsNum()
        right = self.rightWordsNum()
        wrong = self.wrongWordsNum()
        #اضافه کردن یک رقم به عدد و شمار گزارش <reportNum>
        self.addOneToReportNum()
        #نگاشتن تاریخ یادگیری و تمرین نوبت پسین  و بعدی در فردا
        tomorrowNextTraining = self.obj_DateArrange.getTomorrowNextTraining(self.id)
        houNMTraining = tomorrowNextTraining.strftime("%H:%M")
        wrongWordsNpages = self.wrongWordsWithPages()
        wordsSectionPosition = self.wordsSectionPosition()
        self.obj_Counter.putZeroToCounter()
        #گرفتن سال ، ماه نویسه ای ، روز
        # monthAlpha,year,month,day,monthAlphaFinglish,weekDayPer,weekDayFinglish
        monthAlpha,year,_,day,_,_,_ = self.obj_DateArrange.convertToKhorshidi(tomorrowNextTraining) 
        # print(ـ)
        weekDay = self.obj_DateArrange.getWeekDay(tomorrowNextTraining)
        #Grigori date sort and tidy
        dateGriNextTraining = tomorrowNextTraining.date().strftime("%B %d, %Y")
        # print(f"dateGriNextTraining = {dateGriNextTraining}")
        return all,right,wrong,wrongWordsNpages,weekDay,day,monthAlpha,year,houNMTraining,dateGriNextTraining,wordsSectionPosition,


       #گزارش نخستین یادگیری 
    def getReportNum(self):
        for col in self.obj_Db.userCollection.find({"userId":self.id},{"reportNum":1,"_id":0}):
            for keys in col.keys():
                 
                return col[keys]

    def addOneToReportNum(self):
        num = 0
        num = self.getReportNum()
        numPlus = num +1
        self.obj_Db.userCollection.update_many({"userId":self.id},{"$set":{"reportNum":numPlus}})
        # pass

    def addReportNumField(self):
        self.obj_Db.userCollection.update_many({"userId":self.id},{"$set":{"reportNum":0}})
    #واژه های درست 
    def rightWords(self):
        wordsDictionary = self.obj_Vazhegan.getTodayWordsCorrections()
        # print(f"wordsDictionary = {wordsDictionary}")
        rightCorrections = []
        for x in wordsDictionary:
            # print(wordsDictionary[x])
            if wordsDictionary[x] == True:
                rightCorrections.append(wordsDictionary[x])
        # print(f"rightCorrections = {rightCorrections}")
        return rightCorrections

    #شمار و تعداد واژه های درست
    def rightWordsNum(self):
        rightCorrections = self.rightWords()
        # print(f"rightCorrections = {rightCorrections}")
        lengthRightCorrections = len(rightCorrections)
        # print(f"lengthRightCorrections={lengthRightCorrections}")
        return lengthRightCorrections

        #واژه های نادرست امروز
    def wrongWords(self):
        wordsDictionary = self.obj_Vazhegan.getTodayWordsCorrections()
        # print(f"wordsDictionary = {wordsDictionary}")
        wrongCorrections = []
        for x in wordsDictionary:
            # print(wordsDictionary[x])
            if wordsDictionary[x] == False:
                wrongCorrections.append(x)
               
        # print(f"wrongCorrections = {wrongCorrections}")
        return wrongCorrections

        #تعداد واژه های نادرست
    def wrongWordsNum(self):
        lengthWrongCorrections = len(self.wrongWords())
        # print(f"lengthWrongCorrections={lengthWrongCorrections}")
        return lengthWrongCorrections

    # تمام واژه های کار شده امروز
    def allWordsNum(self):
        lengthAllWordsNum = len(self.obj_Vazhegan.getTodayWordsCorrections())
        # print(f"lengthAllWordsNum = {lengthAllWordsNum}")
        return lengthAllWordsNum

    def wrongWordsPages(self):
        wrongWords = self.wrongWords()
        # print(f"wrongWords = {wrongWords}")
        pages = []
        for x in wrongWords:
            # print(f"x = {x}")
            for col in self.obj_Db.bookCollection.find({"word":x},{"_id":0,"page":1}):
                for keys in col.keys():
                    pages.append(col[keys])
                    # print(f"{x} = {pages}")
        
        # print(f"pages = {pages}")
        return pages

    #درآوردن واژه های درون هر قسمت در بسته
    def wordsSectionPosition(self):
        section_1_words = []
        for col in self.obj_Db.sectionCollection.find({"userId":self.id,"section":1},{"word":1,"_id":0}):
            for keys in col.keys():
               section_1_words.append(col[keys])
        # print(f"section_1_words = {section_1_words}")
        section_1 = len(section_1_words) 
        # print(f"section_1 = {section_1}")
        section_2_words = []
        for col in self.obj_Db.sectionCollection.find({"userId":self.id,"section":2},{"word":1,"_id":0}):
            for keys in col.keys():
               section_2_words.append(col[keys])
        # print(f"section_2_words = {section_2_words}")
        section_2 = len(section_2_words)
        # print(f"section_2 = {section_2}") 

        section_3_words = []
        for col in self.obj_Db.sectionCollection.find({"userId":self.id,"section":3},{"word":1,"_id":0}):
            for keys in col.keys():
               section_3_words.append(col[keys])
        # print(f"section_3_words = {section_3_words}")
        section_3 = len(section_3_words) 
        # print(f"section_3 = {section_3}")

        section_4_words = []
        for col in self.obj_Db.sectionCollection.find({"userId":self.id,"section":4},{"word":1,"_id":0}):
            for keys in col.keys():
               section_4_words.append(col[keys])
        # print(f"section_4_words = {section_4_words}")
        section_4 = len(section_4_words)
        # print(f"section_4 = {section_4}") 

        section_5_words = []
        for col in self.obj_Db.sectionCollection.find({"userId":self.id,"section":5},{"word":1,"_id":0}):
            for keys in col.keys():
               section_5_words.append(col[keys])
        # print(f"section_5_words = {section_5_words}")
        section_5 = len(section_5_words)
        # print(f"section_5 = {section_5}") 

        section_6_words = []
        for col in self.obj_Db.sectionCollection.find({"userId":self.id,"section":6},{"word":1,"_id":0}):
            for keys in col.keys():
               section_6_words.append(col[keys])
        # print(f"section_6_words = {section_6_words}")
        section_6 = len(section_6_words) 
        # print(f"section_6 = {section_6}")

        section_7_words = []
        for col in self.obj_Db.sectionCollection.find({"userId":self.id,"section":7},{"word":1,"_id":0}):
            for keys in col.keys():
               section_7_words.append(col[keys])
        # print(f"section_7_words = {section_7_words}")
        section_7 = len(section_7_words) 
        # print(f"section_7 = {section_7}")
        all = [section_1,section_2,section_3,section_4,section_5,section_6,section_7]
        # print(f"wordsSectionPosition() = {all}")
        return all

    # قراردادن برگ های کتاب در مقابل واژه های نادرست  در چاچوب استرینگ
    def wrongWordsWithPages(self):
        wrongWords = self.wrongWords()
        pages = self.wrongWordsPages()
        dicWWordsNPages = dict(zip(wrongWords,pages))
        # print(f"wrongWords = {wrongWords}")
        # print(f"pages = {pages}")
        stringDWWANP = str(dicWWordsNPages)
        DWWANP = stringDWWANP.replace("{","")
        DWWANP2 = DWWANP.replace("}","")
        DWWANPOutput = DWWANP2.replace("&","-")
        # print(f"DWWANPOutput = {DWWANPOutput}")
        
        languageIn =self.obj_UILanguage.getUIL()
        # print(f"languageIn = {languageIn}")
        if languageIn == "De":
                output = "Du hattest heute keine falschen Worte"
        elif languageIn == "En":
                output = "You didn't have any wrong words today"
        elif languageIn == "Per":
                output = "امروز هیچ واژه نادرستی نداشتی"
        else:
                output = "امروز هیچ واژه نادرستی نداشتی"

        if len(DWWANPOutput) == 0 :
            return output
        else :
            return DWWANPOutput


    ####گزارش واژگان ناتوان ####

    # واژه های ضعیف به همراه تاریخ ورود به جعبه و بخش در چهارچوب دیکشنری
    def weakWordDateEnterBoxSection(self):
        
        # self.obj_Db.
        agg = [
            {"$match":{"userId":self.id}},
            {"$lookup":{
            "from":"section",
            "localField":"userId",
            "foreignField":"userId",
            "as":"join"
        }}
        ,{"$unwind":"$join"},
        {"$project":{"_id":0,
        "dateEnterTorBox":"$join.dateEnterTorBox",
        "word":"$join.word",
        "section":"$join.section",
        "userId":"$join.userId"
        }}
        ]
        # agg
        
        c = self.obj_Db.userCollection.aggregate(agg)
        # c.aggregate([{"$match":{"userId":self.id}}])
        
        dict = []
        for item in c :
            dict.append(item)
        # print(f"dict = {dict}")
        return dict
   

        
    


    # واژه های ضعیف به همراه مدت زمان و بخش 
    def weakWordDuraionSection(self):
        outputList = []
        dict = self.weakWordDateEnterBoxSection()
        for i in range(len(dict)):
            a = str(datetime.datetime.now() - dict[i]["dateEnterTorBox"])
            word = dict [i]["word"]
            word = word.replace(",",";")
            sectionNum = str(dict [i]["section"])
            languageIn =self.obj_UILanguage.getUIL()
            # print(f"languageIn = {languageIn}")
            if languageIn == "De":
                sectionDictDe = {"1":"1. Partition","2":"2. Partition","3":"3. Partition","4":"4. Partition","5":"5. Partition","6":"6. Partition"}
                sectionDict = sectionDictDe
            elif languageIn == "En":
                sectionDictEn = {"1":"1Th partition","2":"2Th partition","3":"3Th partition","4":"4Th partition","5":"5Th partition","6":"6Th partition"}
                sectionDict = sectionDictEn
            elif languageIn == "Per":
                sectionDictPer = {"1":"بخش نخست","2":"بخش دوم","3":"بخش سوم","4":"بخش چهارم","5":"بخش پنجم","6":"بخش ششم"}
                sectionDict = sectionDictPer

            section = ""
            for col in sectionDict:
                if  col == sectionNum:
                    section = sectionDict[col]
            a = a.split(" ")
            try:
                lengthDay = int(a[0])
                if  lengthDay >30:
                    if languageIn == "De":
                        day = "Tage"
                    elif languageIn == "En":
                        day = "Days"
                    elif languageIn == "Per":
                        day = "روز"
                    oneRec = (word,":",section,lengthDay,f"{day}$")
                    # print(oneRec)
                    outputList.append(oneRec)
            except:
                pass
        outputSorted = sorted(outputList, key = lambda x: float(x[3]), reverse = True)
        outputStr = str(outputSorted)
        output = outputStr.replace(",","")
        output = output.replace("$","\n")
        
        output = output[1:]
        length = len(output)
        output = output[:length-1]
        output = output.replace("(","")
        output = output.replace(")","")
        output = output.replace("'","")
        output = str(output)
        languageIn =self.obj_UILanguage.getUIL()
        # print(f"languageIn = {languageIn}")

        
        if output != "":
            print (f"output = {output}")
        elif languageIn == "De":
            output = "Es gibt noch keinen schwachen Wortschatz"
        elif languageIn == "En":
            output = "There is no weak vocabulary yet"
        elif languageIn == "Per":
            output = "واژگان ناتوان تا کنون وجود ندارد"
        else :
            output = "واژگان ناتوان تا کنون وجود ندارد"
            # print (f"output = {output}")
        return output

    #  درصد ،گراف و بخش واژگان ناتوان
    def weakWordsPercentageGraphSection(self):
        dict = self.weakWordDateEnterBoxSection()
        words = []
        sections = []
        sectionsCount = [0,0,0,0,0,0,0]
        for i in range(len(dict)):
            a = str(datetime.datetime.now() - dict[i]["dateEnterTorBox"])
            a = a.split(" ")
            # print(f"a = {a}")
            try:
                lengthDay = int(a[0])
                if  lengthDay >30:
                    words.append(dict [i]["word"])
                    sections.append(dict [i]["section"])
            except:
                pass
        # print(f"words = {words} \n section = {sections}")
        if words != "":
                weakWordsLength = len(words)  
                for i in range(len(sections)):
                    if sections[i] == 1:
                        sectionsCount[1] +=1
                    elif sections[i] == 2:
                        sectionsCount[2] +=1
                    elif sections[i] == 3:
                        sectionsCount[3] +=1
                    elif sections[i] == 4:
                        sectionsCount[4] +=1
                    elif sections[i] == 5:
                        sectionsCount[5] +=1
                    elif sections[i] == 6:
                        sectionsCount[6] +=1
                
                languageIn =self.obj_UILanguage.getUIL()
                # print(f"languageIn = {languageIn}")


            
                if languageIn == "De":

                    sectionDictDe = ("Schwache Wörter in der 1. Partition",self.obj_Graph.graph(sectionsCount[1],weakWordsLength),"%","first^",self.obj_Percentage.percentage(sectionsCount[1],weakWordsLength),"last^","$"),("Schwache Wörter in der 2. Partition",self.obj_Graph.graph(sectionsCount[2],weakWordsLength),"%","first^",self.obj_Percentage.percentage(sectionsCount[2],weakWordsLength),"last^","$"),("Schwache Wörter in der 3. Partition",self.obj_Graph.graph(sectionsCount[3],weakWordsLength),"%","first^",self.obj_Percentage.percentage(sectionsCount[3],weakWordsLength),"last^","$"),("Schwache Wörter in der 4. Partition",self.obj_Graph.graph(sectionsCount[4],weakWordsLength),"%","first^",self.obj_Percentage.percentage(sectionsCount[4],weakWordsLength),"last^","$"),("Schwache Wörter in der 5. Partition",self.obj_Graph.graph(sectionsCount[5],weakWordsLength),"%","first^",self.obj_Percentage.percentage(sectionsCount[5],weakWordsLength),"last^","$"),("Schwache Wörter in der 6. Partition",self.obj_Graph.graph(sectionsCount[6],weakWordsLength),"%","first^",self.obj_Percentage.percentage(sectionsCount[6],weakWordsLength),"last^","$")
                    sectionDict = sectionDictDe
                elif languageIn == "En":

                    sectionDictEn = ("Weak words in 1Th partition",self.obj_Graph.graph(sectionsCount[1],weakWordsLength),"%","first^",self.obj_Percentage.percentage(sectionsCount[1],weakWordsLength),"last^","$"),("Weak words in 2Th partition",self.obj_Graph.graph(sectionsCount[2],weakWordsLength),"%","first^",self.obj_Percentage.percentage(sectionsCount[2],weakWordsLength),"last^","$"),("Weak words in 3Th partition",self.obj_Graph.graph(sectionsCount[3],weakWordsLength),"%","first^",self.obj_Percentage.percentage(sectionsCount[3],weakWordsLength),"last^","$"),("Weak words in 4Th partition",self.obj_Graph.graph(sectionsCount[4],weakWordsLength),"%","first^",self.obj_Percentage.percentage(sectionsCount[4],weakWordsLength),"last^","$"),("Weak words in 5Th partition",self.obj_Graph.graph(sectionsCount[5],weakWordsLength),"%","first^",self.obj_Percentage.percentage(sectionsCount[5],weakWordsLength),"last^","$"),("Weak words in 6Th partition",self.obj_Graph.graph(sectionsCount[6],weakWordsLength),"%","first^",self.obj_Percentage.percentage(sectionsCount[6],weakWordsLength),"last^","$")
                    sectionDict = sectionDictEn
                elif languageIn == "Per":

                    sectionDictPer = ("واژه های ناتوان در بخش نخست",self.obj_Graph.graph(sectionsCount[1],weakWordsLength),"%","first^",self.obj_Percentage.percentage(sectionsCount[1],weakWordsLength),"last^","$"),("واژه های ناتوان در بخش دوم",self.obj_Graph.graph(sectionsCount[2],weakWordsLength),"%","first^",self.obj_Percentage.percentage(sectionsCount[2],weakWordsLength),"last^","$"),("واژه های ناتوان در بخش سوم",self.obj_Graph.graph(sectionsCount[3],weakWordsLength),"%","first^",self.obj_Percentage.percentage(sectionsCount[3],weakWordsLength),"last^","$"),("واژه های ناتوان در بخش چهارم",self.obj_Graph.graph(sectionsCount[4],weakWordsLength),"%","first^",self.obj_Percentage.percentage(sectionsCount[4],weakWordsLength),"last^","$"),("واژه های ناتوان در بخش پنجم",self.obj_Graph.graph(sectionsCount[5],weakWordsLength),"%","first^",self.obj_Percentage.percentage(sectionsCount[5],weakWordsLength),"last^","$"),("واژه های ناتوان در بخش ششم",self.obj_Graph.graph(sectionsCount[6],weakWordsLength),"%","first^",self.obj_Percentage.percentage(sectionsCount[6],weakWordsLength),"last^","$")
                    sectionDict = sectionDictPer
                else :
                    sectionDict = sectionDictPer

                outputSorted = sorted(sectionDict, key = lambda x: float(x[4]), reverse = True)
                sectionDictR = str(outputSorted)
                sectionDictR = sectionDictR.replace("(","")
                sectionDictR = sectionDictR.replace(")","")
                sectionDictR = sectionDictR.replace(")","")
                sectionDictR = sectionDictR.replace("first^","<b>")
                sectionDictR = sectionDictR.replace("last^","</b>")
                sectionDictR = sectionDictR.replace("[","")
                sectionDictR = sectionDictR.replace("]","")
                sectionDictR = sectionDictR.replace("'","")
                sectionDictR = sectionDictR.replace(",","")
                sectionDictR = sectionDictR.replace("$","\n")
                # print(sectionDictR)
                return sectionDictR
        else:
                return "----"
 
    # گزارش واژگان در بخش ها📈
    def reportWordsSectionsPercentage(self):
        dash = "___________________________________" 
        array = self.wordsSectionPosition()
        allWordsLength = len(self.obj_Vazhegan.getAllWordsSection())
        output = [("شمار واژه ها در بخش نخست :",f"<b>{int(array[0])}</b>","$",f"<b>{self.obj_Percentage.percentage(int(array[0]),allWordsLength)}</b>","%",self.obj_Graph.graph(int(array[0]),allWordsLength),"$$")
        ,("شمار واژه ها در بخش دوم :",f"<b>{int(array[1])}</b>","$",f"<b>{self.obj_Percentage.percentage(array[1],allWordsLength)}</b>","%",self.obj_Graph.graph(array[1],allWordsLength),"$$"),("شمار واژه ها در بخش سوم :",f"<b>{array[2]}</b>","$",f"<b>{self.obj_Percentage.percentage(array[2],allWordsLength)}</b>","%",self.obj_Graph.graph(array[2],allWordsLength),"$$"),("شمار واژه ها در بخش چهارم :",f"<b>{array[3]}</b>","$",f"<b>{self.obj_Percentage.percentage(array[3],allWordsLength)}</b>","%",self.obj_Graph.graph(array[3],allWordsLength),"$$"),("شمار واژه ها در بخش پنجم :",f"<b>{array[4]}</b>","$",f"<b>{self.obj_Percentage.percentage(array[4],allWordsLength)}</b>","%",self.obj_Graph.graph(array[4],allWordsLength),"$$"),("شمار واژه ها در بخش ششم :",f"<b>{array[5]}</b>","$",f"<b>{self.obj_Percentage.percentage(array[5],allWordsLength)}</b>","%",self.obj_Graph.graph(array[5],allWordsLength),"$$"),(dash,"$"),(" واژه های یادگیری شده به صورت کامل :",f"<b>{array[6]}</b>")]
        output = str(output)
        output = output.replace("[","")
        output = output.replace("]","")
        output = output.replace("(","")
        output = output.replace(")","")
        output = output.replace(",","")
        output = output.replace("'","")
        output = output.replace("$","\n")


        # print(f"output = {output}")
        return output

    # گزارش واژگان در بخش هابه انلگیسی📈
    def reportWordsSectionsPercentageEn(self):
        dash = "___________________________________" 
        array = self.wordsSectionPosition()
        allWordsLength = len(self.obj_Vazhegan.getAllWordsSection())
        output = [("Words number in 1Th partition :",f"<b>{int(array[0])}</b>","$",f"<b>{self.obj_Percentage.percentage(int(array[0]),allWordsLength)}</b>","%",self.obj_Graph.graph(int(array[0]),allWordsLength),"$$")
        ,("Words number in 2Th partition :",f"<b>{int(array[1])}</b>","$",f"<b>{self.obj_Percentage.percentage(array[1],allWordsLength)}</b>","%",self.obj_Graph.graph(array[1],allWordsLength),"$$"),("Words number in 3Th partition :",f"<b>{array[2]}</b>","$",f"<b>{self.obj_Percentage.percentage(array[2],allWordsLength)}</b>","%",self.obj_Graph.graph(array[2],allWordsLength),"$$"),("Words number in 4Th partition :",f"<b>{array[3]}</b>","$",f"<b>{self.obj_Percentage.percentage(array[3],allWordsLength)}</b>","%",self.obj_Graph.graph(array[3],allWordsLength),"$$"),("Words number in 5Th partition :",f"<b>{array[4]}</b>","$",f"<b>{self.obj_Percentage.percentage(array[4],allWordsLength)}</b>","%",self.obj_Graph.graph(array[4],allWordsLength),"$$"),("Words number in 6Th partition :",f"<b>{array[5]}</b>","$",f"<b>{self.obj_Percentage.percentage(array[5],allWordsLength)}</b>","%",self.obj_Graph.graph(array[5],allWordsLength),"$$"),(dash,"$"),("Number of fully learned vocabular :",f"<b>{array[6]}</b>")]
        output = str(output)
        output = output.replace("[","")
        output = output.replace("]","")
        output = output.replace("(","")
        output = output.replace(")","")
        output = output.replace(",","")
        output = output.replace("'","")
        output = output.replace("$","\n")


        # print(f"output = {output}")
        return output
    # گزارش واژگان در بخش هابه آلمانی
    def reportWordsSectionsPercentageDe(self):
        dash = "___________________________________" 
        array = self.wordsSectionPosition()
        allWordsLength = len(self.obj_Vazhegan.getAllWordsSection())
        output = [("Wortnummer in der 1. Partition :",f"<b>{int(array[0])}</b>","$",f"<b>{self.obj_Percentage.percentage(int(array[0]),allWordsLength)}</b>","%",self.obj_Graph.graph(int(array[0]),allWordsLength),"$$")
        ,("Wortnummer in der 2. Partition :",f"<b>{int(array[1])}</b>","$",f"<b>{self.obj_Percentage.percentage(array[1],allWordsLength)}</b>","%",self.obj_Graph.graph(array[1],allWordsLength),"$$"),("Wortnummer in der 3. Partition :",f"<b>{array[2]}</b>","$",f"<b>{self.obj_Percentage.percentage(array[2],allWordsLength)}</b>","%",self.obj_Graph.graph(array[2],allWordsLength),"$$"),("Wortnummer in der 4. Partition :",f"<b>{array[3]}</b>","$",f"<b>{self.obj_Percentage.percentage(array[3],allWordsLength)}</b>","%",self.obj_Graph.graph(array[3],allWordsLength),"$$"),("Wortnummer in der 5. Partition :",f"<b>{array[4]}</b>","$",f"<b>{self.obj_Percentage.percentage(array[4],allWordsLength)}</b>","%",self.obj_Graph.graph(array[4],allWordsLength),"$$"),("Wortnummer in der 6. Partition :",f"<b>{array[5]}</b>","$",f"<b>{self.obj_Percentage.percentage(array[5],allWordsLength)}</b>","%",self.obj_Graph.graph(array[5],allWordsLength),"$$"),(dash,"$"),("Anzahl der vollständig erlernten Vokabeln :",f"<b>{array[6]}</b>")]
        output = str(output)
        output = output.replace("[","")
        output = output.replace("]","")
        output = output.replace("(","")
        output = output.replace(")","")
        output = output.replace(",","")
        output = output.replace("'","")
        output = output.replace("$","\n")


        # print(f"output = {output}")
        return output

    def getAccoutDetails(self):
        # dash = "〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️" 
        #🔅🗓📎
        dash =""
        ##today khorshidi
        today = datetime.datetime.now()
        dateGri = today.date().strftime("%B %d, %Y")
        # monthAlpha,year,month,day,monthAlphaFinglish,weekDayPer,weekDayFinglish
        monthAlpha,year,_,day,_,weekDayKhorshidi,_ = self.obj_DateArrange.convertToKhorshidi(today)
        # weekDay = today.strftime("%A")
        # dictDay = {"Sunday":"یکشنبه","Monday":"دوشنبه","Tuesday":"سه شنبه","Wednesday":"چهارشنبه","Thursday":"پنج شنبه","Friday":"جمعه","Saturday":"شنبه"}
        # weekDayKhorshidi = dictDay[weekDay]
        # print(f"weekDay = {weekDay}")
        # print(f"weekDayKhorshidi = {weekDayKhorshidi}")
        outpuTodayDateNTime = f"🗓امروز: {weekDayKhorshidi}  {day} {monthAlpha} {year}  \n📎{dateGri}"
        ########
        ##way
        way = self.obj_RaveshYadgiri.getWay()
        if isinstance(way,list):
            arrayWay = []
            for item in way:
                if item != BtnS().persianTextEn:
                    arrayWay.append(item)
                elif item == BtnS().persianTextEn:
                    arrayWay.append(BtnS().persianText)
        else:
            if  way == BtnS().persianTextEn:
                arrayWay = BtnS().persianText   
        wayStr = str(arrayWay)
        # print(way)
        wayStr = wayStr.replace("[","")
        wayStr = wayStr.replace("]","")
        wayStr = wayStr.replace("'","")

        outputWay = f"🔅روش :‌<b> {wayStr}</b>"
        #####
        ##words number
        wordNumPerDay = self.obj_ShomarVazhgan.getWordNum()
        outputNum = f"🔅شمار واژگان روزانه :<b> {wordNumPerDay}</b>"
        ######
        ##next Training
        tomorrowNextTraining =self.obj_DateArrange.getTomorrowNextTraining(self.id)
        dateGriNextTraining = tomorrowNextTraining.date().strftime("%B %d, %Y")
        hourMin = tomorrowNextTraining.strftime("%H:%M")
        #گرفتن سال ، ماه نویسه ای ، روز
        # monthAlpha,year,month,day,monthAlphaFinglish,weekDayPer,weekDayFinglish
        # monthAlpha,year,month,day,monthAlphaFinglish,weekDay,weekDayFinglish
        monthAlphaNextTrain,yearNextTrain,_,dayNextTrain,weekDayNextTrainKhorshidi,_,_ = self.obj_DateArrange.convertToKhorshidi(tomorrowNextTraining)
        # گرفتن نام روز در هفته به پارسی
        # weekDayNextTrain = tomorrowNextTraining.strftime("%A")
        # weekDayNextTrainKhorshidi = dictDay[weekDayNextTrain]
        # outputNextTraining = f"<b> {weekDayNextTrainKhorshidi} {dayNextTrain} {monthAlphaNextTrain} {yearNextTrain} </b>, در ساعت و زمان  <b>{hourMin} </b> "
        # outputNextTraining = f"👈یادگیری واژگان روزانه👉 بعدی و پسین‌ در تاریخ <b> {weekDayNextTrainKhorshidi} {dayNextTrain} {monthAlphaNextTrain} {yearNextTrain} </b>, در ساعت و زمان  <b>{hourMin} </b> به وقت ایران می باشد.\n  مصادف با :\n <b> {dateGriNextTraining} </b>"
        outputNextTraining = f"🔅نوبت بعدی یادگیری واژگان :‌ <b> {weekDayNextTrainKhorshidi} {dayNextTrain} {monthAlphaNextTrain} {yearNextTrain} </b>, در ساعت و زمان  <b>{hourMin} </b> به وقت ایران\n📎مصادف با : <b> {dateGriNextTraining} </b>"
        ###language of keyboard and message
        languageIn = self.obj_UILanguage.getUIL()
        dictDay = {"De":"🇩🇪","En":"🇬🇧","Per":"🇮🇷"}
        lan = dictDay[languageIn]
        language = f"🔅زبان 💬⌨️ : {lan}"
        ######
        output = f"{outputWay}\n{dash}\n{outputNum}\n{dash}\n{outputNextTraining}\n{dash}\n{language}"
        return outpuTodayDateNTime,output


    def getAccoutDetailsDe(self):
        # dash = "〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️" 
        dash =""
        ##today khorshidi
        today = datetime.datetime.now()
        dateGri = today.date().strftime("%B %d, %Y")
        # monthAlpha,year,month,day,monthAlphaFinglish,weekDayPer,weekDayFinglish
        _,year,_,day,monthAlphaFinglish,_,_ = self.obj_DateArrange.convertToKhorshidi(today)
        weekDay = today.strftime("%A")
        # dictMonth = {"فروردین":"Farvardin","اردیبهشت":"Ordibehesht","خرداد":"Khordad","تیر":"Tir","مرداد":"Mordad","شهریور":"Shahrivar","مهر":"Mehr","آبان":"Aban","آذر":"Azar","دی":"Dey","بهمن":"Bahman","اسفند":"Esfand"}
        # dictMonth = {1:"Farvardin",2:"Ordibehesht",3:"Khordad",4:"Tir",5:"Mordad",6:"Shahrivar",7:"Mehr",8:"Aban",9:"Azar",10:"Dey",11:"Bahman",12:"Esfand"}
        dictDay = {"Sunday":"Sontag","Monday":"Montag","Tuesday":"Dienstag","Wednesday":"Mittwoch","Thursday":"Donnerstag","Friday":"Freitag","Saturday":"Samstag"}
        weekDayDe = dictDay[weekDay]
        # weekDayKhorshidi = dictDay[weekDay]
        # monthAlphaEn = dictMonth[month]
        # print(f"weekDay = {weekDayDe}")
        # print(f"weekDayKhorshidi = {weekDayKhorshidi}")
        outpuTodayDateNTime = f"🗓Heute: {weekDayDe}  {day} {monthAlphaFinglish} {year}  \n📎{dateGri}"
        ########
        ##way
        way = self.obj_RaveshYadgiri.getWay()
        if isinstance(way,list):
            arrayWay = []
            for item in way:
                if item != BtnS().persianTextEn:
                    arrayWay.append(item)
                elif item == BtnS().persianTextEn:
                    arrayWay.append(BtnS().persianText)
        else:
            if  way == BtnS().persianTextEn:
                arrayWay = BtnS().persianText   
        wayStr = str(arrayWay)
        # print(way)
        wayStr = wayStr.replace("[","")
        wayStr = wayStr.replace("]","")
        wayStr = wayStr.replace("'","")

        outputWay = f"🔅Methode :‌<b> {wayStr}</b>"
        #####
        ##words number
        wordNumPerDay = self.obj_ShomarVazhgan.getWordNum()
        outputNum = f"🔅Tägliche Anzahl von Wörtern :<b> {wordNumPerDay}</b>"
        ######
        ##next Training
        tomorrowNextTraining =self.obj_DateArrange.getTomorrowNextTraining(self.id)
        dateGriNextTraining = tomorrowNextTraining.date().strftime("%B %d, %Y")
        hourMin = tomorrowNextTraining.strftime("%H:%M")
        #گرفتن سال ، ماه نویسه ای ، روز
        # monthAlpha,year,month,day,monthAlphaFinglish,weekDay,weekDayFinglish
        _,yearNextTrain,_,_,monthAlphaNextTrainEn,_,dayNextTrain = self.obj_DateArrange.convertToKhorshidi(tomorrowNextTraining)
        # monthAlphaNextTrainEn = dictMonth[monthAlphaNextTrain]
        # گرفتن نام روز در هفته به پارسی
        weekDayNextTrain = tomorrowNextTraining.strftime("%A")
        weekDayNextTrainDe = dictDay[weekDayNextTrain]
        # next time training
        outputNextTraining = f"🔅 Die 👉Lern den Wortschatz täglich👈 Weiter am :‌ <b> {weekDayNextTrainDe} {dayNextTrain} {monthAlphaNextTrainEn} {yearNextTrain} </b>, um  <b>{hourMin} </b> In der Zeit des Iran \n📎Fällt zusammen mit : <b> {dateGriNextTraining} </b>"
        #language of keyboard and message
        languageIn = self.obj_UILanguage.getUIL()
        dictDay = {"De":"🇩🇪","En":"🇬🇧","Per":"🇮🇷"}
        lan = dictDay[languageIn]
        language = f"🔅💬⌨Sprache : {lan}"
        ######
        output = f"{outputWay}\n{dash}\n{outputNum}\n{dash}\n{outputNextTraining}\n{dash}\n{language}"
        return outpuTodayDateNTime,output


    def getAccoutDetailsEn(self):
        # dash = "〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️" 
        #🔅🗓📎
        dash =""
        ##today khorshidi
        today = datetime.datetime.now()
        dateGri = today.date().strftime("%B %d, %Y")
        # monthAlpha,year,month,day,monthAlphaFinglish,weekDayPer,weekDayFinglish
        _,year,_,day,monthAlphaFinglish,_,_ = self.obj_DateArrange.convertToKhorshidi(today)
        weekDay = today.strftime("%A")
        # dictMonth = {"فروردین":"Farvardin","اردیبهشت":"Ordibehesht","خرداد":"Khordad","تیر":"Tir","مرداد":"Mordad","شهریور":"Shahrivar","مهر":"Mehr","آبان":"Aban","آذر":"Azar","دی":"Dey","بهمن":"Bahman","اسفند":"Esfand"}
        # dictMonth = {1:"Farvardin",2:"Ordibehesht",3:"Khordad",4:"Tir",5:"Mordad",6:"Shahrivar",7:"Mehr",8:"Aban",9:"Azar",10:"Dey",11:"Bahman",12:"Esfand"}
        # weekDayKhorshidi = dictDay[weekDay]
        # monthAlphaEn = dictMonth[monthAlpha]
        # print(f"weekDay = {weekDay}")
        # print(f"weekDayKhorshidi = {weekDayKhorshidi}")
        outpuTodayDateNTime = f"🗓Today: {weekDay}  {day} {monthAlphaFinglish} {year}  \n📎{dateGri}"
        ########
        ##way
        way = self.obj_RaveshYadgiri.getWay()
        if isinstance(way,list):
            arrayWay = []
            for item in way:
                if item != BtnS().persianTextEn:
                    arrayWay.append(item)
                elif item == BtnS().persianTextEn:
                    arrayWay.append(BtnS().persianText)
        else:
            if  way == BtnS().persianTextEn:
                arrayWay = BtnS().persianText   
        wayStr = str(arrayWay)
        # print(way)
        wayStr = wayStr.replace("[","")
        wayStr = wayStr.replace("]","")
        wayStr = wayStr.replace("'","")

        outputWay = f"🔅Method :‌<b> {wayStr}</b>"
        #####
        ##words number
        wordNumPerDay = self.obj_ShomarVazhgan.getWordNum()
        outputNum = f"🔅Daily Number of Words :<b> {wordNumPerDay}</b>"
        ######
        ##next Training
        tomorrowNextTraining =self.obj_DateArrange.getTomorrowNextTraining(self.id)
        dateGriNextTraining = tomorrowNextTraining.date().strftime("%B %d, %Y")
        hourMin = tomorrowNextTraining.strftime("%H:%M")
        #گرفتن سال ، ماه نویسه ای ، روز
        # monthAlpha,year,month,day,monthAlphaFinglish,weekDayPer,weekDayFinglish
        _,yearNextTrain,_,dayNextTrain,monthAlphaFinglishNxt,_,_ = self.obj_DateArrange.convertToKhorshidi(tomorrowNextTraining)
        # monthAlphaNextTrainEn = dictMonth[monthAlphaNextTrain]
        # گرفتن نام روز در هفته به پارسی
        weekDayNextTrain = tomorrowNextTraining.strftime("%A")
        outputNextTraining = f"🔅The 👉Learn Vocabulary Daily👈 next on :‌ <b> {weekDayNextTrain} {dayNextTrain} {monthAlphaFinglishNxt} {yearNextTrain} </b>, at  <b>{hourMin} </b> In the time of Iran \n📎Coincides with : <b> {dateGriNextTraining} </b>"
        #language of keyboard and message
        languageIn = self.obj_UILanguage.getUIL()
        dictDay = {"De":"🇩🇪","En":"🇬🇧","Per":"🇮🇷"}
        lan = dictDay[languageIn]
        language = f"🔅💬⌨Language : {lan}"
        ######
        output = f"{outputWay}\n{dash}\n{outputNum}\n{dash}\n{outputNextTraining}\n\n{language}"
        return outpuTodayDateNTime,output





class CountingDateNTime:
    def __init__(self,id):
        pass    

class Percentage:
    def __init__(self):
        pass
    def percentage(self,denominator,numerator):
        try:
            answer =denominator*100/numerator
        except:
            answer = 0
        answerRound = round(answer,1)
        # print(f"answerRound = {answerRound}")
        return answerRound

class Graph:
    def __init__(self):
        pass
    def graph(self,denominator,numerator):
        # print(f"\ndenominator = {denominator}\nnumerator = {numerator}")
        equalSign = ""
        try:
            all =  round(denominator*13/numerator,None) 
        except:
            all = 0
        for _ in range(all):
            equalSign+= "="
        # print(equalSign)
        return equalSign



class DateArrange:
    def __init__(self,id=None,firstName=None):
        self.id = id
        # self.hourTime = hourTime
        self.obj_Db = Db()
        self.firstName = firstName
        # self.duraion = {"days":0,"seconds":0,"microseconds":0,"milliseconds":0,"minutes":0,"hours":24,"weeks":0}
        self.duraionToSave = {"days":0,"seconds":5,"microseconds":0,"milliseconds":0,"minutes":0,"hours":0,"weeks":0}
        self.obj_UILanguage = UILanguage(id)

    #TODO must merge with convertToKhorshidi(self,val)
    def getWeekDay(self,date):
        dayEn = date.strftime("%A")
        dayDeDict = {"Sunday":"Sonntag","Monday":"Montag","Tuesday":"Dienstag","Wednesday":"Mittwoch","Thursday":"Donnerstag","Friday":"Freitag","Saturday":"Samstag"}
        dayPerDict = {"Sunday":"یکشنبه","Monday":"دوشنبه","Tuesday":"سه شنبه","Wednesday":"چهارشنبه","Thursday":"پنج شنبه","Friday":"جمعه","Saturday":"شنبه"}
        dayDe = dayDeDict[dayEn]
        dayPer = dayPerDict[dayEn]
        language = self.obj_UILanguage.getUIL()
        if language == "De":
                output = dayDe
        elif language == "En":
                output = dayEn
        elif language == "Per":
                output = dayPer
        return output

    #TODO must merge with convertToKhorshidi(self,val)
    def getMonthKhorshidi(self,number):
        dictPerMonth = {1:"فروردین",2:"اردیبهشت",3:"خرداد",4:"تیر",5:"مرداد",6:"شهریور",7:"مهر",8:"آبان",9:"آذر",10:"دی",11:"بهمن",12:"اسفند"}
        dictFinglishMonth = {1:"Farvardin",2:"Ordibehesht",3:"Khordad",4:"Tir",5:"Mordad",6:"Shahrivar",7:"Mehr",8:"Aban",9:"Azar",10:"Dey",11:"Bahman",12:"Esfand"}
        # print(self.id)
        language = self.obj_UILanguage.getUIL()
        monthPer = dictPerMonth[number]
        # print(number,language)
        monthFinglish = dictFinglishMonth[number]
        if language == "De" or language == "En" :
                output = monthFinglish
        elif language == "Per" or language == "":
                output = monthPer
        return output


# حساب کردن و دادن زمان محاسبه شده تمرین بعد
    def askedNextTraining(self,val):
        nextTrainingDate = self.getTomorrowNextTraining(self.id)
        hourO = int(nextTrainingDate.strftime("%H"))
        if val<hourO:
            #اضافه کردن یک روز به  اضافه ساعت وارد شده به تمرین روز فردا به دلیل کوچک تر بودن زمان وارد شده
            output = nextTrainingDate.replace(hour=val) + relativedelta(days=1)
            # print(f"output = {output}")
            return output
        elif  hourO<val:
            #عدم نیاز به اضافه کردن یک روز زیرا ساعت وارد شده از ساعت روز بعد بیشتر است پس اضافه کردن یک روز منتفی است
            output = nextTrainingDate.replace(hour=val)
            # print(f"output = {output}")
            return output
        else:
            pass    


#ذخیره و قراردادن مقد ار در پایگاه داده درصورت کمتر یا بیشتر از ۲۴ ساعت بودن از زمان تغییر
    def checkIsValue24(self,val):
        nextTrainingDate = self.getTomorrowNextTraining(self.id)
        hourO = int(nextTrainingDate.strftime("%H"))
        # print(f"val = {val}\n hourO ={hourO}")
        # print(f"dayO = {dayO}\n hourO ={hourO}")
        if val<hourO:
            #اضافه کردن یک روز به  اضافه ساعت وارد شده به تمرین روز فردا به دلیل کوچک تر بودن زمان وارد شده
            # output = nextTrainingDate
            output = nextTrainingDate.replace(hour=val) + relativedelta(days=1)
            # print(f"output = {output}")
            # print("it must be atleast 24 hours distance between excercises")
            self.obj_Db.userCollection.update_many({"userId":self.id},{"$set":{"nextTrainingDate":output}})
           
        elif  hourO<val:
            #عدم نیاز به اضافه کردن یک روز زیرا ساعت وارد شده از ساعت روز بعد بیشتر است پس اضافه کردن یک روز منتفی است
            output = nextTrainingDate.replace(hour=val)
            # print(f"output less than hours = {output}")
            self.obj_Db.userCollection.update_many({"userId":self.id},{"$set":{"nextTrainingDate":output}})
           
        else:
            pass

    # نگاشتن هنگامه تمرین و یادگیری
    def saveTomorrowNextTraining(self,id):
        now = datetime.datetime.now()        
        result = now + relativedelta(days=1,minutes=5)
        # print(f"result = {result}")
        # result = now + timedelta(minutes=5)
        result = result.replace(minute=0,second=0,microsecond=0)
        self.obj_Db.userCollection.update_many({"userId":id},{"$set":{"nextTrainingDate":result}})


    #گرفتن هنگامه یادگیری و تمرین
    def getTomorrowNextTraining(self,id):
        tomorrowNextTraining = ""
        for col in self.obj_Db.userCollection.find({"userId":id},{"nextTrainingDate":1,"_id":0}):
            for keys in col.keys():
                tomorrowNextTraining = col[keys]
        # print(f"tomorrowNextTraining = {tomorrowNextTraining}")
        return tomorrowNextTraining
    # قابل خواندن کردن تاریخ و زمان
    def makeDateTimeReadable(self,val):
        # array = str(self.getTomorrowNextTraining(self.id)).split("-")
        array = str(val).split("-")
        # print(f"array = {array}")
        month = array[1]
        dic = {"1":"Jan","2":"Feb","3":"Mar","4":"Apr","5":"May","6":"Jun","7":"Jul", "8":"Aug","9":"Sep","10":"Oct","11":"Nov","12":"Dec","01":"Jan","02":"Feb","03":"Mar","04":"Apr","05":"May","06":"Jun","07":"Jul", "08":"Aug","09":"Sep"}
        alMonth = dic[month]
        array[1] = alMonth
        convertArrayToString =",".join(array)
        convertArrayToString =  convertArrayToString.replace(",","-")
        # print(f"convertArrayToString = {convertArrayToString}")
        #mac
        # myDateTime = datetime.datetime.strptime(convertArrayToString,"%Y-%b-%d %H:%M:%S.%f")
        #win
        try : 
            myDateTime = datetime.datetime.strptime(convertArrayToString,"%Y-%b-%d %H:%M:%S.%f")

            # myDateTime = datetime.datetime.strptime(convertArrayToString,"%Y-%b-%d %H:%M:%S")

        except:
            # myDateTime = datetime.datetime.strptime(convertArrayToString,"%Y-%b-%d %H:%M:%S.%f")
            myDateTime = datetime.datetime.strptime(convertArrayToString,"%Y-%b-%d %H:%M:%S")
        # print(f"myDateTime = {myDateTime}")
        return myDateTime
    
    # def getWeekDay(self,val):
    #     dateTimeInput = self.makeDateTimeReadable(val)

    #     myDate =datetime.date(dateTimeInput.year,dateTimeInput.month,dateTimeInput.day)
    #     print(f"myDate = {myDate}")
    #     # w = calendar.day_name[a.weekday()]
    #     wD = calendar.day_name[myDate.weekday()]
    #     print(f"inside getWeekDay(self) = {wD}")
    #     return wD

    # def convertPersianWeekDay(self,val):
    #     dictDay = {"Sunday":"یکشنبه","Monday":"دوشنبه","Tuesday":"سه شنبه","Wednesday":"چهارشنبه","Thursday":"پنج شنبه","Friday":"جمعه","Saturday":"شنبه"}
    #     input = self.getWeekDay(val)
    #     print(f"input = {input}")
    #     persianWd = dictDay[input]
    #     print(f"persianWd = {persianWd}")
    #     return persianWd
    


   # save temporary NextTrainingsHour in termporary field
    def saveTemporaryNextTrainingsHour(self,hourTime):
        # time = {"dailyTime":hourTime}
        # self.obj_Db.userCollection.updsate_many({"userId":self.id},{"$set":{"temporary":time}})
        try:
            self.obj_Db.userCollection.update_many({"userId":self.id},{"$set":{"temporary.dailyTime":hourTime}})
        except:
            tempContent = {"dailyTime":hourTime,"rightWrongLampFlag":True,"automateMsgFlag":False}
            self.obj_Db.userCollection.update_many({"userId":self.id},{"$set":{"temporary":tempContent}})


    def standizedUsersTemp(self):
        ids = []
        for col in self.obj_Db.userCollection.find({"termporary":{"$eq":"null"}},{"userId":1,"_id":0}):
            for keys in col.keys():
                ids.append(col[keys])
        tempContent = {"rightWrongLampFlag":True,"automateMsgFlag":False}
        for i in ids:
            self.obj_Db.userCollection.update_many({"userId":i},{"$set":{"termporary":tempContent}})




# برای استفاده 💡 , ❌ , ✅ فقط در زمان تپ کردن بر <<👈👈یادگیری واژگان روزانه👉👉>> ه  
    def saveTrueRightWrongLampFlag(self,id):
        try:
           self.obj_Db.userCollection.update_many({"userId":id},{"$set":{"temporary.rightWrongLampFlag":True}})
        except:
           tempContent = {"rightWrongLampFlag":True,"automateMsgFlag":False}
           self.obj_Db.userCollection.update_many({"userId":id},{"$set":{"termporary":tempContent}}) 

    def saveFalseRightWrongLampFlag(self,id):
        try:
              self.obj_Db.userCollection.update_many({"userId":id},{"$set":{"temporary.rightWrongLampFlag":False}})
        except:
              tempContent = {"rightWrongLampFlag":True,"automateMsgFlag":False}
              self.obj_Db.userCollection.update_many({"userId":id},{"$set":{"termporary":tempContent}})  



    def getRightWrongLampFlag(self,id):
        for col in self.obj_Db.userCollection.find({"userId":id},{"temporary.rightWrongLampFlag":1,"_id":0}):
            # print(f"col = {col}")
            for _,y in col.items():
                for _,b in y.items():
                    return b
# برای استفاده <<👈👈یادگیری واژگان روزانه👉👉>> فقط در زمان تپ کردن بر <<👈👈یادگیری واژگان روزانه👉👉>> ه  
    def saveTrueAutomateMsgFlag(self,id):
        # print(f"id = {id}")
        id = int(id)
        try:
           self.obj_Db.userCollection.update_many({"userId":id},{"$set":{"temporary.automateMsgFlag":True}})
        except:
           tempContent = {"rightWrongLampFlag":True,"automateMsgFlag":True}
           self.obj_Db.userCollection.update_many({"userId":id},{"$set":{"termporary":tempContent}})  

    def saveFalseAutomateMsgFlag(self,id):
        try:
           self.obj_Db.userCollection.update_many({"userId":id},{"$set":{"temporary.automateMsgFlag":False}})
        except:
           tempContent = {"rightWrongLampFlag":True,"automateMsgFlag":False}
           self.obj_Db.userCollection.update_many({"userId":id},{"$set":{"termporary":tempContent}}) 



    def getAutomateMsgFlag(self,id):
        id = int(id)
        for col in self.obj_Db.userCollection.find({"userId":id},{"temporary.automateMsgFlag":1,"_id":0}):
            # print(f"col = {col}")
            for _,y in col.items():
                for _,b in y.items():
                    return b



  
    def getFirstName(self,id):
        firstName=""
        # print(f"id = {id}")
        id = int(id)
        for col in self.obj_Db.userCollection.find({"userId":id},{"firstName":1,"_id":0}) :
            for keys in col.keys() :
                firstName = col[keys]
        return firstName


   # get temporary NextTrainingsHour in termporary field
    def getTemporaryNextTrainingsHour(self):
        temp = ""
        for col in self.obj_Db.userCollection.find({"userId":self.id},{"temporary":1,"_id":0}):
            for keys in col.keys():
                temp = col[keys]
        dailyTime = int(temp["dailyTime"])
        # print(f"dailyTime = {dailyTime}")
        return dailyTime

    def saveNextTrainingsHourbyTemp(self,temp):
        # now = datetime.datetime.now()
        tomorrowNextTrainingImport = self.getTomorrowNextTraining(self.id)
        # tomorrowNextTraining = tomorrowNextTrainingImport + datetime.timedelta(hours=temp)
        tomorrowNextTraining = tomorrowNextTrainingImport.replace(hour=int(temp))

        # print(f"tomorrowNextTraining = {tomorrowNextTraining}")
        self.obj_Db.userCollection.update_many({"userId":self.id},{"$set":{"nextTrainingDate":tomorrowNextTraining}})



    
    #تبدیل تاریخ گریگوریان به خورشیدی با خروجی روز و ماه و سال و 
    def convertToKhorshidi(self,val):
        try:
            dateTimeInput = self.makeDateTimeReadable(val)
        except:
            dateTimeInput =val
        # print(f"dateTimeInput = {dateTimeInput}")
        convertToKhorshidi =str(convertdate.persian.from_gregorian(dateTimeInput.year,dateTimeInput.month,dateTimeInput.day))
        # print(f"convertToKhorshidi = {convertToKhorshidi}")
        convertToKhorshidi = convertToKhorshidi.replace("(","")
        convertToKhorshidi = convertToKhorshidi.replace(")","")
        try:
            year,month,day = map(int,convertToKhorshidi.split(","))
        except:
            year,month,day = map(int,convertToKhorshidi.split("-"))
        dictMonthFing = {1:"Farvardin",2:"Ordibehesht",3:"Khordad",4:"Tir",5:"Mordad",6:"Shahrivar",7:"Mehr",8:"Aban",9:"Azar",10:"Dey",11:"Bahman",12:"Esfand"}   
        monthAlphaFinglish = dictMonthFing[month]
        dictMonth = {1:"فروردین",2:"اردیبهشت",3:"خرداد",4:"تیر",5:"مرداد",6:"شهریور",7:"مهر",8:"آبان",9:"آذر",10:"دی",11:"بهمن",12:"اسفند"}  
        #FIXME پاکش کن کل تابع اگر کارای نداره getMonthKhorshidi(month)
        # monthAlpha = self.getMonthKhorshidi(month)
        monthAlpha = dictMonth[month]
        weeDayKhorshidiDict = {"Sun":"یکشنبه","Mon":"دوشنبه","Tue":"سه شنبه","Wed":"چهارشنبه","Thu":"پنج شنبه","Fri":"جمعه","Sat":"یکشنبه"}

        # weeDayKhorshidiDict = {0:"دوشنبه",1:"سه شنبه",2:"چهارشنبه",3:"پنج شنبه",4:"جمعه",5:"شنبه",6:"یکشنبه"}
        dayNum = val.strftime("%a")
        weekDay = weeDayKhorshidiDict[dayNum]
        dictWeekDayFing = {"Sun":"Yekshanbeh","Mon":"Doshanbeh","Tue":"Seshanbeh","Wed":"Chaharshanbeh","Thu":"Panjshanbeh","Fri":"Jomeh","Sat":"Shanbeh"}   
        weekDayFinglish = dictWeekDayFing[dayNum]
        # print(f"inside function ...year = {year} , month = {month} monthAlpha = {monthAlpha}, day = {day}")
        # must be add monthAlphaFinglish,weekDay,weekDayFinglish
        return monthAlpha,year,month,day,monthAlphaFinglish,weekDay,weekDayFinglish

  

    # گرفتن تاریخ ورود واژه به قسمت 
    def giveDateTimeLastSectionEnterTo(self):
        dateTime = ""
        for col in Db().sectionCollection.find({"userId":self.id},{"dateTimeEnterToSection":1,"_id":0}):
            for keys in col.keys():
                dateTime = col[keys]
        # print(f"dateTime = {dateTime}")
        return dateTime

    def addOneDay(self):
        result = self.giveDateTimeLastSectionEnterTo() + timedelta(1)
        # print(f"result = {result}")
        return result

    def firstDateTillNow(self):
        now = datetime.datetime.now()
        # print(f"now = {now}")
        userStartDay = ""
        for col in self.obj_Db.userCollection.find({"userId":self.id},{"userStartDay":1,"_id":0}):
            for keys in col.keys():
                userStartDay = col[keys]
        # print(f"userStartDay = {userStartDay}")
  
        if userStartDay == "":
            return False
        else:
            distanceStr =  str(now -userStartDay)
            distanceArray = distanceStr.split(" ")
            # disArray = list(distanceStr)
            # print(f"distanceArray : {distanceArray}")
            try:
                distance =int(distanceArray[0])
                # print(f"distance = {distance}")
                return distance
            except :
                distance = False
                return distance

    def getTomorrowNextTrainingAll(self,subtractionIds):
        dateNId = []
        dateNIdWithField = []
        for col in self.obj_Db.userCollection.find({},{"nextTrainingDate":1,"userId":1,"_id":0}):
            for keys in col.keys():
                dateNId.append(col[keys])
                # print(f"col[keys] = {col[keys]}")
            # print(f"col = {col}")
            dateNIdWithField.append(col)
        # print(f"dateNId = {dateNId}")
        # print(f"dateNIdWithField = {dateNIdWithField}")
        notReapeated = [x for x in dateNIdWithField if x not in subtractionIds]
        # print(f"subtractionIds = {subtractionIds}")
        # print(f"notReapeated = {notReapeated}") 
        return notReapeated
    
    # add nextTrain Time in middle  nextTrainTimeNId = self.getTomorrowNextTrainingAll() if it doesn't work
    def idsTrainTime(self,dateNIdWithField):
        # nextTrainTimeNId = self.getTomorrowNextTrainingAll()
        # nxtTrain = self.getTomorrowNextTrainingAll()
        now = datetime.datetime.now()
        #it should be change after test to day = 1
        #فاصله بررسی و ارسال ایدی ها
       
        # limitOneDay = datetime.timedelta(days=0, seconds=5, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0)
        limitOneDay = datetime.timedelta(days=self.duraionToSave["days"], seconds=self.duraionToSave["seconds"], microseconds=self.duraionToSave["microseconds"], milliseconds=self.duraionToSave["milliseconds"], minutes=self.duraionToSave["minutes"], hours=self.duraionToSave["hours"], weeks=self.duraionToSave["weeks"])
        ids = []
        for x in dateNIdWithField:
            # print(f"id = {x['userId']},now = {now},nextTrainingDate =  {x['nextTrainingDate']}") 
            if x["nextTrainingDate"] !="":
                print(x["nextTrainingDate"])
                if   now < x["nextTrainingDate"]:
                    distance = x["nextTrainingDate"] - now
                    if  distance <= limitOneDay  :
                        # print(f"TIME train of {x['userId']} , nextTraining = {x['nextTrainingDate']}, now = {now}")
                        # print(f"id = {x['userId']},nextTrainingDate =  {x['nextTrainingDate']}")
                        # print(f"now     = {now}") 
                        ids.append(x["userId"])
                    # print(f"ids = {ids}")
                    
                else:
                    pass
                    # print(f"now is not time of next train of {x['userId']} , nextTraining = {x['nextTrainingDate']}, now = {now}")
            else:
                pass
                # print(f"this {x['userId']} is middle of registeration and first train")
            
        return ids


    def saveIdsNDateTimes(self,ids):

        # ids = str(ids)
        # print(f"ids array = {ids}")
        for i in range(0, len(ids)): 
            ids[i] = str(ids[i]) 
        # ids = tuple(i for i in ids)
        ids = tuple(ids)
        # print(f"ids tuple = {ids}")
        idsDict = {t:"not yet" for t in ids}
        # print(f"idsDict = {idsDict}")
        inputInfo = {"enterDatatime":datetime.datetime.now(),"idsDict":idsDict}
        self.obj_Db.settingCollection.insert_one(inputInfo)

    def getIdsDictN_id(self):
        now = datetime.datetime.now()
        # print(f"now = {now}" )
        # duration = datetime.timedelta(days=self.duraion["days"], seconds=self.duraion["seconds"], microseconds=self.duraion["microseconds"], milliseconds=self.duraion["milliseconds"], minutes=self.duraion["minutes"], hours=self.duraion["hours"], weeks=self.duraion["weeks"])

        timePast = now - relativedelta(days=1)
        # timePast = now - datetime.timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=5, hours=0, weeks=0)
        # print(f"timePast = {timePast}")
        #test update don't use it after enter real data  IT IS DANGEROUS 
        # self.obj_Db.settingCollection.update_many({},{"$set":{"enterDatatime":now}})
        condition = {"enterDatatime":{"$lte":now,"$gte":timePast}}
        idsDictN_id=[]
        for col in self.obj_Db.settingCollection.find(condition,{"idsDict":1,"_id":1}):

                 idsDictN_id.append(col)
        # ids and object together
        # print(f"idsDictN_id = {idsDictN_id}")     
        return idsDictN_id 

    def getIdN_idSeparatly(self,myDict):
        # print(f"myDict = {myDict}")
        ids = []
        objectId = ""
        # print(f"myDict = {myDict}")
        for col in myDict:
                # print(f"col['_id'] = {col['_id']}")
                objectId = col['_id']
                # print(f"col['idsDict'] = {col['idsDict']}")
                middleDict = col['idsDict']
                for field,key in middleDict.items():
                    if key == "not yet":
                        ids.append(field)

        # print(f"ids = {ids}") 
        return ids,objectId        
    
    
  
    #after sending message to user update next training and value of user which is "sent"    
    def updateSentIdsNNextTrainDate(self,object,id):
        #we are going to get idsDict first
        myDict = ""
        for col in self.obj_Db.settingCollection.find({"_id":object},{"_id":0,"idsDict":1}):
            for keys in col.keys():
                myDict = col[keys]
        # print(f"myDict before change = {myDict}")
        #then change id value to sent
        for field,_ in myDict.items():
            if field == id:
                myDict[field] = "sent"
        #to ignore warning
        # print(value)
        # print(f"myDict after change = {myDict}")
        #then update idsDict by changed changed ids values (myDict)
        self.obj_Db.settingCollection.update_many({"_id":object},{"$set":{"idsDict":myDict}})
        id = int(id)
        self.saveTomorrowNextTraining(id)
        self.getTomorrowNextTraining(id)

    #گرفتن ایدی های ستینگ کمتر از یک روز از ورودشان به پایگاه داده گذشته باشد باشند و ارسال هم شده باشند  الف 
    def getIdsSent(self):
        now = datetime.datetime.now()
        myDict = []
        subtractionIds=[]
        repeatedIds = []
        # duration = datetime.timedelta(days=self.duraion["days"], seconds=self.duraion["seconds"], microseconds=self.duraion["microseconds"], milliseconds=self.duraion["milliseconds"], minutes=self.duraion["minutes"], hours=self.duraion["hours"], weeks=self.duraion["weeks"])

        # oneDay = datetime.timedelta(minutes=5)
        limit = now - relativedelta(days=1)
        condition = {"enterDatatime":{"$lte":now,"$gte":limit}}
        for col in self.obj_Db.settingCollection.find(condition,{"_id":0,"idsDict":1}) :
            for keys in col.keys():
                myDict = col[keys]
                # print(f"myDict = {myDict}")
                
                for key,value in myDict.items():
                # for field,value in myDict.items():
                    if value == "sent":

                            repeatedIds.append(int(key))

        for i in repeatedIds:
            if i not in subtractionIds:
                subtractionIds.append(i)
        # print(f"repeatedIds = {repeatedIds}")
        # print(f"subtractionIds = {subtractionIds}")
        return subtractionIds


    def testSaveTomorrowNextTraining(self):
        now = datetime.datetime.now()
        # plusTime = datetime.timedelta(days=self.duraion["days"], seconds=self.duraion["seconds"], microseconds=self.duraion["microseconds"], milliseconds=self.duraion["milliseconds"], minutes=self.duraion["minutes"], hours=self.duraion["hours"], weeks=self.duraion["weeks"])
        # result = now + plusTime
        
        result = now + datetime.timedelta(minutes=1)
        
        # print(f"result = {result}")
        # result = now + timedelta(minutes=1)
        # result = result.replace(minute=0,second=0,microsecond=0)
        self.obj_Db.userCollection.update_many({},{"$set":{"nextTrainingDate":result}})
    
    def getNextTraining(self):
        tomorrowNextTraining =self.getTomorrowNextTraining(self.id)
        hourMin = tomorrowNextTraining.strftime("%H:%M")
        #گرفتن سال ، ماه نویسه ای ، روز
        # monthAlpha,year,month,day,monthAlphaFinglish,weekDayPer,weekDayFinglish
        monthAlpha,year,_,day,_,_,_ = self.convertToKhorshidi(tomorrowNextTraining)
        # گرفتن نام روز در هفته به پارسی
        weekDay = self.getWeekDay(tomorrowNextTraining)
        # weekDay = self.convertPersianWeekDay(tomorrowNextTraining)
        msgNextTrainingTimeDate = f"👈یادگیری واژگان روزانه👉 بعدی و پسین‌ات {self.firstName} عزیز 🌺🌸 در تاریخ  <b> {weekDay} {day} {monthAlpha} {year} </b>, در ساعت و زمان  <b>{hourMin} </b> می باشد."
        return msgNextTrainingTimeDate

    #گرفتن ایدهایی که زمان تمرین بعدیشان از امروز کوچک تر است و تغییر آنها به امروز در صورتیکه بازهم کوچکتر نباشند و در صورت کوچکتر بودن تغییر آنها به فردا
    def correctNextTrainings(self):
        today = datetime.datetime.now()
        # todayHour = today.hour
        condition = {"nextTrainingDate":{"$lt":today}}
        ids = []
        for col in self.obj_Db.userCollection.find(condition,{"userId":1 ,"_id":0}):
            for keys in col.keys():
                ids.append(col[keys])
        if len(ids) !=0:
            for id in ids:
                nextTrainingDate = ""
                for col in self.obj_Db.userCollection.find({"userId":id},{"nextTrainingDate":1,"_id":0}):
                    for keys in col.keys():
                        nextTrainingDate = col[keys]
                nextTrainingDateHour = nextTrainingDate.hour
                #در صورتیکه تفاوت این ساعت با ۲۴ ساعت بعد از ساعت نکست ترینیگ بیشتر از ۲۴ ساعت باشد
                # if todayHour< nextTrainingDateHour or nextTrainingDateHour == todayHour:

                #     putingNewNextTrainingDate = today.replace(hour = nextTrainingDateHour ) + relativedelta(days =1)
                #     self.obj_Db.userCollection.update_many({"userId":id},{"$set":{"nextTrainingDate":putingNewNextTrainingDate}})
                #در صورتیکه تفاوت این ساعت با ۲۴ ساعت بعد از ساعت نکست ترینیگ کمتر از ۲۴ ساعت باشد
                # elif nextTrainingDateHour< todayHour :

                #     putingNewNextTrainingDate = today.replace(hour = nextTrainingDateHour ) + relativedelta(days =2) 
                #     self.obj_Db.userCollection.update_many({"userId":id},{"$set":{"nextTrainingDate":putingNewNextTrainingDate}})      
                # else:
                #     pass    

                putingNewNextTrainingDate = today.replace(hour = nextTrainingDateHour,minute=0 ) + relativedelta(days =1)
                self.obj_Db.userCollection.update_many({"userId":id},{"$set":{"nextTrainingDate":putingNewNextTrainingDate}})
        else:
            pass      

                







# items.find({
#     created_at: {
#         $lt:"Mon May 30 18:47:00 +0000 2015",
#         $gt: "Sun May 30 20:40:36 +0000 2010"
#     }
# })








class Sections :
    def __init__(self,id):
        self.id = id
        self.obj_Db = Db()
######################
    def getSectionOne(self):
        section_1_words = []
        for col in self.obj_Db.sectionCollection.find({"userId":self.id,"section":1},{"word":1,"_id":0}):
            for keys in col.keys():
               section_1_words.append(col[keys])
        # print(f"section_1_words = {section_1_words}")
        return section_1_words

    def getSectionTwo(self):
        section_2_words = []
        for col in self.obj_Db.sectionCollection.find({"userId":self.id,"section":2},{"word":1,"_id":0}):
            for keys in col.keys():
               section_2_words.append(col[keys])
        # print(f"section_2_words = {section_2_words}")
        return section_2_words

    def getSectionThree(self):
        section_3_words = []
        for col in self.obj_Db.sectionCollection.find({"userId":self.id,"section":3},{"word":1,"_id":0}):
            for keys in col.keys():
               section_3_words.append(col[keys])
        # print(f"section_3_words = {section_3_words}")
        return section_3_words

    def getSectionFour(self):
        section_4_words = []
        for col in self.obj_Db.sectionCollection.find({"userId":self.id,"section":4},{"word":1,"_id":0}):
            for keys in col.keys():
               section_4_words.append(col[keys])
        # print(f"section_4_words = {section_4_words}")
        return section_4_words

    def getSectionFive(self):   
        section_5_words = []
        for col in self.obj_Db.sectionCollection.find({"userId":self.id,"section":5},{"word":1,"_id":0}):
            for keys in col.keys():
               section_5_words.append(col[keys])
        # print(f"section_5_words = {section_5_words}")
        return section_5_words
         
    def getSectionSix(self):
        section_6_words = []
        for col in self.obj_Db.sectionCollection.find({"userId":self.id,"section":6},{"word":1,"_id":0}):
            for keys in col.keys():
               section_6_words.append(col[keys])
        # print(f"section_6_words = {section_6_words}")
        return section_6_words

class Edit:
    def __init__(self):
        self.obj_Db = Db()
        
# add voice to db collection word
    def addVoiceFiled(self):
        field = {"deufVoice":{"deuName":"","deuTelegramLink":""}}
        self.obj_Db.meaningCollection.update_many({},{"$set":field})
        
# add voice to db collection word
    def deleteVoiceFiled(self):
        self.obj_Db.meaningCollection.update_many( {},{ "$unset": {"dafVoice": ""}})
        # db.items1.update( {},{ "$unset": {"dafVoice": ""}})

# add voice to db collection word
    def addVoiceFiledEn(self):
        field = {"engVoice":{"engName":"","engTelegramLink":""}}
        self.obj_Db.meaningCollection.update_many({},{"$set":field})
        
        
# add voice to db collection word
    def addVoiceFiledPer(self):
        field = {"perVoice":{"perName":"","perTelegramLink":""}}
        self.obj_Db.meaningCollection.update_many({},{"$set":field})


# edit word
    def changeWord(self):
         condition = {"word":"Entschuldigung die;-,en"}
         changed = {"word":"die Entschuldigung;-,en"}
         self.obj_Db.meaningCollection.update_many(condition,{"$set":changed})
         self.obj_Db.bookCollection.update_many(condition,{"$set":changed})
         self.obj_Db.wordCollection.update_many(condition,{"$set":changed})
         self.obj_Db.sectionCollection.update_many(condition,{"$set":changed})

    def changeWord2(self):
         condition = {"word":"Herr der,-(e)n, -en"}
         changed = {"word":"der Herr;-(e)n, -en"}
         self.obj_Db.meaningCollection.update_many(condition,{"$set":changed})
         self.obj_Db.bookCollection.update_many(condition,{"$set":changed})
         self.obj_Db.wordCollection.update_many(condition,{"$set":changed})
         self.obj_Db.sectionCollection.update_many(condition,{"$set":changed})

    def changeWord3(self):
         condition = {"word":"Kollege der;-n, -n"}
         changed = {"word":"der Kollege;-n, -n"}
         self.obj_Db.meaningCollection.update_many(condition,{"$set":changed})
         self.obj_Db.bookCollection.update_many(condition,{"$set":changed})
         self.obj_Db.wordCollection.update_many(condition,{"$set":changed})
         self.obj_Db.sectionCollection.update_many(condition,{"$set":changed})

    def changeWord4(self):
         condition = {"word":"Frau die; -, -en"}
         changed = {"word":"die Frau; -, -en"}
         self.obj_Db.meaningCollection.update_many(condition,{"$set":changed})
         self.obj_Db.bookCollection.update_many(condition,{"$set":changed})
         self.obj_Db.wordCollection.update_many(condition,{"$set":changed})
         self.obj_Db.sectionCollection.update_many(condition,{"$set":changed})

    def changeWord5(self):
         condition = {"word":"Name der; -ns, -n"}
         changed = {"word":"der Name; -ns, -n"}
         self.obj_Db.meaningCollection.update_many(condition,{"$set":changed})
         self.obj_Db.bookCollection.update_many(condition,{"$set":changed})
         self.obj_Db.wordCollection.update_many(condition,{"$set":changed})
         self.obj_Db.sectionCollection.update_many(condition,{"$set":changed})

    def changeWord6(self):
         condition = {"word":"Mahlzeit die"}
         changed = {"word":"die Mahlzeit"}
         self.obj_Db.meaningCollection.update_many(condition,{"$set":changed})
         self.obj_Db.bookCollection.update_many(condition,{"$set":changed})
         self.obj_Db.wordCollection.update_many(condition,{"$set":changed})
         self.obj_Db.sectionCollection.update_many(condition,{"$set":changed})

    def changeWord7(self):
         condition = {"word":"Tag der; -(e)s, -e"}
         changed = {"word":"der Tag; -(e)s, -e"}
         self.obj_Db.meaningCollection.update_many(condition,{"$set":changed})
         self.obj_Db.bookCollection.update_many(condition,{"$set":changed})
         self.obj_Db.wordCollection.update_many(condition,{"$set":changed})
         self.obj_Db.sectionCollection.update_many(condition,{"$set":changed})

    def changeWord8(self):
         condition = {"word":"Karte die; -, -n"}
         changed = {"word":"die Karte; -, -n"}
         self.obj_Db.meaningCollection.update_many(condition,{"$set":changed})
         self.obj_Db.bookCollection.update_many(condition,{"$set":changed})
         self.obj_Db.wordCollection.update_many(condition,{"$set":changed})
         self.obj_Db.sectionCollection.update_many(condition,{"$set":changed})

    def changeWord9(self):
         condition = {"word":"Hilfe die; -, -n"}
         changed = {"word":"die Hilfe; -, -n"}
         self.obj_Db.meaningCollection.update_many(condition,{"$set":changed})
         self.obj_Db.bookCollection.update_many(condition,{"$set":changed})
         self.obj_Db.wordCollection.update_many(condition,{"$set":changed})
         self.obj_Db.sectionCollection.update_many(condition,{"$set":changed})

    def changeWord10(self):
         condition = {"word":"Dank der"}
         changed = {"word":"der Dank"}
         self.obj_Db.meaningCollection.update_many(condition,{"$set":changed})
         self.obj_Db.bookCollection.update_many(condition,{"$set":changed})
         self.obj_Db.wordCollection.update_many(condition,{"$set":changed})
         self.obj_Db.sectionCollection.update_many(condition,{"$set":changed})


    def changeWord11(self):
         condition = {"word":"Freund der; -(e)s, -e"}
         changed = {"word":"der Freund; -(e)s, -e"}
         self.obj_Db.meaningCollection.update_many(condition,{"$set":changed})
         self.obj_Db.bookCollection.update_many(condition,{"$set":changed})
         self.obj_Db.wordCollection.update_many(condition,{"$set":changed})
         self.obj_Db.sectionCollection.update_many(condition,{"$set":changed})

    def changeWord12(self):
         condition = {"word":"freuen [vr]"}
         changed = {"word":"sich freuen [vr]"}
         self.obj_Db.meaningCollection.update_many(condition,{"$set":changed})
         self.obj_Db.bookCollection.update_many(condition,{"$set":changed})
         self.obj_Db.wordCollection.update_many(condition,{"$set":changed})
         self.obj_Db.sectionCollection.update_many(condition,{"$set":changed})


    def changeWordPersianMeaning(self):
         condition = {"$or":[{"word":"Karte die; -, -n"},{"word":"die Karte; -, -n"}]}
         changed = {"persian":" سپاسگذاری،  تشکر ; jmdm. (für etwas) ~ sagen (برای/از بابت چیزی) از کسی تشکر کردن"}
         self.obj_Db.meaningCollection.update_many(condition,{"$set":changed})

    def renameField(self):
        #  changed = {"$rename":{"deufVoice":"deuVoice"}}
        #  self.obj_Db.meaningCollection.update_many({},changed,False,True)
         condition = {"deufVoice":{"$exists":True}}       
         changed = {"$rename":{"deufVoice":"deuVoice"}}
         self.obj_Db.meaningCollection.update_many(condition,changed)

    def emptyValues(self):
        #  changed = {"$rename":{"deufVoice":"deuVoice"}}
        #  self.obj_Db.meaningCollection.update_many({},changed,False,True)
        # field = {"deuVoice":{"deuName":"","deuTelegramLink":""}}
        # self.obj_Db.meaningCollection.update_many({},{"$set":field})
        # field = {"synVoice":{"synName":"","synTelegramLink":""}}
        # self.obj_Db.meaningCollection.update_many({},{"$set":field})
        # field = {"allVoice":{"allName":"","allTelegramLink":""}}
        # self.obj_Db.meaningCollection.update_many({},{"$set":field})
        pass

    def deleteField(self):
        self.obj_Db.meaningCollection.update_many( {},{ "$unset": {"deufVoice": ""}})


        #اضافه کردن نام و لینک یک فایل
    def updateVoiceMeaningNameNAddress(self,word,deFileName,deLink,enFileName,enLink,syFileName,syLink,perFileName,perLink,wordFileName,wordLink):
        condition = {"word" : word}
        ########### DE ##########
        fileNameNLinkDe= {"$set":{"deuVoice.deuName":deFileName,"deuVoice.deuTelegramLink":deLink}}
        self.obj_Db.meaningCollection.update_many(condition,fileNameNLinkDe)
        ############ EN #########
        fileNameNLinkEn= {"$set":{"engVoice.engName":enFileName,"engVoice.engTelegramLink":enLink}}
        self.obj_Db.meaningCollection.update_many(condition,fileNameNLinkEn)
        ########### SY ##########
        fileNameNLinkSy= {"$set":{"synVoice.synName":syFileName,"synVoice.synTelegramLink":syLink}}
        self.obj_Db.meaningCollection.update_many(condition,fileNameNLinkSy)
        ########### PER ##########
        fileNameNLinkPer= {"$set":{"perVoice.perName":perFileName,"perVoice.perTelegramLink":perLink}}
        self.obj_Db.meaningCollection.update_many(condition,fileNameNLinkPer)
        ########### ALL ##########
        # fileNameNLinkAll= {"$set":{"allVoice.allName":allFileName,"allVoice.allTelegramLink":allLink}}
        # self.obj_Db.meaningCollection.update_many(condition,fileNameNLinkAll)
        ####### word #####
        fileNameNLinkWord= {"$set":{"voice.name":wordFileName,"voice.telegramLink":wordLink}}
        self.obj_Db.wordCollection.update_many(condition,fileNameNLinkWord)




#######################




################ add voice and link to database####################
# word = ""
# wordNamePart = ""
# middle = ""
# en = ""
# syn = ""
# per = ""
# de = ""
# all = ""
#wordLink = ""





# deFileName = f"{wordNamePart}{middle}De.mp3"
# linkPart = "https://t.me/guew_resource/"
# deLink = f"{linkPart}{de}"

# enFileName = f"{wordNamePart}{middle}En.mp3"
# enLink = f"{linkPart}{en}"

# syFileName = f"{wordNamePart}{middle}Sy.mp3"
# syLink = f"{linkPart}{syn}"

# perFileName = f"{wordNamePart}{middle}Per.mp3"
# perLink = f"{linkPart}{per}"

# allFileName = f"{wordNamePart}{middle}All.mp3"
# allLink = f"{linkPart}{all}"

# Edit().updateVoiceMeaningNameNAddress(word,deFileName,deLink,enFileName,enLink,syFileName,syLink,perFileName,perLink,allFileName,allLink)
################################################

# Edit().emptyValues()
# Edit().addVoiceFiledPer()
# Edit().addVoiceFiledEn()
# Edit().renameField()

    # Sections(73543260).deleteVoiceFiled()
    # Sections(73543260).addVoiceFiled()
    # Sections(73543260).addVoiceFiledEn()
    # Sections(73543260).addVoiceFiledPer()
    # Sections(73543260).changeWord()
    # Sections(73543260).changeWord2()
    # Sections(73543260).changeWord3()
    # Sections(73543260).changeWord4()
    # Sections(73543260).changeWord5()
    # Sections(73543260).changeWord6()
    # Sections(73543260).changeWord7()
    # Sections(73543260).changeWord8()
    # Sections(73543260).changeWord9()
    # Sections(73543260).changeWord10()
    # Sections(73543260).changeWord11()
    # Sections(73543260).changeWordPersianMeaning()
# Edit().renameField()
#FIXME TestCodes
# DeleteBot(73543260).deleteUser()

# Review(73543260).getReviewWords()
# Review(73543260).sortSectionBase()
# Review(73543260).sortChapterContentBase()
# b = Msg().getMessagesToday(73543260)
# Msg().getMessagesTodayOfAll()
# Msg().isTheLastOneRepeatedMsg(73543260)
# Admin(73543260).getMessagesTodayOfAll()
# l = Vazhegan(73543260).audioWord("freuen [vr]")
# print(f"link = {l}")