import json
import requests
import sys
sys.path.append( "../")

from mainV2.base.Buttons import ButtonEn as Btn
from mainV2.base.Buttons import ButtonSame as BtnS
from mainV2.base.ButtonsA import ButtonAdminEn as BtnA 
from mainV2.base.Keys import SKeys
from mainV2.base.Keys import EnKeys  as Keys 
from mainV2.base.KeysA import EnKeysA as AKeys
from mainV2.base.Txt import MessageNVarEn as MNV
from mainV2.base import Txt

from mainV2.set import dbContact
from mainV2 import pybotc

import datetime
import os


class Inline:
    def __init__(self,id,msgId,first_name=None):
        self.id = id
        self.msgId = msgId
        self.firstName = first_name
        self.bot = pybotc.Bot("config.cfg")
        # self.obj_dbContatct = dbContact()

     #######BETWEEN#########
    def dataWord(self,way,newWordsMsg,msgKey):
        parse_mode = "HTML"
        self.bot.sendMessage(self.id,msgKey,parse_mode,Keys().getBackKeys)       
        antwortKey = SKeys(Btn(),MNV()).wordKeys(way)
        self.bot.sendMessage(self.id,newWordsMsg,parse_mode,antwortKey)


    def dataWordWithGuide(self,way,newWordsMsg,msgKey):
        antwortKey = SKeys(Btn(),MNV()).wordKeys(way)
        parse_mode = "HTML"     
        self.bot.sendMessage(self.id,msgKey,parse_mode,Keys().getBackKeys)
        self.bot.sendMessage(self.id,newWordsMsg,parse_mode,antwortKey)




      #######BETWEEN#########
    def dataWordQuery(self,way,newWordsMsg):
        # print(way)
        antwortKey = SKeys(Btn(),MNV()).wordKeys(way)
        parse_mode = "HTML"
        self.bot.editMessage(self.id,self.msgId,newWordsMsg,parse_mode,antwortKey)

    def dataWordWithGuideQuery(self,way,newWordsMsg):
        # print(way)
        antwortKey = SKeys(Btn(),MNV()).wordKeys(way)
        parse_mode = "HTML"
        self.bot.editMessage(self.id,self.msgId,newWordsMsg,parse_mode,antwortKey)


    def answerWord(self,data,way,newWordsMsg):
               #63 blank space
        # answerInTopOfCard = MNV().answerInTopOfCard(data,icon)
        # newWordsMsg = f"<b>{answerInTopOfCard}</b>\n{answerLink} {standardizedAnswer.center(63)}."
        rWAKey = SKeys(Btn(),MNV()).answerKeys(data,way,Btn().word)
        parse_mode = "HTML"
        self.bot.editMessage(self.id,self.msgId,newWordsMsg,parse_mode,rWAKey)
        # self.bot.sendMessage(self.id,newWordsMsg,parse_mode,rWAKey)
    


    def answerWordWithGuide(self,data,way,newWordsMsg):

        rWAKey = SKeys(Btn(),MNV()).answerKeys(data,way,Btn().word)
        parse_mode = "HTML"
        self.bot.editMessage(self.id,self.msgId,newWordsMsg,parse_mode,rWAKey)
        # self.bot.sendMessage(self.id,newWordsMsg,parse_mode,rWAKey)

    def sendVideoReport(self,pathNFile):
        caption = Txt.PublicMsgNVar().gudwbot
        video ={'document': open(pathNFile,"rb")}
        self.bot.sendDocument(self.id,video,caption)

    def report(self,daliyReport):
        backToHomePage = ""
        parse_mode = "HTML"
        self.bot.editMessage(self.id,self.msgId,daliyReport,parse_mode,backToHomePage)
     
        #####review#####   
    def reviewOne(self,waysRevTypeCB,ways,length,wordDetails,msg):
        keys = SKeys(Btn(),MNV()).reviewOne(waysRevTypeCB,ways,length,Btn().getBack,MNV().endReview)
        parse_mode = "HTML"
        reviewBtns = [Btn().chapterNSection,Btn().leitnerBoxParts,Btn().weakWords]
        wordBCs = [BtnS().wordChapNSCB,BtnS().wordLeitBPCB,BtnS().wordWWCB]
        removeKeys = SKeys(Btn(),MNV()).removeKeyboard
        if msg  not in wordBCs and msg in reviewBtns:
            self.bot.sendMessage(self.id,msg,parse_mode,removeKeys)
            self.bot.sendMessage(self.id,wordDetails,parse_mode,keys)
        else:
            self.bot.editMessage(self.id,self.msgId,wordDetails,parse_mode,keys)


        #msg is self.msg and msgkey is messeage which must show for word details
    def reviewMoreThanOne(self,counter,waysRevTypeCB,ways,length,wordDetails,msg):
        keys = SKeys(Btn(),MNV()).reviewMoreThanOne(counter,waysRevTypeCB,ways,length,msg)
        parse_mode = "HTML"
        reviewBtns = [Btn().chapterNSection,Btn().leitnerBoxParts,Btn().weakWords]
        wordBCs = [BtnS().wordChapNSCB,BtnS().wordLeitBPCB,BtnS().wordWWCB]
        removeKeys = SKeys(Btn(),MNV()).removeKeyboard
        # Keys().getBackKeys
        if msg  not in wordBCs and msg in reviewBtns:
            self.bot.sendMessage(self.id,msg,parse_mode,removeKeys)
            self.bot.sendMessage(self.id,wordDetails,parse_mode,keys)
        else:
            self.bot.editMessage(self.id,self.msgId,wordDetails,parse_mode,keys)


        #msg is self.msg and msgkey is messeage which must show for word details
    def reviewAnswer(self,reviewsKeysCB,data,ways,counter,length,answer,wordType):
        keys = SKeys(Btn(),MNV()).reviewAnswer(reviewsKeysCB,ways,counter,length,data,wordType)
        # keys = ''
        parse_mode = "HTML"
        self.bot.editMessage(self.id,self.msgId,answer,parse_mode,keys)
    
    def getBack(self,msgEdit):
        keys = ""
        # msgEdit = Btn().endReview
        parse_mode="HTML"
        keysSend = Keys().secondMenu
        msgSend = Btn().getBack
        self.bot.editMessage(self.id,self.msgId,msgEdit,parse_mode,keys)
        self.bot.sendMessage(self.id,msgSend,parse_mode,keysSend)
      #######way####  
    def addWay(self,way):
        msg = MNV(self.firstName).addWayBeforeTxt()
        keys = SKeys(Btn(),MNV()).addWayKeys(way)
        parse_mode="HTML"
        self.bot.editMessage(self.id,self.msgId,msg,parse_mode,keys)

    def addedWayBefore(self,way):
        keys = ""
        msgEdit = MNV(self.firstName).addedWaytxt(way)
        keySend = Keys().secondMenu
        msgSend = MNV(self.firstName).secondMenu
        parse_mode="HTML"
        self.bot.editMessage(self.id,self.msgId,msgEdit,parse_mode,keys)
        self.bot.sendMessage(self.id,msgSend,parse_mode,keySend)




    def subtractWay(self,way):
        msg = MNV(self.firstName).subtractWayTxt()
        keys = SKeys(Btn(),MNV()).subtractWayKeys(way)
        parse_mode="HTML"
        self.bot.editMessage(self.id,self.msgId,msg,parse_mode,keys)

    def subtractedWayBefre(self,way):
        # msg = ""
        keys = ""
        msgEdit = MNV(self.firstName).subtractedWayBeforeTxt(way)
        parse_mode="HTML"
        keySend = Keys().secondMenu
        msgSend = MNV(self.firstName).secondMenu
        self.bot.editMessage(self.id,self.msgId,msgEdit,parse_mode,keys)
        self.bot.sendMessage(self.id,msgSend,parse_mode,keySend)

    def changeWayBefore(self,way):
        parse_mode="HTML"
        # keys = SKeys(Btn(),MNV()).changeWayKeys(way)
        keys = SKeys(Btn(),MNV()).changeWayKeys(way,Btn().getBack,MNV().secondMenu)
        # keys = ""
        msgEdit = MNV(self.firstName).changeWayBeforeTxt(way)
        self.bot.editMessage(self.id,self.msgId,msgEdit,parse_mode,keys)

    def changeWay(self,add,subtract):
        parse_mode="HTML"
        keys = ""
        # keys = ""
        msgEdit = MNV(self.firstName).changeWayTxt(add,subtract)
        self.bot.editMessage(self.id,self.msgId,msgEdit,parse_mode,keys)
        keySend = Keys().secondMenu
        msgSend = MNV(self.firstName).secondMenu
        self.bot.sendMessage(self.id,msgSend,parse_mode,keySend)
     

#تمامی کیبوردها و پیام های بخش استارت و خود دکمه استارت
class Start:
    def __init__(self,id,firstName,msg):
        self.id = id
        self.firstName = firstName
        self.msg = msg
        self.bot = pybotc.Bot("config.cfg")
        # self.obj_dbContatct = dbContact()
        
    def memberChannel(self,chat_id):
         keys = ""
         msg = MNV(self.firstName).memberInCannel(chat_id)
         self.bot.sendMessage(self.id,msg,"HTML",keys)

    #این دکمه ها و پیام  می آیند Start در صورت زدن دکمه
    def sendKeyAndMessagesUI(self):
         languageMsg = f"Dear {self.firstName} 🌺🌸, select your favorite language for bots message and keyboard"
        #  languagesKey = json.dumps({"keyboard":[[BtnS().keyNMsgDe],[BtnS().keyNMsgEn],[BtnS().keyNMsgPer]],"resize_keyboard":True}) 
         languagesKey = SKeys(Btn(),MNV()).uI
         self.bot.sendMessage(self.id,languageMsg,"none",languagesKey)

   #    یا کیبورد و پیام پارسی⌨💬 این دکمه ها و پیام از فهرست نخستین🛎 و اولیه  می آیند  deutsch Menu, english Menu  در صورت زدن یکی از دکمه های  
    def sendKeyAndMessageFNVAUIselected(self):
        languageSelectedMsg = f"{self.msg} is chosen for bot."
        # firstHomePageKey = json.dumps({"keyboard":[[Btn().startLearning],[Btn().aboutBotNew,Btn().uILangNKeyEditNew]], "resize_keyboard": True})
        firstHomePageKey = Keys().firstMenu
        self.bot.sendMessage(self.id,languageSelectedMsg,"none",firstHomePageKey)
    

    def sendKeyAndMessageFNVAUINakhostin(self):
        languageSelectedMsg = "Menu🛎"
        # firstHomePageKey = json.dumps({"keyboard":[[Btn().startLearning],[Btn().aboutBotNew,Btn().uILangNKeyEditNew]], "resize_keyboard": True})
        firstHomePageKey = Keys().firstMenu
        self.bot.sendMessage(self.id,languageSelectedMsg,"none",firstHomePageKey) 



#تمامی کیبوردها و پیام های بخش آغاز یادگیری واژه های کتاب
class AghazYadgiriVazhehayeKetab:
    def __init__(self,id,firstName,msg):
        self.id = id
        self.firstName = firstName
        self.msg = msg
        self.bot = pybotc.Bot("config.cfg")
        self.obj_dbContatct = dbContact

    def sendAccountInfoKeyAndMessageBBFA(self,outpuTodayDateNTime,output):
        msgNextTrainingTimeDate = output
        ent = "▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️"
        dash = "〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️" 
        msgNextTrainingTimeDate = f"Dear <i> {self.firstName} </i>🌺🌸 Your Account\n{ent}\n{output}\n{dash}\n {outpuTodayDateNTime}\n @DeutschOhal"
        # regularHomePageKey = json.dumps({"keyboard":[[Btn().reviewWords],[Btn().wordsNum,Btn().wayEdit,Btn().account],[Btn().timeLearnEdit,Btn().reportActivity],[Btn().deleteBot,Btn().aboutBot,Btn().uILangNKeyEdit],[Btn().opinion]],"resize_keyboard":True})
        regularHomePageKey = Keys().secondMenu
        self.bot.sendMessage(self.id,msgNextTrainingTimeDate,"none",regularHomePageKey)


    #در صورت زدن دکمه((آعاز یادگیری واژه های کتاب)) این دکمه ها و پیام می آیند
    def sendAYVKKeyAndMessage327(self):
        wortZahlMsg = f" Dear {self.firstName} 🌺🌸, how many new words do you want in a day?"        
        # wortZahlKey = json.dumps({"keyboard":[[BtnS().threeNew],[BtnS().twoNew],[BtnS().oneNew]],"resize_keyboard":True})
        wortZahlKey = SKeys(Btn(),MNV()).numWordsNew
        print(wortZahlKey)
        # wortZahlKey = ""
        self.bot.sendMessage(self.id,wortZahlMsg,"none",wortZahlKey)
    #در صورت زدن یکی از دکمه های ۳ یا ۵  یا ۷ این دکمه ها و پیام می آیند
    def send357KeyAndMessageDESP(self):
        waysMsg = f"Dear {self.firstName}  🌺🌸, Choose the Method to Learn Book Words."
        # wayKey = json.dumps({"keyboard":[[BtnS().deutschNew],[BtnS().englishNew],[BtnS().synonymNew],[BtnS().persianNew]],"resize_keyboard":True}) 
        wayKey = SKeys(Btn(),MNV()).waysNew
        self.bot.sendMessage(self.id,waysMsg,"none",wayKey)

    

     #    یا پارسی این دکمه و پیام می آیند  deutsch , english , synonym  در صورت زدن یکی از دکمه های  
    def sendDESPKeyAndMessageLampGuid(self,way,wKind,numW,numAll,standardizedWord,content,chapter,wordsPage,wordLink):
        dash = "___________________________________"
        guide = f"Hint🔔: Read the word and say {way} of that and remember it then tap on 💡 to see the correct answer and compare it with your answer."
        newWordsMsg = f".{numW}/{numAll}                                         {wKind}.\n<b>{standardizedWord}</b>\n.Chapter : {content}\nSection : {chapter} \nPage:{wordsPage}.\n{dash}\n{wordLink}{guide}"
        
        # {content}\n{cotentNChap} \nPage:{wordsPage}
        # antwortKey = json.dumps({"keyboard":[[BtnS().lamp]],"resize_keyboard":True}) 
        antwortKey = SKeys(Btn(),MNV()).lampKeys
        self.bot.sendMessage(self.id,newWordsMsg,"none",antwortKey)


                               
   #    یا پارسی این دکمه و پیام می آیند  deutsch , english , synonym  در صورت زدن یکی از دکمه های  
    def sendDESPKeyAndMessageLamp(self,wKind,numW,numAll,standardizedWord,content,chapter,wordsPage,wordLink):
        newWordsMsg = f".{numW}/{numAll}                                         {wKind}.\n<b>{standardizedWord}</b>\n.Chapter : {content}\nSection : {chapter} \nPage:{wordsPage}.\n. \n {wordLink}"
        # {content}\n{cotentNChap} \nPage:{wordsPage}
        # antwortKey = json.dumps({"keyboard":[[BtnS().lamp]],"resize_keyboard":True}) 
        antwortKey = SKeys(Btn(),MNV()).lampKeys
        self.bot.sendMessage(self.id,newWordsMsg,"none",antwortKey)



   #در صورت زدن دکمه 💡 این دکمه و پیام می آید 
    def sendLampKeyAndMessageVXGuide(self,way,icon,standardizedAnswer,answerLink):
               #63 blank space
        # dash 35
        dash = "___________________________________"
        # print(f"len(dash)={len(dash)}")
        # guide 102 فارسی
        guide = f"Hint🔔: By checking the reply sent and your answer, choose your answer correctly or incorrectly by selecting ❌ or ✅."
        
        pa = f"Answer into  {way} {icon}"
        lenngthPa = len(pa)
        pa = pa.center(72 - lenngthPa)
        # print(f"len(pa) = {len(pa)}")       
        newWordsMsg = f"<b>{pa}</b>\n{standardizedAnswer}\n{dash}\n{answerLink}{guide}"
        # length = len(newWordsMsg)
        # print(f"length = {length}")
        # sum = len(dash) + len(guide) + len(standardizedAnswer) + len(pa)
        # print(f"sum = {sum}")
        # rwKey = json.dumps({"keyboard":[[BtnS().crossCheck,BtnS().check]],"resize_keyboard":True}) 
        rwKey = SKeys(Btn(),MNV()).rW
        self.bot.sendMessage(self.id,newWordsMsg,"none",rwKey)


   #در صورت زدن دکمه 💡 این دکمه و پیام می آید 
    def sendLampKeyAndMessageVX(self,way,icon,standardizedAnswer,answerLink):
               #63 blank space
        pa = f"Answer into  {way} {icon}"
        lenngthPa = len(pa)
        pa = pa.center(72 - lenngthPa)
        newWordsMsg = f"<b>{pa}</b>\n{standardizedAnswer.center(63)}.\n {answerLink}"
        # rwKey = json.dumps({"keyboard":[[BtnS().crossCheck,BtnS().check]],"resize_keyboard":True}) 
        rwKey = SKeys(Btn(),MNV()).rW
        self.bot.sendMessage(self.id,newWordsMsg,"none",rwKey)
    #done section 7
    #در صورت زدن آخرین دکمه از❌","✅ این دکمه و پیام می آیند  
    def sendLastVXKeyAndMessageBBFA(self,nWorkedWords,nRWords,nWWrong,wrongWordsNpages,weekDay,day,month,year,houNMTraining,dateGriNextTraining,wordsSectionPosition):
        dash = "___________________________________"
        print(f"nRWords = {nRWords},nWorkedWords = {nWorkedWords}")
        percentageRight = self.obj_dbContatct.Percentage().percentage(nRWords,nWorkedWords)
        percentageWrong = self.obj_dbContatct.Percentage().percentage(nWWrong,nWorkedWords)
        graphRight = self.obj_dbContatct.Graph().graph(nRWords,nWorkedWords)
        graphWrong = self.obj_dbContatct.Graph().graph(nWWrong,nWorkedWords)
        guide = f"🔔 After tap on '{Btn().getBack}' You can select '{Btn().reviewWords}' to review the words you have done."

        daliyReport =  f" Dear {self.firstName}  🌺🌸 <i> Report your activities, Today: </i> \n {dash.center(14)} \n Number of Practiced Words: <b> {nWorkedWords} </b> \n Number of correct words: <b> {nRWords} </b> \n Number of incorrect words: <b> {nWWrong} </b> \n {dash.center(14)} \n <i> percentage of correct and incorrect Words: </i> \n  Correct <b> {graphRight}% {percentageRight} </b> \n  incorrect <b> {graphWrong}% {percentageWrong} </b> \n  {dash.center(14)} \n  List of incorrect words today with the page address in the book: \n  <b> {wrongWordsNpages} </b> \n  {dash.center(14)} \n The 👉Learn Vocabulary Daily👈 next on <b> { weekDay} {day} {month} {year} </b>, at <b> {houNMTraining} </b> In the time of Iran, Coincides with <b>{dateGriNextTraining}</b>\n {dash} \n <i> Partition and number of all words in the Lightner box: </i> \n  Words number in 1Th partition: <b> {wordsSectionPosition[0]} </b> \n  Words number in 2Th partition: <b> {wordsSectionPosition[1]} </b> \n  Words number in 3Th partition: <b> {wordsSectionPosition[2]} </b> \n  Words number in 4Th partition: <b> {wordsSectionPosition[3]} </b> \n  Words number in 5Th partition:  <b> {wordsSectionPosition[4]} </b> \n  Words number in 6Th partition: <b> {wordsSectionPosition[5]} </b> \n {dash} \n  Number of fully learned vocabulary: <b> {wordsSectionPosition[6]} </b> \n {dash} \n  <i> {guide} </i> \n @DeutschOhal \n"
        print(f"daily report = {daliyReport}")
        # backToHomePage = json.dumps({"keyboard":[[Btn().getBack]],"resize_keyboard":True})
        backToHomePage = Keys().getBackKeys
        self.bot.sendMessage(self.id,daliyReport,"none",backToHomePage)
       
    # فرستادن تاریخ و زمان یادگیری واژگان بعدی پسین
    def sendNextTrainingDateTimeKeyAndMessageBBFA(self,weekDay,day,monthAlpha,year,hourMin):
        # y = "یادگیری واژگان روزانه"
        msgNextTrainingTimeDate = f"Dear <i>{self.firstName}</i>🌺🌸, The 👉Learn Vocabulary Daily👈 next on <b> {weekDay} {day} {monthAlpha} {year} </b>, at <b> {hourMin} </b>. \n@DeutschOhal"
        # regularHomePageKey = json.dumps({"keyboard":[[Btn().reviewWords],[Btn().wordsNum,Btn().wayEdit,Btn().account],[Btn().timeLearnEdit,Btn().reportActivity],[Btn().deleteBot,Btn().aboutBot,Btn().uILangNKeyEdit],[Btn().opinion]],"resize_keyboard":True})
        regularHomePageKey = Keys().secondMenu
        self.bot.sendMessage(self.id,msgNextTrainingTimeDate,"none",regularHomePageKey)





     #در صورت زدن  دکمه بازگشت به فهرست آغازین🏡 به بخش فهرست آغازین و اصلی منتقل شده و این دکمه ها و پیام می آیند 
     #FIXME حذف این تابع از کیبورد و جایگزینی در آنالیز AYVK.sendKeyAndMessageFAVA()
    def sendKeyAndMessageFAVA(self):
        fehrestAghazinMsg = "Home"
        # regularHomePageKey = json.dumps({"keyboard":[[Btn().reviewWords],[Btn().wordsNum,Btn().wayEdit,Btn().account],[Btn().timeLearnEdit,Btn().reportActivity],[Btn().deleteBot,Btn().aboutBot,Btn().uILangNKeyEdit],[Btn().opinion]],"resize_keyboard":True})
        regularHomePageKey = Keys().secondMenu
        self.bot.sendMessage(self.id,fehrestAghazinMsg,"none",regularHomePageKey)

    def sendKeyAndMessageUserMustWait(self):
        fehrestAghazinMsg = "Until the next date"
        # regularHomePageKey = json.dumps({"keyboard":[[Btn().reviewWords],[Btn().wordsNum,Btn().wayEdit,Btn().account],[Btn().timeLearnEdit,Btn().reportActivity],[Btn().deleteBot,Btn().aboutBot,Btn().uILangNKeyEdit],[Btn().opinion]],"resize_keyboard":True})
        regularHomePageKey = Keys().secondMenu
        self.bot.sendMessage(self.id,fehrestAghazinMsg,"none",regularHomePageKey)

class ErrorMsgs:
    def __init__(self,id,firstName,msg):
        self.id = id
        self.firstName = firstName
        self.msg = msg
        self.bot = pybotc.Bot("config.cfg")
        self.obj_dbContatct = dbContact
    #spam warning BtnS().crossCheck,"✅ پیام خطا به جهت فرستادن تکراری 
    def sendWarningKeyAndMessageLamp(self):
        msgWarning = "⛔️😡😡⛔️ Avoid sending Spam ⛔️😡😡⛔️"
        # antwortKey = json.dumps({"keyboard":[[BtnS().lamp]],"resize_keyboard":True}) 
        # antwortKey = SKeys(Btn(),MNV()).lampKeys
        antwortKey = ""
        self.bot.sendMessage(self.id,msgWarning,"none",antwortKey)
        #spam warning هنگامه آخرین واژه BtnS().crossCheck,"✅ پیام خطا به جهت فرستادن تکراری 
    def sendWarningKeyAndMessageBBFA(self):
        msgWarning = "⛔️😡😡⛔️ Avoid sending Spam ⛔️😡😡⛔️"
        # backToHomePage = json.dumps({"keyboard":[[Btn().getBack]],"resize_keyboard":True})
        # backToHomePage = Keys().getBackKeys
        backToHomePage = ""
        self.bot.sendMessage(self.id,msgWarning,"none",backToHomePage)
     
    #spam warning  پیام خطا به جهت فرستادن تکراری برای کاربری که هنوز نام نویسی نشده 
    def sendWarningRepeatedKeyAndMessageToNoneUser(self):
        msgWarning = "⛔️😡😡⛔️ Avoid sending Spam ⛔️😡😡⛔️"
        # firstHomePageKey = json.dumps({"keyboard":[[Btn().startLearning],[Btn().aboutBotNew,Btn().uILangNKeyEditNew]], "resize_keyboard": True}) 
        # firstHomePageKey = Keys().firstMenu
        firstHomePageKey = ""
        self.bot.sendMessage(self.id,msgWarning,"none",firstHomePageKey)


    #spam warning  پیام خطا به جهت فرستادن تکراری برای کاربر  
    def sendWarningRepeatedKeyAndMessageToUser(self):
        msgWarning = "⛔️😡😡⛔️ Avoid sending Spam ⛔️😡😡⛔️"
        # regularHomePageKey = json.dumps({"keyboard":[[Btn().reviewWords],[Btn().wordsNum,Btn().wayEdit,Btn().account],[Btn().timeLearnEdit,Btn().reportActivity],[Btn().deleteBot,Btn().aboutBot,Btn().uILangNKeyEdit],[Btn().opinion]],"resize_keyboard":True})
        # regularHomePageKey = Keys().secondMenu
        regularHomePageKey = ""
        self.bot.sendMessage(self.id,msgWarning,"none",regularHomePageKey) 
   
      #none keyboard warning  پیام خطا به جهت عدم استفاده از کیبورد رباط  
    def sendWarningNoneKeyboardToUser(self):
        msgWarning = "Only use the Bot keyboard!"
        # regularHomePageKey = json.dumps({"keyboard":[[Btn().reviewWords],[Btn().wordsNum,Btn().wayEdit,Btn().account],[Btn().timeLearnEdit,Btn().reportActivity],[Btn().deleteBot,Btn().aboutBot,Btn().uILangNKeyEdit],[Btn().opinion]],"resize_keyboard":True})
        regularHomePageKey = Keys().secondMenu
        # regularHomePageKey=""
        self.bot.sendMessage(self.id,msgWarning,"none",regularHomePageKey) 

      #none keyboard warning  پیام خطا به جهت عدم استفاده از کیبورد رباط  
    def sendWarningNoneKeyboardToGuest(self):
        msgWarning = "Only use the Bot keyboard!"
        # firstHomePageKey = json.dumps({"keyboard":[[Btn().startLearning],[Btn().aboutBotNew,Btn().uILangNKeyEditNew]], "resize_keyboard": True}) 
        firstHomePageKey = Keys().firstMenu
        # firstHomePageKey =""
        self.bot.sendMessage(self.id,msgWarning,"none",firstHomePageKey) 


class AutomaticMessage:
    def __init__(self,id,firstName):
        self.id = id
        self.bot = pybotc.Bot("config.cfg")
        self.firstName = firstName
    def sendKeyAndMessageDailyLearn(self):
        msg = f"Dear <i> {self.firstName}</i>  🌺🌸, Begin learning and practicing vocabulary, tap on '👉👉Learn Vocabulary Daily👈👈' by keyboards bot!"

        # learnKey = json.dumps({"keyboard":[[Btn().dailyLearnWords]],"resize_keyboard":True})
        learnKey = Keys().dailyLearnKeys
        self.bot.sendMessage(self.id,msg,"none",learnKey)

#تمامی کیبوردها و پیام های بخش دگزسانی زبان در فهرست نخستین🛎 واولیه
class DegarsaniZaban1:
    def __init__(self,id,firstName,msg):
        self.id = id
        self.firstName = firstName
        self.msg = msg
        self.bot = pybotc.Bot("config.cfg")
        self.obj_Start = Start(id,firstName,msg)
    #در صورت زدن دکمه 📝 زبان پیام و کیبورد ⌨ این دکمه ها و پیام می آیند    
  
    #FIXME  Start.sendKeyAndMessagesUI() در حذف و یاگزین کردن   
    # در آنالیز
    def sendKeyAndMessageUI1(self):
        self.obj_Start.sendKeyAndMessagesUI()


#تمامی کیبوردها و پیام های بخش درباره ربات ℹ️ در فهرست نخستین🛎 واولیه
class DarbarehRobat1:
    def __init__(self,id,firstName,msg):
        self.id = id
        self.firstName = firstName
        self.bot = pybotc.Bot("config.cfg")
    #در صورت زدن دکمه درباره ربات ℹ️ در بخش نخستین و اولیه این دکمه ها و پیام می آیند    
    def sendKeyAndMessageDarbarehRobat1(self):
        aboutMsg =f" Greetings Dear <i> {self.firstName} </i>🌺🌸, This Bot can learn all the new and emphasized words of the book <b>'Großes Übungsbuch Wortschatz'</b>  in the context of Leitner's repetition and practice daily in the calendar structure. With the ability to remind you and choose the answer in German, it enables synonyms, English and Persian using authentic German language resources, so that full mastery of a word and word is achieved in at least one month. From your short-term memory, it will be in your long-term memory." 
        # firstHomePageKey = json.dumps({"keyboard":[[Btn().startLearning],[Btn().aboutBotNew,Btn().uILangNKeyEditNew]], "resize_keyboard": True}) 
        firstHomePageKey = Keys().firstMenu
        self.bot.sendMessage(self.id,aboutMsg,"none",firstHomePageKey)

#تمامی کیبوردها و پیام های بخش «مرور واژه های گذشته🧐» در فهرست نخستین🛎 واولیه
class MorureVazhehhayeGozashteh:
    def __init__(self,id,firstName,msg):
        self.id = id
        self.firstName = firstName
        self.bot = pybotc.Bot("config.cfg")
        self.obj_AYVK = AghazYadgiriVazhehayeKetab(id,firstName,msg)
        
        #در صورت زدن دکمه «مرور واژه های گذشته🧐» در بخش آغازین و اصلی بخش "تفکیک مرور واژه های گذشته🧐"  دکمه ها و پیام می آیند 
    def sendMVGKeyAndMessageTMVG(self):
        reviewMsg = f"Dear {self.firstName}🌺🌸, Choose vocabulary reviewing method, based on one of the options."
        # reviewKey = json.dumps({"keyboard":[[Btn().chapterNSection],[Btn().leitnerBoxParts],[Btn().weakWords],[Btn().getBack]],"resize_keyboard":True}) 
        reviewKey = Keys().revKeys
        self.bot.sendMessage(self.id,reviewMsg,"none",reviewKey)
        
        #🔎
        ###در صورت زدن دکمه «Chapter و Section» در بخش آغازین و اصلی این  دکمه ها و پیام نخستین واژه می آیند 
    def sendWordsChapterContentKeyAndMessageFirstOLdWord(self,content,chapter,word,answer,counter,length,section,page,link):
        oldWordsMsg = f".Chapter : {content}\nSection : {chapter}\n\n<b>{word}</b>\n\n{answer.center(63)}\n\n.Page :{page}                         {section}: {length}/{counter+1}{link}."
        # reviewNextKey = json.dumps({"keyboard":[[Btn().nextWordChapNS],[Btn().getBack]],"resize_keyboard":True}) 
        reviewNextKey = Keys().revChapNexKeys
        self.bot.sendMessage(self.id,oldWordsMsg,"none",reviewNextKey)

    def sendWordsChapterContentKeyAndMessageFirstOLdWordOneLength(self,content,chapter,word,answer,counter,length,section,page,link):
        oldWordsMsg = f".Chapter : {content}\nSection : {chapter}\n\n<b>{word}</b>\n\n{answer.center(63)}\n\n.Page :{page}                         {section}: {length}/{counter+1}{link}."
        # reviewNextKey = json.dumps({"keyboard":[[Btn().getBack]],"resize_keyboard":True}) 
        backToHomePage = Keys().getBackKeys
        self.bot.sendMessage(self.id,oldWordsMsg,"none",backToHomePage)




    #Chapter و Section- کیبورد حاوی قبلی و بعدی  
    def sendWordsChapterContentKeyAndMessagMiddleOLdWord(self,content,chapter,word,answer,counter,length,section,page,link):
        oldWordsMsg = f".Chapter : {content}\nSection : {chapter}\n\n<b>{word}</b>\n\n{answer.center(63)}\n\n.Page :{page}                         {section}: {length}/{counter+1}{link}."
        # reviewNextKey = json.dumps({"keyboard":[[Btn().beforeWordChapNS, Btn().nextWordChapNS],[Btn().getBack]], "resize_keyboard": True}) 
        reviewMiddleKeys = Keys().revChapMidKeys

        self.bot.sendMessage(self.id,oldWordsMsg,"none",reviewMiddleKeys)
    
    #Chapter و Section- کیبورد حاوی قبلی و آخرین واژه  
    def sendWordsChapterContentKeyAndMessagLastOLdWord(self,content,chapter,word,answer,counter,length,section,page,link):
        oldWordsMsg = f".Chapter : {content}\nSection : {chapter}\n\n<b>{word}</b>\n\n{answer.center(63)}\n\n.Page :{page}                         {section}: {length}/{counter+1}{link}."
        # reviewBeforeKey = json.dumps({"keyboard":[[Btn().beforeWordChapNS],[Btn().getBack]],"resize_keyboard":True}) 
        reviewBeforeKey = Keys().revChapBefKeys
        self.bot.sendMessage(self.id,oldWordsMsg,"none",reviewBeforeKey)


    #🔭
    ###در صورت زدن دکمه «بخش ها» در بخش آغازین و اصلی این  دکمه ها و پیام نخستین واژه می آیند 
    def sendBakhshhaKeyAndMessageFirstWord(self,counter,length,section,word,answer,page,content,chapter,link):
        oldWordsMsg = f". {section}: {length}/{counter+1}\n<b>{word}</b>\n\n{answer.center(63)}\n\n.Chapter : {content}\nSection : {chapter} \n{link}\nPage:{page}"
        # reviewNextKey = json.dumps({"keyboard":[[Btn().nextWordLeitBP],[Btn().getBack]],"resize_keyboard":True}) 
        reviewNextKey = Keys().revLeitNexKeys
        self.bot.sendMessage(self.id,oldWordsMsg,"none",reviewNextKey)
    # وقتی طول آریه یکی است
    def sendBakhshhaKeyAndMessageFirstWordOneLength(self,counter,length,section,word,answer,page,content,chapter,link):
        oldWordsMsg = f". {section}: {length}/{counter+1}\n<b>{word}</b>\n\n{answer.center(63)}\n\n.Chapter : {content}\nSection : {chapter} \n{link}\nPage:{page}"
        # reviewNextKey = json.dumps({"keyboard":[[Btn().getBack]],"resize_keyboard":True}) 
        backToHomePage = Keys().getBackKeys
        self.bot.sendMessage(self.id,oldWordsMsg,"none",backToHomePage)


        #بخش ها- کیبورد حاوی قبلی و بعدی 
    def sendBakhshhaKeyAndMessageMiddleWord(self,counter,length,section,word,answer,page,content,chapter,link):
        oldWordsMsg = f". {section}: {length}/{counter+1}\n<b>{word}</b>\n\n{answer.center(63)}\n\n.Chapter : {content}\nSection : {chapter} \n{link}\nPage:{page}"
        #اگر واژه ای بعد از این هنوز موجود باشد
        # reviewBackNextKey = json.dumps({"keyboard":[[Btn().beforeWordLeitBP,Btn().nextWordLeitBP],[Btn().getBack]],"resize_keyboard":True}) 
        reviewBackNextKey = Keys().revLeitMidKeys
        self.bot.sendMessage(self.id,oldWordsMsg,"none",reviewBackNextKey)

        #بخش ها- کیبورد حاوی قبلی  
    def sendBakhshhaKeyAndMessageLastWord(self,counter,length,section,word,answer,page,content,chapter,link):
        oldWordsMsg = f". {section}: {length}/{counter+1}\n<b>{word}</b>\n\n{answer.center(63)}\n\n.Chapter : {content}\nSection : {chapter} \n{link}\nPage:{page}"
        #اگر واژه ای بعد از این دیگر موجود نباشد
        # reviewBackKey = json.dumps({"keyboard":[[Btn().beforeWordLeitBP],[Btn().getBack]],"resize_keyboard":True}) 
        reviewBackKey = Keys().revLeitBefKeys

        self.bot.sendMessage(self.id,oldWordsMsg,"none",reviewBackKey)

    #🔬
    ###در صورت زدن دکمه «واژگان ناتوان» در بخش آغازین و اصلی این  دکمه ها و پیام نخستین واژه می آیند 
    def sendWeakWordsKeyAndMessageFirstOLdWord(self,durationDays,counter,length,section,word,answer,content,chapter,page,link):
        oldWordsMsg = f".Days Number : {durationDays}         {section}:{counter+1}/{length}.\n\n<b>{word}</b>\n\n{answer.center(63)}\n\n.Chapter : {content}\nSection : {chapter} \n{link}\nPage:{page}"
        # Page:{page}
        # {page}:Page
        # reviewNextKey = json.dumps({"keyboard":[[Btn().nextWordWW],[Btn().getBack]],"resize_keyboard":True}) 
        reviewNextKey = Keys().revWeakNexKeys
        self.bot.sendMessage(self.id,oldWordsMsg,"none",reviewNextKey)
    #اگر طول آرایه یک بود
    def sendWeakWordsKeyAndMessageFirstOLdWordOneLength(self,durationDays,counter,length,section,word,answer,content,chapter,page,link):
        oldWordsMsg = f".Days Number : {durationDays}         {section}:{counter+1}/{length}.\n\n<b>{word}</b>\n\n{answer.center(63)}\n\n.Chapter : {content}\nSection : {chapter} \n{link}\nPage:{page}"
        # Page:{page}
        # {page}:Page
        # reviewNextKey = json.dumps({"keyboard":[[Btn().getBack]],"resize_keyboard":True}) 
        backToHomePage = Keys().getBackKeys
        self.bot.sendMessage(self.id,oldWordsMsg,"none",backToHomePage)


 
    def sendWeakWordsKeyAndMessageNoWord(self):
        noWeakWordMsg = f" Dear <i>{self.firstName}</i>🌺🌸, You don't have any Weak Vocabulary!"
        # Page:{page}
        # {page}:Page
        # regularHomePageKey = json.dumps({"keyboard":[[Btn().reviewWords],[Btn().wordsNum,Btn().wayEdit,Btn().account],[Btn().timeLearnEdit,Btn().reportActivity],[Btn().deleteBot,Btn().aboutBot,Btn().uILangNKeyEdit],[Btn().opinion]],"resize_keyboard":True})
        regularHomePageKey = Keys().secondMenu
        self.bot.sendMessage(self.id,noWeakWordMsg,"none",regularHomePageKey)   

    def sendWeakWordsKeyAndMessageNoWordOtherReview(self):
        noWeakWordMsg = f"Dear <i> {self.firstName}</i>🌺🌸, you haven't done no word and exercise so far!"
        regularHomePageKey = Keys().secondMenu
        self.bot.sendMessage(self.id,noWeakWordMsg,"none",regularHomePageKey)

    #واژگان ناتوان- کیبورد حاوی قبلی و بعدی  
    def sendWeakWordsKeyAndMessagMiddleOLdWord(self,durationDays,counter,length,section,word,answer,content,chapter,page,link):
        oldWordsMsg = f".Days Number : {durationDays}         {section}:{counter+1}/{length}.\n\n<b>{word}</b>\n\n{answer.center(63)}\n\n.Chapter : {content}\nSection : {chapter} \n{link}\nPage:{page}"
        # reviewNextKey = json.dumps({"keyboard":[[Btn().beforeWordWW,Btn().nextWordWW],[Btn().getBack]],"resize_keyboard":True}) 
        reviewNextKey = Keys().revWeakMidKeys
        self.bot.sendMessage(self.id,oldWordsMsg,"none",reviewNextKey)
    #واژگان ناتوان- کیبورد حاوی قبلی و آخرین واژه  
    def sendWeakWordsKeyAndMessagLastOLdWord(self,durationDays,counter,length,section,word,answer,content,chapter,page,link):
        oldWordsMsg = f".Days Number : {durationDays}         {section}:{counter+1}/{length}.\n\n<b>{word}</b>\n\n{answer.center(63)}\n\n.Chapter : {content}\nSection : {chapter} \n{link}\nPage:{page}"
        # reviewNextKey = json.dumps({"keyboard":[[Btn().beforeWordWW],[Btn().getBack]],"resize_keyboard":True}) 
        reviewNextKey = Keys().revWeakBefKeys
        self.bot.sendMessage(self.id,oldWordsMsg,"none",reviewNextKey)







     #در صورت زدن  دکمه بازگشت به فهرست آغازین🏡 به بخش فهرست آغازین و اصلی منتقل شده و این دکمه ها و پیام می آیند 
     #FIXME حذف این تابع از کیبورد و جایگزینی در آنالیز AYVK.sendKeyAndMessageFAVA()
    def sendKeyAndMessageFAVA(self):
        self.obj_AYVK.sendKeyAndMessageFAVA()

#تمامی کیبوردها و پیام های بخش «📝 روش 🛣» آغازین و اصلی  
class VirayeshRavesh:
    def __init__(self,id,firstName,msg):
        self.id = id
        self.firstName = firstName
        self.msg = msg
        self.obj_AYVK = AghazYadgiriVazhehayeKetab(id,firstName,msg)
        self.bot = pybotc.Bot("config.cfg")    

    #در صورت زدن دکمه «📝 روش 🛣»  این  دکمه ها و پیام می آیند
    def send357KeyAndMessageDESP(self):
        waysMsg = f"Dear {self.firstName}  🌺🌸, Choose the Method to Learn Book Words."
        # wayKey = json.dumps({"keyboard":[[BtnS().deutsch,BtnS().english],[BtnS().synonym,BtnS().persian],[Btn().getBack]],"resize_keyboard":True})
        wayKey = Keys().ways  

        self.bot.sendMessage(self.id,waysMsg,"none",wayKey)
        



     #    یا پارسی  این دکمه ها و پیام می آیند  deutsch , english , synonym  در صورت زدن یکی از دکمه های  
    def sendDESPAllKeyAndMessageYesNo(self,way): 
        waysWarningMsg = f"Dear {self.firstName} 🌺🌸, Are you sure you want to select the new <b> {self.msg} </b> method, because if you select, your Previous record <b> {way} </b> for worked words will be deleted?"
        # yesNoKey = json.dumps({"keyboard":[[Btn().noDot,Btn().yesDot]],"resize_keyboard":True}) 
        yesNoKey = Keys().yNDot
        self.bot.sendMessage(self.id,waysWarningMsg,"none",yesNoKey)


   #    یا پارسی و یکسان بودن با روش قبلی این دکمه ها و پیام می آیند  deutsch , english , synonym  در صورت زدن یکی از دکمه های  
    def sendDESPAllSameKeyAndMessageFAVA(self): 
        waysWarningMsg = f"Your method is <b> {self.msg} </b> right now, No need to change." 
        # regularHomePageKey = json.dumps({"keyboard":[[Btn().reviewWords],[Btn().wordsNum,Btn().wayEdit,Btn().account],[Btn().timeLearnEdit,Btn().reportActivity],[Btn().deleteBot,Btn().aboutBot,Btn().uILangNKeyEdit],[Btn().opinion]],"resize_keyboard":True})
        regularHomePageKey = Keys().secondMenu
        self.bot.sendMessage(self.id,waysWarningMsg,"none",regularHomePageKey)

    #در صورت زدن دکمه «Yes» به فهرست آغازین و اصلی منتقل شده و این  دکمه ها و پیام می آیند 
    def sendBaleKeyAndMessageFAVA(self): 
        waysChangedMsg = f"Method in <b>{self.msg}</b> Edited."
        # regularHomePageKey = json.dumps({"keyboard":[[Btn().reviewWords],[Btn().wordsNum,Btn().wayEdit,Btn().account],[Btn().timeLearnEdit,Btn().reportActivity],[Btn().deleteBot,Btn().aboutBot,Btn().uILangNKeyEdit],[Btn().opinion]],"resize_keyboard":True})
        regularHomePageKey = Keys().secondMenu
        self.bot.sendMessage(self.id,waysChangedMsg,"none",regularHomePageKey)

   #در صورت زدن دکمه «No» به فهرست آغازین و اصلی منتقل شده و این  دکمه ها و پیام می آیند 
    #FIXME حذف این تابع از کیبورد و جایگزینی در آنالیز AYVK.sendKeyAndMessageFAVA()   
    def sendKheyrKeyAndMessageFAVA(self):
        self.obj_AYVK.sendKeyAndMessageFAVA()

    def wayMenu(self,way):
        keys = SKeys(Btn(),MNV()).removeKeyboard
        msg = Btn().wayEdit
        keys2 = SKeys(Btn(),MNV()).wayKeys(way)
        msg2 = MNV(self.firstName).pickOptionTxt()
        # msg2 = f"گزینه دلخواهت  {self.firstName} عزیز 🌺🌸 را انتخاب کن."
        parse_mode="HTML"
        # self.bot.editMessage(self.id,self.msgId,msgEdit,parse_mode,keys)
        self.bot.sendMessage(self.id,msg,parse_mode,keys)
        self.bot.sendMessage(self.id,msg2,parse_mode,keys2)    

#تمامی کیبوردها و پیام های بخش «ویرایش شمار واژگان آغازین و اصلی»  
class VirayeshShomarVazheha:
    def __init__(self,id,firstName,msg):
        self.id = id
        self.firstName = firstName
        self.msg = msg
        self.bot = pybotc.Bot("config.cfg")   
    #در صورت زدن دکمه «📝 شمار  واژه ها 🔢» این  دکمه ها و پیام می آیند 
    def sendVShVMessage357(self):
        wortZahlMsg = f" Dear {self.firstName} 🌺🌸, how many new words do you want in a day?"        
        # wortZahlKey = json.dumps({"keyboard":[[BtnS().three],[BtnS().two],[BtnS().one],[Btn().getBack]],"resize_keyboard":True})
        wortZahlKey = Keys().numWords
        self.bot.sendMessage(self.id,wortZahlMsg,"none",wortZahlKey)
    #در صورت زدن دکمه «۳» یا «۵» یا «۷»این  دکمه ها و پیام می آیند 
    def send357AllVMessageFAVA(self):
        changedWordNum = f"The number of new words changed to <b>{self.msg}</b>."
        # regularHomePageKey = json.dumps({"keyboard":[[Btn().reviewWords],[Btn().wordsNum,Btn().wayEdit,Btn().account],[Btn().timeLearnEdit,Btn().reportActivity],[Btn().deleteBot,Btn().aboutBot,Btn().uILangNKeyEdit],[Btn().opinion]],"resize_keyboard":True})
        regularHomePageKey = Keys().secondMenu
        self.bot.sendMessage(self.id,changedWordNum,"none",regularHomePageKey)

#تمامی کیبوردها و پیام های بخش «📝زمان یادگیری روزانه⏳» آغازین و اصلی
class VireyeshZamanYadgiriRuzaneh:
    def __init__(self,id,firstName,msg=None):
        self.id = id
        self.firstName = firstName
        self.msg = msg
        self.bot = pybotc.Bot("config.cfg")   
        self.obj_AYVK = AghazYadgiriVazhehayeKetab(id,firstName,msg)

    #در صورت زدن دکمه «📝زمان یادگیری روزانه⏳» این  دکمه ها و پیام می آیند 
    def sendVZYRVMessage1_23(self):
        timeLearningMsg = f"Dear {self.firstName} 🌺🌸, Choose your daily learning start time to visit the Bot."
        # hoursKey = json.dumps({"keyboard":[[BtnS().clock1,BtnS().clock2,BtnS().clock3,BtnS().clock4,BtnS().clock5,BtnS().clock6,BtnS().clock7,BtnS().clock8],[BtnS().clock9,BtnS().clock10,BtnS().clock11,BtnS().clock12,BtnS().clock13,BtnS().clock14,BtnS().clock15,BtnS().clock16],[BtnS().clock17,BtnS().clock18,BtnS().clock19,BtnS().clock20,BtnS().clock21,BtnS().clock22,BtnS().clock23],[Btn().getBack]],"resize_keyboard":True}) 
        hoursKey = Keys().hKeys
        self.bot.sendMessage(self.id,timeLearningMsg,"none",hoursKey)
    #در صورت زدن دکمه «۱..۲۳» این  دکمه ها و پیام می آیند 
    def send1_23MessageYesNo(self,year,monthAlpha,day,weekDay,hourMin,askedYear,askedMonthAlpha,askedDay,askedWeekDay,askedHourMin):
        dash = "___________________________________"
        timeLearningWarningMsg = f"Dear {self.firstName} 🌺🌸, Are you confident to change time of 👉Learn Vocabulary Daily👈 to {self.msg} on {askedWeekDay} {askedDay} {askedMonthAlpha} {askedYear}? \n {dash} \n Currently 👉Learn Vocabulary Daily👈 next on {weekDay} {day} {monthAlpha} {year}, <b> At {hourMin} </b>. \n @DeutschOhal"
        

        # yesNoKey = json.dumps({"keyboard":[[Btn().noDash,Btn().yesDash]],"resize_keyboard":True}) 
        yesNoKey = Keys().yNDash
        self.bot.sendMessage(self.id,timeLearningWarningMsg,"none",yesNoKey)


    #در صورت همسان بودن زمان یادگیری روزانه با قبلی  این  دکمه ها و پیام می آیند 
    def sendYesMessageSameFAVA(self,year,monthAlpha,day,weekDay,hourMin):
        dash = "___________________________________"
        # "روش شما در همین هنگام هم  {} هست نیازی تغییر و دگرسانی نیست".format(self.msg)

        timeLearningChangedMsg = f"Your daily learning time is at the same time {self.msg} There is no need to change \n {dash} \n 👉Learn Vocabulary Daily👈 next on <b>  {weekDay} {monthAlpha}{day},</b>   {year}  <b> At <b> {hourMin} </b> \n @DeutschOhal"
        # regularHomePageKey = json.dumps({"keyboard":[[Btn().reviewWords],[Btn().wordsNum,Btn().wayEdit,Btn().account],[Btn().timeLearnEdit,Btn().reportActivity],[Btn().deleteBot,Btn().aboutBot,Btn().uILangNKeyEdit],[Btn().opinion]],"resize_keyboard":True})
        regularHomePageKey = Keys().secondMenu
        self.bot.sendMessage(self.id,timeLearningChangedMsg,"none",regularHomePageKey)


    #در صورت زدن دکمه «Yes» این  دکمه ها و پیام می آیند 
    def sendYesMessageFAVA(self,year,monthAlpha,day,weekDay,hourMin):
        dash = "___________________________________"
        timeLearningChangedMsg = f"Daily Learning Hour changed to <b>{hourMin} </b>. \n{dash} \n👉Learn Vocabulary Daily👈 Next on {weekDay} {day} {monthAlpha} {year}, <b > At {hourMin} </b> \n @DeutschOhal"
        # regularHomePageKey = json.dumps({"keyboard":[[Btn().reviewWords],[Btn().wordsNum,Btn().wayEdit,Btn().account],[Btn().timeLearnEdit,Btn().reportActivity],[Btn().deleteBot,Btn().aboutBot,Btn().uILangNKeyEdit],[Btn().opinion]],"resize_keyboard":True})
        regularHomePageKey = Keys().secondMenu
        self.bot.sendMessage(self.id,timeLearningChangedMsg,"none",regularHomePageKey)

    #در صورت زدن دکمه «نه» به فهرست آغازین و اصلی این  دکمه ها و پیام می آیند 
    #FIXME حذف این تابع از کیبورد و جایگزینی در آنالیز AYVK.sendKeyAndMessageFAVA()
    def sendNoMessageFAVA(self):
        self.obj_AYVK.sendKeyAndMessageFAVA()
        
#تمامی کیبوردها و پیام های بخش «برایند و فرجام»  در فهرست آغازین و اصلی
class BarayandVaFarjam:
    def __init__(self,id,firstName,msg):
        self.id = id
        self.firstName = firstName
        self.msg = msg
        self.bot = pybotc.Bot("config.cfg")
        self.obj_AYVK = AghazYadgiriVazhehayeKetab(id,firstName,msg)
    #در صورت زدن دکمه «برایند و فرجام»  این  دکمه ها و پیام می آیند 
    def sendBVFMessageReports(self):
        reportPageMsg = f"selected { self.msg }."
        # reportKey = json.dumps({"keyboard":[[Btn().reportWordsPartions, Btn().reportWeakWords],[Btn().getBack]], "resize_keyboard": True})
        reportKey = Keys().reportKeys
        self.bot.sendMessage(self.id,reportPageMsg,"none",reportKey)

    #در صورت زدن دکمه «گزارش واژگان در بخش ها📈»  این  دکمه ها و پیام می آیند 
    def sendReportAllWordsMessageBBFA(self,num,reportWordsSectionsPercentage):
        num = f"<b>{num}</b>"
        dash = "___________________________________" 
        reportWordsSectionsMsg = f"Dear {self.firstName} 🌺🌸, Report all your used vocabulary in the partitions, to date: \n {dash} \n \n Number of all vocabulary done to date: {num} \n {dash} \n  Number And the percentage of all words in all partitions of the Leitner box: \n \n {reportWordsSectionsPercentage} \n \n @DeutschOhal"
        # backToHomePageKey = json.dumps({"keyboard":[[Btn().getBack]],"resize_keyboard":True})
        backToHomePage = Keys().getBackKeys
        self.bot.sendMessage(self.id,reportWordsSectionsMsg,"none",backToHomePage)
    #در صورت زدن دکمه «گزارش ناتوانی در واژگان📉»  این  دکمه ها و پیام می آیند 
    # wWDS,wWPGS
    def sendReportWeakWordMessageBBFA(self,wWDS,wWPGS):
        dash = "___________________________________"
        reportWordsSectionsMsg = f"Dear {self.firstName} 🌺🌸, Report the most Weak Vocabulary in learning to date \n (weak  vocabulary means words that have not yet been completed learning for more than a month) \n  {dash} \n A list of vocabulary that has lasted more than a month with the number of days and partition \n\n  <b> {wWDS.center(63)} </b> \n  {dash} \n  Incorrect vocabulary list Percentage order in Leitner box partitions \n\n  {wWPGS} \n  @DeutschOhal "
        # backToHomePageKey = json.dumps({"keyboard":[[Btn().getBack]],"resize_keyboard":True})
        backToHomePage = Keys().getBackKeys
        self.bot.sendMessage(self.id,reportWordsSectionsMsg,"none",backToHomePage)

    #در صورت زدن دکمه «بازگشت به فهرست آغازین🏡»  این  دکمه ها و پیام می آیند 
#FIXME حذف این تابع از کیبورد و جایگزینی در آنالیز AYVK.sendKeyAndMessageFAVA()
    def sendBBFAMessageFAVA(self):
        self.obj_AYVK.sendKeyAndMessageFAVA()

    def reportWeakWords(self,wWDS,wWPGS): 
        dash = "___________________________________"   
        reportMsg = f"\n Dear {self.firstName}🌺🌸, to date, Report the most Weak Vocabulary in learning, \n  {dash.center(73)} \n\n  List of vocabulary that has lasted over a month of learning, expressing the number of days \n\n  {wWDS} \n  {dash.center(73)} \n\n  Weak Vocabulary in order of percentage of each partition of the Leitner box \n\n  {wWPGS} \n  @DeutschOhal"
        # reportKey = json.dumps({"keyboard":[[Btn().getBack]],"resize_keyboard":True})
        backToHomePage = Keys().getBackKeys
        self.bot.sendMessage(self.id,reportMsg,"none",backToHomePage)

#تمامی کیبوردها و پیام های بخش «📝 زبان پیام و کیبورد ⌨  پوسته» در فهرست آغازین و اصلی  
class DegarsaniZaban2:
    def __init__(self,id,firstName,msg):
        self.id = id
        self.firstName = firstName
        self.msg = msg
        self.bot = pybotc.Bot("config.cfg")
        self.obj_Start = Start(id,firstName,msg)
    #در صورت زدن دکمه 📝 زبان پیام و کیبورد ⌨ این دکمه ها و پیام می آیند    
    def sendKeyAndMessageUI2(self):
         languageMsg = f"Dear {self.firstName} 🌺🌸, select your favorite language for bots message and keyboard"
         
        #  languagesKey = json.dumps({"keyboard":[[BtnS().keyNMsgDe],[BtnS().keyNMsgEn],[BtnS().keyNMsgPer],[Btn().getBack]],"resize_keyboard":True}) 
         languagesKey = Keys().lanKeys
         self.bot.sendMessage(self.id,languageMsg,"none",languagesKey)
    
        #در صورت انتخاب و زدن <پوسته فارسی> به فهرست آغازین و اصلی منتقل شده و این  دکمه ها و پیام می آیند 
    def sendBaleKeyAndMessageFAVA(self): 
        languageSelectedMsg = f"Dear {self.firstName} 🌺🌸, select your favorite language for bots message and keyboard"
        # regularHomePageKey = json.dumps({"keyboard":[[Btn().reviewWords],[Btn().wordsNum,Btn().wayEdit,Btn().account],[Btn().timeLearnEdit,Btn().reportActivity],[Btn().deleteBot,Btn().aboutBot,Btn().uILangNKeyEdit],[Btn().opinion]],"resize_keyboard":True})
        regularHomePageKey = Keys().secondMenu
        self.bot.sendMessage(self.id,languageSelectedMsg,"none",regularHomePageKey)




        # self.obj_Start.sendKeyAndMessagesUI()
    #    یا کیبورد و پیام پارسی⌨💬 این دکمه ها و پیام از فهرست آغازین و اصلی  می آیند  deutsch Menu, english Menu  در صورت زدن یکی از دکمه های  
    def sendKeyAndMessageFNVA2(self):
        languageSelectedMsg = f"{self.msg} is chosen for bot."
        # regularHomePageKey = json.dumps({"keyboard":[[Btn().reviewWords],[Btn().wordsNum,Btn().wayEdit,Btn().account],[Btn().timeLearnEdit,Btn().reportActivity],[Btn().deleteBot,Btn().aboutBot,Btn().uILangNKeyEdit],[Btn().opinion]],"resize_keyboard":True})
        regularHomePageKey = Keys().secondMenu
        self.bot.sendMessage(self.id,languageSelectedMsg,"none",regularHomePageKey)



#تمامی کیبوردها و پیام های بخش درباره ربات ℹ️ در فهرست آعازین واصلی
class DarbarehRobat2:
    def __init__(self,id,firstName,msg):
        self.id = id
        self.firstName = firstName
        self.msg = msg
        self.bot = pybotc.Bot("config.cfg")
    #در صورت زدن دکمه درباره ربات ℹ️ در بخش آعازین واصلی این دکمه ها و پیام می آیند    
    def sendKeyAndMessageDarbarehRobat2(self):
        aboutMsg =f" Greetings Dear <i> {self.firstName} </i>🌺🌸, \n This Bot can learn all the new and emphasized words of the book <b>'Großes Übungsbuch Wortschatz'</b>  in the context of Leitner's repetition and practice daily in the calendar structure. With the ability to remind you and choose the answer in German, it enables synonyms, English and Persian using authentic German language resources, so that full mastery of a word and word is achieved in at least one month. From your short-term memory, it will be in your long-term memory." 
        # regularHomePageKey = json.dumps({"keyboard":[[Btn().reviewWords],[Btn().wordsNum,Btn().wayEdit,Btn().account],[Btn().timeLearnEdit,Btn().reportActivity],[Btn().deleteBot,Btn().aboutBot,Btn().uILangNKeyEdit],[Btn().opinion]],"resize_keyboard":True})
        regularHomePageKey = Keys().secondMenu
        self.bot.sendMessage(self.id,aboutMsg,"none",regularHomePageKey)

#FIXME copy these 4 method to every user language
    def sendKeyAndMessageSendingSugession(self):
        aboutMsg =f"Dear <i>{self.firstName}</i>🌺🌸, Any comments, criticisms or suggestions you have, please send them to us."
        # regularHomePageKey = json.dumps({"keyboard":[[Btn().getBack]],"resize_keyboard":True})
        backToHomePage = Keys().getBackKeys
        self.bot.sendMessage(self.id,aboutMsg,"none",backToHomePage)

    def sendKeyAndMessageDeliverOpinion(self,opId):
        aboutMsg =f"Dear <i>{self.firstName}</i>🌺🌸,Your comment was registered,  with this <b>{opId}</b> tracking number."
        # regularHomePageKey = json.dumps({"keyboard":[[Btn().reviewWords],[Btn().wordsNum,Btn().wayEdit,Btn().account],[Btn().timeLearnEdit,Btn().reportActivity],[Btn().deleteBot,Btn().aboutBot,Btn().uILangNKeyEdit],[Btn().opinion]],"resize_keyboard":True})
        regularHomePageKey = Keys().secondMenu
        self.bot.sendMessage(self.id,aboutMsg,"none",regularHomePageKey)

    def sendKeyAndMessageUsingBotKeys(self):
        aboutMsg =f"No text entered! If you want to send a comment, <b>without using the Bot keyboard</b>, enter the text and then send it."
        # regularHomePageKey = json.dumps({"keyboard":[[Btn().reviewWords],[Btn().wordsNum,Btn().wayEdit,Btn().account],[Btn().timeLearnEdit,Btn().reportActivity],[Btn().deleteBot,Btn().aboutBot,Btn().uILangNKeyEdit],[Btn().opinion]],"resize_keyboard":True})
        regularHomePageKey = Keys().secondMenu
        self.bot.sendMessage(self.id,aboutMsg,"none",regularHomePageKey)

    def sendKeyAndMessageOutOfRangeMsg(self):
        aboutMsg =f"The number of characters and words sent is too much! Send your text shorter or in several sections."
        # regularHomePageKey = json.dumps({"keyboard":[[Btn().reviewWords],[Btn().wordsNum,Btn().wayEdit,Btn().account],[Btn().timeLearnEdit,Btn().reportActivity],[Btn().deleteBot,Btn().aboutBot,Btn().uILangNKeyEdit],[Btn().opinion]],"resize_keyboard":True})
        regularHomePageKey = Keys().secondMenu
        self.bot.sendMessage(self.id,aboutMsg,"none",regularHomePageKey)


#تمامی کیبوردها و پیام های بخش «Remove bot 🗑» در فهرست آعازین واصلی
class Hazfbot:
    def __init__(self,id,firstName,msg):
        self.id = id
        self.firstName = firstName
        self.bot = pybotc.Bot("config.cfg")   
        self.obj_AYVK = AghazYadgiriVazhehayeKetab(id,firstName,msg)

    #    self.Hazfbot(id,firstName,msg).sendHRKeyAndMessageYesNo()

    #در صورت زدن دکمه «Remove bot 🗑»  این دکمه ها و پیام می آیند    
    def sendHRKeyAndMessageYesNo(self):
        deleteBotWarnMsg = f"Dear {self.firstName} 🌺🌸, are you sure to deleting bot? cause by that all of your records will be deleted as well, beside no more message sending to you."
        # yesNoKey = json.dumps({"keyboard":[[Btn().no,Btn().yesDelete]],"resize_keyboard":True}) 
        yesNoKey = Keys().yNKeys
        self.bot.sendMessage(self.id,deleteBotWarnMsg,"none",yesNoKey)
    #در صورت زدن دکمه «Yes» به بخش فهرست نخستین🛎 و اولیه منتقل شده و   این دکمه ها و پیام می آیند    
    def sendYesKeyAndMessageFNVA(self):
        deleteBotMsg = "Bot is deleted!"
        # firstHomePageKey = json.dumps({"keyboard":[[Btn().startLearning],[Btn().aboutBotNew,Btn().uILangNKeyEditNew]], "resize_keyboard": True}) 
        firstHomePageKey = Keys().firstMenu
        self.bot.sendMessage(self.id,deleteBotMsg,"none",firstHomePageKey)

    #در صورت زدن دکمه «No» به بخش فهرست آغازین و اصلی منتقل شده و   این دکمه ها و پیام می آیند    
    #FIXME حذف این تابع از کیبورد و جایگزینی در آنالیز AYVK.sendKeyAndMessageFAVA()
    def sendNoKeyAndMessageFAVA(self):
        self.obj_AYVK.sendKeyAndMessageFAVA()

#تمامی کیبوردها و پیام های بخش «یادگیری واژگان روزانه» 
class YadgiriVazheganRuzaneh:
    def __init__(self,id,firstName,msg):
        self.id = id
        self.firstName = firstName
        self.msg = msg
        self.obj_AYVK = AghazYadgiriVazhehayeKetab(id,firstName,msg)
        self.bot = pybotc.Bot("config.cfg")





###################################################admin ادمین و سرپرست#########################################
###################################################admin ادمین و سرپرست#########################################
class AdminInline:
    def __init__(self,id,first_name,msgId=None):
        self.id = id
        self.msgId = msgId
        self.firstName = first_name
        self.bot = pybotc.Bot("config.cfg")
        # self.obj_dbContatct = dbContact()

      #######BETWEEN#########
    def dataWord(self,way,newWordsMsg,msgKey):
        parse_mode = "HTML"
        self.bot.sendMessage(self.id,msgKey,parse_mode,Keys().getBackKeys)       
        antwortKey = SKeys(Btn(),MNV()).wordKeys(way)
        self.bot.sendMessage(self.id,newWordsMsg,parse_mode,antwortKey)

    def dataWordWithGuide(self,way,newWordsMsg,msgKey):
        antwortKey = SKeys(Btn(),MNV()).wordKeys(way)
        parse_mode = "HTML"     
        self.bot.sendMessage(self.id,msgKey,parse_mode,Keys().getBackKeys)
        self.bot.sendMessage(self.id,newWordsMsg,parse_mode,antwortKey)




      #######BETWEEN#########
    def dataWordQuery(self,way,newWordsMsg):
        # print(way)
        antwortKey = SKeys(Btn(),MNV()).wordKeys(way)
        parse_mode = "HTML"
        self.bot.editMessage(self.id,self.msgId,newWordsMsg,parse_mode,antwortKey)

    def dataWordWithGuideQuery(self,way,newWordsMsg):
        # print(way)
        antwortKey = SKeys(Btn(),MNV()).wordKeys(way)
        parse_mode = "HTML"
        self.bot.editMessage(self.id,self.msgId,newWordsMsg,parse_mode,antwortKey)

    def answerWord(self,data,way,newWordsMsg):
               #63 blank space
        # answerInTopOfCard = MNV().answerInTopOfCard(data,icon)
        # newWordsMsg = f"<b>{answerInTopOfCard}</b>\n{answerLink} {standardizedAnswer.center(63)}."
        rWAKey = SKeys(Btn(),MNV()).answerKeys(data,way,Btn().word)
        parse_mode = "HTML"
        self.bot.editMessage(self.id,self.msgId,newWordsMsg,parse_mode,rWAKey)
        # self.bot.sendMessage(self.id,newWordsMsg,parse_mode,rWAKey)
    
    def answerWordWithGuide(self,data,way,newWordsMsg):

        rWAKey = SKeys(Btn(),MNV()).answerKeys(data,way,Btn().word)
        parse_mode = "HTML"
        self.bot.editMessage(self.id,self.msgId,newWordsMsg,parse_mode,rWAKey)
        # self.bot.sendMessage(self.id,newWordsMsg,parse_mode,rWAKey)

    def report(self,daliyReport):
        backToHomePage = ""
        parse_mode = "HTML"
        self.bot.editMessage(self.id,self.msgId,daliyReport,parse_mode,backToHomePage)
    #TODO sendVideoReport(self,pathNFile)
    def sendVideoReport(self,pathNFile):
        caption = Txt.PublicMsgNVar().gudwbot
        video ={'document': open(pathNFile,"rb")}
        self.bot.sendDocument(self.id,video,caption)

        #####review#####   
    def reviewOne(self,waysRevTypeCB,ways,length,wordDetails,msg):
        keys = SKeys(Btn(),MNV()).reviewOne(waysRevTypeCB,ways,length,Btn().getBack,MNV().endReview)
        parse_mode = "HTML"
        reviewBtns = [Btn().chapterNSection,Btn().leitnerBoxParts,Btn().weakWords]
        wordBCs = [BtnS().wordChapNSCB,BtnS().wordLeitBPCB,BtnS().wordWWCB]
        removeKeys = SKeys(Btn(),MNV()).removeKeyboard
        if msg  not in wordBCs and msg in reviewBtns:
            self.bot.sendMessage(self.id,msg,parse_mode,removeKeys)
            self.bot.sendMessage(self.id,wordDetails,parse_mode,keys)
        else:
            self.bot.editMessage(self.id,self.msgId,wordDetails,parse_mode,keys)

        #msg is self.msg and msgkey is messeage which must show for word details
    def reviewMoreThanOne(self,counter,waysRevTypeCB,ways,length,wordDetails,msg):
        keys = SKeys(Btn(),MNV()).reviewMoreThanOne(counter,waysRevTypeCB,ways,length,msg)
        parse_mode = "HTML"
        reviewBtns = [Btn().chapterNSection,Btn().leitnerBoxParts,Btn().weakWords]
        wordBCs = [BtnS().wordChapNSCB,BtnS().wordLeitBPCB,BtnS().wordWWCB]
        removeKeys = SKeys(Btn(),MNV()).removeKeyboard
        if msg  not in wordBCs and msg in reviewBtns:
            self.bot.sendMessage(self.id,msg,parse_mode,removeKeys)
            self.bot.sendMessage(self.id,wordDetails,parse_mode,keys)
        else:
            self.bot.editMessage(self.id,self.msgId,wordDetails,parse_mode,keys)

        #msg is self.msg and msgkey is messeage which must show for word details
    def reviewAnswer(self,reviewsKeysCB,data,ways,counter,length,answer,wordType):
        keys = SKeys(Btn(),MNV()).reviewAnswer(reviewsKeysCB,ways,counter,length,data,wordType)
        # keys = ''
        parse_mode = "HTML"
        self.bot.editMessage(self.id,self.msgId,answer,parse_mode,keys)

    def getBack(self,msgEdit):
        keys = ""
        # msgEdit = Btn().endReview
        parse_mode="HTML"
        keysSend = AKeys().secondMenu
        msgSend = Btn().getBack
        self.bot.editMessage(self.id,self.msgId,msgEdit,parse_mode,keys)
        self.bot.sendMessage(self.id,msgSend,parse_mode,keysSend)
      #######way####  
    def addWay(self,way):
        msg = MNV(self.firstName).addWayBeforeTxt()
        keys = SKeys(Btn(),MNV()).addWayKeys(way)
        parse_mode="HTML"
        self.bot.editMessage(self.id,self.msgId,msg,parse_mode,keys)

    def addedWayBefore(self,way):
        keys = ""
        msgEdit = MNV(self.firstName).addedWaytxt(way)
        keySend = Keys().secondMenu
        msgSend = MNV(self.firstName).secondMenu
        parse_mode="HTML"
        self.bot.editMessage(self.id,self.msgId,msgEdit,parse_mode,keys)
        self.bot.sendMessage(self.id,msgSend,parse_mode,keySend)

    def subtractWay(self,way):
        msg = MNV(self.firstName).subtractWayTxt()
        keys = SKeys(Btn(),MNV()).subtractWayKeys(way)
        parse_mode="HTML"
        self.bot.editMessage(self.id,self.msgId,msg,parse_mode,keys)

    def subtractedWayBefre(self,way):
        # msg = ""
        keys = ""
        msgEdit = MNV(self.firstName).subtractedWayBeforeTxt(way)
        parse_mode="HTML"
        keySend = Keys().secondMenu
        msgSend = MNV(self.firstName).secondMenu
        self.bot.editMessage(self.id,self.msgId,msgEdit,parse_mode,keys)
        self.bot.sendMessage(self.id,msgSend,parse_mode,keySend)

    def changeWayBefore(self,way):
        parse_mode="HTML"
        # getBack = [{'text': PerBtn().getBack,'callback_data':MNVPer().secondMenu}]
        keys = SKeys(Btn(),MNV()).changeWayKeys(way,Btn().getBack,MNV().secondMenu)
        # keys = ""
        msgEdit = MNV(self.firstName).changeWayBeforeTxt(way)
        self.bot.editMessage(self.id,self.msgId,msgEdit,parse_mode,keys)

    def changeWay(self,add,subtract):
        parse_mode="HTML"
        keys = ""
        # keys = ""
        msgEdit = MNV(self.firstName).changeWayTxt(add,subtract)
        self.bot.editMessage(self.id,self.msgId,msgEdit,parse_mode,keys)
        keySend = Keys().secondMenu
        msgSend = MNV(self.firstName).secondMenu
        self.bot.sendMessage(self.id,msgSend,parse_mode,keySend)

#تمامی کیبوردها و پیام های بخش «گردانش ⚙️» 

class AdminGardanesh:
    def __init__(self,id,firstName,msg):
        self.id = id
        self.firstName = firstName
        self.msg = msg
        self.bot = pybotc.Bot("config.cfg")
   # AdminGardanesh().adminSendGTFaraMessageGPanel
    #در صورت زدن دکمه «گردانش ⚙️»  این دکمه ها و پیام می آیند   
    def adminSendGMessageGPanell(self):
        enterPanelMsg = "Admin Desktop⚙️"
        # adminDesktop = json.dumps({"keyboard":[[BtnA().changeUserType, BtnA().sendToAll, BtnA().reportToday, BtnA().reportAll],[BtnA().apply],[Btn().getBack]] , "resize_keyboard": True})  
        adminDesktop = AKeys().adminKeys
        self.bot.sendMessage(self.id,enterPanelMsg,"none",adminDesktop)

    def adminSendGMessageGPanellAppleyChanges(self,outputAll):
        enterPanelMsg = f"{outputAll} Translation and actions, tasks and operations completed."
        # adminDesktop = json.dumps({"keyboard":[[BtnA().changeUserType, BtnA().sendToAll, BtnA().reportToday, BtnA().reportAll],[BtnA().apply],[Btn().getBack]] , "resize_keyboard": True}) 
        adminDesktop = AKeys().adminKeys
        self.bot.sendMessage(self.id,enterPanelMsg,"none",adminDesktop)


     #در صورت زدن دکمه «گزارش تکاپو فراگیر»  این دکمه ها و پیام می آیند  
    def adminSendGTFaraMessageGPanel(self,guestsNum,usersNum,guestInfos,userInfos,monthAlpha,year,day,weekDay):
        dash = "___________________________________" 
        fileW = open("TFaraMessageGPanel.txt", "w",encoding='utf-8') 
        data = f"\n\n <b> User data: \n </b> {userInfos} \n {dash} \n <b> Guest data: \n </b> {guestInfos} \n {dash}"
        # data = f"\n      {userInfos}\n {dash}\n   {guestInfos} \n {dash}"
        # data = f"{userInfos} \n{dash}\n {guestInfos}"
        fileW.write(data) 
        fileW.close() 
        file = open("TFaraMessageGPanel.txt", "rb")
        openedfile ={'document': file}
        dateGri = datetime.datetime.today().date().strftime("%Y-(%B %m)-%d")
        all = guestsNum + usersNum
        reportAllActionMsg = f"  \n\nNumber of users: {usersNum} \nNumber of guests: {guestsNum} \nNumber of people active: {all} \n {dash} \nToday: {weekDay} {day} {monthAlpha} {year} \n {dateGri}     "

        self.bot.sendDocument(self.id,openedfile,reportAllActionMsg,disable_notification=True)
        file.close()
        if os.path.exists("TFaraMessageGPanel.txt"):
            os.remove("TFaraMessageGPanel.txt")
        else:
            print("The file does not exist") 
    
    def adminOpinionsTypes(self):
        enterPanelMsg = "all type of Suggestions Report"
        opKeys = AKeys().opinionKeys
        self.bot.sendMessage(self.id,enterPanelMsg,"none",opKeys)
        
     #در صورت زدن دکمه «گزارش تکاپو فراگیر»  این دکمه ها و پیام می آیند  
    def adminSendAllOpinionUserBase(self,opinions,opinionsNum,suguestersNum,weekDay,day,monthAlpha,year):
        dash = "___________________________________" 
        fileW = open("AllOpinionUserBase.txt", "w",encoding='utf-8') 
        # data = f"\n\n <b> User data: \n </b> {userInfos} \n {dash} \n <b> Guest data: \n </b> {guestInfos} \n {dash}"
        fileW.write(opinions) 
        fileW.close() 
        file = open("AllOpinionUserBase.txt", "rb")
        openedfile ={'document': file}
        dateGri = datetime.datetime.today().date().strftime("%Y-(%B %m)-%d")
        reportAllActionMsg = f"  \nNumber of Opinions : {opinionsNum}\nNumber of users who send Opinions: {suguestersNum} \n {dash} \nToday: {weekDay} {day} {monthAlpha} {year} \n {dateGri}"
        self.bot.sendDocument(self.id,openedfile,reportAllActionMsg,disable_notification=True)
        file.close()
        if os.path.exists("AllOpinionUserBase.txt"):
            os.remove("AllOpinionUserBase.txt")
        else:
            print("The file does not exist") 


     #در صورت زدن دکمه «گزارش تکاپو امروز»  این دکمه ها و پیام می آیند   
    def adminSendGTEmruzMessageGPanel(self,todayActiveUsersNum,todayActiveGuestsNum,activeUsersInfos,activeGuestsInfo,numTodayAllTransactions,monthAlpha,year,day,weekDay):
        dash = "___________________________________" 
        dateGri = datetime.datetime.today().date().strftime("%Y-(%B %m)-%d")
        all = todayActiveUsersNum + todayActiveGuestsNum
        reportAllActionMsg = f"\n\n Names and IDs of today: \n {activeUsersInfos} \n {dash} \n Names and IDs of today's guest: \n {activeGuestsInfo} \n {dash} \n Today's active users : <b> {todayActiveUsersNum} </b> \n Today's active guests today: <b> {todayActiveGuestsNum} </b> \n Today's total actors today: <b> {all} </b> \n {dash } \n Today transactions: <b> {numTodayAllTransactions} </b> \n {dash} \n Today: <b> {weekDay} {day} {monthAlpha} {year} \n {dateGri} </b>"
        # adminDesktop = json.dumps({"keyboard":[[BtnA().changeUserType, BtnA().sendToAll, BtnA().reportToday, BtnA().reportAll],[BtnA().apply],[Btn().getBack]] , "resize_keyboard": True}) 
        adminDesktop = AKeys().adminKeys
        # "دگرسانی گونه کاربر","پیام به همه","گزارش تکاپو امروز","گزارش تکاپو فراگیر","ورزانش و اعمال"
        self.bot.sendMessage(self.id,reportAllActionMsg,"none",adminDesktop)

     #در صورت زدن دکمه «پیام به همه»  این دکمه ها و پیام می آیند   
    def adminSendPBHMessageBBMSVA(self):
        adminMessageToAllEnterMsg = "Enter the message you want to send to all users!"
        # adminSendingKey = json.dumps({"keyboard":[[BtnA().getBackToDesk]],"resize_keyboard":True})
        adminSendingKey = AKeys().getBackDesk
        self.bot.sendMessage(self.id,adminMessageToAllEnterMsg,"none",adminSendingKey)
     #در صورت فرستادن پیام از روش کیبورد مبایل(نه ربات)   این دکمه ها و پیام می آیند   
    def adminSendGosilMessageYesNo(self,msg):
        adminMessageToAllWarningMsg = f"{msg} \n\nAre you sure you want to send these 👆 texts to all users?"
        
        # yesNoKey = json.dumps({"keyboard":[[BtnA().noDoubleComma,BtnA().yesSendIt]],"resize_keyboard":True}) 
        yesNoKey = AKeys().yNDoubleKomma
        self.bot.sendMessage(self.id,adminMessageToAllWarningMsg,"none",yesNoKey)

    # بیشتر شدن کاراکترها بیشتر از 4050
    def adminSendGMessageGPanellCharMore(self,msg):
        length = len(msg)
        msgMore4050 = f"The number of message characters is {length} up to 4050 and cannot be sent !!!"
        # adminDesktop = json.dumps({"keyboard":[[BtnA().changeUserType, BtnA().sendToAll, BtnA().reportToday, BtnA().reportAll],[BtnA().apply],[Btn().getBack]] , "resize_keyboard": True})
        adminDesktop = AKeys().adminKeys
        self.bot.sendMessage(self.id,msgMore4050,"none",adminDesktop)

    # کد بگو  
    def adminSendGMessageGPanellCode(self):
        enterPanelMsg = "What was that?"
        # adminSendingKey = json.dumps({"keyboard":[[BtnA().getBackToDesk]],"resize_keyboard":True})
        adminSendingKey = AKeys().getBackDesk
        self.bot.sendMessage(self.id,enterPanelMsg,"none",adminSendingKey)


    def adminSendMsgToAll(self,id,msg):
        # backToHomePage = json.dumps({"keyboard":[[Btn().getBack]],"resize_keyboard":True})
        backToHomePage = Keys().getBackKeys
        self.bot.sendMessage(id,msg,"none",backToHomePage)
    
     #در صورت زدن دکمه «بازگشت به میز سرپرست و ادمین»  این دکمه ها و پیام می آیند   
    def adminSendBBMSVAMessageGPanel(self):
        backToAdminDesk = "Admin Desktop⚙️"
        # adminDesktop = json.dumps({"keyboard":[[BtnA().changeUserType, BtnA().sendToAll, BtnA().reportToday, BtnA().reportAll],[BtnA().apply],[Btn().getBack]] , "resize_keyboard": True}) 
        adminDesktop = AKeys().adminKeys
        self.bot.sendMessage(self.id,backToAdminDesk,"none",adminDesktop)
    
     #در صورت زدن دکمه «Yes،گسیل شود!»  این دکمه ها و پیام می آیند   
    def adminSendYeslMessageGPanel(self):
        adminMessageToAllSentMsg = "Your message was sent to all users"
        # adminDesktop = json.dumps({"keyboard":[[BtnA().changeUserType, BtnA().sendToAll, BtnA().reportToday, BtnA().reportAll],[BtnA().apply],[Btn().getBack]] , "resize_keyboard": True}) 
        adminDesktop = AKeys().adminKeys
        self.bot.sendMessage(self.id,adminMessageToAllSentMsg,"none",adminDesktop)
   
     #در صورت زدن دکمه «No»  این دکمه ها و پیام می آیند   
    def adminSendNolMessageGPanel(self):
        backToAdminDesk = "Admin Desktop⚙️"
        # adminDesktop = json.dumps({"keyboard":[[BtnA().changeUserType, BtnA().sendToAll, BtnA().reportToday, BtnA().reportAll],[BtnA().apply],[Btn().getBack]] , "resize_keyboard": True}) 
        adminDesktop = AKeys().adminKeys
        self.bot.sendMessage(self.id,backToAdminDesk,"none",adminDesktop)
   
     #در صورت زدن دکمه «دگرسانی گونه کاربر»  این دکمه ها و پیام می آیند   
    def adminSendDGKlMessageGBBMSVA(self):
        dGKGUIdeMsg = "userId 12 ... or username @ ... Enter your favorite user"
        # adminSendingKey = json.dumps({"keyboard":[[BtnA().send],[BtnA().getBackToDesk]],"resize_keyboard":True})
        adminSendingKey = AKeys().sendChangeUser
        self.bot.sendMessage(self.id,dGKGUIdeMsg,"none",adminSendingKey)
   
     #در صورت زدن دکمه «گسیل» و فرستادن شناسه کاربری یا نام کاربری اشتباه این دکمه ها و پیام می آیند   
    def adminSendWrongGMessageGBBMSVA(self):
        dGKGUIdeMsg = "Enter username or userId correctly"
        # adminSendingKey = json.dumps({"keyboard":[[BtnA().send],[BtnA().getBackToDesk]],"resize_keyboard":True})
        adminSendingKey = AKeys().sendChangeUser
        self.bot.sendMessage(self.id,dGKGUIdeMsg,"none",adminSendingKey)
   
     #در صورت زدن دکمه «گسیل» و وارد کردن نام درست کاربری یا شناسه کاربری   این دکمه ها و پیام می آیند   
    def adminSendًRightGMessageGPanel(self):
        successfulChangedMsg = f"User { self.msg } changed from simple user to special user."
        # adminSendingKey = json.dumps({"keyboard":[[BtnA().send],[BtnA().getBackToDesk]],"resize_keyboard":True})
        adminSendingKey = AKeys().sendChangeUser
        self.bot.sendMessage(self.id,successfulChangedMsg,"none",adminSendingKey)

#تمامی کیبوردها و پیام های بخش استارت و خود دکمه استارت
class AdminStart:
    def __init__(self,id,firstName,msg):
        self.id = id
        self.firstName = firstName
        self.msg = msg
        self.bot = pybotc.Bot("config.cfg")
        # self.bot = BotTel()
        self.obj_dbContatct = dbContact
    #این دکمه ها و پیام  می آیند Start در صورت زدن دکمه
    def sendKeyAndMessagesUI(self):
         languageMsg = f"Dear {self.firstName} 🌺🌸, select your favorite language for bots message and keyboard"
        #  languagesKey = json.dumps({"keyboard":[[BtnS().keyNMsgDe],[BtnS().keyNMsgEn],[BtnS().keyNMsgPer]],"resize_keyboard":True}) 
         languagesKey = SKeys(Btn(),MNV()).uI
         self.bot.sendMessage(self.id,languageMsg,"none",languagesKey)

   #    یا کیبورد و پیام پارسی⌨💬 این دکمه ها و پیام از فهرست نخستین🛎 و اولیه  می آیند  deutsch Menu, english Menu  در صورت زدن یکی از دکمه های  
    def sendKeyAndMessageFNVAUIselected(self):
        languageSelectedMsg = f"{self.msg} is chosen for bot."
        # firstHomePageKey = json.dumps({"keyboard":[[BtnA().admin, Btn().startLearning],[Btn().aboutBotNew, Btn().uILangNKeyEditNew]], "resize_keyboard": True}) 
        firstHomePageKey = AKeys().firstMenu
        self.bot.sendMessage(self.id,languageSelectedMsg,"none",firstHomePageKey)
    

    def sendKeyAndMessageFNVAUINakhostin(self):
         languageSelectedMsg = "Menu🛎"
        #  firstHomePageKey = json.dumps({"keyboard":[[BtnA().admin, Btn().startLearning],[Btn().aboutBotNew, Btn().uILangNKeyEditNew]], "resize_keyboard": True}) 
         firstHomePageKey = AKeys().firstMenu
         self.bot.sendMessage(self.id,languageSelectedMsg,"none",firstHomePageKey) 

 
#تمامی کیبوردها و پیام های بخش آغاز یادگیری واژه های کتاب
class AdminAghazYadgiriVazhehayeKetab:
    def __init__(self,id,firstName,msg):
        self.id = id
        self.firstName = firstName
        self.msg = msg
        self.bot = pybotc.Bot("config.cfg")
        self.obj_dbContatct = dbContact
        
    def sendAccountInfoKeyAndMessageBBFA(self,outpuTodayDateNTime,output):
        msgNextTrainingTimeDate = output
        ent = "▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️▫️"
        dash = "〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️" 
        msgNextTrainingTimeDate = f"Dear <i> {self.firstName} </i>🌺🌸 Your Account\n{ent}\n{output}\n{dash}\n {outpuTodayDateNTime}\n @DeutschOhal"
        # regularHomePageKey = json.dumps({"keyboard":[[BtnA().admin,Btn().reviewWords],[Btn().wordsNum,Btn().wayEdit,Btn().account],[Btn().timeLearnEdit,Btn().reportActivity],[Btn().deleteBot,Btn().aboutBot,Btn().uILangNKeyEdit],[Btn().opinion]],"resize_keyboard":True})
        regularHomePageKey = AKeys().secondMenu
        
        self.bot.sendMessage(self.id,msgNextTrainingTimeDate,"none",regularHomePageKey)
    
    #در صورت زدن دکمه((آعاز یادگیری واژه های کتاب)) این دکمه ها و پیام می آیند
    def sendAYVKKeyAndMessage327(self):
        wortZahlMsg = f" Dear {self.firstName} 🌺🌸, how many new words do you want in a day?"        
        # wortZahlKey = json.dumps({"keyboard":[[BtnS().threeNew],[BtnS().twoNew],[BtnS().oneNew],[BtnS().fiveNew,BtnS().tenNew,BtnS().fifteenNew,BtnS().twentyNew]],"resize_keyboard":True})
        wortZahlKey = AKeys().wordsNumNew
        self.bot.sendMessage(self.id,wortZahlMsg,"none",wortZahlKey)
    #در صورت زدن یکی از دکمه های ۳ یا ۵  یا ۷ این دکمه ها و پیام می آیند
    def send357KeyAndMessageDESP(self):
        waysMsg = f"Dear {self.firstName}  🌺🌸, Choose the Method to Learn Book Words."
        # wayKey = json.dumps({"keyboard":[[BtnS().deutschNew,BtnS().englishNew,BtnS().synonymNew],[BtnS().allTogetherNew,BtnS().persianNew]],"resize_keyboard":True}) 
        wayKey = AKeys().waysNew
        self.bot.sendMessage(self.id,waysMsg,"none",wayKey)

  
   #    یا پارسی این دکمه و پیام می آیند  deutsch , english , synonym  در صورت زدن یکی از دکمه های  
    def sendDESPKeyAndMessageLampGuid(self,way,wKind,numW,numAll,standardizedWord,content,chapter,wordsPage,linkWord):
        dash = "___________________________________"
        guide = f"Hint🔔: Read the word and say {way} of that and remember it then tap on 💡 to see the correct answer and compare it with your answer."
        newWordsMsg = f".{numW}/{numAll}                                         {wKind}.\n<b>{standardizedWord}</b>\n.Chapter : {content}\nSection : {chapter} \nPage:{wordsPage}.\n{dash}\n{linkWord}{guide}"
        antwortKey = SKeys(Btn(),MNV()).lampKeys
        self.bot.sendMessage(self.id,newWordsMsg,"none",antwortKey)


                               
   #    یا پارسی این دکمه و پیام می آیند  deutsch , english , synonym  در صورت زدن یکی از دکمه های  
    def sendDESPKeyAndMessageLamp(self,wKind,numW,numAll,standardizedWord,content,chapter,wordsPage,linkWord):
        newWordsMsg = f".{numW}/{numAll}                                         {wKind}.\n<b>{standardizedWord}</b>\n.Chapter : {content}\nSection : {chapter} \nPage:{wordsPage}. \n {linkWord}."
        # {content}\n{cotentNChap} \nPage:{wordsPage}
        # antwortKey = json.dumps({"keyboard":[[BtnS().lamp]],"resize_keyboard":True}) 
        antwortKey = SKeys(Btn(),MNV()).lampKeys
        self.bot.sendMessage(self.id,newWordsMsg,"none",antwortKey)



   #در صورت زدن دکمه 💡 این دکمه و پیام می آید 
    def sendLampKeyAndMessageVXGuide(self,way,icon,standardizedAnswer,answerLink):
               #63 blank space
        dash = "___________________________________"
        guide = f"Hint🔔: By checking the reply sent and your answer, choose your answer correctly or incorrectly by selecting ❌ or ✅."

        pa = f"Answer into  {way} {icon}"
        lenngthPa = len(pa)
        pa = pa.center(72 - lenngthPa)
        # print(f"len(pa) = {len(pa)}")       
        newWordsMsg = f"<b>{pa}</b>\n{standardizedAnswer}\n{dash}\n{answerLink}{guide}"
        # rwKey = json.dumps({"keyboard":[[BtnS().crossCheck,BtnS().check]],"resize_keyboard":True}) 
        rwKey = SKeys(Btn(),MNV()).rW
        self.bot.sendMessage(self.id,newWordsMsg,"none",rwKey)


   #در صورت زدن دکمه 💡 این دکمه و پیام می آید 
    def sendLampKeyAndMessageVX(self,way,icon,standardizedAnswer,answerLink):
               #63 blank space
        pa = f"Answer into  {way} {icon}"
        lenngthPa = len(pa)
        pa = pa.center(72 - lenngthPa)
        newWordsMsg = f"<b>{pa}</b>\n{standardizedAnswer}.\n {answerLink}"
        # rwKey = json.dumps({"keyboard":[[BtnS().crossCheck,BtnS().check]],"resize_keyboard":True}) 
        rwKey = SKeys(Btn(),MNV()).rW
        self.bot.sendMessage(self.id,newWordsMsg,"none",rwKey)
    #done section 7
    #در صورت زدن آخرین دکمه از❌","✅ این دکمه و پیام می آیند  
    def sendLastVXKeyAndMessageBBFA(self,nWorkedWords,nRWords,nWWrong,wrongWordsNpages,weekDay,day,month,year,houNMTraining,dateGriNextTraining,wordsSectionPosition):
        dash = "___________________________________"
        print(f"nRWords = {nRWords},nWorkedWords = {nWorkedWords}")
        percentageRight = self.obj_dbContatct.Percentage().percentage(nRWords,nWorkedWords)
        percentageWrong = self.obj_dbContatct.Percentage().percentage(nWWrong,nWorkedWords)
        graphRight = self.obj_dbContatct.Graph().graph(nRWords,nWorkedWords)
        graphWrong = self.obj_dbContatct.Graph().graph(nWWrong,nWorkedWords)
        guide = f"🔔 After tap on '{Btn().getBack}' You can select '{Btn().reviewWords}' to review the words you have done."
        daliyReport = f" Dear {self.firstName}  🌺🌸 <i> Report your activities, Today: </i> \n {dash.center(14)} \n Number of Practiced Words: <b> {nWorkedWords} </b> \n Number of correct words: <b> {nRWords} </b> \n Number of incorrect words: <b> {nWWrong} </b> \n {dash.center(14)} \n <i> percentage of correct and incorrect Words: </i> \n  Correct <b> {graphRight}% {percentageRight} </b> \n  incorrect <b> {graphWrong}% {percentageWrong} </b> \n  {dash.center(14)} \n  List of incorrect words today with the page address in the book: \n  <b> {wrongWordsNpages} </b> \n  {dash.center(14)} \n The 👉Learn Vocabulary Daily👈 next on <b> { weekDay} {day} {month} {year} </b>, at <b> {houNMTraining} </b> In the time of Iran, Coincides with <b>{dateGriNextTraining}</b>\n {dash} \n <i> Partition and number of all words in the Lightner box: </i> \n  Words number in 1Th partition: <b> {wordsSectionPosition[0]} </b> \n  Words number in 2Th partition: <b> {wordsSectionPosition[1]} </b> \n  Words number in 3Th partition: <b> {wordsSectionPosition[2]} </b> \n  Words number in 4Th partition: <b> {wordsSectionPosition[3]} </b> \n  Words number in 5Th partition:  <b> {wordsSectionPosition[4]} </b> \n  Words number in 6Th partition: <b> {wordsSectionPosition[5]} </b> \n {dash} \n  Number of fully learned vocabulary: <b> {wordsSectionPosition[6]} </b> \n {dash} \n  <i> {guide} </i> \n @DeutschOhal \n"
        print(f"daily report = {daliyReport}")
        # backToHomePage = json.dumps({"keyboard":[[Btn().getBack]],"resize_keyboard":True})
        backToHomePage = Keys().getBackKeys
        self.bot.sendMessage(self.id,daliyReport,"none",backToHomePage)
       
    # فرستادن تاریخ و زمان یادگیری واژگان بعدی پسین
    def sendNextTrainingDateTimeKeyAndMessageBBFA(self,weekDay,day,monthAlpha,year,hourMin):
        # y = "یادگیری واژگان روزانه"
        
        msgNextTrainingTimeDate = f"Dear <i>{self.firstName}</i>🌺🌸, The 👉Learn Vocabulary Daily👈 next on <b> {weekDay} {day} {monthAlpha} {year} </b>, at <b> {hourMin} </b>. \n@DeutschOhal"
        # msgNextTrainingTimeDate = "g"
        # regularHomePageKey = json.dumps({"keyboard":[[BtnA().admin,Btn().reviewWords],[Btn().wordsNum,Btn().wayEdit,Btn().account],[Btn().timeLearnEdit,Btn().reportActivity],[Btn().deleteBot,Btn().aboutBot,Btn().uILangNKeyEdit],[Btn().opinion]],"resize_keyboard":True})
        regularHomePageKey = AKeys().secondMenu
        self.bot.sendMessage(self.id,msgNextTrainingTimeDate,"none",regularHomePageKey)






     #در صورت زدن  دکمه بازگشت به فهرست آغازین🏡 به بخش فهرست آغازین و اصلی منتقل شده و این دکمه ها و پیام می آیند 

#FIXME حذف این تابع از کیبورد و جایگزینی در آنالیز AYVK.sendKeyAndMessageFAVA()
    def sendKeyAndMessageFAVA(self):
        fehrestAghazinMsg = "Home"
        # regularHomePageKey = json.dumps({"keyboard":[[BtnA().admin,Btn().reviewWords],[Btn().wordsNum,Btn().wayEdit,Btn().account],[Btn().timeLearnEdit,Btn().reportActivity],[Btn().deleteBot,Btn().aboutBot,Btn().uILangNKeyEdit],[Btn().opinion]],"resize_keyboard":True})
        regularHomePageKey = AKeys().secondMenu
        self.bot.sendMessage(self.id,fehrestAghazinMsg,"none",regularHomePageKey)

    def sendKeyAndMessageUserMustWait(self):
        fehrestAghazinMsg = "Until the next date"
        # regularHomePageKey = json.dumps({"keyboard":[[BtnA().admin,Btn().reviewWords],[Btn().wordsNum,Btn().wayEdit,Btn().account],[Btn().timeLearnEdit,Btn().reportActivity],[Btn().deleteBot,Btn().aboutBot,Btn().uILangNKeyEdit],[Btn().opinion]],"resize_keyboard":True})
        regularHomePageKey = AKeys().secondMenu
        self.bot.sendMessage(self.id,fehrestAghazinMsg,"none",regularHomePageKey)


class AdminErrorMsgs:
    def __init__(self,id,firstName,msg):
        self.id = id
        self.firstName = firstName
        self.msg = msg
        self.bot = pybotc.Bot("config.cfg")
        self.obj_dbContatct = dbContact
    #spam warning BtnS().crossCheck,"✅ پیام خطا به جهت فرستادن تکراری 
    def sendWarningKeyAndMessageLamp(self):
        msgWarning = "⛔️😡😡⛔️ Avoid sending Spam ⛔️😡😡⛔️"
        # antwortKey = json.dumps({"keyboard":[[BtnS().lamp]],"resize_keyboard":True}) 
        # antwortKey = SKeys(Btn(),MNV()).lampKeys
        antwortKey = ""
        self.bot.sendMessage(self.id,msgWarning,"none",antwortKey)
        #spam warning هنگامه آخرین واژه BtnS().crossCheck,"✅ پیام خطا به جهت فرستادن تکراری 
    def sendWarningKeyAndMessageBBFA(self):
        msgWarning = "⛔️😡😡⛔️ Avoid sending Spam ⛔️😡😡⛔️"
        # backToHomePage = json.dumps({"keyboard":[[Btn().getBack]],"resize_keyboard":True})
        backToHomePage = Keys().getBackKeys
        backToHomePage =""
        self.bot.sendMessage(self.id,msgWarning,"none",backToHomePage)
     
    #spam warning  پیام خطا به جهت فرستادن تکراری برای کاربری که هنوز نام نویسی نشده 
    def sendWarningRepeatedKeyAndMessageToAdminGuest(self):
        msgWarning = "⛔️😡😡⛔️ Avoid sending Spam ⛔️😡😡⛔️"
        # firstHomePageKey = json.dumps({"keyboard":[[BtnA().admin, Btn().startLearning],[Btn().aboutBotNew, Btn().uILangNKeyEditNew]], "resize_keyboard": True}) 
        # firstHomePageKey = AKeys().firstMenu
        firstHomePageKey =""
        self.bot.sendMessage(self.id,msgWarning,"none",firstHomePageKey)


    #spam warning  پیام خطا به جهت فرستادن تکراری برای کاربر  
    def sendWarningRepeatedKeyAndMessageToAdmin(self):
        msgWarning = "⛔️😡😡⛔️ Avoid sending Spam ⛔️😡😡⛔️"
        # regularHomePageKey = json.dumps({"keyboard":[[BtnA().admin, Btn().reviewWords],[Btn().wordsNum, Btn().wayEdit, Btn().account]),[Btn().timeLearnEdit, Btn().uILangNKeyEdit],[Btn().deleteBot,Btn().aboutBot,Btn().reportActivity]]," resize_keyboard ": True})
        regularHomePageKey =""  
        self.bot.sendMessage(self.id,msgWarning,"none",regularHomePageKey) 
    
   
    #none keyboard warning  پیام خطا به جهت عدم استفاده از کیبورد ربات برای ادمین عضو شده  
    def sendWarningNoneKeyboardToAdmin(self):
        msgWarning = "Only use the Bot keyboard!"
        # regularHomePageKey = json.dumps({"keyboard":[[BtnA().admin,Btn().reviewWords],[Btn().wordsNum,Btn().wayEdit,Btn().account],[Btn().timeLearnEdit,Btn().reportActivity],[Btn().deleteBot,Btn().aboutBot,Btn().uILangNKeyEdit],[Btn().opinion]],"resize_keyboard":True})
        regularHomePageKey = AKeys().secondMenu
        # regularHomePageKey=""
        self.bot.sendMessage(self.id,msgWarning,"none",regularHomePageKey) 

    #none keyboard warning  پیام خطا به جهت عدم استفاده از کیبورد ربات برای ادمین میهمان   
    def sendWarningNoneKeyboardToAdminGuest(self):
        msgWarning = "Only use the Bot keyboard!"
        # firstHomePageKey = json.dumps({"keyboard":[[BtnA().admin, Btn().startLearning],[Btn().aboutBotNew, Btn().uILangNKeyEditNew]], "resize_keyboard": True}) 
        # firstHomePageKey = AKeys().firstMenu
        firstHomePageKey =""
        self.bot.sendMessage(self.id,msgWarning,"none",firstHomePageKey) 

class AdminAutomaticMessage:
    def __init__(self,id,firstName):
        self.id = id
        self.bot = pybotc.Bot("config.cfg")
        self.firstName = firstName
    def sendKeyAndMessageDailyLearn(self):
        msg = f"Dear <i> {self.firstName}</i>  🌺🌸, Begin learning and practicing vocabulary, tap on '👉👉Learn Vocabulary Daily👈👈' by keyboards bot!"
        # learnKey = json.dumps({"keyboard":[[Btn().dailyLearnWords]],"resize_keyboard":True})
        learnKey = Keys().dailyLearnKeys
        self.bot.sendMessage(self.id,msg,"none",learnKey)

#تمامی کیبوردها و پیام های بخش دگزسانی زبان در فهرست نخستین🛎 واولیه
class AdminDegarsaniZaban1:
    def __init__(self,id,firstName,msg):
        self.id = id
        self.firstName = firstName
        self.msg = msg
        self.bot = pybotc.Bot("config.cfg")
        self.obj_Start = Start(id,firstName,msg)
 
    #در صورت زدن دکمه 📝 زبان پیام و کیبورد ⌨ این دکمه ها و پیام می آیند    
    #FIXME  Start.sendKeyAndMessagesUI() در حذف و یاگزین کردن   
    # در آنالیز
    def sendKeyAndMessageUI1(self):
        self.obj_Start.sendKeyAndMessagesUI()


#تمامی کیبوردها و پیام های بخش درباره ربات ℹ️ در فهرست نخستین🛎 واولیه
class AdminDarbarehRobat1:
    def __init__(self,id,firstName,msg):
        self.id = id
        self.firstName = firstName
        self.bot = pybotc.Bot("config.cfg")
    #در صورت زدن دکمه درباره ربات ℹ️ در بخش نخستین و اولیه این دکمه ها و پیام می آیند    
    def sendKeyAndMessageDarbarehRobat1(self):
        aboutMsg = f" Greetings Dear <i> {self.firstName} </i>🌺🌸, \n This Bot can learn all the new and emphasized words of the book <b>'Großes Übungsbuch Wortschatz'</b>  in the context of Leitner's repetition and practice daily in the calendar structure. With the ability to remind you and choose the answer in German, it enables synonyms, English and Persian using authentic German language resources, so that full mastery of a word and word is achieved in at least one month. From your short-term memory, it will be in your long-term memory." 
        # firstHomePageKey = json.dumps({"keyboard":[[BtnA().admin, Btn().startLearning],[Btn().aboutBotNew, Btn().uILangNKeyEditNew]], "resize_keyboard": True})
        firstHomePageKey = AKeys().firstMenu
        self.bot.sendMessage(self.id,aboutMsg,"none",firstHomePageKey)

#تمامی کیبوردها و پیام های بخش «مرور واژه های گذشته🧐» در فهرست نخستین🛎 واولیه
class AdminMorureVazhehhayeGozashteh:
    def __init__(self,id,firstName,msg):
        self.id = id
        self.firstName = firstName
        self.bot = pybotc.Bot("config.cfg")
        self.obj_AYVK = AghazYadgiriVazhehayeKetab(id,firstName,msg)
    
    
        #در صورت زدن دکمه «مرور واژه های گذشته🧐» در بخش آغازین و اصلی بخش "تفکیک مرور واژه های گذشته🧐"  دکمه ها و پیام می آیند 
    def sendMVGKeyAndMessageTMVG(self):
        reviewMsg = f"Dear {self.firstName}🌺🌸, Choose vocabulary reviewing method, based on one of the options."
        # print(f"Btn().chapterNSection = {Btn().chapterNSection} ,Btn().leitnerBoxParts ={Btn().leitnerBoxParts} ,Btn().weakWords = {Btn().weakWords},Btn().getBack = {Btn().getBack}")
        # reviewKey = json.dumps({"keyboard":[[Btn().chapterNSection],[Btn().leitnerBoxParts],[Btn().weakWords],[Btn().getBack]],"resize_keyboard":True})  
        reviewKey = Keys().revKeys
        # reviewKey = json.dumps({"keyboard":[["Btn().chapterNSection],[Btn().leitnerBoxParts],[Btn().weakWords],[Btn().getBack"]],"resize_keyboard":True})  
        self.bot.sendMessage(self.id,reviewMsg,"none",reviewKey)
        
        #🔎
        ###در صورت زدن دکمه «Chapter و Section» در بخش آغازین و اصلی این  دکمه ها و پیام نخستین واژه می آیند 
    def sendWordsChapterContentKeyAndMessageFirstOLdWord(self,content,chapter,word,answer,counter,length,section,page,link):
        oldWordsMsg = f".Chapter : {content}\nSection : {chapter}\n\n<b>{word}</b>\n\n{answer.center(63)}\n\n.Page :{page}                         {section}: {length}/{counter+1}{link}."
        # reviewNextKey = json.dumps({"keyboard":[[Btn().nextWordChapNS],[Btn().getBack]],"resize_keyboard":True}) 
        reviewNextKey = Keys().revChapNexKeys
        self.bot.sendMessage(self.id,oldWordsMsg,"none",reviewNextKey)
        ## وقتی طول آرایه یکی بود
    def sendWordsChapterContentKeyAndMessageFirstOLdWordOneLength(self,content,chapter,word,answer,counter,length,section,page,link):
        oldWordsMsg = f".Chapter : {content}\nSection : {chapter}\n\n<b>{word}</b>\n\n{answer.center(63)}\n\n.Page :{page}                         {section}: {length}/{counter+1}{link}."
        # reviewNextKey = json.dumps({"keyboard":[[Btn().getBack]],"resize_keyboard":True}) 
        backToHomePage = Keys().getBackKeys
        self.bot.sendMessage(self.id,oldWordsMsg,"none",backToHomePage)


    #Chapter و Section- کیبورد حاوی قبلی و بعدی  
    def sendWordsChapterContentKeyAndMessagMiddleOLdWord(self,content,chapter,word,answer,counter,length,section,page,link):
        oldWordsMsg = f".Chapter : {content}\nSection : {chapter}\n\n<b>{word}</b>\n\n{answer.center(63)}\n\n.Page :{page}                         {section}: {length}/{counter+1}{link}."
        # reviewNextKey = json.dumps({"keyboard":[[Btn().beforeWordChapNS, Btn().nextWordChapNS],[Btn().getBack]], "resize_keyboard": True}) 
        reviewMiddleKeys = Keys().revChapMidKeys
        self.bot.sendMessage(self.id,oldWordsMsg,"none",reviewMiddleKeys)
    
    #Chapter و Section- کیبورد حاوی قبلی و آخرین واژه  
    def sendWordsChapterContentKeyAndMessagLastOLdWord(self,content,chapter,word,answer,counter,length,section,page,link):
        oldWordsMsg = f".Chapter : {content}\nSection : {chapter}\n\n<b>{word}</b>\n\n{answer.center(63)}\n\n.Page :{page}                         {section}: {length}/{counter+1}{link}."
        # reviewBeforeKey = json.dumps({"keyboard":[[Btn().beforeWordChapNS],[Btn().getBack]],"resize_keyboard":True}) 
        reviewBeforeKey = Keys().revChapBefKeys
        self.bot.sendMessage(self.id,oldWordsMsg,"none",reviewBeforeKey)


    #🔭
    ###در صورت زدن دکمه «بخش ها» در بخش آغازین و اصلی این  دکمه ها و پیام نخستین واژه می آیند 
    def sendBakhshhaKeyAndMessageFirstWord(self,counter,length,section,word,answer,page,content,chapter,link):
        oldWordsMsg = f". {section}: {length}/{counter+1}\n<b>{word}</b>\n\n{answer.center(63)}\n\n.Chapter : {content}\nSection : {chapter} \n{link}\nPage:{page}"
        # reviewNextKey = json.dumps({"keyboard":[[Btn().nextWordLeitBP],[Btn().getBack]],"resize_keyboard":True}) 
        reviewNextKey = Keys().revLeitNexKeys
        self.bot.sendMessage(self.id,oldWordsMsg,"none",reviewNextKey)

    def sendBakhshhaKeyAndMessageFirstWordOneLength(self,counter,length,section,word,answer,page,content,chapter,link):
        oldWordsMsg = f". {section}: {length}/{counter+1}\n<b>{word}</b>\n\n{answer.center(63)}\n\n.Chapter : {content}\nSection : {chapter} \n{link}\nPage:{page}"
        # backToHomePage = json.dumps({"keyboard":[[Btn().getBack]],"resize_keyboard":True}) 
        backToHomePage = Keys().getBackKeys
        self.bot.sendMessage(self.id,oldWordsMsg,"none",backToHomePage)



        #بخش ها- کیبورد حاوی قبلی و بعدی 
    def sendBakhshhaKeyAndMessageMiddleWord(self,counter,length,section,word,answer,page,content,chapter,link):
        oldWordsMsg = f". {section}: {length}/{counter+1}\n<b>{word}</b>\n\n{answer.center(63)}\n\n.Chapter : {content}\nSection : {chapter} \n{link}\nPage:{page}"
        #اگر واژه ای بعد از این هنوز موجود باشد
        # reviewBackNextKey = json.dumps({"keyboard":[[Btn().beforeWordLeitBP,Btn().nextWordLeitBP],[Btn().getBack]],"resize_keyboard":True}) 
        reviewBackNextKey = Keys().revLeitMidKeys
        self.bot.sendMessage(self.id,oldWordsMsg,"none",reviewBackNextKey)

        #بخش ها- کیبورد حاوی قبلی  
    def sendBakhshhaKeyAndMessageLastWord(self,counter,length,section,word,answer,page,content,chapter,link):
        oldWordsMsg = f". {section}: {length}/{counter+1}\n<b>{word}</b>\n\n{answer.center(63)}\n\n.Chapter : {content}\nSection : {chapter} \n{link}\nPage:{page}"
        #اگر واژه ای بعد از این دیگر موجود نباشد
        # reviewBackKey = json.dumps({"keyboard":[[Btn().beforeWordLeitBP],[Btn().getBack]],"resize_keyboard":True}) 
        reviewBackKey = Keys().revLeitBefKeys
        self.bot.sendMessage(self.id,oldWordsMsg,"none",reviewBackKey)

    #🔬
    ###در صورت زدن دکمه «واژگان ناتوان» در بخش آغازین و اصلی این  دکمه ها و پیام نخستین واژه می آیند 
    def sendWeakWordsKeyAndMessageFirstOLdWord(self,durationDays,counter,length,section,word,answer,content,chapter,page,link):
        oldWordsMsg = f".Days Number : {durationDays}         {section}:{counter+1}/{length}.\n\n<b>{word}</b>\n\n{answer.center(63)}\n\n.Chapter : {content}\nSection : {chapter} \n{link}\nPage:{page}"
        # Page:{page}
        # {page}:Page
        # reviewNextKey = json.dumps({"keyboard":[[Btn().nextWordWW],[Btn().getBack]],"resize_keyboard":True}) 
        reviewNextKey = Keys().revWeakNexKeys
        self.bot.sendMessage(self.id,oldWordsMsg,"none",reviewNextKey)

    #وقتی طول آرایه یکی باشد
    def sendWeakWordsKeyAndMessageFirstOLdWordOneLength(self,durationDays,counter,length,section,word,answer,content,chapter,page,link):
        oldWordsMsg = f".Days Number : {durationDays}         {section}:{counter+1}/{length}.\n\n<b>{word}</b>\n\n{answer.center(63)}\n\n.Chapter : {content}\nSection : {chapter} \n{link}\nPage:{page}"
        # Page:{page}
        # {page}:Page
        # backToHomePage = json.dumps({"keyboard":[[Btn().getBack]],"resize_keyboard":True}) 
        backToHomePage = Keys().getBackKeys
        self.bot.sendMessage(self.id,oldWordsMsg,"none",backToHomePage)



# {self.firstName}
    def sendWeakWordsKeyAndMessageNoWord(self):
        noWeakWordMsg = f" Dear <i>{self.firstName}</i>🌺🌸, You don't have any Weak Vocabulary!"
        regularHomePageKey = AKeys().secondMenu

        self.bot.sendMessage(self.id,noWeakWordMsg,"none",regularHomePageKey)
    def sendWeakWordsKeyAndMessageNoWordOtherReview(self):
        noWeakWordMsg = f"Dear <i> {self.firstName}</i>🌺🌸, you haven't done no word and exercise so far!"
        regularHomePageKey = Keys().secondMenu
        self.bot.sendMessage(self.id,noWeakWordMsg,"none",regularHomePageKey)

    #واژگان ناتوان- کیبورد حاوی قبلی و بعدی  
    def sendWeakWordsKeyAndMessagMiddleOLdWord(self,durationDays,counter,length,section,word,answer,content,chapter,page,link):
        oldWordsMsg = f".Days Number : {durationDays}         {section}:{counter+1}/{length}.\n\n<b>{word}</b>\n\n{answer.center(63)}\n\n.Chapter : {content}\nSection : {chapter} \n{link}\nPage:{page}"
        # reviewNextKey = json.dumps({"keyboard":[[Btn().beforeWordWW,Btn().nextWordWW],[Btn().getBack]],"resize_keyboard":True}) 
        reviewNextKey = Keys().revWeakMidKeys
        self.bot.sendMessage(self.id,oldWordsMsg,"none",reviewNextKey)
    #واژگان ناتوان- کیبورد حاوی قبلی و آخرین واژه  
    def sendWeakWordsKeyAndMessagLastOLdWord(self,durationDays,counter,length,section,word,answer,content,chapter,page,link):
        oldWordsMsg = f".Days Number : {durationDays}         {section}:{counter+1}/{length}.\n\n<b>{word}</b>\n\n{answer.center(63)}\n\n.Chapter : {content}\nSection : {chapter} \n{link}\nPage:{page}"
        # reviewNextKey = json.dumps({"keyboard":[[Btn().beforeWordWW],[Btn().getBack]],"resize_keyboard":True}) 
        reviewNextKey = Keys().revWeakBefKeys
        self.bot.sendMessage(self.id,oldWordsMsg,"none",reviewNextKey)







     #در صورت زدن  دکمه بازگشت به فهرست آغازین🏡 به بخش فهرست آغازین و اصلی منتقل شده و این دکمه ها و پیام می آیند 
#FIXME حذف این تابع از کیبورد و جایگزینی در آنالیز AYVK.sendKeyAndMessageFAVA()
    def sendKeyAndMessageFAVA(self):
        self.obj_AYVK.sendKeyAndMessageFAVA()

#تمامی کیبوردها و پیام های بخش «📝 روش 🛣» آغازین و اصلی  
class AdminVirayeshRavesh:
    def __init__(self,id,firstName,msg):
        self.id = id
        self.firstName = firstName
        self.msg = msg
        self.obj_AYVK = AghazYadgiriVazhehayeKetab(id,firstName,msg)
        self.bot = pybotc.Bot("config.cfg")    

    #در صورت زدن دکمه «📝 روش 🛣»  این  دکمه ها و پیام می آیند
    def send357KeyAndMessageDESP(self):
        waysMsg = f"Dear {self.firstName}  🌺🌸, Choose the Method to Learn Book Words."
        # wayKey = json.dumps({"keyboard":[[BtnS().deutsch,BtnS().english,BtnS().synonym],[BtnS().allTogether,BtnS().persian],[Btn().getBack]],"resize_keyboard":True}) 
        wayKey = AKeys().ways
        self.bot.sendMessage(self.id,waysMsg,"none",wayKey)



     #    یا پارسی  این دکمه ها و پیام می آیند  deutsch , english , synonym  در صورت زدن یکی از دکمه های  
    def sendDESPAllKeyAndMessageYesNo(self,way): 
        waysWarningMsg = f"Dear {self.firstName} 🌺🌸, Are you sure you want to select the new <b> {self.msg} </b> method, because if you select, your Previous record <b> {way} </b> for worked words will be deleted?"
        # yesNoKey = json.dumps({"keyboard":[[Btn().noDot,Btn().yesDot]],"resize_keyboard":True}) 
        yesNoKey = Keys().yNDot
        self.bot.sendMessage(self.id,waysWarningMsg,"none",yesNoKey)


   #    یا پارسی و یکسان بودن با روش قبلی این دکمه ها و پیام می آیند  deutsch , english , synonym  در صورت زدن یکی از دکمه های  
    def sendDESPAllSameKeyAndMessageFAVA(self): 
        waysWarningMsg = f"Your method is <b> {self.msg} </b> right now, No need to change." 
        # regularHomePageKey = json.dumps({"keyboard":[[BtnA().admin,Btn().reviewWords],[Btn().wordsNum,Btn().wayEdit,Btn().account],[Btn().timeLearnEdit,Btn().reportActivity],[Btn().deleteBot,Btn().aboutBot,Btn().uILangNKeyEdit],[Btn().opinion]],"resize_keyboard":True})
        regularHomePageKey = AKeys().secondMenu
        self.bot.sendMessage(self.id,waysWarningMsg,"none",regularHomePageKey)

    #در صورت زدن دکمه «Yes» به فهرست آغازین و اصلی منتقل شده و این  دکمه ها و پیام می آیند 
    def sendBaleKeyAndMessageFAVA(self): 
        waysChangedMsg = f"Method in {self.msg} Edited."
        # regularHomePageKey = json.dumps({"keyboard":[[BtnA().admin,Btn().reviewWords],[Btn().wordsNum,Btn().wayEdit,Btn().account],[Btn().timeLearnEdit,Btn().reportActivity],[Btn().deleteBot,Btn().aboutBot,Btn().uILangNKeyEdit],[Btn().opinion]],"resize_keyboard":True})
        regularHomePageKey = AKeys().secondMenu
        self.bot.sendMessage(self.id,waysChangedMsg,"none",regularHomePageKey)

   #در صورت زدن دکمه «No» به فهرست آغازین و اصلی منتقل شده و این  دکمه ها و پیام می آیند 
    #FIXME حذف این تابع از کیبورد و جایگزینی در آنالیز AYVK.sendKeyAndMessageFAVA()
    def sendKheyrKeyAndMessageFAVA(self):
        self.obj_AYVK.sendKeyAndMessageFAVA()

    def wayMenu(self,way):
        keys = SKeys(Btn(),MNV()).removeKeyboard
        msg = Btn().wayEdit
        keys2 = SKeys(Btn(),MNV()).wayKeys(way)
        msg2 = MNV(self.firstName).pickOptionTxt()
        # msg2 = f"گزینه دلخواهت  {self.firstName} عزیز 🌺🌸 را انتخاب کن."
        parse_mode="HTML"
        # self.bot.editMessage(self.id,self.msgId,msgEdit,parse_mode,keys)
        self.bot.sendMessage(self.id,msg,parse_mode,keys)
        self.bot.sendMessage(self.id,msg2,parse_mode,keys2)

#تمامی کیبوردها و پیام های بخش «ویرایش شمار واژگان آغازین و اصلی»  
class AdminVirayeshShomarVazheha:
    def __init__(self,id,firstName,msg):
        self.id = id
        self.firstName = firstName
        self.msg = msg
        self.bot = pybotc.Bot("config.cfg")   
    #در صورت زدن دکمه «📝 شمار  واژه ها 🔢» این  دکمه ها و پیام می آیند 
    def sendVShVMessage357(self):
        wortZahlMsg = f" Dear {self.firstName} 🌺🌸, how many new words do you want in a day?"        
        # wortZahlKey = json.dumps({"keyboard":[[BtnS().three],[BtnS().two],[BtnS().one],[BtnS().five,BtnS().ten,BtnS().fifteen,BtnS().twenty],[Btn().getBack]],"resize_keyboard":True})
        wortZahlKey = AKeys().wordsNum
        self.bot.sendMessage(self.id,wortZahlMsg,"none",wortZahlKey)
    #در صورت زدن دکمه «۳» یا «۵» یا «۷»این  دکمه ها و پیام می آیند 
    def send357AllVMessageFAVA(self):
        changedWordNum = f"The number of new words changed to <b>{self.msg}</b>."
        # regularHomePageKey = json.dumps({"keyboard":[[BtnA().admin,Btn().reviewWords],[Btn().wordsNum,Btn().wayEdit,Btn().account],[Btn().timeLearnEdit,Btn().reportActivity],[Btn().deleteBot,Btn().aboutBot,Btn().uILangNKeyEdit],[Btn().opinion]],"resize_keyboard":True})
        regularHomePageKey = AKeys().secondMenu
        self.bot.sendMessage(self.id,changedWordNum,"none",regularHomePageKey)

#تمامی کیبوردها و پیام های بخش «📝زمان یادگیری روزانه⏳» آغازین و اصلی
class AdminVireyeshZamanYadgiriRuzaneh:
    def __init__(self,id,firstName,msg=None):
        self.id = id
        self.firstName = firstName
        self.msg = msg
        self.bot = pybotc.Bot("config.cfg")   
        self.obj_AYVK = AghazYadgiriVazhehayeKetab(id,firstName,msg)

    #در صورت زدن دکمه «📝زمان یادگیری روزانه⏳» این  دکمه ها و پیام می آیند 
    def sendVZYRVMessage1_23(self):
        timeLearningMsg = f"Dear {self.firstName} 🌺🌸, Choose your daily learning start time to visit the Bot."
        # hoursKey = json.dumps({"keyboard":[[BtnS().clock1,BtnS().clock2,BtnS().clock3,BtnS().clock4,BtnS().clock5,BtnS().clock6,BtnS().clock7,BtnS().clock8],[BtnS().clock9,BtnS().clock10,BtnS().clock11,BtnS().clock12,BtnS().clock13,BtnS().clock14,BtnS().clock15,BtnS().clock16],[BtnS().clock17,BtnS().clock18,BtnS().clock19,BtnS().clock20,BtnS().clock21,BtnS().clock22,BtnS().clock23],[Btn().getBack]],"resize_keyboard":True}) 
        hoursKey = Keys().hKeys
        self.bot.sendMessage(self.id,timeLearningMsg,"none",hoursKey)
    #در صورت زدن دکمه «۱..۲۳» این  دکمه ها و پیام می آیند 
    def send1_23MessageYesNo(self,year,monthAlpha,day,weekDay,hourMin,askedYear,askedMonthAlpha,askedDay,askedWeekDay,askedHourMin):
        dash = "___________________________________"
        timeLearningWarningMsg = f"Dear {self.firstName} 🌺🌸, Are you confident to change time of 👉Learn Vocabulary Daily👈 to {self.msg} on {askedWeekDay} {askedDay} {askedMonthAlpha} {askedYear}? \n {dash} \n Currently 👉Learn Vocabulary Daily👈 next on {weekDay} {day} {monthAlpha} {year}, <b> At {hourMin} </b>. \n @DeutschOhal"
        

        # yesNoKey = json.dumps({"keyboard":[[Btn().noDash,Btn().yesDash]],"resize_keyboard":True}) 
        yesNoKey = Keys().yNDash
        self.bot.sendMessage(self.id,timeLearningWarningMsg,"none",yesNoKey)


    #در صورت همسان بودن زمان یادگیری روزانه با قبلی  این  دکمه ها و پیام می آیند 
    def sendYesMessageSameFAVA(self,year,monthAlpha,day,weekDay,hourMin):
        dash = "___________________________________"
        # "روش شما در همین هنگام هم  {} هست نیازی تغییر و دگرسانی نیست".format(self.msg)

        timeLearningChangedMsg = f"Your daily learning time is at the same time {self.msg} There is no need to change \n {dash} \n 👉Learn Vocabulary Daily👈 next on <b>  {weekDay} {monthAlpha}{day},</b>   {year}  <b> At <b> {hourMin} </b> \n @DeutschOhal "
        # regularHomePageKey = json.dumps({"keyboard":[[BtnA().admin,Btn().reviewWords],[Btn().wordsNum,Btn().wayEdit,Btn().account],[Btn().timeLearnEdit,Btn().reportActivity],[Btn().deleteBot,Btn().aboutBot,Btn().uILangNKeyEdit],[Btn().opinion]],"resize_keyboard":True})
        regularHomePageKey = AKeys().secondMenu
        self.bot.sendMessage(self.id,timeLearningChangedMsg,"none",regularHomePageKey)


    #در صورت زدن دکمه «Yes» این  دکمه ها و پیام می آیند 
    def sendYesMessageFAVA(self,year,monthAlpha,day,weekDay,hourMin):
        dash = "___________________________________"
        timeLearningChangedMsg = f"Daily Learning Hour changed to <b> {hourMin} </b>. \n{dash} \n👉Learn Vocabulary Daily👈 Next on {weekDay} {day} {monthAlpha} {year}, <b > At {hourMin} </b> \n @DeutschOhal"
        # regularHomePageKey = json.dumps({"keyboard":[[BtnA().admin,Btn().reviewWords],[Btn().wordsNum,Btn().wayEdit,Btn().account],[Btn().timeLearnEdit,Btn().reportActivity],[Btn().deleteBot,Btn().aboutBot,Btn().uILangNKeyEdit],[Btn().opinion]],"resize_keyboard":True})
        regularHomePageKey = AKeys().secondMenu
        self.bot.sendMessage(self.id,timeLearningChangedMsg,"none",regularHomePageKey)
    #در صورت زدن دکمه «نه» به فهرست آغازین و اصلی این  دکمه ها و پیام می آیند 
    def sendNoMessageFAVA(self):
        fehrestAghazinMsg = "Home"
        # regularHomePageKey = json.dumps({"keyboard":[[BtnA().admin,Btn().reviewWords],[Btn().wordsNum,Btn().wayEdit,Btn().account],[Btn().timeLearnEdit,Btn().reportActivity],[Btn().deleteBot,Btn().aboutBot,Btn().uILangNKeyEdit],[Btn().opinion]],"resize_keyboard":True})
        regularHomePageKey = AKeys().secondMenu
        self.bot.sendMessage(self.id,fehrestAghazinMsg,"none",regularHomePageKey)
        
#تمامی کیبوردها و پیام های بخش «برایند و فرجام»  در فهرست آغازین و اصلی
class AdminBarayandVaFarjam:
    def __init__(self,id,firstName,msg):
        self.id = id
        self.firstName = firstName
        self.msg = msg
        self.bot = pybotc.Bot("config.cfg")
        self.obj_AYVK = AghazYadgiriVazhehayeKetab(id,firstName,msg)
    #در صورت زدن دکمه «برایند و فرجام»  این  دکمه ها و پیام می آیند 
    def sendBVFMessageReports(self):
        reportPageMsg = f"selected { self.msg }."
        # reportKey = json.dumps({"keyboard":[[Btn().reportWordsPartions, Btn().reportWeakWords],[Btn().getBack]], "resize_keyboard": True})
        reportKey = Keys().reportKeys
        self.bot.sendMessage(self.id,reportPageMsg,"none",reportKey)

    #در صورت زدن دکمه «گزارش واژگان در بخش ها📈»  این  دکمه ها و پیام می آیند 
    def sendReportAllWordsMessageBBFA(self,num,reportWordsSectionsPercentage):
        dash = "___________________________________" 
        reportWordsSectionsMsg = f"Dear {self.firstName} 🌺🌸, Report all your used vocabulary in the partitions, to date: \n {dash} \n \n Number of all vocabulary done to date: {num} \n {dash} \n  Number And the percentage of all words in all partitions of the Leitner box: \n \n {reportWordsSectionsPercentage} \n \n @DeutschOhal"
        # backToHomePage = json.dumps({"keyboard":[[Btn().getBack]],"resize_keyboard":True})
        backToHomePage = Keys().getBackKeys
        self.bot.sendMessage(self.id,reportWordsSectionsMsg,"none",backToHomePage)
    #در صورت زدن دکمه «گزارش ناتوانی در واژگان📉»  این  دکمه ها و پیام می آیند 
    # wWDS,wWPGS
    def sendReportWeakWordMessageBBFA(self,wWDS,wWPGS):
        dash = "___________________________________"
        reportWordsSectionsMsg = f"Dear {self.firstName} 🌺🌸, Report the most Weak Vocabulary in learning to date \n (weak  vocabulary means words that have not yet been completed learning for more than a month) \n  {dash} \n A list of vocabulary that has lasted more than a month with the number of days and partition \n\n  <b> {wWDS.center(63)} </b> \n  {dash} \n  Incorrect vocabulary list Percentage order in Leitner box partitions \n\n  {wWPGS} \n  @DeutschOhal "
        # backToHomePage = json.dumps({"keyboard":[[Btn().getBack]],"resize_keyboard":True})
        backToHomePage = Keys().getBackKeys
        self.bot.sendMessage(self.id,reportWordsSectionsMsg,"none",backToHomePage)
    #در صورت زدن دکمه «بازگشت به فهرست آغازین🏡»  این  دکمه ها و پیام می آیند 
    #FIXME حذف این تابع از کیبورد و جایگزینی در آنالیز AYVK.sendKeyAndMessageFAVA()
    def sendBBFAMessageFAVA(self):
        self.obj_AYVK.sendKeyAndMessageFAVA()

    def reportWeakWords(self,wWDS,wWPGS): 
        dash = "___________________________________"   
        reportMsg = f"\n Dear {self.firstName}🌺🌸, to date, Report the most Weak Vocabulary in learning, \n  {dash.center(73)} \n\n  List of vocabulary that has lasted over a month of learning, expressing the number of days \n\n  {wWDS} \n  {dash.center(73)} \n\n  Weak Vocabulary in order of percentage of each partition of the Leitner box \n\n  {wWPGS} \n  @DeutschOhal"
        # backToHomePage = json.dumps({"keyboard":[[Btn().getBack]],"resize_keyboard":True})
        backToHomePage = Keys().getBackKeys
        self.bot.sendMessage(self.id,reportMsg,"none",backToHomePage)

#تمامی کیبوردها و پیام های بخش «📝 زبان پیام و کیبورد ⌨  پوسته» در فهرست آغازین و اصلی  
class AdminDegarsaniZaban2:
    def __init__(self,id,firstName,msg):
        self.id = id
        self.firstName = firstName
        self.msg = msg
        self.bot = pybotc.Bot("config.cfg")
        self.obj_Start = Start(id,firstName,msg)
    #در صورت زدن دکمه 📝 زبان پیام و کیبورد ⌨ این دکمه ها و پیام می آیند    
    def sendKeyAndMessageUI2(self):
         languageMsg = f"Dear {self.firstName} 🌺🌸, select your favorite language for bots message and keyboard"
         
        #  languagesKey = json.dumps({"keyboard":[[BtnS().keyNMsgDe],["English Keyboard and Message⌨️💬"],[BtnS().keyNMsgPer],[Btn().getBack]],"resize_keyboard":True}) 
         languagesKey = Keys().lanKeys
         self.bot.sendMessage(self.id,languageMsg,"none",languagesKey)
    
        #در صورت انتخاب و زدن <پوسته فارسی> به فهرست آغازین و اصلی منتقل شده و این  دکمه ها و پیام می آیند 
    def sendBaleKeyAndMessageFAVA(self): 
        languageSelectedMsg = f"{self.msg} is chosen for bot."
        # regularHomePageKey = json.dumps({"keyboard":[[BtnA().admin,Btn().reviewWords],[Btn().wordsNum,Btn().wayEdit,Btn().account],[Btn().timeLearnEdit,Btn().reportActivity],[Btn().deleteBot,Btn().aboutBot,Btn().uILangNKeyEdit],[Btn().opinion]],"resize_keyboard":True})
        regularHomePageKey = AKeys().secondMenu
        self.bot.sendMessage(self.id,languageSelectedMsg,"none",regularHomePageKey)




        # self.obj_Start.sendKeyAndMessagesUI()
    #    یا کیبورد و پیام پارسی⌨💬 این دکمه ها و پیام از فهرست آغازین و اصلی  می آیند  deutsch Menu, english Menu  در صورت زدن یکی از دکمه های  
    def sendKeyAndMessageFNVA2(self):
        languageSelectedMsg = f"{self.msg} is chosen for bot."
        # regularHomePageKey = json.dumps({"keyboard":[[BtnA().admin,Btn().reviewWords],[Btn().wordsNum,Btn().wayEdit,Btn().account],[Btn().timeLearnEdit,Btn().reportActivity],[Btn().deleteBot,Btn().aboutBot,Btn().uILangNKeyEdit],[Btn().opinion]],"resize_keyboard":True})
        regularHomePageKey = AKeys().secondMenu
        self.bot.sendMessage(self.id,languageSelectedMsg,"none",regularHomePageKey)


#تمامی کیبوردها و پیام های بخش درباره ربات ℹ️ در فهرست آعازین واصلی
class AdminDarbarehRobat2:
    def __init__(self,id,firstName,msg):
        self.id = id
        self.firstName = firstName
        self.msg = msg
        self.bot = pybotc.Bot("config.cfg")
    #در صورت زدن دکمه درباره ربات ℹ️ در بخش آعازین واصلی این دکمه ها و پیام می آیند    
    def sendKeyAndMessageDarbarehRobat2(self):
        aboutMsg =f" Greetings Dear <i> {self.firstName} </i>🌺🌸, \n This robot can learn all the new and emphasized words of the book <b>'Großes Übungsbuch Wortschatz'</b>  in the context of Leitner's repetition and practice daily in the calendar structure. With the ability to remind you and choose the answer in German, it enables synonyms, English and Persian using authentic German language resources, so that full mastery of a word and word is achieved in at least one month. From your short-term memory, it will be in your long-term memory." 
        # regularHomePageKey = json.dumps({"keyboard":[[BtnA().admin,Btn().reviewWords],[Btn().wordsNum,Btn().wayEdit,Btn().account],[Btn().timeLearnEdit,Btn().reportActivity],[Btn().deleteBot,Btn().aboutBot,Btn().uILangNKeyEdit],[Btn().opinion]],"resize_keyboard":True})
        regularHomePageKey = AKeys().secondMenu
        self.bot.sendMessage(self.id,aboutMsg,"none",regularHomePageKey)

#FIXME copy these 4 method to every user language
    def sendKeyAndMessageSendingSugession(self):
        aboutMsg =f"Dear <i>{self.firstName}</i>🌺🌸, Any comments, criticisms or suggestions you have, please send them to us."
        # backToHomePage = json.dumps({"keyboard":[[Btn().getBack]],"resize_keyboard":True})
        backToHomePage = Keys().getBackKeys
        self.bot.sendMessage(self.id,aboutMsg,"none",backToHomePage)

    def sendKeyAndMessageDeliverOpinion(self,opId):
        aboutMsg =f"Dear <i>{self.firstName}</i>🌺🌸,Your comment was registered,  with this <b>{opId}</b> tracking number."
        # regularHomePageKey = json.dumps({"keyboard":[[Btn().reviewWords],[Btn().wordsNum,Btn().wayEdit,Btn().account],[Btn().timeLearnEdit,Btn().reportActivity],[Btn().deleteBot,Btn().aboutBot,Btn().uILangNKeyEdit],[Btn().opinion]],"resize_keyboard":True})
        regularHomePageKey = AKeys().secondMenu
        self.bot.sendMessage(self.id,aboutMsg,"none",regularHomePageKey)

    def sendKeyAndMessageUsingBotKeys(self):
        aboutMsg =f"No text entered! If you want to send a comment, <b>without using the Bot keyboard</b>, enter the text and then send it."
        # regularHomePageKey = json.dumps({"keyboard":[[Btn().reviewWords],[Btn().wordsNum,Btn().wayEdit,Btn().account],[Btn().timeLearnEdit,Btn().reportActivity],[Btn().deleteBot,Btn().aboutBot,Btn().uILangNKeyEdit],[Btn().opinion]],"resize_keyboard":True})
        regularHomePageKey = Keys().secondMenu
        self.bot.sendMessage(self.id,aboutMsg,"none",regularHomePageKey)

    def sendKeyAndMessageOutOfRangeMsg(self):
        aboutMsg =f"The number of characters and words sent is too much! Send your text shorter or in several sections."
        # regularHomePageKey = json.dumps({"keyboard":[[Btn().reviewWords],[Btn().wordsNum,Btn().wayEdit,Btn().account],[Btn().timeLearnEdit,Btn().reportActivity],[Btn().deleteBot,Btn().aboutBot,Btn().uILangNKeyEdit],[Btn().opinion]],"resize_keyboard":True})
        regularHomePageKey = Keys().secondMenu
        self.bot.sendMessage(self.id,aboutMsg,"none",regularHomePageKey)

#تمامی کیبوردها و پیام های بخش «Remove bot 🗑» در فهرست آعازین واصلی
class AdminHazfbot:
    def __init__(self,id,firstName,msg):
        self.id = id
        self.firstName = firstName
        self.bot = pybotc.Bot("config.cfg")   
        self.obj_AYVK = AghazYadgiriVazhehayeKetab(id,firstName,msg)

    #    self.Hazfbot(id,firstName,msg).sendHRKeyAndMessageYesNo()

    #در صورت زدن دکمه «Remove bot 🗑»  این دکمه ها و پیام می آیند    
    def sendHRKeyAndMessageYesNo(self):
        deleteBotWarnMsg = f"Dear {self.firstName} 🌺🌸, are you sure to deleting bot? cause by that all of your records will be deleted as well, beside no more message sending to you."
        # yesNoKey = json.dumps({"keyboard":[[Btn().no,Btn().yesDelete]],"resize_keyboard":True}) 
        yesNoKey = Keys().yNKeys
        self.bot.sendMessage(self.id,deleteBotWarnMsg,"none",yesNoKey)
    #در صورت زدن دکمه «Yes» به بخش فهرست نخستین🛎 و اولیه منتقل شده و   این دکمه ها و پیام می آیند    
    def sendYesKeyAndMessageFNVA(self):
        deleteBotMsg = "Bot is deleted!"
        # firstHomePageKey = json.dumps({"keyboard":[[BtnA().admin, Btn().startLearning],[Btn().aboutBotNew, Btn().uILangNKeyEditNew]], "resize_keyboard": True})
        firstHomePageKey = AKeys().firstMenu
        self.bot.sendMessage(self.id,deleteBotMsg,"none",firstHomePageKey)

    #در صورت زدن دکمه «No» به بخش فهرست آغازین و اصلی منتقل شده و   این دکمه ها و پیام می آیند   
    #FIXME حذف این تابع از کیبورد و جایگزینی در آنالیز AYVK.sendKeyAndMessageFAVA() 
    def sendNoKeyAndMessageFAVA(self):
        self.obj_AYVK.sendKeyAndMessageFAVA()



#تمامی کیبوردها و پیام های بخش «دگرسانی زبان» در فهرست آعازین واصلی


#تمامی کیبوردها و پیام های بخش «یادگیری واژگان روزانه» 
class AdminYadgiriVazheganRuzaneh:
    def __init__(self,id,firstName,msg):
        self.id = id
        self.firstName = firstName
        self.msg = msg
        self.obj_AYVK = AghazYadgiriVazhehayeKetab(id,firstName,msg)
        self.bot = pybotc.Bot("config.cfg")

