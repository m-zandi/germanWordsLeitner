import json
import requests
import sys
sys.path.append( "../")

from mainV2.base.Buttons import ButtonDe as Btn
from mainV2.base.Buttons import ButtonSame as BtnS
from mainV2.base.ButtonsA import ButtonAdminDe as BtnA 
from mainV2.base.Keys import SKeys
from mainV2.base.Keys import DeKeys as Keys 
from mainV2.base.KeysA import DeKeysA as AKeys
from mainV2.base import Txt
from mainV2.base.Txt import MessageNVarDe as MNV

from mainV2.set import dbContact
import pybotc

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
        self.obj_dbContatct = dbContact


    def memberChannel(self,chat_id):
         keys = ""
         msg = MNV(self.firstName).memberInCannel(chat_id)
         self.bot.sendMessage(self.id,msg,"HTML",keys)


    #این دکمه ها و پیام  می آیند Start در صورت زدن دکمه
    def sendKeyAndMessagesUI(self):
         languageMsg =  f"Liebe/Lieber {self.firstName} 🌺🌸, wählen Sie Ihre Lieblingssprache für Bots-Nachricht und Tastatur"
        #  languagesKey = json.dumps({"keyboard":[[BtnS().keyNMsgDe],[BtnS().keyNMsgEn],[BtnS().keyNMsgPer]],"resize_keyboard":True})
         languagesKey = SKeys(Btn(),MNV()).uI
         self.bot.sendMessage(self.id,languageMsg,"none",languagesKey)

   #    یا کیبورد و پیام پارسی⌨💬 این دکمه ها و پیام از فهرست نخستین🛎 و اولیه  می آیند  deutsch Menu, english Menu  در صورت زدن یکی از دکمه های  
    def sendKeyAndMessageFNVAUIselected(self):
        languageSelectedMsg = f"{self.msg} ist für bot ausgewählt"
        # firstHomePageKey = json.dumps({"keyboard": [[Btn().startLearning], [Btn().aboutBotNew, Btn().uILangNKeyEditNew]], "resize_keyboard": True})
        firstHomePageKey = Keys().firstMenu
        self.bot.sendMessage(self.id,languageSelectedMsg,"none",firstHomePageKey)
    

    def sendKeyAndMessageFNVAUINakhostin(self):
        languageSelectedMsg = "Menü🛎"
        # firstHomePageKey = json.dumps({"keyboard": [[Btn().startLearning], [Btn().aboutBotNew, Btn().uILangNKeyEditNew]], "resize_keyboard": True})
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
        msgNextTrainingTimeDate =  f"Liebe/Lieber <i> {self.firstName} </i>  🌺🌸 Deine Konto\n{ent}\n{output}\n{dash}\n {outpuTodayDateNTime}\n @DeutschOhal"
        # regularHomePageKey = json.dumps({"keyboard":[[Btn().reviewWords],[Btn().wordsNum,Btn().wayEdit,Btn().account],[Btn().timeLearnEdit,Btn().reportActivity],[Btn().deleteBot,Btn().aboutBot,Btn().uILangNKeyEdit],[Btn().opinion]],"resize_keyboard":True})
        regularHomePageKey = Keys().secondMenu
        self.bot.sendMessage(self.id,msgNextTrainingTimeDate,"none",regularHomePageKey)


    #در صورت زدن دکمه ((آعاز یادگیری واژه های کتاب)) این دکمه ها و پیام می آیند
    def sendAYVKKeyAndMessage327(self):
        wortZahlMsg = f"Liebe/Lieber {self.firstName} 🌺🌸, wie viele neue Wörter möchten Sie an einem Tag?"        
        # wortZahlKey = json.dumps({"keyboard":[[BtnS().threeNew],[BtnS().twoNew],[BtnS().oneNew]],"resize_keyboard":True})
        wortZahlKey = SKeys(Btn(),MNV()).numWordsNew
        self.bot.sendMessage(self.id,wortZahlMsg,"none",wortZahlKey)
    #در صورت زدن یکی از دکمه های ۳ یا ۵  یا ۷ این دکمه ها و پیام می آیند
    def send357KeyAndMessageDESP(self):
        wayMsg = f"Liebe/Lieber {self.firstName} 🌺🌸, wähle die Methode zum Lernen von Buchwörtern"
        # wayKey = json.dumps({"keyboard":[[BtnS().deutschNew],[BtnS().englishNew],[BtnS().synonymNew],[BtnS().persianNew]],"resize_keyboard":True}) 
        wayKey = SKeys(Btn(),MNV()).waysNew
        self.bot.sendMessage(self.id,wayMsg,"none",wayKey)

    

     #    یا پارسی این دکمه و پیام می آیند  deutsch , english , synonym  در صورت زدن یکی از دکمه های  
    def sendDESPKeyAndMessageLampGuid(self,way,wKind,numW,numAll,standardizedWord,content,chapter,wordsPage,wordLink):
        dash = "___________________________________"
        guide = f"Hinweis🔔: Lies das Wort und sage {way} dazu und erinnere dich daran. Tippe dann auf 💡, um die richtige Antwort zu sehen und sie mit deiner Antwort zu vergleichen."
        

        newWordsMsg = f".{numW}/{numAll}                                         {wKind}.<b>{standardizedWord.center(63)}</b>\n.Kapitel : {content}\nAbschnitt : {chapter} \nSeite:{wordsPage}.\n{dash}\n{wordLink}{guide}"


        # {content}\n{cotentNChap} \nبرگ:{wordsPage}
        # antwortKey = json.dumps({"keyboard":[[BtnS().lamp]],"resize_keyboard":True}) 
        antwortKey = SKeys(Btn(),MNV()).lampKeys
        self.bot.sendMessage(self.id,newWordsMsg,"none",antwortKey)


                               
   #    یا پارسی این دکمه و پیام می آیند  deutsch , english , synonym  در صورت زدن یکی از دکمه های  
    def sendDESPKeyAndMessageLamp(self,wKind,numW,numAll,standardizedWord,content,chapter,wordsPage,wordLink):


        newWordsMsg = f".{numW}/{numAll}                                         {wKind}.\n<b>{standardizedWord}</b>\n.Kapitel : {content}\nAbschnitt : {chapter} \nSeite:{wordsPage}.\n. \n {wordLink} "
        # {content}\n{cotentNChap} \nبرگ:{wordsPage}
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
        guide = "Hinweis🔔: Wenn Sie die gesendete Antwort und Ihre Antwort überprüfen, wählen Sie Ihre Antwort richtig oder falsch aus, indem Sie ❌ oder ✅ auswählen."

        pa = f"Antworte in {way} {icon}"
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
        pa = f"Antworte in {way} {icon}"
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
        guide = f"🔔 Nachdem Sie auf'{Btn().getBack}' getippt haben, können Sie '{Btn().reviewWords}' auswählen, um die von Ihnen eingegebenen Wörter zu überprüfen."

        daliyReport = f"Liebe/Lieber <i>{self.firstName}</i>🌺🌸  Melde deine Aktivitäten heute:  \n{dash.center(14)}\n Anzahl der geübten Wörter: <b> {nWorkedWords} </b> \n Anzahl der richtigen Wörter: <b>{nRWords}</b>\n Anzahl der falschen Wörter: <b>{nWWrong}</b>\n{dash.center(14)}\n<i> Prozentsatz der richtigen und falschen Wörter: </i> \n Richtig <b> {graphRight}% {percentageRight} </b> \n falsch <b> {graphWrong}% {percentageWrong} </b> \n {dash.center(14)} \n Liste der heute falschen Wörter mit der Seitenadresse im Buch: \n <b> {wrongWordsNpages} </b> \n {dash.center(14)} \n The 👉Lern den Wortschatz täglich👈 Weiter am <b> {weekDay} {day} {month} {year} </b>, um <b>{houNMTraining}</b> In der Zeit des Iran, Fällt zusammen mit <b>{dateGriNextTraining}</b> \n{dash}\n<i>Partition und Anzahl aller Wörter in der Lightner-Box: </i>\nWortnummer in der 1. Partition: <b>{wordsSectionPosition[0]} </b> \n Wortnummer in der 2. Partition: <b> {wordsSectionPosition[1]} </b> \n Wortnummer in der 3. Partition: <b> {wordsSectionPosition[2]} </b> \n Wortnummer in der 4. Partition: <b> {wordsSectionPosition[3]} </b> \n Wortnummer in der 5. Partition: <b> {wordsSectionPosition[4]} </b> \n Wortnummer in der 6. Partition: <b> {wordsSectionPosition[5]} </b> \n {dash} \n Anzahl der vollständig erlernten Vokabeln: <b> {wordsSectionPosition[6]} </b> \n {dash} \n <i> {guide} </i> \n @DeutschOhal \n"



        print(f"daily report = {daliyReport}")
        # backToHomePage = json.dumps({"keyboard":[[Btn().getBack]],"resize_keyboard":True})
        backToHomePage = Keys().getBackKeys
        self.bot.sendMessage(self.id,daliyReport,"none",backToHomePage)
       
    # فرستادن تاریخ و زمان یادگیری واژگان بعدی پسین
    def sendNextTrainingDateTimeKeyAndMessageBBFA(self,weekDay,day,monthAlpha,year,hourMin):
        # y = "یادگیری واژگان روزانه"
        msgNextTrainingTimeDate = f"Liebe/Lieber <i> {self.firstName} </i>🌺🌸, 👉Lern den Wortschatz täglich👈 als nächstes am <b> {weekDay} {day} {monthAlpha} {year} </b>, um <b> {hourMin} </b>. \n@DeutschOhal"


        # regularHomePageKey = json.dumps({"keyboard":[[Btn().reviewWords],[Btn().wordsNum,Btn().wayEdit,Btn().account],[Btn().timeLearnEdit,Btn().reportActivity],[Btn().deleteBot,Btn().aboutBot,Btn().uILangNKeyEdit],[Btn().opinion]],"resize_keyboard":True})
        regularHomePageKey = Keys().secondMenu
        self.bot.sendMessage(self.id,msgNextTrainingTimeDate,"none",regularHomePageKey)





     #در صورت زدن  دکمه بازگشت به فهرست آغازین🏡 به بخش فهرست آغازین و اصلی منتقل شده و این دکمه ها و پیام می آیند 
     #FIXME حذف این تابع از کیبورد و جایگزینی در آنالیز AYVK.sendKeyAndMessageFAVA()
    def sendKeyAndMessageFAVA(self):
        fehrestAghazinMsg = "Startseite"
        # regularHomePageKey = json.dumps({"keyboard":[[Btn().reviewWords],[Btn().wordsNum,Btn().wayEdit,Btn().account],[Btn().timeLearnEdit,Btn().reportActivity],[Btn().deleteBot,Btn().aboutBot,Btn().uILangNKeyEdit],[Btn().opinion]],"resize_keyboard":True})
        regularHomePageKey = Keys().secondMenu
        self.bot.sendMessage(self.id,fehrestAghazinMsg,"none",regularHomePageKey)

    def sendKeyAndMessageUserMustWait(self):
        fehrestAghazinMsg = "Bis zum nächsten Datum"
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
        msgWarning ="⛔️😡😡⛔️ Vermeiden Sie das Versenden von Spam ⛔️😡😡⛔️"
        # antwortKey = json.dumps({"keyboard":[[BtnS().lamp]],"resize_keyboard":True}) 
        # antwortKey = SKeys(Btn(),MNV()).lampKeys
        antwortKey = ""
        self.bot.sendMessage(self.id,msgWarning,"none",antwortKey)

        #spam warning هنگامه آخرین واژه BtnS().crossCheck,"✅ پیام خطا به جهت فرستادن تکراری 
    def sendWarningKeyAndMessageBBFA(self):
        msgWarning ="⛔️😡😡⛔️ Vermeiden Sie das Versenden von Spam ⛔️😡😡⛔️"
        # backToHomePage = json.dumps({"keyboard":[[Btn().getBack]],"resize_keyboard":True})
        # backToHomePage = Keys().getBackKeys
        backToHomePage = ""
        self.bot.sendMessage(self.id,msgWarning,"none",backToHomePage)
     
    #spam warning  پیام خطا به جهت فرستادن تکراری برای کاربری که هنوز نام نویسی نشده 
    def sendWarningRepeatedKeyAndMessageToNoneUser(self):
        msgWarning = "⛔️😡😡⛔️ Vermeiden Sie das Versenden von Spam ⛔️😡😡⛔️"
        # firstHomePageKey = json.dumps({"keyboard": [[Btn().startLearning], [Btn().aboutBotNew, Btn().uILangNKeyEdit]], "resize_keyboard": True}) 
        firstHomePageKey = ""
        self.bot.sendMessage(self.id,msgWarning,"none",firstHomePageKey)


    #spam warning  پیام خطا به جهت فرستادن تکراری برای کاربر  
    def sendWarningRepeatedKeyAndMessageToUser(self):
        msgWarning = "⛔️😡😡⛔️ Vermeiden Sie das Versenden von Spam ⛔️😡😡⛔️"
        # regularHomePageKey = json.dumps({"keyboard":[[Btn().reviewWords],[Btn().wordsNum,Btn().wayEdit,Btn().account],[Btn().timeLearnEdit,Btn().reportActivity],[Btn().deleteBot,Btn().aboutBot,Btn().uILangNKeyEdit],[Btn().opinion]],"resize_keyboard":True})
        # regularHomePageKey = Keys().secondMenu
        regularHomePageKey = ""
        self.bot.sendMessage(self.id,msgWarning,"none",regularHomePageKey) 

   
      #none keyboard warning  پیام خطا به جهت عدم استفاده از کیبورد رباط  
    def sendWarningNoneKeyboardToUser(self):
        msgWarning = "Verwenden Sie nur die Bottastatur!"
        # regularHomePageKey = json.dumps({"keyboard":[[Btn().reviewWords],[Btn().wordsNum,Btn().wayEdit,Btn().account],[Btn().timeLearnEdit,Btn().reportActivity],[Btn().deleteBot,Btn().aboutBot,Btn().uILangNKeyEdit],[Btn().opinion]],"resize_keyboard":True})
        regularHomePageKey = Keys().secondMenu
        # regularHomePageKey=""
        self.bot.sendMessage(self.id,msgWarning,"none",regularHomePageKey) 

      #none keyboard warning  پیام خطا به جهت عدم استفاده از کیبورد رباط  
    def sendWarningNoneKeyboardToGuest(self):
        msgWarning = "Verwenden Sie nur die Bottastatur!"
        # firstHomePageKey = json.dumps({"keyboard": [[Btn().startLearning], [Btn().aboutBotNew, Btn().uILangNKeyEditNew]], "resize_keyboard": True}) 
        firstHomePageKey = Keys().firstMenu
        # firstHomePageKey =""
        self.bot.sendMessage(self.id,msgWarning,"none",firstHomePageKey) 


class AutomaticMessage:
    def __init__(self,id,firstName):
        self.id = id
        self.bot = pybotc.Bot("config.cfg")
        self.firstName = firstName
    def sendKeyAndMessageDailyLearn(self):
        msg = f"Liebe/Lieber <i> {self.firstName} </i> 🌺🌸, beginne mit dem Lernen und Üben von Vokabeln, tippe auf '👉👉Lern den Wortschatz täglich👈👈'!" 
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
        aboutMsg =f"Grüße Liebe/Lieber <i> {self.firstName} </i>🌺🌸, Dieser Bot kann alle neuen und hervorgehobenen Wörter des Buches <b>'Großes Übungsbuch Wortschatz'</b> im Kontext von Leitners Wiederholung lernen und täglich in der Kalenderstruktur üben. Mit der Möglichkeit, Sie daran zu erinnern und die Antwort auf Deutsch zu wählen, werden Synonyme, Englisch und Persisch unter Verwendung authentischer deutscher Sprachressourcen aktiviert, sodass die vollständige Beherrschung eines Wortes und eines Wortes in mindestens einem Monat erreicht wird. Aus Ihrem Kurzzeitgedächtnis wird es in Ihrem Langzeitgedächtnis sein."
        # firstHomePageKey = json.dumps({"keyboard": [[Btn().startLearning], [Btn().aboutBotNew, Btn().uILangNKeyEditNew]], "resize_keyboard": True}) 
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
        reviewMsg = f"Liebe/Lieber {self.firstName} 🌺🌸, Wählen Sie die Methode zur Überprüfung des Wortschatzes basierend auf einer der Optionen."
        
        # reviewKey = json.dumps({"keyboard": [[Btn().chapterNSection], [Btn().leitnerBoxParts], [Btn().weakWords], [Btn().getBack]], "resize_keyboard": True}) 
        reviewKey = Keys().revKeys
        self.bot.sendMessage(self.id,reviewMsg,"none",reviewKey)
        
        #🔎
        ###در صورت زدن دکمه «سرفصل و فصل» در بخش آغازین و اصلی این  دکمه ها و پیام نخستین واژه می آیند 
    def sendWordsChapterContentKeyAndMessageFirstOLdWord(self,content,chapter,word,answer,counter,length,section,page,link):
        oldWordsMsg = f".Kapitel : {content}\nAbschnitt : {chapter}\n\n<b>{word}</b>\n\n{answer.center(63)}\n{link}\n.Seite :{page}                         {section}: {length}/{counter+1}"
        # reviewNextKey = json.dumps({"keyboard":[[Btn().nextWordChapNS],[Btn().getBack]],"resize_keyboard":True}) 
        reviewNextKey = Keys().revChapNexKeys
        self.bot.sendMessage(self.id,oldWordsMsg,"none",reviewNextKey)

    def sendWordsChapterContentKeyAndMessageFirstOLdWordOneLength(self,content,chapter,word,answer,counter,length,section,page,link):
        oldWordsMsg = f".Kapitel : {content}\nAbschnitt : {chapter}\n\n<b>{word}</b>\n\n{answer.center(63)}\n{link}\n.Seite :{page}                         {section}: {length}/{counter+1}"
        # backToHomePage = json.dumps({"keyboard":[[Btn().getBack]],"resize_keyboard":True}) 
        backToHomePage = Keys().getBackKeys
        self.bot.sendMessage(self.id,oldWordsMsg,"none",backToHomePage)




    #سرفصل و فصل- کیبورد حاوی قبلی و بعدی  
    def sendWordsChapterContentKeyAndMessagMiddleOLdWord(self,content,chapter,word,answer,counter,length,section,page,link):
        oldWordsMsg = f".Kapitel : {content}\nAbschnitt : {chapter}\n\n<b>{word}</b>\n\n{answer.center(63)}\n{link}\n.Seite :{page}                         {section}: {length}/{counter+1}"
        # reviewNextKey = json.dumps({"keyboard":[[Btn().beforeWordChapNS,Btn().nextWordChapNS],[Btn().getBack]],"resize_keyboard":True})
        reviewMiddleKeys = Keys().revChapMidKeys 
        self.bot.sendMessage(self.id,oldWordsMsg,"none",reviewMiddleKeys)
    
    #سرفصل و فصل- کیبورد حاوی قبلی و آخرین واژه  
    def sendWordsChapterContentKeyAndMessagLastOLdWord(self,content,chapter,word,answer,counter,length,section,page,link):
        oldWordsMsg = f".Kapitel : {content}\nAbschnitt : {chapter}\n\n<b>{word}</b>\n\n{answer.center(63)}\n{link}\n.Seite :{page}                         {section}: {length}/{counter+1}"
        # reviewBeforeKey = json.dumps({"keyboard":[[Btn().beforeWordChapNS],[Btn().getBack]],"resize_keyboard":True}) 
        reviewBeforeKey = Keys().revChapBefKeys
        self.bot.sendMessage(self.id,oldWordsMsg,"none",reviewBeforeKey)


    #🔭
    ###در صورت زدن دکمه «بخش ها» در بخش آغازین و اصلی این  دکمه ها و پیام نخستین واژه می آیند 
    def sendBakhshhaKeyAndMessageFirstWord(self,counter,length,section,word,answer,page,content,chapter,link):
        oldWordsMsg = f". {section}: {length}/{counter+1}\n<b>{word}</b>\n\n{answer.center(63)}\n\n.Kapitel : {content}\nAbschnitt : {chapter} \n {link} \n Seite :{page}"
        # reviewNextKey = json.dumps({"keyboard":[[Btn().nextWordLeitBP],[Btn().getBack]],"resize_keyboard":True}) 
        reviewNextKey = Keys().revLeitNexKeys
        self.bot.sendMessage(self.id,oldWordsMsg,"none",reviewNextKey)
    # وقتی طول آریه یکی است
    def sendBakhshhaKeyAndMessageFirstWordOneLength(self,counter,length,section,word,answer,page,content,chapter,link):
        oldWordsMsg = f". {section}: {length}/{counter+1}\n<b>{word}</b>\n\n{answer.center(63)}\n\n.Kapitel : {content}\nAbschnitt : {chapter} \n {link} \n Seite :{page}"
        # backToHomePage = json.dumps({"keyboard":[[Btn().getBack]],"resize_keyboard":True}) 
        backToHomePage = Keys().getBackKeys
        self.bot.sendMessage(self.id,oldWordsMsg,"none",backToHomePage)


        #بخش ها- کیبورد حاوی قبلی و بعدی 
    def sendBakhshhaKeyAndMessageMiddleWord(self,counter,length,section,word,answer,page,content,chapter,link):
        oldWordsMsg = f". {section}: {length}/{counter+1}\n<b>{word}</b>\n\n{answer.center(63)}\n\n.Kapitel : {content}\nAbschnitt : {chapter} \n {link} \n Seite :{page}"
        #اگر واژه ای بعد از این هنوز موجود باشد
        # reviewBackNextKey = json.dumps({"keyboard":[[Btn().beforeWordLeitBP,Btn().nextWordLeitBP],[Btn().getBack]],"resize_keyboard":True}) 
        reviewBackNextKey = Keys().revLeitMidKeys
        self.bot.sendMessage(self.id,oldWordsMsg,"none",reviewBackNextKey)

        #بخش ها- کیبورد حاوی قبلی  
    def sendBakhshhaKeyAndMessageLastWord(self,counter,length,section,word,answer,page,content,chapter,link):
        oldWordsMsg = f". {section}: {length}/{counter+1}\n<b>{word}</b>\n\n{answer.center(63)}\n\n.Kapitel : {content}\nAbschnitt : {chapter} \n {link} \n Seite :{page}"
        #اگر واژه ای بعد از این دیگر موجود نباشد
        # reviewBackKey = json.dumps({"keyboard":[[Btn().beforeWordLeitBP],[Btn().getBack]],"resize_keyboard":True}) 
        reviewBackKey = Keys().revLeitBefKeys
        self.bot.sendMessage(self.id,oldWordsMsg,"none",reviewBackKey)

    #🔬
    ###در صورت زدن دکمه «واژگان ناتوان» در بخش آغازین و اصلی این  دکمه ها و پیام نخستین واژه می آیند 
    def sendWeakWordsKeyAndMessageFirstOLdWord(self,durationDays,counter,length,section,word,answer,content,chapter,page,link):
        oldWordsMsg = f".Tage Nummer: {durationDays}         {section}:{counter+1}/{length}.\n\n<b>{word}</b>\n\n{answer.center(63)}\n\n Kapitel : {content}\nAbschnitt : {chapter} \n {link} \n{page}:Seite"
        # برگ:{page}
        # {page}:برگ
        # reviewNextKey = json.dumps({"keyboard":[[Btn().nextWordWW],[Btn().getBack]],"resize_keyboard":True}) 
        reviewNextKey = Keys().revWeakNexKeys
        self.bot.sendMessage(self.id,oldWordsMsg,"none",reviewNextKey)
    #اگر طول آرایه یک بود
    def sendWeakWordsKeyAndMessageFirstOLdWordOneLength(self,durationDays,counter,length,section,word,answer,content,chapter,page,link):
        oldWordsMsg = f".Tage Nummer: {durationDays}         {section}:{counter+1}/{length}.\n\n<b>{word}</b>\n\n{answer.center(63)}\n\n Kapitel : {content}\nAbschnitt : {chapter} \n {link} \n{page}:Seite"
        # برگ:{page}
        # {page}:برگ
        # reviewNextKey = json.dumps({"keyboard":[[Btn().getBack]],"resize_keyboard":True}) 
        backToHomePage = Keys().getBackKeys
        self.bot.sendMessage(self.id,oldWordsMsg,"none",backToHomePage)


 
    def sendWeakWordsKeyAndMessageNoWord(self):
        noWeakWordMsg = f"Liebe/Lieber <i> {self.firstName} </i>🌺🌸, du hast keinen schwachen Wortschatz!"
        # برگ:{page}
        # {page}:برگ
        # regularHomePageKey = json.dumps({"keyboard":[[Btn().reviewWords],[Btn().wordsNum,Btn().wayEdit,Btn().account],[Btn().timeLearnEdit,Btn().reportActivity],[Btn().deleteBot,Btn().aboutBot,Btn().uILangNKeyEdit],[Btn().opinion]],"resize_keyboard":True})
        regularHomePageKey = Keys().secondMenu
        self.bot.sendMessage(self.id,noWeakWordMsg,"none",regularHomePageKey)   

    def sendWeakWordsKeyAndMessageNoWordOtherReview(self):
        noWeakWordMsg = f"Liebe/Lieber <i>{self.firstName}</i>🌺🌸, du hast bisher noch kein Wort und keine Übung gemacht!"
        regularHomePageKey = Keys().secondMenu
        self.bot.sendMessage(self.id,noWeakWordMsg,"none",regularHomePageKey)


    #واژگان ناتوان- کیبورد حاوی قبلی و بعدی  
    def sendWeakWordsKeyAndMessagMiddleOLdWord(self,durationDays,counter,length,section,word,answer,content,chapter,page,link):
        oldWordsMsg = f".Tage Nummer: {durationDays}         {section}:{counter+1}/{length}.\n\n<b>{word}</b>\n\n{answer.center(63)}\n\n Kapitel : {content}\nAbschnitt : {chapter} \n {link} \n{page}:Seite"
        # reviewNextKey = json.dumps({"keyboard":[[Btn().beforeWordWW,Btn().nextWordWW],[Btn().getBack]],"resize_keyboard":True}) 
        reviewNextKey = Keys().revWeakMidKeys
        self.bot.sendMessage(self.id,oldWordsMsg,"none",reviewNextKey)
    #واژگان ناتوان- کیبورد حاوی قبلی و آخرین واژه  
    def sendWeakWordsKeyAndMessagLastOLdWord(self,durationDays,counter,length,section,word,answer,content,chapter,page,link):
        oldWordsMsg = f".Tage Nummer: {durationDays}         {section}:{counter+1}/{length}.\n\n<b>{word}</b>\n\n{answer.center(63)}\n\n Kapitel : {content}\nAbschnitt : {chapter} \n {link} \n{page}:Seite"
        # reviewNextKey = json.dumps({"keyboard":[[Btn().beforeWordWW],[Btn().getBack]],"resize_keyboard":True}) 
        reviewNextKey = Keys().revWeakBefKeys
        self.bot.sendMessage(self.id,oldWordsMsg,"none",reviewNextKey)







     #در صورت زدن  دکمه بازگشت به فهرست آغازین🏡 به بخش فهرست آغازین و اصلی منتقل شده و این دکمه ها و پیام می آیند 
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

    #در صورت زدن دکمه «📝 روش 🛣»  این  دکمه ها و پیام می آیند
    def send357KeyAndMessageDESP(self):
        waysMsg = f"Liebe/Lieber {self.firstName} 🌺🌸, wähle die Methode zum Lernen von Buchwörtern"
        # wayKey = json.dumps({"keyboard":[[BtnS().deutsch,BtnS().english],[BtnS().synonym,BtnS().persian],[Btn().getBack]],"resize_keyboard":True}) 
        wayKey = Keys().ways 
        self.bot.sendMessage(self.id,waysMsg,"none",wayKey)
        



     #    یا پارسی  این دکمه ها و پیام می آیند  deutsch , english , synonym  در صورت زدن یکی از دکمه های  
    def sendDESPAllKeyAndMessageYesNo(self,way): 
        waysWarningMsg = f"Liebe/Lieber {self.firstName} 🌺🌸, Sind Sie sicher, dass Sie die neue Methode <b> {self.msg} </b> auswählen möchten, denn wenn Sie auswählen, wird Ihr vorheriger Datensatz <b> {way} ausgewählt. </b> für bearbeitete Wörter werden gelöscht?"
        # yesNoKey = json.dumps({"keyboard":[[Btn().yesDot, Btn().noDot]],"resize_keyboard":True})
        yesNoKey = Keys().yNDot
        self.bot.sendMessage(self.id,waysWarningMsg,"none",yesNoKey)


   #    یا پارسی و یکسان بودن با روش قبلی این دکمه ها و پیام می آیند  deutsch , english , synonym  در صورت زدن یکی از دکمه های  
    def sendDESPAllSameKeyAndMessageFAVA(self): 
        waysWarningMsg = f"Ihre Methode ist derzeit <b> {self.msg} </b>. Sie müssen nicht geändert werden."
        # regularHomePageKey = json.dumps({"keyboard":[[Btn().reviewWords],[Btn().wordsNum,Btn().wayEdit,Btn().account],[Btn().timeLearnEdit,Btn().reportActivity],[Btn().deleteBot,Btn().aboutBot,Btn().uILangNKeyEdit],[Btn().opinion]],"resize_keyboard":True})
        regularHomePageKey = Keys().secondMenu
        self.bot.sendMessage(self.id,waysWarningMsg,"none",regularHomePageKey)

    #در صورت زدن دکمه «بله» به فهرست آغازین و اصلی منتقل شده و این  دکمه ها و پیام می آیند 
    def sendBaleKeyAndMessageFAVA(self): 
        waysChangedMsg = "📝 روش 🛣 به {} انجام شد".format(self.msg)
        # regularHomePageKey = json.dumps({"keyboard":[[Btn().reviewWords],[Btn().wordsNum,Btn().wayEdit,Btn().account],[Btn().timeLearnEdit,Btn().reportActivity],[Btn().deleteBot,Btn().aboutBot,Btn().uILangNKeyEdit],[Btn().opinion]],"resize_keyboard":True})
        regularHomePageKey = Keys().secondMenu
        self.bot.sendMessage(self.id,waysChangedMsg,"none",regularHomePageKey)

   #در صورت زدن دکمه «خیر» به فهرست آغازین و اصلی منتقل شده و این  دکمه ها و پیام می آیند 
  
    #FIXME حذف این تابع از کیبورد و جایگزینی در آنالیز AYVK.sendKeyAndMessageFAVA()
    def sendKheyrKeyAndMessageFAVA(self):
        self.obj_AYVK.sendKeyAndMessageFAVA()

#تمامی کیبوردها و پیام های بخش «ویرایش شمار واژگان آغازین و اصلی»  
class VirayeshShomarVazheha:
    def __init__(self,id,firstName,msg):
        self.id = id
        self.firstName = firstName
        self.msg = msg
        self.bot = pybotc.Bot("config.cfg")   
        # { h h }
    #در صورت زدن دکمه «📝 شمار  واژه ها 🔢» این  دکمه ها و پیام می آیند 
    def sendVShVMessage357(self):
        wortZahlMsg = f"Liebe/Lieber {self.firstName} 🌺🌸, wie viele neue Wörter möchten Sie an einem Tag?"   
    
        # wortZahlKey = json.dumps({"keyboard":[[BtnS().three],[BtnS().two],[BtnS().one],[Btn().getBack]],"resize_keyboard":True})
        wortZahlKey = Keys().numWords
        self.bot.sendMessage(self.id,wortZahlMsg,"none",wortZahlKey)
    #در صورت زدن دکمه «۳» یا «۵» یا «۷»این  دکمه ها و پیام می آیند 
    def send357AllVMessageFAVA(self):
        changedWordNum = f"Die Anzahl der neuen Wörter wurde in <b> {self.msg}</b> geändert."
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
        timeLearningMsg = f"Liebe/Lieber {self.firstName} 🌺🌸, wähle deine tägliche Lernstartzeit, um den Bot zu besuchen."
        # hoursKey = json.dumps({"keyboard":[[BtnS().clock1,BtnS().clock2,BtnS().clock3,BtnS().clock4,BtnS().clock5,BtnS().clock6,BtnS().clock7,BtnS().clock8],[BtnS().clock9,BtnS().clock10,BtnS().clock11,BtnS().clock12,BtnS().clock13,BtnS().clock14,BtnS().clock15,BtnS().clock16],[BtnS().clock17,BtnS().clock18,BtnS().clock19,BtnS().clock20,BtnS().clock21,BtnS().clock22,BtnS().clock23],[Btn().getBack]],"resize_keyboard":True}) 
        hoursKey = Keys().hKeys
        self.bot.sendMessage(self.id,timeLearningMsg,"none",hoursKey)
    #در صورت زدن دکمه «۱..۲۳» این  دکمه ها و پیام می آیند 
    def send1_23MessageYesNo(self,year,monthAlpha,day,weekDay,hourMin,askedYear,askedMonthAlpha,askedDay,askedWeekDay,askedHourMin):
        dash = "___________________________________"
        timeLearningWarningMsg = f"Liebe/Lieber {self.firstName} 🌺🌸, sind Sie zuversichtlich, die Zeit von zu ändern 👉Lern den Wortschatz täglich👈 zu {self.msg} auf {askedWeekDay} {askedDay} {askedMonthAlpha} {askedYear}? \n {dash} \n Zur Zeit 👉Lern den Wortschatz täglich👈 als nächstes auf {weekDay} {day} {monthAlpha} {year}, <b> Beim {hourMin} </b>. \n @DeutschOhal "
        # yesNoKey = json.dumps({"keyboard":[[Btn().yesDash,Btn().noDash]],"resize_keyboard":True}) 
        yesNoKey = Keys().yNDash
        self.bot.sendMessage(self.id,timeLearningWarningMsg,"none",yesNoKey)


    #در صورت همسان بودن زمان یادگیری روزانه با قبلی  این  دکمه ها و پیام می آیند 
    def sendYesMessageSameFAVA(self,year,monthAlpha,day,weekDay,hourMin):
        dash = "___________________________________"
        # "روش شما در همین هنگام هم  {} هست نیازی تغییر و دگرسانی نیست".format(self.msg)

        timeLearningChangedMsg = f"Ihre tägliche Lernzeit ist zur gleichen Zeit {self.msg}. Es ist nicht erforderlich, \n {dash} \n 👉Lern den Wortschatz täglich👈 am <b> {weekDay} {monthAlpha} {day} zu ändern. , </b> {year} <b> Um <b> {hourMin} </b> \n @DeutschOhal"

        # regularHomePageKey = json.dumps({"keyboard":[[Btn().reviewWords],[Btn().wordsNum,Btn().wayEdit,Btn().account],[Btn().timeLearnEdit,Btn().reportActivity],[Btn().deleteBot,Btn().aboutBot,Btn().uILangNKeyEdit],[Btn().opinion]],"resize_keyboard":True})
        regularHomePageKey = Keys().secondMenu
        self.bot.sendMessage(self.id,timeLearningChangedMsg,"none",regularHomePageKey)


    #در صورت زدن دکمه «بله» این  دکمه ها و پیام می آیند 
    def sendYesMessageFAVA(self,year,monthAlpha,day,weekDay,hourMin):
        dash = "___________________________________"
        timeLearningChangedMsg = f"Die tägliche Lernstunde wurde in <b> {hourMin} </b> geändert. \n {dash} \n👉Lern den Wortschatz täglich👈 Weiter am {weekDay} {day} {monthAlpha} {year}, <b> Um {hourMin} </b> \n @DeutschOhal"


        timeLearningChangedMsg = f"Die tägliche Lernstunde wurde in <b> {hourMin} </b> geändert. \n {dash} \n👉Lern den Wortschatz täglich👈 Weiter am {weekDay} {day} {monthAlpha} {year}, <b> Um {hourMin} </b> \n @DeutschOhal"

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
        reportPageMsg = f"ausgewählt {self.msg}."
        # reportKey = json.dumps ({"keyboard": [[Btn().reportWordsPartions, Btn().reportWeakWords], [Btn().getBack]], "resize_keyboard": True})
        reportKey = Keys().reportKeys
        self.bot.sendMessage(self.id,reportPageMsg,"none",reportKey)

    #در صورت زدن دکمه «گزارش واژگان در بخش ها📈»  این  دکمه ها و پیام می آیند 
    def sendReportAllWordsMessageBBFA(self,num,reportWordsSectionsPercentage):
        num = f"<b>{num}</b>"
        dash = "___________________________________" 
        reportWordsSectionsMsg =  f"Liebe/Lieber {self.firstName} 🌺🌸, Melden Sie Ihr gesamtes verwendetes Vokabular in den Partitionen bis heute: \n {dash} \n \n Anzahl aller bisher erstellten Vokabeln: {num} \n {dash} \n Anzahl und der Prozentsatz aller Wörter in allen Partitionen des Leitner-Box: \n \n {reportWordsSectionsPercentage} \n \n @DeutschOhal"
        # backToHomePageKey = json.dumps({"keyboard":[[Btn().getBack]],"resize_keyboard":True})
        backToHomePage = Keys().getBackKeys
        self.bot.sendMessage(self.id,reportWordsSectionsMsg,"none",backToHomePage)
    #در صورت زدن دکمه «گزارش ناتوانی در واژگان📉»  این  دکمه ها و پیام می آیند 
    # wWDS,wWPGS
   
    def sendReportWeakWordMessageBBFA(self,wWDS,wWPGS):
        dash = "___________________________________"
        reportWordsSectionsMsg = f"\n Liebe/Lieber {self.firstName}🌺🌸, bis heute, melde den schwächsten Wortschatz beim Lernen, \n {dash.center(73)} \n \n Liste der Vokabeln, die über einen Monat des Lernens gedauert haben und ausgedrückt haben die Anzahl der Tage \n\n<b> {wWDS.center(63)} </b>  \n {dash.center(73)} \n\n Schwacher Wortschatz in der Reihenfolge des Prozentsatzes jeder Partition der Leitner-Box \n \n {wWPGS} \n @DeutschOhal"
        # backToHomePageKey = json.dumps({"keyboard":[[Btn().getBack]],"resize_keyboard":True})
        backToHomePage = Keys().getBackKeys
        self.bot.sendMessage(self.id,reportWordsSectionsMsg,"none",backToHomePage)


    #در صورت زدن دکمه «بازگشت به فهرست آغازین🏡»  این  دکمه ها و پیام می آیند 
    #FIXME حذف این تابع از کیبورد و جایگزینی در آنالیز AYVK.sendKeyAndMessageFAVA()
    def sendBBFAMessageFAVA(self):
        self.obj_AYVK.sendKeyAndMessageFAVA()
   
    def reportWeakWords(self,wWDS,wWPGS): 
        dash = "___________________________________"   
        reportMsg = f"\n Liebe/Lieber {self.firstName}🌺🌸, bis heute, melde den schwächsten Wortschatz beim Lernen, \n {dash.center(73)} \n \n Liste der Vokabeln, die über einen Monat des Lernens gedauert haben und ausgedrückt haben die Anzahl der Tage \n\n {wWDS} \n {dash.center(73)} \n\n Schwacher Wortschatz in der Reihenfolge des Prozentsatzes jeder Partition der Leitner-Box \n \n {wWPGS} \n @DeutschOhal"
        # backToHomePage = json.dumps({"keyboard":[[Btn().getBack]],"resize_keyboard":True})
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
         languageMsg = f"Lieber/Liebe {self.firstName} 🌺🌸, wählen Sie Ihre Lieblingssprache für Bots-Nachricht und Tastatur"
        #  languagesKey = json.dumps({"keyboard":[[BtnS().keyNMsgDe],[BtnS().keyNMsgEn],[BtnS().keyNMsgPer],[Btn().getBack]],"resize_keyboard":True}) 
         languagesKey = Keys().lanKeys
         self.bot.sendMessage(self.id,languageMsg,"none",languagesKey)
    
        #در صورت انتخاب و زدن <پوسته فارسی> به فهرست آغازین و اصلی منتقل شده و این  دکمه ها و پیام می آیند 
    def sendBaleKeyAndMessageFAVA(self): 
        languageSelectedMsg = f"{self.msg} ist für bot ausgewählt"
        # regularHomePageKey = json.dumps({"keyboard":[[Btn().reviewWords],[Btn().wordsNum,Btn().wayEdit,Btn().account],[Btn().timeLearnEdit,Btn().reportActivity],[Btn().deleteBot,Btn().aboutBot,Btn().uILangNKeyEdit],[Btn().opinion]],"resize_keyboard":True})
        regularHomePageKey = Keys().secondMenu
        self.bot.sendMessage(self.id,languageSelectedMsg,"none",regularHomePageKey)




        # self.obj_Start.sendKeyAndMessagesUI()
    #    یا کیبورد و پیام پارسی⌨💬 این دکمه ها و پیام از فهرست آغازین و اصلی  می آیند  deutsch Menu, english Menu  در صورت زدن یکی از دکمه های  
    def sendKeyAndMessageFNVA2(self):
        languageSelectedMsg = f"{self.msg} ist für bot ausgewählt"
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
        aboutMsg =f"Grüße Liebe/Lieber <i> {self.firstName} </i>🌺🌸, Dieser Bot kann alle neuen und hervorgehobenen Wörter des Buches <b> 'Großes Übungsbuch Wortschatz' </b> im Kontext von Leitners Wiederholung lernen und täglich in der Kalenderstruktur üben. Mit der Möglichkeit, Sie daran zu erinnern und die Antwort auf Deutsch zu wählen, werden Synonyme, Englisch und Persisch unter Verwendung authentischer deutscher Sprachressourcen aktiviert, sodass die vollständige Beherrschung eines Wortes und eines Wortes in mindestens einem Monat erreicht wird. Aus Ihrem Kurzzeitgedächtnis wird es in Ihrem Langzeitgedächtnis sein."
        # regularHomePageKey = json.dumps({"keyboard":[[Btn().reviewWords],[Btn().wordsNum,Btn().wayEdit,Btn().account],[Btn().timeLearnEdit,Btn().reportActivity],[Btn().deleteBot,Btn().aboutBot,Btn().uILangNKeyEdit],[Btn().opinion]],"resize_keyboard":True})
        regularHomePageKey = Keys().secondMenu
        self.bot.sendMessage(self.id,aboutMsg,"none",regularHomePageKey)

#FIXME copy these 4 method to every user language
    def sendKeyAndMessageSendingSugession(self):
        aboutMsg =f"Liebe/Lieber <i>{self.firstName}</i>🌺🌸,Wenn du Kommentare, Kritik oder Vorschläge hast, sende diese bitte an uns."
        # backToHomePage = json.dumps({"keyboard":[[Btn().getBack]],"resize_keyboard":True})
        backToHomePage = Keys().getBackKeys
        self.bot.sendMessage(self.id,aboutMsg,"none",backToHomePage)

    def sendKeyAndMessageDeliverOpinion(self,opId):
        aboutMsg =f"Liebe/Lieber <i> {self.firstName} </i>🌺🌸, deine Kommentar wurde mit dieser <b>{opId}</b> Tracking-Nummer registriert."
        # regularHomePageKey = json.dumps({"keyboard":[[Btn().reviewWords],[Btn().wordsNum,Btn().wayEdit,Btn().account],[Btn().timeLearnEdit,Btn().reportActivity],[Btn().deleteBot,Btn().aboutBot,Btn().uILangNKeyEdit],[Btn().opinion]],"resize_keyboard":True})
        regularHomePageKey = Keys().secondMenu
        self.bot.sendMessage(self.id,aboutMsg,"none",regularHomePageKey)

    def sendKeyAndMessageUsingBotKeys(self):
        aboutMsg =f"Kein Text eingegeben! Wenn Sie einen Kommentar senden möchten, <b>ohne Verwendung der Bottastatur</b>, geben Sie den Text ein und senden Sie ihn dann."
        # regularHomePageKey = json.dumps({"keyboard":[[Btn().reviewWords],[Btn().wordsNum,Btn().wayEdit,Btn().account],[Btn().timeLearnEdit,Btn().reportActivity],[Btn().deleteBot,Btn().aboutBot,Btn().uILangNKeyEdit],[Btn().opinion]],"resize_keyboard":True})
        regularHomePageKey = Keys().secondMenu
        self.bot.sendMessage(self.id,aboutMsg,"none",regularHomePageKey)

    def sendKeyAndMessageOutOfRangeMsg(self):
        aboutMsg =f"Die Anzahl der gesendeten characters und Wörter ist zu hoch! Senden Sie Ihren Text kürzer oder in mehreren Abschnitten."
        # regularHomePageKey = json.dumps({"keyboard":[[Btn().reviewWords],[Btn().wordsNum,Btn().wayEdit,Btn().account],[Btn().timeLearnEdit,Btn().reportActivity],[Btn().deleteBot,Btn().aboutBot,Btn().uILangNKeyEdit],[Btn().opinion]],"resize_keyboard":True})
        regularHomePageKey = Keys().secondMenu
        self.bot.sendMessage(self.id,aboutMsg,"none",regularHomePageKey)

#تمامی کیبوردها و پیام های بخش «حذف ربات 🗑» در فهرست آعازین واصلی
class HazfRobot:
    def __init__(self,id,firstName,msg):
        self.id = id
        self.firstName = firstName
        self.bot = pybotc.Bot("config.cfg")   
        self.obj_AYVK = AghazYadgiriVazhehayeKetab(id,firstName,msg)

    #    self.HazfRobot(id,firstName,msg).sendHRKeyAndMessageYesNo()

    #در صورت زدن دکمه «حذف ربات 🗑»  این دکمه ها و پیام می آیند    
    def sendHRKeyAndMessageYesNo(self):
        deleteBotWarnMsg = f"Liebe/Lieber {self.firstName} 🌺🌸, sind Sie sicher, Bot zu löschen? Dadurch werden auch alle Ihre Datensätze gelöscht, und es werden keine weiteren Nachrichten an Sie gesendet."
        # yesNoKey = json.dumps({"keyboard":[[Btn().no, Btn().yesDelete]],"resize_keyboard":True}) 
        yesNoKey = Keys().yNKeys
        self.bot.sendMessage(self.id,deleteBotWarnMsg,"none",yesNoKey)
    #در صورت زدن دکمه «بله» به بخش فهرست نخستین🛎 و اولیه منتقل شده و   این دکمه ها و پیام می آیند    
    def sendYesKeyAndMessageFNVA(self):
        deleteBotMsg = "Bot wird gelöscht!"
        # firstHomePageKey = json.dumps({"keyboard": [[Btn().startLearning], [Btn().aboutBotNew, Btn().uILangNKeyEditNew]], "resize_keyboard": True}) 
        firstHomePageKey = Keys().firstMenu
        self.bot.sendMessage(self.id,deleteBotMsg,"none",firstHomePageKey)

    #در صورت زدن دکمه «خیر» به بخش فهرست آغازین و اصلی منتقل شده و   این دکمه ها و پیام می آیند    
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
        # adminDesktop = json.dumps ({"keyboard": [[BtnA().changeUserType, BtnA().sendToAll, BtnA().reportToday, BtnA().reportAll], [BtnA().apply], [Btn().getBack]]," resize_keyboard ": True}) 
        adminDesktop = AKeys().adminKeys
        self.bot.sendMessage(self.id,enterPanelMsg,"none",adminDesktop)

    def adminSendGMessageGPanellAppleyChanges(self,outputAll):
        enterPanelMsg = f"{outputAll} \n Übersetzung und Aktionen, Aufgaben und Operationen abgeschlossen."
        # adminDesktop = json.dumps ({"keyboard": [[BtnA().changeUserType, BtnA().sendToAll, BtnA().reportToday, BtnA().reportAll], [BtnA().apply], [Btn().getBack]]," resize_keyboard ": True}) 
        adminDesktop = AKeys().adminKeys
        self.bot.sendMessage(self.id,enterPanelMsg,"none",adminDesktop)


     #در صورت زدن دکمه «گزارش تکاپو فراگیر»  این دکمه ها و پیام می آیند  
    def adminSendGTFaraMessageGPanel(self,guestsNum,usersNum,guestInfos,userInfos,monthAlpha,year,day,weekDay):
        dash = "___________________________________" 
        fileW = open("TFaraMessageGPanel.txt", "w",encoding='utf-8') 
        data = f"\n \n <b> Benutzerdaten: \n </b> {userInfos} \n {dash} \n <b> Gastdaten: \n </b> {guestInfos} \n {dash}"
        # data = f"\n      {userInfos}\n {dash}\n   {guestInfos} \n {dash}"
        # data = f"{userInfos} \n{dash}\n {guestInfos}"
        fileW.write(data) 
        fileW.close() 
        file = open("TFaraMessageGPanel.txt", "rb")
        openedfile ={'document': file}
        dateGri = datetime.datetime.today().date().strftime("%Y-(%B %m)-%d")
        all = guestsNum + usersNum
        # reportAllActionMsg = f"   \n\n  <b>  داده های کاربران :\n</b>  {userInfos}\n {dash}\n<b>  داده های مهمانان :\n</b> {guestInfos} \n {dash} \nشمار کاربران : <b>{usersNum}</b>\nشمار مهمانان : <b>{guestsNum}</b>\n شمار افراد کنشگر فراگیر : <b>{all}</b> \n {dash} \n امروز: <b>{weekDay}  {day} {monthAlpha} {year} \n {dateGri}</b>     "
        reportAllActionMsg = f"  \n \nAnzahl der Benutzer: {usersNum}\n Anzahl der Gäste: {guestsNum} \n Anzahl der aktiven Personen: {all} \n {dash} \nHeute: {weekDay} {day} {monthAlpha} {year} \n {dateGri}     "
        # adminDesktop = json.dumps ({"keyboard": [[BtnA().changeUserType, BtnA().sendToAll, BtnA().reportToday, BtnA().reportAll], [BtnA().apply], [Btn().getBack]]," resize_keyboard ": True})
        # self.bot.sendMessage(self.id,reportAllActionMsg,"none",adminDesktop)
        self.bot.sendDocument(self.id,openedfile,reportAllActionMsg,disable_notification=True)
        file.close()
        if os.path.exists("TFaraMessageGPanel.txt"):
            os.remove("TFaraMessageGPanel.txt")
        else:
            print("The file does not exist") 
        

    def adminOpinionsTypes(self):
        enterPanelMsg = "alle Arten von Vorschlagsberichten"
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
        reportAllActionMsg = f"  \nAnzahl der Meinungen : {opinionsNum}\nAnzahl der Benutzer, die Meinungen senden: {suguestersNum} \n {dash} \nToday: {weekDay} {day} {monthAlpha} {year} \n {dateGri}"
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
        reportAllActionMsg = f"\n \n Namen und IDs von heute: \n {activeUsersInfos} \n {dash} \n Namen und IDs des heutigen Gastes: \n {activeGuestsInfo} \n {dash} \n Aktive Benutzer von heute: <b> {todayActiveUsersNum} </b> \n Heutige aktive Gäste heute: <b> {todayActiveGuestsNum} </b> \n Heutige Gesamtakteure heute: <b> {all} </b> \n {dash} \n Heute Transaktionen: <b> {numTodayAllTransactions} </b> \n {dash} \n Heute: <b> {weekDay} {day} {monthAlpha} {year} \n {dateGri} </b>"
        # adminDesktop = json.dumps ({"keyboard": [[BtnA().changeUserType, BtnA().sendToAll, BtnA().reportToday, BtnA().reportAll], [BtnA().apply], [Btn().getBack]]," resize_keyboard ": True}) 
        adminDesktop = AKeys().adminKeys
        # "دگرسانی گونه کاربر","پیام به همه","گزارش تکاپو امروز","گزارش تکاپو فراگیر","ورزانش و اعمال"
        self.bot.sendMessage(self.id,reportAllActionMsg,"none",adminDesktop)

     #در صورت زدن دکمه «پیام به همه»  این دکمه ها و پیام می آیند   
    def adminSendPBHMessageBBMSVA(self):
        adminMessageToAllEnterMsg = "Geben Sie die Nachricht ein, die Sie an alle Benutzer senden möchten."
        # adminSendingKey = json.dumps({"keyboard":[[BtnA().getBackToDesk]],"resize_keyboard":True})
        adminSendingKey = AKeys().getBackDesk
        self.bot.sendMessage(self.id,adminMessageToAllEnterMsg,"none",adminSendingKey)
     #در صورت فرستادن پیام از روش کیبورد مبایل(نه ربات)   این دکمه ها و پیام می آیند   
    def adminSendGosilMessageYesNo(self,msg):
        adminMessageToAllWarningMsg = f"{msg} \n \n Sind Sie sicher, dass Sie diese 👆 Texte an alle Benutzer senden möchten?" 
        # yesNoKey = json.dumps({"keyboard":[[BtnA().noDoubleComma,BtnA().yesSendIt]],"resize_keyboard":True})  
        yesNoKey = AKeys().yNDoubleKomma
        self.bot.sendMessage(self.id,adminMessageToAllWarningMsg,"none",yesNoKey)

    # بیشتر شدن کاراکترها بیشتر از 4050
    def adminSendGMessageGPanellCharMore(self,msg):
        length = len(msg)
        msgMore4050 = f"Die Anzahl der Nachrichtenzeichen beträgt {length} bis zu 4050 und kann nicht gesendet werden !!!"
        # adminDesktop = json.dumps ({"keyboard": [[BtnA().changeUserType, BtnA().sendToAll, BtnA().reportToday, BtnA().reportAll], [BtnA().apply], [Btn().getBack]]," resize_keyboard ": True})
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
        backToAdminDesk =  "Admin Desktop⚙️"
        # adminDesktop = json.dumps ({"keyboard": [[BtnA().changeUserType, BtnA().sendToAll, BtnA().reportToday, BtnA().reportAll], [BtnA().apply], [Btn().getBack]]," resize_keyboard ": True}) 
        adminDesktop = AKeys().adminKeys
        self.bot.sendMessage(self.id,backToAdminDesk,"none",adminDesktop)
    
     #در صورت زدن دکمه «بله،گسیل شود!»  این دکمه ها و پیام می آیند   
    def adminSendYeslMessageGPanel(self):
        adminMessageToAllSentMsg = "Ihre Nachricht wurde an alle Benutzer gesendet"
        # adminDesktop = json.dumps ({"keyboard": [[BtnA().changeUserType, BtnA().sendToAll, BtnA().reportToday, BtnA().reportAll], [BtnA().apply], [Btn().getBack]]," resize_keyboard ": True}) 
        adminDesktop = AKeys().adminKeys
        self.bot.sendMessage(self.id,adminMessageToAllSentMsg,"none",adminDesktop)
   
     #در صورت زدن دکمه «خیر»  این دکمه ها و پیام می آیند   
    def adminSendNolMessageGPanel(self):
        backToAdminDesk =  "Admin Desktop⚙️"
        # adminDesktop = json.dumps ({"keyboard": [[BtnA().changeUserType, BtnA().sendToAll, BtnA().reportToday, BtnA().reportAll], [BtnA().apply], [Btn().getBack]]," resize_keyboard ": True}) 
        adminDesktop = AKeys().adminKeys
        self.bot.sendMessage(self.id,backToAdminDesk,"none",adminDesktop)
   
     #در صورت زدن دکمه «دگرسانی گونه کاربر»  این دکمه ها و پیام می آیند   
    def adminSendDGKlMessageGBBMSVA(self):
        dGKGUIdeMsg = "userId 12 ... or username @ ... Geben Sie Ihren Lieblingsbenutzer ein"
        # adminSendingKey = json.dumps({"keyboard": [[BtnA().send], [BtnA().getBackToDesk]], "resize_keyboard": True})
        adminSendingKey = AKeys().sendChangeUser
        self.bot.sendMessage(self.id,dGKGUIdeMsg,"none",adminSendingKey)
   
     #در صورت زدن دکمه «گسیل» و فرستادن شناسه کاربری یا نام کاربری اشتباه این دکمه ها و پیام می آیند   
    def adminSendWrongGMessageGBBMSVA(self):
        dGKGUIdeMsg = "username oder userId korrekt eingeben"
        # adminSendingKey = json.dumps({"keyboard": [[BtnA().send], [BtnA().getBackToDesk]], "resize_keyboard": True})
        adminSendingKey = AKeys().sendChangeUser
        self.bot.sendMessage(self.id,dGKGUIdeMsg,"none",adminSendingKey)
   
     #در صورت زدن دکمه «گسیل» و وارد کردن نام درست کاربری یا شناسه کاربری   این دکمه ها و پیام می آیند   
    def adminSendًRightGMessageGPanel(self):
        successfulChangedMsg = f"Benutzer {self.msg} wurde von einem einfachen Benutzer zu einem speziellen Benutzer geändert."
        # adminSendingKey = json.dumps({"keyboard": [[BtnA().send], [BtnA().getBackToDesk]], "resize_keyboard": True})
        adminSendingKey = AKeys().sendChangeUser
        self.bot.sendMessage(self.id,successfulChangedMsg,"none",adminSendingKey)


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
         languageMsg = f"Lieber/Liebe {self.firstName} 🌺🌸, wählen Sie Ihre Lieblingssprache für Bots-Nachricht und Tastatur"
        #  languagesKey = json.dumps({"keyboard":[[BtnS().keyNMsgDe],[BtnS().keyNMsgEn],[BtnS().keyNMsgPer]],"resize_keyboard":True})
         languagesKey = SKeys(Btn(),MNV()).uI
         self.bot.sendMessage(self.id,languageMsg,"none",languagesKey)

   #    یا کیبورد و پیام پارسی⌨💬 این دکمه ها و پیام از فهرست نخستین🛎 و اولیه  می آیند  deutsch Menu, english Menu  در صورت زدن یکی از دکمه های  
    def sendKeyAndMessageFNVAUIselected(self):
        languageSelectedMsg = f"{self.msg} ist für bot ausgewählt"
        # firstHomePageKey = json.dumps ({"keyboard": [[BtnA().admin, Btn().startLearning], [Btn().aboutBotNew, Btn().uILangNKeyEditNew]], " resize_keyboard ": True}) 
        firstHomePageKey = AKeys().firstMenu
        self.bot.sendMessage(self.id,languageSelectedMsg,"none",firstHomePageKey)
    

    def sendKeyAndMessageFNVAUINakhostin(self):
         languageSelectedMsg = "Menü🛎"
        #  firstHomePageKey = json.dumps ({"keyboard": [[BtnA().admin, Btn().startLearning], [Btn().aboutBotNew, Btn().uILangNKeyEditNew]], " resize_keyboard ": True}) 
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
        msgNextTrainingTimeDate = f"Liebe/Lieber <i> {self.firstName} </i>  🌺🌸 Deine Konto\n{ent}\n{output}\n{dash}\n {outpuTodayDateNTime}\n @DeutschOhal"
        # regularHomePageKey = json.dumps({"keyboard":[[BtnA().admin,Btn().reviewWords],[Btn().wordsNum,Btn().wayEdit,Btn().account],[Btn().timeLearnEdit,Btn().reportActivity],[Btn().deleteBot,Btn().aboutBot,Btn().uILangNKeyEdit],[Btn().opinion]],"resize_keyboard":True})
        regularHomePageKey = AKeys().secondMenu
        self.bot.sendMessage(self.id,msgNextTrainingTimeDate,"none",regularHomePageKey)
    
    #در صورت زدن دکمه ((آعاز یادگیری واژه های کتاب)) این دکمه ها و پیام می آیند
    def sendAYVKKeyAndMessage327(self):
        wortZahlMsg = f"Liebe/Lieber {self.firstName} 🌺🌸, wie viele neue Wörter möchten Sie an einem Tag?"        
        # wortZahlKey = json.dumps({"keyboard":[[BtnS().threeNew],[BtnS().twoNew],[BtnS().oneNew],[BtnS().fiveNew,BtnS().tenNew,BtnS().fifteenNew,BtnS().twentyNew]],"resize_keyboard":True})
        wortZahlKey = AKeys().wordsNumNew
        self.bot.sendMessage(self.id,wortZahlMsg,"none",wortZahlKey)
    #در صورت زدن یکی از دکمه های ۳ یا ۵  یا ۷ این دکمه ها و پیام می آیند
    def send357KeyAndMessageDESP(self):
        waysMsg = f"Liebe/Lieber {self.firstName} 🌺🌸, wähle die Methode zum Lernen von Buchwörtern"
        # wayKey = json.dumps({"keyboard":[[BtnS().deutschNew,BtnS().englishNew,BtnS().synonymNew],[BtnS().allTogetherNew,BtnS().persianNew]],"resize_keyboard":True}) 
        wayKey = AKeys().waysNew
        self.bot.sendMessage(self.id,waysMsg,"none",wayKey)

  
   #    یا پارسی این دکمه و پیام می آیند  deutsch , english , synonym  در صورت زدن یکی از دکمه های  
    def sendDESPKeyAndMessageLampGuid(self,way,wKind,numW,numAll,standardizedWord,content,chapter,wordsPage,linkWord):
        dash = "___________________________________"
        guide = f"Hinweis🔔: Lies das Wort und sage {way} dazu und erinnere dich daran. Tippe dann auf 💡, um die richtige Antwort zu sehen und sie mit deiner Antwort zu vergleichen."


        newWordsMsg = f". {numW} / {numAll} {wKind}. \n <b> {standardizedWord} </b> \n.Kapitel: {content} \nAbschnitt: {chapter} \nSeite: {wordsPage}. \n {dash}   \n {linkWord}{guide}"


        # {content}\n{cotentNChap} \nبرگ:{wordsPage}
        # antwortKey = json.dumps({"keyboard":[[BtnS().lamp]],"resize_keyboard":True}) 
        antwortKey = SKeys(Btn(),MNV()).lampKeys
        self.bot.sendMessage(self.id,newWordsMsg,"none",antwortKey)


                               
   #    یا پارسی این دکمه و پیام می آیند  deutsch , english , synonym  در صورت زدن یکی از دکمه های  
    def sendDESPKeyAndMessageLamp(self,wKind,numW,numAll,standardizedWord,content,chapter,wordsPage,linkWord):
        newWordsMsg = f".{numW}/{numAll}                                         {wKind}.\n<b>{standardizedWord}</b>\n.Kapitel : {content}\nAbschnitt : {chapter} \nSeite:{wordsPage}. \n {linkWord}\n."
        # {content}\n{cotentNChap} \nبرگ:{wordsPage}
        # antwortKey = json.dumps({"keyboard":[[BtnS().lamp]],"resize_keyboard":True}) 
        antwortKey = SKeys(Btn(),MNV()).lampKeys
        self.bot.sendMessage(self.id,newWordsMsg,"none",antwortKey)



   #در صورت زدن دکمه 💡 این دکمه و پیام می آید 
    def sendLampKeyAndMessageVXGuide(self,way,icon,standardizedAnswer,answerLink):
               #63 blank space
        dash = "___________________________________"
        guide = f"Hinweis🔔: Wenn Sie die gesendete Antwort und Ihre Antwort überprüfen, wählen Sie Ihre Antwort richtig oder falsch aus, indem Sie ❌ oder ✅ auswählen."

        pa = f"Antworte in {way} {icon}"
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
        pa = f"Antworte in {way} {icon}"
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
        guide = f"🔔 Nachdem Sie auf'{Btn().getBack}' getippt haben, können Sie '{Btn().reviewWords}' auswählen, um die von Ihnen eingegebenen Wörter zu überprüfen."

        daliyReport = f"Liebe/Lieber <i>{self.firstName}</i>🌺🌸  Melde deine Aktivitäten heute:  \n{dash.center(14)}\n Anzahl der geübten Wörter: <b> {nWorkedWords} </b> \n Anzahl der richtigen Wörter: <b>{nRWords}</b>\n Anzahl der falschen Wörter: <b>{nWWrong}</b>\n{dash.center(14)}\n<i> Prozentsatz der richtigen und falschen Wörter: </i> \n Richtig <b> {graphRight}% {percentageRight} </b> \n falsch <b> {graphWrong}% {percentageWrong} </b> \n {dash.center(14)} \n Liste der heute falschen Wörter mit der Seitenadresse im Buch: \n <b> {wrongWordsNpages} </b> \n {dash.center(14)} \n The 👉Lern den Wortschatz täglich👈 Weiter am <b> {weekDay} {day} {month} {year} </b>, um <b>{houNMTraining}</b> In der Zeit des Iran, Fällt zusammen mit <b>{dateGriNextTraining}</b> \n{dash}\n<i>Partition und Anzahl aller Wörter in der Lightner-Box: </i>\nWortnummer in der 1. Partition: <b>{wordsSectionPosition[0]} </b> \n Wortnummer in der 2. Partition: <b> {wordsSectionPosition[1]} </b> \n Wortnummer in der 3. Partition: <b> {wordsSectionPosition[2]} </b> \n Wortnummer in der 4. Partition: <b> {wordsSectionPosition[3]} </b> \n Wortnummer in der 5. Partition: <b> {wordsSectionPosition[4]} </b> \n Wortnummer in der 6. Partition: <b> {wordsSectionPosition[5]} </b> \n {dash} \n Anzahl der vollständig erlernten Vokabeln: <b> {wordsSectionPosition[6]} </b> \n {dash} \n <i> {guide} </i> \n @DeutschOhal \n"
        
        # f"<i>گزارش کارکردت، {self.firstName} عزیز 🌺🌸 در امروز:</i>\n{dash.center(14)}\nشمار وا‌ژه های کار شده : <b>{nWorkedWords}</b>\nشمار واژه های درست : <b>{nRWords}</b>\nشمار واژه های نادرست : <b>{nWWrong}</b>\n{dash.center(14)}\n<i>درصد درستی و نادرستی واژه ها :</i>\nدرستی <b>{graphRight} % {percentageRight} </b>\nنادرستی <b>{graphWrong} % {percentageWrong}</b> \n{dash.center(14)}\nفهرست واژه های نادرست امروز به همراه نشانی برگ در کتاب :\n <b>{wrongWordsNpages}</b>\n{dash.center(14)}\n👈یادگیری واژگان روزانه👉 بعدی و پسین در تاریخ <b> {weekDay} {day} {month} {year} </b>, در ساعت و زمان <b>{houNMTraining}</b>\n{dash}\n<i>بخش و شمار تمامی واژه ها در جعبه لایتنر :</i>\nشمار واژه ها در بخش نخست :<b>{wordsSectionPosition[0]} </b>\nشمار واژه ها در بخش دوم :<b> {wordsSectionPosition[1]} </b>\nشمار واژه ها در بخش سوم : <b>{wordsSectionPosition[2]} </b>\nشمار واژه ها در بخش چهارم :<b> {wordsSectionPosition[3]}</b> \nشمار واژه ها در بخش پنجم :‌<b>{wordsSectionPosition[4]}</b> \nشمار واژه ها در بخش ششم :<b>‌{wordsSectionPosition[5]}</b>\n{dash}\nشمار واژگان به صورت کامل یادگیری شده :<b>‌{wordsSectionPosition[6]}</b>\n{dash} \n<i>{guide}</i>\n@DeutschOhal\n"



        print(f"daily report = {daliyReport}")
        # backToHomePage = json.dumps({"keyboard":[[Btn().getBack]],"resize_keyboard":True})
        backToHomePage = Keys().getBackKeys
        self.bot.sendMessage(self.id,daliyReport,"none",backToHomePage)
       
    # فرستادن تاریخ و زمان یادگیری واژگان بعدی پسین
    def sendNextTrainingDateTimeKeyAndMessageBBFA(self,weekDay,day,monthAlpha,year,hourMin):
        # y = "یادگیری واژگان روزانه"
        
        msgNextTrainingTimeDate = f"Liebe/Lieber <i> {self.firstName} </i>🌺🌸, 👉Lern den Wortschatz täglich👈 als nächstes am <b> {weekDay} {day} {monthAlpha} {year} </b>, um <b> {hourMin} </b>. \n@DeutschOhal"
        # msgNextTrainingTimeDate = "g"
        # regularHomePageKey = json.dumps({"keyboard":[[BtnA().admin,Btn().reviewWords],[Btn().wordsNum,Btn().wayEdit,Btn().account],[Btn().timeLearnEdit,Btn().reportActivity],[Btn().deleteBot,Btn().aboutBot,Btn().uILangNKeyEdit],[Btn().opinion]],"resize_keyboard":True})
        regularHomePageKey = AKeys().secondMenu
        self.bot.sendMessage(self.id,msgNextTrainingTimeDate,"none",regularHomePageKey)






     #در صورت زدن  دکمه بازگشت به فهرست آغازین🏡 به بخش فهرست آغازین و اصلی منتقل شده و این دکمه ها و پیام می آیند 
   #FIXME حذف این تابع از کیبورد و جایگزینی در آنالیز AYVK.sendKeyAndMessageFAVA()

    def sendKeyAndMessageFAVA(self):
        fehrestAghazinMsg = "Startseite"
        # regularHomePageKey = json.dumps({"keyboard":[[BtnA().admin,Btn().reviewWords],[Btn().wordsNum,Btn().wayEdit,Btn().account],[Btn().timeLearnEdit,Btn().reportActivity],[Btn().deleteBot,Btn().aboutBot,Btn().uILangNKeyEdit],[Btn().opinion]],"resize_keyboard":True})
        regularHomePageKey = AKeys().secondMenu
        self.bot.sendMessage(self.id,fehrestAghazinMsg,"none",regularHomePageKey)
    def sendKeyAndMessageUserMustWait(self):
        fehrestAghazinMsg = "Bis zum nächsten Datum"
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
        msgWarning ="⛔️😡😡⛔️ Vermeiden Sie das Versenden von Spam ⛔️😡😡⛔️"
        # antwortKey = json.dumps({"keyboard":[[BtnS().lamp]],"resize_keyboard":True}) 
        # antwortKey = SKeys(Btn(),MNV()).lampKeys
        antwortKey = ""
        self.bot.sendMessage(self.id,msgWarning,"none",antwortKey)
        #spam warning هنگامه آخرین واژه BtnS().crossCheck,"✅ پیام خطا به جهت فرستادن تکراری 
    def sendWarningKeyAndMessageBBFA(self):
        msgWarning ="⛔️😡😡⛔️ Vermeiden Sie das Versenden von Spam ⛔️😡😡⛔️"
        # backToHomePage = json.dumps({"keyboard":[[Btn().getBack]],"resize_keyboard":True})
        # backToHomePage = Keys().getBackKeys
        backToHomePage =""
        self.bot.sendMessage(self.id,msgWarning,"none",backToHomePage)
     
    #spam warning  پیام خطا به جهت فرستادن تکراری برای کاربری که هنوز نام نویسی نشده 
    def sendWarningRepeatedKeyAndMessageToAdminGuest(self):
        msgWarning = "⛔️😡😡⛔️ Vermeiden Sie das Versenden von Spam ⛔️😡😡⛔️"
        # firstHomePageKey = json.dumps ({"keyboard": [[BtnA().admin, Btn().startLearning], [Btn().aboutBotNew, Btn().uILangNKeyEditNew]], " resize_keyboard ": True}) 
        # firstHomePageKey = AKeys().firstMenu
        firstHomePageKey =""
        self.bot.sendMessage(self.id,msgWarning,"none",firstHomePageKey)


    #spam warning  پیام خطا به جهت فرستادن تکراری برای کاربر  
    def sendWarningRepeatedKeyAndMessageToAdmin(self):
        msgWarning = "⛔️😡😡⛔️ Vermeiden Sie das Versenden von Spam ⛔️😡😡⛔️"
        # regularHomePageKey = json.dumps({"keyboard":[[BtnA().admin,Btn().reviewWords],[Btn().wordsNum,Btn().wayEdit,Btn().account],[Btn().timeLearnEdit,Btn().reportActivity],[Btn().deleteBot,Btn().aboutBot,Btn().uILangNKeyEdit],[Btn().opinion]],"resize_keyboard":True})
        regularHomePageKey =""  
        self.bot.sendMessage(self.id,msgWarning,"none",regularHomePageKey) 

    #none keyboard warning  پیام خطا به جهت عدم استفاده از کیبورد ربات برای ادمین عضو شده  
    def sendWarningNoneKeyboardToAdmin(self):
        msgWarning = "Verwenden Sie nur die Bottastatur!"
        # regularHomePageKey = json.dumps({"keyboard":[[BtnA().admin,Btn().reviewWords],[Btn().wordsNum,Btn().wayEdit,Btn().account],[Btn().timeLearnEdit,Btn().reportActivity],[Btn().deleteBot,Btn().aboutBot,Btn().uILangNKeyEdit],[Btn().opinion]],"resize_keyboard":True})
        regularHomePageKey = AKeys().secondMenu
        # regularHomePageKey=""
        self.bot.sendMessage(self.id,msgWarning,"none",regularHomePageKey) 

    #none keyboard warning  پیام خطا به جهت عدم استفاده از کیبورد ربات برای ادمین میهمان   
    def sendWarningNoneKeyboardToAdminGuest(self):
        msgWarning = "Verwenden Sie nur die Bottastatur!"
        # firstHomePageKey = json.dumps ({"keyboard": [[BtnA().admin, Btn().startLearning], [Btn().aboutBotNew, Btn().uILangNKeyEditNew]], " resize_keyboard ": True}) 
        firstHomePageKey = AKeys().firstMenu
        # firstHomePageKey =""
        self.bot.sendMessage(self.id,msgWarning,"none",firstHomePageKey) 

class AdminAutomaticMessage:
    def __init__(self,id,firstName):
        self.id = id
        self.bot = pybotc.Bot("config.cfg")
        self.firstName = firstName
    def sendKeyAndMessageDailyLearn(self):
        msg = f"Grüße Liebe/Lieber <i> {self.firstName} </i>🌺🌸, Dieser Bot kann alle neuen und hervorgehobenen Wörter des Buches <b> 'Großes Übungsbuch Wortschatz' </b> im Kontext von Leitners Wiederholung lernen und täglich in der Kalenderstruktur üben. Mit der Möglichkeit, Sie daran zu erinnern und die Antwort auf Deutsch zu wählen, werden Synonyme, Englisch und Persisch unter Verwendung authentischer deutscher Sprachressourcen aktiviert, sodass die vollständige Beherrschung eines Wortes und eines Wortes in mindestens einem Monat erreicht wird. Aus Ihrem Kurzzeitgedächtnis wird es in Ihrem Langzeitgedächtnis sein."
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
        aboutMsg =f"Grüße Liebe/Lieber <i> {self.firstName} </i>🌺🌸, Dieser Bot kann alle neuen und hervorgehobenen Wörter des Buches <b> 'Großes Übungsbuch Wortschatz' </b> im Kontext von Leitners Wiederholung lernen und täglich in der Kalenderstruktur üben. Mit der Möglichkeit, Sie daran zu erinnern und die Antwort auf Deutsch zu wählen, werden Synonyme, Englisch und Persisch unter Verwendung authentischer deutscher Sprachressourcen aktiviert, sodass die vollständige Beherrschung eines Wortes und eines Wortes in mindestens einem Monat erreicht wird. Aus Ihrem Kurzzeitgedächtnis wird es in Ihrem Langzeitgedächtnis sein."
        # firstHomePageKey = json.dumps ({"keyboard": [[BtnA().admin, Btn().startLearning], [Btn().aboutBotNew, Btn().uILangNKeyEditNew]], " resize_keyboard ": True})
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
        reviewMsg = f"Liebe/Lieber {self.firstName} 🌺🌸, Wählen Sie die Methode zur Überprüfung des Wortschatzes basierend auf einer der Optionen."
        # reviewKey = json.dumps({"keyboard": [[Btn().chapterNSection], [Btn().leitnerBoxParts], [Btn().weakWords], [Btn().getBack]], "resize_keyboard": True}) 
        reviewKey = Keys().revKeys
        self.bot.sendMessage(self.id,reviewMsg,"none",reviewKey)
        
        #🔎
        ###در صورت زدن دکمه «سرفصل و فصل» در بخش آغازین و اصلی این  دکمه ها و پیام نخستین واژه می آیند 
    def sendWordsChapterContentKeyAndMessageFirstOLdWord(self,content,chapter,word,answer,counter,length,section,page,link):
        oldWordsMsg = f".Kapitel : {content}\nAbschnitt : {chapter}\n\n<b>{word}</b>\n\n{answer.center(63)}\n{link}\n.Seite :{page}                         {section}: {length}/{counter+1}"
        # reviewNextKey = json.dumps({"keyboard":[[Btn().nextWordChapNS],[Btn().getBack]],"resize_keyboard":True}) 
        reviewNextKey = Keys().revChapNexKeys
        self.bot.sendMessage(self.id,oldWordsMsg,"none",reviewNextKey)
        ## وقتی طول آرایه یکی بود
    def sendWordsChapterContentKeyAndMessageFirstOLdWordOneLength(self,content,chapter,word,answer,counter,length,section,page,link):
        oldWordsMsg = f".Kapitel : {content}\nAbschnitt : {chapter}\n\n<b>{word}</b>\n\n{answer.center(63)}\n{link}\n.Seite :{page}                         {section}: {length}/{counter+1}"
        # backToHomePage = json.dumps({"keyboard":[[Btn().getBack]],"resize_keyboard":True}) 
        backToHomePage = Keys().getBackKeys
        self.bot.sendMessage(self.id,oldWordsMsg,"none",backToHomePage)


    #سرفصل و فصل- کیبورد حاوی قبلی و بعدی  
    def sendWordsChapterContentKeyAndMessagMiddleOLdWord(self,content,chapter,word,answer,counter,length,section,page,link):
        oldWordsMsg = f".Kapitel : {content}\nAbschnitt : {chapter}\n\n<b>{word}</b>\n\n{answer.center(63)}\n{link}\n.Seite :{page}                         {section}: {length}/{counter+1}"
        # reviewNextKey = json.dumps({"keyboard":[[Btn().beforeWordChapNS,Btn().nextWordChapNS],[Btn().getBack]],"resize_keyboard":True}) 
        reviewMiddleKeys = Keys().revChapMidKeys
        self.bot.sendMessage(self.id,oldWordsMsg,"none",reviewMiddleKeys)
    
    #سرفصل و فصل- کیبورد حاوی قبلی و آخرین واژه  
    def sendWordsChapterContentKeyAndMessagLastOLdWord(self,content,chapter,word,answer,counter,length,section,page,link):
        oldWordsMsg = f".Kapitel : {content}\nAbschnitt : {chapter}\n\n<b>{word}</b>\n\n{answer.center(63)}\n{link}\n.Seite :{page}                         {section}: {length}/{counter+1}"
        # reviewNextKey = json.dumps({"keyboard":[[Btn().beforeWordChapNS],[Btn().getBack]],"resize_keyboard":True}) 
        reviewBeforeKey = Keys().revChapBefKeys
        self.bot.sendMessage(self.id,oldWordsMsg,"none",reviewBeforeKey)


    #🔭
    ###در صورت زدن دکمه «بخش ها» در بخش آغازین و اصلی این  دکمه ها و پیام نخستین واژه می آیند 
    def sendBakhshhaKeyAndMessageFirstWord(self,counter,length,section,word,answer,page,content,chapter,link):
        oldWordsMsg = f". {section}: {length}/{counter+1}\n<b>{word}</b>\n\n{answer.center(63)}\n\n.Kapitel : {content}\nAbschnitt : {chapter} \n {link} \n Seite :{page}"
        # reviewNextKey = json.dumps({"keyboard":[[Btn().nextWordLeitBP],[Btn().getBack]],"resize_keyboard":True}) 
        reviewNextKey = Keys().revLeitNexKeys
        self.bot.sendMessage(self.id,oldWordsMsg,"none",reviewNextKey)

    def sendBakhshhaKeyAndMessageFirstWordOneLength(self,counter,length,section,word,answer,page,content,chapter,link):
        oldWordsMsg = f". {section}: {length}/{counter+1}\n<b>{word}</b>\n\n{answer.center(63)}\n\n.سرفصل : {content}\nفصل : {chapter}  {link}\nبرگ:{page}"
        # backToHomePage = json.dumps({"keyboard":[[Btn().getBack]],"resize_keyboard":True}) 
        backToHomePage = Keys().getBackKeys
        self.bot.sendMessage(self.id,oldWordsMsg,"none",backToHomePage)



        #بخش ها- کیبورد حاوی قبلی و بعدی 
    def sendBakhshhaKeyAndMessageMiddleWord(self,counter,length,section,word,answer,page,content,chapter,link):
        oldWordsMsg = f". {section}: {length}/{counter+1}\n<b>{word}</b>\n\n{answer.center(63)}\n\n.Kapitel : {content}\nAbschnitt : {chapter} \n {link} \n Seite :{page}"
        #اگر واژه ای بعد از این هنوز موجود باشد
        # reviewBackNextKey = json.dumps({"keyboard":[[Btn().beforeWordLeitBP,Btn().nextWordLeitBP],[Btn().getBack]],"resize_keyboard":True}) 
        reviewBackNextKey = Keys().revLeitMidKeys
        self.bot.sendMessage(self.id,oldWordsMsg,"none",reviewBackNextKey)

        #بخش ها- کیبورد حاوی قبلی  
    def sendBakhshhaKeyAndMessageLastWord(self,counter,length,section,word,answer,page,content,chapter,link):
        oldWordsMsg = f". {section}: {length}/{counter+1}\n<b>{word}</b>\n\n{answer.center(63)}\n\n.Kapitel : {content}\nAbschnitt : {chapter} \n {link} \n Seite :{page}"
        #اگر واژه ای بعد از این دیگر موجود نباشد
        # reviewBackKey = json.dumps({"keyboard":[[Btn().beforeWordLeitBP],[Btn().getBack]],"resize_keyboard":True}) 
        reviewBackKey = Keys().revLeitBefKeys
        self.bot.sendMessage(self.id,oldWordsMsg,"none",reviewBackKey)

    #🔬
    ###در صورت زدن دکمه «واژگان ناتوان» در بخش آغازین و اصلی این  دکمه ها و پیام نخستین واژه می آیند 
    def sendWeakWordsKeyAndMessageFirstOLdWord(self,durationDays,counter,length,section,word,answer,content,chapter,page,link):
        oldWordsMsg = f".Tage Nummer: {durationDays}         {section}:{counter+1}/{length}.\n\n<b>{word}</b>\n\n{answer.center(63)}\n\n Kapitel : {content}\nAbschnitt : {chapter} \n {link} \n{page}:Seite"
        # برگ:{page}
        # {page}:برگ
        # reviewNextKey = json.dumps({"keyboard":[[Btn().nextWordWW],[Btn().getBack]],"resize_keyboard":True}) 
        reviewNextKey = Keys().revWeakNexKeys
        self.bot.sendMessage(self.id,oldWordsMsg,"none",reviewNextKey)

    #وقتی طول آرایه یکی باشد
    def sendWeakWordsKeyAndMessageFirstOLdWordOneLength(self,durationDays,counter,length,section,word,answer,content,chapter,page,link):
        oldWordsMsg = f".Tage Nummer: {durationDays}         {section}:{counter+1}/{length}.\n\n<b>{word}</b>\n\n{answer.center(63)}\n\n Kapitel : {content}\nAbschnitt : {chapter} \n {link} \n{page}:Seite"
        # برگ:{page}
        # {page}:برگ
        
        # backToHomePage = json.dumps({"keyboard":[[Btn().getBack]],"resize_keyboard":True}) 
        backToHomePage = Keys().getBackKeys
        self.bot.sendMessage(self.id,oldWordsMsg,"none",backToHomePage)



# {self.firstName}
    def sendWeakWordsKeyAndMessageNoWord(self):
        noWeakWordMsg = f"Liebe/Lieber <i> {self.firstName} </i>🌺🌸, du hast keinen schwachen Wortschatz!"
        # برگ:{page}
        # {page}:برگ
        # regularHomePageKey = json.dumps({"keyboard":[[BtnA().admin,Btn().reviewWords],[Btn().wordsNum,Btn().wayEdit,Btn().account],[Btn().timeLearnEdit,Btn().reportActivity],[Btn().deleteBot,Btn().aboutBot,Btn().uILangNKeyEdit],[Btn().opinion]],"resize_keyboard":True})
        regularHomePageKey = AKeys().secondMenu
        self.bot.sendMessage(self.id,noWeakWordMsg,"none",regularHomePageKey)
  
    def sendWeakWordsKeyAndMessageNoWordOtherReview(self):
        noWeakWordMsg = f"Liebe/Lieber <i> {self.firstName}</i>🌺🌸, du hast bisher noch kein Wort und keine Übung gemacht!"
        regularHomePageKey = Keys().secondMenu
        self.bot.sendMessage(self.id,noWeakWordMsg,"none",regularHomePageKey)

    #واژگان ناتوان- کیبورد حاوی قبلی و بعدی  
    def sendWeakWordsKeyAndMessagMiddleOLdWord(self,durationDays,counter,length,section,word,answer,content,chapter,page,link):
        oldWordsMsg = f".Tage Nummer: {durationDays}         {section}:{counter+1}/{length}.\n\n<b>{word}</b>\n\n{answer.center(63)}\n\n Kapitel : {content}\nAbschnitt : {chapter} \n {link} \n{page}:Seite"
        # reviewNextKey = json.dumps({"keyboard":[[Btn().beforeWordWW,Btn().nextWordWW],[Btn().getBack]],"resize_keyboard":True}) 
        reviewNextKey = Keys().revWeakMidKeys
        self.bot.sendMessage(self.id,oldWordsMsg,"none",reviewNextKey)
    #واژگان ناتوان- کیبورد حاوی قبلی و آخرین واژه  
    def sendWeakWordsKeyAndMessagLastOLdWord(self,durationDays,counter,length,section,word,answer,content,chapter,page,link):
        oldWordsMsg = f".Tage Nummer: {durationDays}         {section}:{counter+1}/{length}.\n\n<b>{word}</b>\n\n{answer.center(63)}\n\n Kapitel : {content}\nAbschnitt : {chapter} \n {link} \n{page}:Seite"
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

    #در صورت زدن دکمه «📝 روش 🛣»  این  دکمه ها و پیام می آیند
    def send357KeyAndMessageDESP(self):
        waysMsg = f"Liebe/Lieber {self.firstName} 🌺🌸, wähle die Methode zum Lernen von Buchwörtern"
        # wayKey = json.dumps({"keyboard":[[BtnS().deutsch,BtnS().english,BtnS().synonym],[BtnS().allTogether,BtnS().persian],[Btn().getBack]],"resize_keyboard":True}) 
        wayKey = AKeys().ways
        self.bot.sendMessage(self.id,waysMsg,"none",wayKey)



     #    یا پارسی  این دکمه ها و پیام می آیند  deutsch , english , synonym  در صورت زدن یکی از دکمه های  
    def sendDESPAllKeyAndMessageYesNo(self,way): 
        waysWarningMsg = f"Liebe/Lieber {self.firstName} 🌺🌸, Sind Sie sicher, dass Sie die neue Methode <b> {self.msg} </b> auswählen möchten, denn wenn Sie auswählen, wird Ihr vorheriger Datensatz <b> {way} ausgewählt. </b> für bearbeitete Wörter werden gelöscht?"
        # yesNoKey = json.dumps({"keyboard":[[Btn().yesDot, Btn().noDot]],"resize_keyboard":True}) 
        yesNoKey = Keys().yNDot
        self.bot.sendMessage(self.id,waysWarningMsg,"none",yesNoKey)


   #    یا پارسی و یکسان بودن با روش قبلی این دکمه ها و پیام می آیند  deutsch , english , synonym  در صورت زدن یکی از دکمه های  
    def sendDESPAllSameKeyAndMessageFAVA(self): 
        waysWarningMsg = f"Ihre Methode ist derzeit <b> {self.msg} </b>. Sie müssen nicht geändert werden."
        # regularHomePageKey = json.dumps({"keyboard":[[BtnA().admin,Btn().reviewWords],[Btn().wordsNum,Btn().wayEdit,Btn().account],[Btn().timeLearnEdit,Btn().reportActivity],[Btn().deleteBot,Btn().aboutBot,Btn().uILangNKeyEdit],[Btn().opinion]],"resize_keyboard":True})
        regularHomePageKey = AKeys().secondMenu
        self.bot.sendMessage(self.id,waysWarningMsg,"none",regularHomePageKey)

    #در صورت زدن دکمه «بله» به فهرست آغازین و اصلی منتقل شده و این  دکمه ها و پیام می آیند 
    def sendBaleKeyAndMessageFAVA(self): 
        waysChangedMsg = "📝 روش 🛣 به {} انجام شد".format(self.msg)
        # regularHomePageKey = json.dumps({"keyboard":[[BtnA().admin,Btn().reviewWords],[Btn().wordsNum,Btn().wayEdit,Btn().account],[Btn().timeLearnEdit,Btn().reportActivity],[Btn().deleteBot,Btn().aboutBot,Btn().uILangNKeyEdit],[Btn().opinion]],"resize_keyboard":True})
        regularHomePageKey = AKeys().secondMenu
        self.bot.sendMessage(self.id,waysChangedMsg,"none",regularHomePageKey)

   #در صورت زدن دکمه «خیر» به فهرست آغازین و اصلی منتقل شده و این  دکمه ها و پیام می آیند 
    #FIXME حذف این تابع از کیبورد و جایگزینی در آنالیز AYVK.sendKeyAndMessageFAVA()
    def sendKheyrKeyAndMessageFAVA(self):
        self.obj_AYVK.sendKeyAndMessageFAVA()

#تمامی کیبوردها و پیام های بخش «ویرایش شمار واژگان آغازین و اصلی»  
class AdminVirayeshShomarVazheha:
    def __init__(self,id,firstName,msg):
        self.id = id
        self.firstName = firstName
        self.msg = msg
        self.bot = pybotc.Bot("config.cfg")   
    #در صورت زدن دکمه «📝 شمار  واژه ها 🔢» این  دکمه ها و پیام می آیند 
    def sendVShVMessage357(self):
        wortZahlMsg = f"Liebe/Lieber {self.firstName} 🌺🌸, wie viele neue Wörter möchten Sie an einem Tag?"        
        # wortZahlKey = json.dumps({"keyboard":[[BtnS().three],[BtnS().two],[BtnS().one],[BtnS().five,BtnS().ten,BtnS().fifteen,BtnS().twenty],[Btn().getBack]],"resize_keyboard":True})
        wortZahlKey = AKeys().wordsNum
        self.bot.sendMessage(self.id,wortZahlMsg,"none",wortZahlKey)
    #در صورت زدن دکمه «۳» یا «۵» یا «۷»این  دکمه ها و پیام می آیند 
    def send357AllVMessageFAVA(self):
        changedWordNum = f"Die Anzahl der neuen Wörter wurde in <b> {self.msg}</b> geändert."
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
        timeLearningMsg = f"Liebe/Lieber {self.firstName} 🌺🌸, wähle deine tägliche Lernstartzeit, um den Bot zu besuchen."
        # hoursKey = json.dumps({"keyboard":[[BtnS().clock1,BtnS().clock2,BtnS().clock3,BtnS().clock4,BtnS().clock5,BtnS().clock6,BtnS().clock7,BtnS().clock8],[BtnS().clock9,BtnS().clock10,BtnS().clock11,BtnS().clock12,BtnS().clock13,BtnS().clock14,BtnS().clock15,BtnS().clock16],[BtnS().clock17,BtnS().clock18,BtnS().clock19,BtnS().clock20,BtnS().clock21,BtnS().clock22,BtnS().clock23],[Btn().getBack]],"resize_keyboard":True}) 
        hoursKey = Keys().hKeys
        self.bot.sendMessage(self.id,timeLearningMsg,"none",hoursKey)
    #در صورت زدن دکمه «۱..۲۳» این  دکمه ها و پیام می آیند 
    def send1_23MessageYesNo(self,year,monthAlpha,day,weekDay,hourMin,askedYear,askedMonthAlpha,askedDay,askedWeekDay,askedHourMin):
        dash = "___________________________________"
        timeLearningWarningMsg = f"Liebe/Lieber {self.firstName} 🌺🌸, sind Sie zuversichtlich, die Zeit von zu ändern 👉Lern den Wortschatz täglich👈 zu {self.msg} auf {askedWeekDay} {askedDay} {askedMonthAlpha} {askedYear}? \n {dash} \n Zur Zeit 👉Lern den Wortschatz täglich👈 als nächstes auf {weekDay} {day} {monthAlpha} {year}, <b> Beim {hourMin} </b>. \n @DeutschOhal "
        # yesNoKey = json.dumps({"keyboard":[[Btn().yesDash,Btn().noDash]],"resize_keyboard":True}) 
        yesNoKey = Keys().yNDash
        self.bot.sendMessage(self.id,timeLearningWarningMsg,"none",yesNoKey)


    #در صورت همسان بودن زمان یادگیری روزانه با قبلی  این  دکمه ها و پیام می آیند 
    def sendYesMessageSameFAVA(self,year,monthAlpha,day,weekDay,hourMin):
        dash = "___________________________________"
        # "روش شما در همین هنگام هم  {} هست نیازی تغییر و دگرسانی نیست".format(self.msg)

        timeLearningChangedMsg = f"Ihre tägliche Lernzeit ist zur gleichen Zeit {self.msg}. Es ist nicht erforderlich, \n {dash} \n 👉Lern den Wortschatz täglich👈 am <b> {weekDay} {monthAlpha} {day} zu ändern. , </b> {year} <b> Um <b> {hourMin} </b> \n @DeutschOhal"
        # regularHomePageKey = json.dumps({"keyboard":[[BtnA().admin,Btn().reviewWords],[Btn().wordsNum,Btn().wayEdit,Btn().account],[Btn().timeLearnEdit,Btn().reportActivity],[Btn().deleteBot,Btn().aboutBot,Btn().uILangNKeyEdit],[Btn().opinion]],"resize_keyboard":True})
        regularHomePageKey = AKeys().secondMenu
        self.bot.sendMessage(self.id,timeLearningChangedMsg,"none",regularHomePageKey)


    #در صورت زدن دکمه «بله» این  دکمه ها و پیام می آیند 
    def sendYesMessageFAVA(self,year,monthAlpha,day,weekDay,hourMin):
        dash = "___________________________________"
        timeLearningChangedMsg = f"Die tägliche Lernstunde wurde in <b> {hourMin} </b> geändert. \n {dash} \n👉Lern den Wortschatz täglich👈 Weiter am {weekDay} {day} {monthAlpha} {year}, <b> Um {hourMin} </b> \n @DeutschOhal"
        # regularHomePageKey = json.dumps({"keyboard":[[BtnA().admin,Btn().reviewWords],[Btn().wordsNum,Btn().wayEdit,Btn().account],[Btn().timeLearnEdit,Btn().reportActivity],[Btn().deleteBot,Btn().aboutBot,Btn().uILangNKeyEdit],[Btn().opinion]],"resize_keyboard":True})
        regularHomePageKey = AKeys().secondMenu
        self.bot.sendMessage(self.id,timeLearningChangedMsg,"none",regularHomePageKey)
    #در صورت زدن دکمه «نه» به فهرست آغازین و اصلی این  دکمه ها و پیام می آیند 
    def sendNoMessageFAVA(self):
        fehrestAghazinMsg = "Startseite"
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
        reportPageMsg = f"ausgewählt {self.msg}."
        # reportKey = json.dumps ({"keyboard": [[Btn().reportWordsPartions, Btn().reportWeakWords], [Btn().getBack]], "resize_keyboard": True})
        reportKey = Keys().reportKeys
        self.bot.sendMessage(self.id,reportPageMsg,"none",reportKey)

    #در صورت زدن دکمه «گزارش واژگان در بخش ها📈»  این  دکمه ها و پیام می آیند 
    def sendReportAllWordsMessageBBFA(self,num,reportWordsSectionsPercentage):
        dash = "___________________________________" 
        reportWordsSectionsMsg =  f"Liebe/Lieber {self.firstName} 🌺🌸, Melden Sie Ihr gesamtes verwendetes Vokabular in den Partitionen bis heute: \n {dash} \n \n Anzahl aller bisher erstellten Vokabeln: {num} \n {dash} \n Anzahl und der Prozentsatz aller Wörter in allen Partitionen des Leitner-Box: \n \n {reportWordsSectionsPercentage} \n \n @DeutschOhal"
        # backToHomePage = json.dumps({"keyboard":[[Btn().getBack]],"resize_keyboard":True})
        backToHomePage = Keys().getBackKeys
        self.bot.sendMessage(self.id,reportWordsSectionsMsg,"none",backToHomePage)
    #در صورت زدن دکمه «گزارش ناتوانی در واژگان📉»  این  دکمه ها و پیام می آیند 
    # wWDS,wWPGS
    def sendReportWeakWordMessageBBFA(self,wWDS,wWPGS):
        dash = "___________________________________"
        reportWordsSectionsMsg = f"\n Liebe/Lieber {self.firstName}🌺🌸, bis heute, melde den schwächsten Wortschatz beim Lernen, \n {dash.center(73)} \n \n Liste der Vokabeln, die über einen Monat des Lernens gedauert haben und ausgedrückt haben die Anzahl der Tage \n\n<b> {wWDS.center(63)} </b>  \n  {dash.center(73)} \n\n Schwacher Wortschatz in der Reihenfolge des Prozentsatzes jeder Partition der Leitner-Box \n \n {wWPGS} \n @DeutschOhal"
        # backToHomePage = json.dumps({"keyboard":[[Btn().getBack]],"resize_keyboard":True})
        backToHomePage = Keys().getBackKeys
        self.bot.sendMessage(self.id,reportWordsSectionsMsg,"none",backToHomePage)
    #در صورت زدن دکمه «بازگشت به فهرست آغازین🏡»  این  دکمه ها و پیام می آیند 

    #FIXME حذف این تابع از کیبورد و جایگزینی در آنالیز AYVK.sendKeyAndMessageFAVA()
    def sendBBFAMessageFAVA(self):
        self.obj_AYVK.sendKeyAndMessageFAVA()

    def reportWeakWords(self,wWDS,wWPGS): 
        dash = "___________________________________"   
        reportMsg = f"\n Liebe/Lieber {self.firstName}🌺🌸, bis heute, melde den schwächsten Wortschatz beim Lernen, \n {dash.center(73)} \n \n Liste der Vokabeln, die über einen Monat des Lernens gedauert haben und ausgedrückt haben die Anzahl der Tage \n\n {wWDS} \n {dash.center(73)} \n\n Schwacher Wortschatz in der Reihenfolge des Prozentsatzes jeder Partition der Leitner-Box \n \n {wWPGS} \n @DeutschOhal"
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
         languageMsg = f"Lieber/Liebe {self.firstName} 🌺🌸, wählen Sie Ihre Lieblingssprache für Bots-Nachricht und Tastatur"
         
        #  languagesKey = json.dumps({"keyboard":[[BtnS().keyNMsgDe],[BtnS().keyNMsgEn],[BtnS().keyNMsgPer],[Btn().getBack]],"resize_keyboard":True}) 
         languagesKey = Keys().lanKeys
         self.bot.sendMessage(self.id,languageMsg,"none",languagesKey)
    
        #در صورت انتخاب و زدن <پوسته فارسی> به فهرست آغازین و اصلی منتقل شده و این  دکمه ها و پیام می آیند 
    def sendBaleKeyAndMessageFAVA(self): 
        languageSelectedMsg = f"{self.msg} ist für bot ausgewählt"
        # regularHomePageKey = json.dumps({"keyboard":[[BtnA().admin,Btn().reviewWords],[Btn().wordsNum,Btn().wayEdit,Btn().account],[Btn().timeLearnEdit,Btn().reportActivity],[Btn().deleteBot,Btn().aboutBot,Btn().uILangNKeyEdit],[Btn().opinion]],"resize_keyboard":True})
        regularHomePageKey = AKeys().secondMenu
        self.bot.sendMessage(self.id,languageSelectedMsg,"none",regularHomePageKey)




        # self.obj_Start.sendKeyAndMessagesUI()
    #    یا کیبورد و پیام پارسی⌨💬 این دکمه ها و پیام از فهرست آغازین و اصلی  می آیند  deutsch Menu, english Menu  در صورت زدن یکی از دکمه های  
    def sendKeyAndMessageFNVA2(self):
        languageSelectedMsg = f"{self.msg} ist für bot ausgewählt"
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
        aboutMsg =f"Grüße Liebe/Lieber <i> {self.firstName} </i>🌺🌸, Dieser Bot kann alle neuen und hervorgehobenen Wörter des Buches <b> 'Großes Übungsbuch Wortschatz' </b> im Kontext von Leitners Wiederholung lernen und täglich in der Kalenderstruktur üben. Mit der Möglichkeit, Sie daran zu erinnern und die Antwort auf Deutsch zu wählen, werden Synonyme, Englisch und Persisch unter Verwendung authentischer deutscher Sprachressourcen aktiviert, sodass die vollständige Beherrschung eines Wortes und eines Wortes in mindestens einem Monat erreicht wird. Aus Ihrem Kurzzeitgedächtnis wird es in Ihrem Langzeitgedächtnis sein."
        # regularHomePageKey = json.dumps({"keyboard":[[BtnA().admin,Btn().reviewWords],[Btn().wordsNum,Btn().wayEdit,Btn().account],[Btn().timeLearnEdit,Btn().reportActivity],[Btn().deleteBot,Btn().aboutBot,Btn().uILangNKeyEdit],[Btn().opinion]],"resize_keyboard":True})
        regularHomePageKey = AKeys().secondMenu
        self.bot.sendMessage(self.id,aboutMsg,"none",regularHomePageKey)

#FIXME copy these 4 method to every user language
    def sendKeyAndMessageSendingSugession(self):
        aboutMsg =f"Liebe/Lieber <i>{self.firstName}</i>🌺🌸,Wenn du Kommentare, Kritik oder Vorschläge hast, sende diese bitte an uns."
        # backToHomePage = json.dumps({"keyboard":[[Btn().getBack]],"resize_keyboard":True})
        backToHomePage = Keys().getBackKeys
        
        self.bot.sendMessage(self.id,aboutMsg,"none",backToHomePage)

    def sendKeyAndMessageDeliverOpinion(self,opId):
        aboutMsg =f"Liebe/Lieber <i>{self.firstName}</i>🌺🌸, deine Kommentar wurde mit dieser <b>{opId}</b> Tracking-Nummer registriert."
        # regularHomePageKey = json.dumps({"keyboard":[[Btn().reviewWords],[Btn().wordsNum,Btn().wayEdit,Btn().account],[Btn().timeLearnEdit,Btn().reportActivity],[Btn().deleteBot,Btn().aboutBot,Btn().uILangNKeyEdit],[Btn().opinion]],"resize_keyboard":True})
        regularHomePageKey = AKeys().secondMenu
        self.bot.sendMessage(self.id,aboutMsg,"none",regularHomePageKey)

    def sendKeyAndMessageUsingBotKeys(self):
        aboutMsg =f"Kein Text eingegeben! Wenn Sie einen Kommentar senden möchten, <b>ohne Verwendung der Bottastatur</b>, geben Sie den Text ein und senden Sie ihn dann."
        # regularHomePageKey = json.dumps({"keyboard":[[Btn().reviewWords],[Btn().wordsNum,Btn().wayEdit,Btn().account],[Btn().timeLearnEdit,Btn().reportActivity],[Btn().deleteBot,Btn().aboutBot,Btn().uILangNKeyEdit],[Btn().opinion]],"resize_keyboard":True})
        regularHomePageKey = Keys().secondMenu
        self.bot.sendMessage(self.id,aboutMsg,"none",regularHomePageKey)

    def sendKeyAndMessageOutOfRangeMsg(self):
        aboutMsg =f"Die Anzahl der gesendeten characters und Wörter ist zu hoch! Senden Sie Ihren Text kürzer oder in mehreren Abschnitten."
        # regularHomePageKey = json.dumps({"keyboard":[[Btn().reviewWords],[Btn().wordsNum,Btn().wayEdit,Btn().account],[Btn().timeLearnEdit,Btn().reportActivity],[Btn().deleteBot,Btn().aboutBot,Btn().uILangNKeyEdit],[Btn().opinion]],"resize_keyboard":True})
        regularHomePageKey = Keys().secondMenu
        self.bot.sendMessage(self.id,aboutMsg,"none",regularHomePageKey)

#تمامی کیبوردها و پیام های بخش «حذف ربات 🗑» در فهرست آعازین واصلی
class AdminHazfRobot:
    def __init__(self,id,firstName,msg):
        self.id = id
        self.firstName = firstName
        self.bot = pybotc.Bot("config.cfg")   
        self.obj_AYVK = AghazYadgiriVazhehayeKetab(id,firstName,msg)

    #    self.HazfRobot(id,firstName,msg).sendHRKeyAndMessageYesNo()

    #در صورت زدن دکمه «حذف ربات 🗑»  این دکمه ها و پیام می آیند    
    def sendHRKeyAndMessageYesNo(self):
        deleteBotWarnMsg = f"Liebe/Lieber {self.firstName} 🌺🌸, sind Sie sicher, Bot zu löschen? Dadurch werden auch alle Ihre Datensätze gelöscht, und es werden keine weiteren Nachrichten an Sie gesendet."
        # yesNoKey = json.dumps({"keyboard":[[Btn().no, Btn().yesDelete]],"resize_keyboard":True}) 
        yesNoKey = Keys().yNKeys
        self.bot.sendMessage(self.id,deleteBotWarnMsg,"none",yesNoKey)
    #در صورت زدن دکمه «بله» به بخش فهرست نخستین🛎 و اولیه منتقل شده و   این دکمه ها و پیام می آیند    
    def sendYesKeyAndMessageFNVA(self):
        deleteBotMsg = "Bot wird gelöscht!"
        # firstHomePageKey = json.dumps ({"keyboard": [[BtnA().admin, Btn().startLearning], [Btn().aboutBotNew, Btn().uILangNKeyEditNew]], " resize_keyboard ": True})
        firstHomePageKey = AKeys().firstMenu
        self.bot.sendMessage(self.id,deleteBotMsg,"none",firstHomePageKey)

    #در صورت زدن دکمه «خیر» به بخش فهرست آغازین و اصلی منتقل شده و   این دکمه ها و پیام می آیند    
    #FIXME حذف این تابع از کیبورد و جایگزینی در آنالیز AYVK.sendKeyAndMessageFAVA()
    def sendNoKeyAndMessageFAVA(self):
        self.obj_AYVK.sendKeyAndMessageFAVA()



#تمامی کیبوردها و پیام های بخش «یادگیری واژگان روزانه» 
class AdminYadgiriVazheganRuzaneh:
    def __init__(self,id,firstName,msg):
        self.id = id
        self.firstName = firstName
        self.msg = msg
        self.obj_AYVK = AghazYadgiriVazhehayeKetab(id,firstName,msg)
        self.bot = pybotc.Bot("config.cfg")

#last