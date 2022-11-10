# coding=utf8
import requests
import json
import pymongo
import telegram

import sys
sys.path.append( "../")
from mainV2.AnalyzeLn import AnalyzeDe
from mainV2.AnalyzeLn import AnalyzePer
from mainV2.AnalyzeLn import AnalyzeEn
from mainV2.KeysNMsgs import KeysNMsgsDe as kNMDe
from mainV2.KeysNMsgs import KeysNMsgsEn as kNMEn
from mainV2.KeysNMsgs import KeysNMsgsPer as kNMPer

from mainV2.set import dbContact as dbC
import pybotc
# import AnalyzeNewTest as Analyze
#abstraction
from abc import ABC,abstractclassmethod
# from string import strip
import strip
import threading



def main():
        # msgArray = []
        # myId = 130405462
        update_id = None
        last_name = None
        username = None
        # kNM = Sending
        f = "config.cfg"
        bot = pybotc.Bot(f) 
        # kind ="server"
        kind = pybotc.Type(f).typSystem()
        dbCEx = dbC.ExportDb(kind)
        # idThread=None
        # def analyzeFunc(userId,first_name,msg,callBackQuery_id,msgId,data,last_name,username):
        #     try:
        #         # print(f"userId = {userId}")
        #         language = dbC.UILanguage(userId).getUIL()
        #         print(f"language = {language}")
        #         if language == "Per" or language == "" or language == None:
        #                 AnalyzePer.KindOfUser(userId,first_name,msg,callBackQuery_id,msgId,data,last_name,username).identifyUserAndMsg()   
        #         # AnalyzePer.KindOfUser(userId,first_name,msg,callBackQuery_id,msgId,data,last_name,username).identifyUserAndMsg()   

        #         #FIXME fix callBackQuery_id,msgId,data to en and de as well
        #         elif language == "En":
        #                 AnalyzeEn.KindOfUser(userId,first_name,msg,callBackQuery_id,msgId,data,last_name,username).identifyUserAndMsg()   
        #         elif language == "De":
        #                 AnalyzeDe.KindOfUser(userId,first_name,msg,callBackQuery_id,msgId,data,last_name,username).identifyUserAndMsg()
        #     except:         
        #         AnalyzePer.KindOfUser(userId,first_name,msg,callBackQuery_id,msgId,data,last_name,username).identifyUserAndMsg()
        
        
        while True:
            try:
                    # getUpdate =pybotc.Bot("config.cfg").get_updates 
                    getUpdate =bot.get_updates
                    # getUpdate =BotTel().get_updates
                    updates = getUpdate(offset=update_id)
                    updates = updates["result"]
                    # print("updates :",updates)
                    # print("updates = ",updates)
                    if updates:
                            for item in updates:
                                update_id = item["update_id"]
                                # userId = str(item["message"]["from"]["id"])
                                try:
                                    userId = item["message"]["from"]["id"]
                                    # print("userId =",userId)
                                    first_name = item["message"]["from"]["first_name"]
                                    # print("first_name =",first_name)
                                    msg = item["message"]["text"]
                                    # msgArray.append(msg)
                                    # print("msg = ",msg)
                                    # print("msgArray = ",msgArray)
                                    callBackQuery_id = None
                                    msgId = None      
                                    data = None
                                except:
                                    userId = item['callback_query']['from']['id'] 
                                    first_name = item["callback_query"]["from"]["first_name"]
                                    msg=None
                                    callBackQuery_id = item['callback_query']['id']
                                    msgId = item['callback_query']['message']['message_id']         
                                    data = item['callback_query']['data']



                                try:    
                                    username = item["message"]["from"]["username"]
                                    # print("username = ",username)
                                    # Karbar.getUsertName(username)
                                except:
                                    username=""
                                    # print("this user {} with chatId {} has no user_name".format(first_name,userId))

                                try:    
                                    last_name = item["message"]["from"]["last_name"] 
                                    # print("last_name =",last_name)
                                    # Karbar.getLastName(last_name)
                                except:
                                    last_name = ""
                                    # print("this user {} with chatId {} has no last_name".format(first_name,userId))


                                try:
                                    try:
                                        # print(f"userId = {userId}")
                                        language = dbC.UILanguage(userId).getUIL()
                                        print(f"language = {language}")
                                        if language == "Per" or language == "" or language == None:
                                             AnalyzePer.KindOfUser(userId,first_name,msg,callBackQuery_id,msgId,data,last_name,username).identifyUserAndMsg()   
                                        # AnalyzePer.KindOfUser(userId,first_name,msg,callBackQuery_id,msgId,data,last_name,username).identifyUserAndMsg()   

                                        #FIXME fix callBackQuery_id,msgId,data to en and de as well
                                        elif language == "En":
                                             AnalyzeEn.KindOfUser(userId,first_name,msg,callBackQuery_id,msgId,data,last_name,username).identifyUserAndMsg()   
                                        elif language == "De":
                                             AnalyzeDe.KindOfUser(userId,first_name,msg,callBackQuery_id,msgId,data,last_name,username).identifyUserAndMsg()
                                    except:         
                                        AnalyzePer.KindOfUser(userId,first_name,msg,callBackQuery_id,msgId,data,last_name,username).identifyUserAndMsg()
                                    # if userId!=idThread:
                                    #     threading.Thread(target=analyzeFunc(userId,first_name,msg,callBackQuery_id,msgId,data,last_name,username), name=str(userId)).start()
                                    # else:
                                    #     analyzeFunc(userId,first_name,msg,callBackQuery_id,msgId,data,last_name,username)
                                    
                                    # idThread = userId 
                                        
                                
                                    
                                
                                except:
                                    pass
            except:
                    print("result issue")                        


            ### پیام خودکار به کاربر inja
            #این سه خط پایین بررسی شود
            #گرفتن ایدی های ستینگ پیش از یک زمان مشخص شده ارسال شده باشند (جهت کسر شدن از ایدی های که بعدن می خواهند ارسال شوند)  الف =done
            subtractionIds = dbC.DateArrange().getIdsSent()
            #گرفتن کلیه ایدی ها از کالکشن یوزر
            dateNIdWithField=dbC.DateArrange().getTomorrowNextTrainingAll(subtractionIds)

            # ب کسر ایدی های الف تمامی ایدی های یافت شدهsubtractionIds
            #dateNIdWithField یا ادغام ب و =don
            # print(f"dateNIdWithField = {dateNIdWithField}")
            #گرفتن ایدهایی گرفته از کالکشن یوزر که با محدودیت فاصله زمانی جهت ارسال معرفی می شود
            ids = dbC.DateArrange().idsTrainTime(dateNIdWithField)
            # print(f"ids = {ids}")
            if len(ids)!=0:
                 dbC.DateArrange().saveIdsNDateTimes(ids)
            #گرفتن آیدی ها به علاوه آبجکت آیدی رکورد در غالب یک دیکشنری با محدودیت زمان از کالکشن ستینگ 
            myDict = dbC.DateArrange().getIdsDictN_id()
            #تفکیک دیکشنری به ایدی ها و آبجکت شان 
            ids,objectIds = dbC.DateArrange().getIdN_idSeparatly(myDict)
            # print(f"ids = {ids} , objectIds = {objectIds}")
            for i in ids:
                fN = dbC.DateArrange().getFirstName(i)
                # print(f"fN = {fN}")
                dbC.DateArrange().saveTrueAutomateMsgFlag(i)
                languageIn = dbC.UILanguage(int(i)).getUIL()
                # print(f"languageIn = {languageIn}")
                if languageIn == "En":
                   kNMEn.AutomaticMessage(i,fN).sendKeyAndMessageDailyLearn()     
                elif languageIn == "De":
                   kNMDe.AutomaticMessage(i,fN).sendKeyAndMessageDailyLearn()  
                elif languageIn == "Per" or languageIn == "":
                   kNMPer.AutomaticMessage(i,fN).sendKeyAndMessageDailyLearn()  
                #ذخیره زمان تمرین فردا در یوزرو ارسال شده در ستینگ 
                dbC.DateArrange().updateSentIdsNNextTrainDate(objectIds,i)
            #######
            dbCEx.hourlyBackup()
            dbCEx.makeCollectionsZip()
            dbCEx.checkFullBackupSentNUpdate()
            #######
            dbC.DateArrange().correctNextTrainings()


if __name__ == '__main__':
  main()