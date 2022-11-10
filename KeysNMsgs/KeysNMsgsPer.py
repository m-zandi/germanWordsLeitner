import json
import requests
import sys
sys.path.append( "../")

from mainV2.base.Buttons import ButtonPer as Btn
from mainV2.base.Buttons import ButtonSame as BtnS
from mainV2.base.ButtonsA import ButtonAdminPer as BtnA 
from mainV2.base.Keys import SKeys
from mainV2.base.Keys import PerKeys  as Keys 
from mainV2.base.KeysA import PerKeysA as AKeys
from mainV2.base.Txt import MessageNVarPer as MNV

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
        print(f"way = {way}")
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
         languageMsg = "زبان دلخواهت انتخاب کن {} عزیز 🌺🌸 برای پیام ها و فهرست ربات".format(self.firstName)
        #  languagesKey = json.dumps({"keyboard":[[BtnS().keyNMsgDe],[BtnS().keyNMsgEn],[BtnS().keyNMsgPer]],"resize_keyboard":True}) 
         languagesKey = SKeys(Btn(),MNV()).uI
         self.bot.sendMessage(self.id,languageMsg,"none",languagesKey)

   #    یا کیبورد و پیام پارسی⌨💬 این دکمه ها و پیام از فهرست نخستین🛎 و اولیه  می آیند  deutsch Menu, english Menu  در صورت زدن یکی از دکمه های  
    def sendKeyAndMessageFNVAUIselected(self):
        languageSelectedMsg = f"برای ربات {self.msg} انتخاب شد."
        # firstHomePageKey = json.dumps({"keyboard":[[Btn().startLearning],[Btn().aboutBotNew,Btn().uILangNKeyEditNew]],"resize_keyboard":True})
        firstHomePageKey = Keys().firstMenu
        self.bot.sendMessage(self.id,languageSelectedMsg,"none",firstHomePageKey)
    

    def sendKeyAndMessageFNVAUINakhostin(self):
        languageSelectedMsg = "فهرست نخستین🛎"
        # firstHomePageKey = json.dumps({"keyboard":[[Btn().startLearning],[Btn().aboutBotNew,Btn().uILangNKeyEditNew]],"resize_keyboard":True})
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
        msgNextTrainingTimeDate = f"حساب کاربریت <i>{self.firstName}</i> عزیز 🌺🌸 \n{ent}\n{output}\n{dash}\n{outpuTodayDateNTime}\n@DeutschOhal"
        # regularHomePageKey = json.dumps({"keyboard":[[Btn().reviewWords],[Btn().wordsNum,Btn().wayEdit,Btn().account],[Btn().timeLearnEdit,Btn().reportActivity],[Btn().deleteBot,Btn().aboutBot,Btn().uILangNKeyEdit],[Btn().opinion]],"resize_keyboard":True})
        regularHomePageKey = Keys().secondMenu
        self.bot.sendMessage(self.id,msgNextTrainingTimeDate,"none",regularHomePageKey)


    #در صورت زدن دکمه ((آعاز یادگیری واژه های کتاب)) این دکمه ها و پیام می آیند
    def sendAYVKKeyAndMessage327(self):
        wortZahlMsg = "چه تعداد و شمار واژه نو {} عزیز 🌺🌸 در روز می خواهی؟".format(self.firstName)        
        # wortZahlKey = json.dumps({"keyboard":[[BtnS().threeNew],[BtnS().twoNew],[BtnS().oneNew]],"resize_keyboard":True})
        wortZahlKey = SKeys(Btn(),MNV()).numWordsNew
        self.bot.sendMessage(self.id,wortZahlMsg,"none",wortZahlKey)
    #در صورت زدن یکی از دکمه های ۳ یا ۵  یا ۷ این دکمه ها و پیام می آیند
    def send357KeyAndMessageDESP(self):
        waysMsg = "روش یادگیری واژه های کتاب را {} عزیز 🌺🌸 انتخاب کن.".format(self.firstName)
        # wayKey = json.dumps({"keyboard":[[BtnS().deutschNew],[BtnS().englishNew],[BtnS().synonymNew],[BtnS().persianNew]],"resize_keyboard":True}) 
        wayKey = SKeys(Btn(),MNV()).waysNew
        self.bot.sendMessage(self.id,waysMsg,"none",wayKey)

    

     #    یا پارسی این دکمه و پیام می آیند  deutsch , english , synonym  در صورت زدن یکی از دکمه های  
    def sendDESPKeyAndMessageLampGuid(self,way,wKind,numW,numAll,standardizedWord,content,chapter,wordsPage,wordLink):
        dash = "___________________________________"
        guide = f" راهنمایی🔔: واژه را مطالعه کنید و {way} آن را بگویید و به خاطر بسپارید پس از آن جهت دیدن پاسخ درست و مقایسه  با پاسخ خود روی 💡 تلنگر بزنید. "
        newWordsMsg = f".{numW}/{numAll}                                         {wKind}.<b>{standardizedWord.center(63)}</b>\n.سرفصل : {content}\nفصل : {chapter} \nبرگ:{wordsPage}.\n{dash}\n{wordLink}{guide}"
        # {content}\n{cotentNChap} \nبرگ:{wordsPage}
        # antwortKey = json.dumps({"keyboard":[[BtnS().lamp]],"resize_keyboard":True}) 
        antwortKey = SKeys(Btn(),MNV()).lampKeys
        self.bot.sendMessage(self.id,newWordsMsg,"none",antwortKey)


                               
   #    یا پارسی این دکمه و پیام می آیند  deutsch , english , synonym  در صورت زدن یکی از دکمه های  
    def sendDESPKeyAndMessageLamp(self,wKind,numW,numAll,standardizedWord,content,chapter,wordsPage,wordLink):
        newWordsMsg = f".{numW}/{numAll}                                         {wKind}.\n<b>{standardizedWord}</b>\n.سرفصل : {content}\nفصل : {chapter} \nبرگ:{wordsPage}.\n. \n {wordLink} "
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
        guide = f"راهنمایی🔔: با بررسی پاسخ فرستاده شده و پاسخ خود ،درستی یا نادرستی پاسخ خود را با انتخاب ✅ یا ❌ برگزینید."
        pa = f"{icon}{way} پاسخ به "
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
        pa = f"{icon}{way} پاسخ به "
        lenngthPa = len(pa)
        pa = pa.center(72 - lenngthPa)
        newWordsMsg = f"<b>{pa}</b>\n{standardizedAnswer.center(63)}.\n {answerLink}"
        # rwKey = json.dumps({"keyboard":[[BtnS().crossCheck,BtnS().check]],"resize_keyboard":True}) 
        rwKey = SKeys(Btn(),MNV()).rW
        self.bot.sendMessage(self.id,newWordsMsg,"none",rwKey)
    #done section 7
    #در صورت زدن آخرین دکمه از❌","✅ این دکمه و پیام می آیند  
    def sendLastVXKeyAndMessageBBFA(self,msgId,nWorkedWords,nRWords,nWWrong,wrongWordsNpages,weekDay,day,month,year,houNMTraining,dateGriNextTraining,wordsSectionPosition):
        dash = "___________________________________"
        # print(f"nRWords = {nRWords},nWorkedWords = {nWorkedWords}")
        percentageRight = self.obj_dbContatct.Percentage().percentage(nRWords,nWorkedWords)
        percentageWrong = self.obj_dbContatct.Percentage().percentage(nWWrong,nWorkedWords)
        graphRight = self.obj_dbContatct.Graph().graph(nRWords,nWorkedWords)
        graphWrong = self.obj_dbContatct.Graph().graph(nWWrong,nWorkedWords)
        guide = f"🔔 برای مرور واژهای کار شده می توانید پس از انتخاب ({Btn().getBack}) ،({Btn().reviewWords}) را انتخاب کنید. "

        daliyReport = f"<i>گزارش کارکردت، {self.firstName} عزیز 🌺🌸 در امروز:</i>\n{dash.center(14)}\nشمار وا‌ژه های کار شده : <b>{nWorkedWords}</b>\nشمار واژه های درست : <b>{nRWords}</b>\nشمار واژه های نادرست : <b>{nWWrong}</b>\n{dash.center(14)}\n<i>درصد درستی و نادرستی واژه ها :</i>\nدرستی <b>{graphRight} % {percentageRight} </b>\nنادرستی <b>{graphWrong} % {percentageWrong}</b> \n{dash.center(14)}\nفهرست واژه های نادرست امروز به همراه نشانی برگ در کتاب :\n <b>{wrongWordsNpages}</b>\n{dash.center(14)}\n👈یادگیری واژگان روزانه👉 بعدی و پسین در تاریخ <b> {weekDay} {day} {month} {year} </b>, در ساعت و زمان <b>{houNMTraining}</b> به وقت ایران، مصادف با <b>{dateGriNextTraining}</b>\n{dash}\n<i>بخش و شمار تمامی واژه ها در جعبه لایتنر :</i>\nشمار واژه ها در بخش نخست :<b>{wordsSectionPosition[0]} </b>\nشمار واژه ها در بخش دوم :<b> {wordsSectionPosition[1]} </b>\nشمار واژه ها در بخش سوم : <b>{wordsSectionPosition[2]} </b>\nشمار واژه ها در بخش چهارم :<b> {wordsSectionPosition[3]}</b> \nشمار واژه ها در بخش پنجم :‌<b>{wordsSectionPosition[4]}</b> \nشمار واژه ها در بخش ششم :<b>‌{wordsSectionPosition[5]}</b>\n{dash}\nشمار واژگان به صورت کامل یادگیری شده :<b>‌{wordsSectionPosition[6]}</b>\n{dash} \n<i>{guide}</i>\n@DeutschOhal\n"
        # print(f"daily report = {daliyReport}")
        parse_mode = "HTML"
        # backToHomePage = json.dumps({"keyboard":[[Btn().getBack]],"resize_keyboard":True})
        backToHomePage = Keys().getBackKeys
        # self.bot.sendMessage(self.id,daliyReport,"none",backToHomePage)
        self.bot.editMessage(self.id,msgId,daliyReport,parse_mode,backToHomePage)
        
       
    # فرستادن تاریخ و زمان یادگیری واژگان بعدی پسین
    def sendNextTrainingDateTimeKeyAndMessageBBFA(self,weekDay,day,monthAlpha,year,hourMin):
        # y = "یادگیری واژگان روزانه"
        msgNextTrainingTimeDate = f"👈یادگیری واژگان روزانه👉 بعدی و پسین‌ات {self.firstName} عزیز 🌺🌸 در تاریخ  <b> {weekDay} {day} {monthAlpha} {year} </b>, در ساعت و زمان  <b>{hourMin} </b> می باشد.\n@DeutschOhal"
        # regularHomePageKey = json.dumps({"keyboard":[[Btn().reviewWords],[Btn().wordsNum,Btn().wayEdit,Btn().account],[Btn().timeLearnEdit,Btn().reportActivity],[Btn().deleteBot,Btn().aboutBot,Btn().uILangNKeyEdit],[Btn().opinion]],"resize_keyboard":True})
        regularHomePageKey = Keys().secondMenu
        self.bot.sendMessage(self.id,msgNextTrainingTimeDate,"none",regularHomePageKey)





     #در صورت زدن  دکمه بازگشت به فهرست آغازین🏡 به بخش فهرست آغازین و اصلی منتقل شده و این دکمه ها و پیام می آیند 
     #FIXME حذف این تابع از کیبورد و جایگزینی در آنالیز AYVK.sendKeyAndMessageFAVA()
    def sendKeyAndMessageFAVA(self):
        fehrestAghazinMsg = "فهرست آغازین"
        # regularHomePageKey = json.dumps({"keyboard":[[Btn().reviewWords],[Btn().wordsNum,Btn().wayEdit,Btn().account],[Btn().timeLearnEdit,Btn().reportActivity],[Btn().deleteBot,Btn().aboutBot,Btn().uILangNKeyEdit],[Btn().opinion]],"resize_keyboard":True})
        regularHomePageKey = Keys().secondMenu
        self.bot.sendMessage(self.id,fehrestAghazinMsg,"none",regularHomePageKey)

    def sendKeyAndMessageUserMustWait(self):
        fehrestAghazinMsg = "تا تاریخ بعدی "
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
        msgWarning = "⛔️😡😡⛔️از فرستادن Spam خودداری کنید⛔️😡😡⛔️"
        # antwortKey = json.dumps({"keyboard":[[BtnS().lamp]],"resize_keyboard":True}) 
        # antwortKey = SKeys(Btn(),MNV()).lampKeys
        antwortKey = ""
        self.bot.sendMessage(self.id,msgWarning,"none",antwortKey)
        #spam warning هنگامه آخرین واژه BtnS().crossCheck,"✅ پیام خطا به جهت فرستادن تکراری 
    def sendWarningKeyAndMessageBBFA(self):
        msgWarning = "⛔️😡😡⛔️از فرستادن Spam خودداری کنید⛔️😡😡⛔️"
        # backToHomePage = json.dumps({"keyboard":[[Btn().getBack]],"resize_keyboard":True})
        # backToHomePage = Keys().getBackKeys
        backToHomePage = ""
        self.bot.sendMessage(self.id,msgWarning,"none",backToHomePage)
     
    #spam warning  پیام خطا به جهت فرستادن تکراری برای کاربری که هنوز نام نویسی نشده 
    def sendWarningRepeatedKeyAndMessageToNoneUser(self):
        msgWarning = "⛔️😡😡⛔️از فرستادن Spam  خودداری کنید⛔️😡😡⛔️"
        # firstHomePageKey = json.dumps({"keyboard":[[Btn().startLearning],[Btn().aboutBotNew,Btn().uILangNKeyEditNew]],"resize_keyboard":True}) 
        # firstHomePageKey = Keys().firstMenu
        firstHomePageKey = ""
        self.bot.sendMessage(self.id,msgWarning,"none",firstHomePageKey)


    #spam warning  پیام خطا به جهت فرستادن تکراری برای کاربر  
    def sendWarningRepeatedKeyAndMessageToUser(self):
        msgWarning = "⛔️😡😡⛔️از فرستادن Spam  خودداری کنید⛔️😡😡⛔️"
        # regularHomePageKey = json.dumps({"keyboard":[[Btn().reviewWords],[Btn().wordsNum,Btn().wayEdit,Btn().account],[Btn().timeLearnEdit,Btn().reportActivity],[Btn().deleteBot,Btn().aboutBot,Btn().uILangNKeyEdit],[Btn().opinion]],"resize_keyboard":True})
        # regularHomePageKey = Keys().secondMenu
        regularHomePageKey = ""
        self.bot.sendMessage(self.id,msgWarning,"none",regularHomePageKey) 

   
      #none keyboard warning  پیام خطا به جهت عدم استفاده از کیبورد رباط  
    def sendWarningNoneKeyboardToUser(self):
        msgWarning = "فقط از کیبورد ربات استفاده کنید!"
        # regularHomePageKey = json.dumps({"keyboard":[[Btn().reviewWords],[Btn().wordsNum,Btn().wayEdit,Btn().account],[Btn().timeLearnEdit,Btn().reportActivity],[Btn().deleteBot,Btn().aboutBot,Btn().uILangNKeyEdit],[Btn().opinion]],"resize_keyboard":True})
        regularHomePageKey = Keys().secondMenu
        # regularHomePageKey=""
        self.bot.sendMessage(self.id,msgWarning,"none",regularHomePageKey) 

   
      #none keyboard warning  پیام خطا به جهت عدم استفاده از کیبورد رباط  
    def sendWarningNoneKeyboardToGuest(self):
        msgWarning = "فقط از کیبورد ربات استفاده کنید!"
        # firstHomePageKey = json.dumps({"keyboard":[[Btn().startLearning],[Btn().aboutBotNew,Btn().uILangNKeyEditNew]],"resize_keyboard":True}) 
        firstHomePageKey = Keys().firstMenu
        # firstHomePageKey =""
        self.bot.sendMessage(self.id,msgWarning,"none",firstHomePageKey) 


class AutomaticMessage:
    def __init__(self,id,firstName):
        self.id = id
        self.bot = pybotc.Bot("config.cfg")
        self.firstName = firstName
    def sendKeyAndMessageDailyLearn(self):
        msg = f"آغاز یادگیری و تمرین واژگان، <i>{self.firstName}</i> عزیز 🌺🌸 روی یادگیری واژگان روزانه تلنگر بزن ! "
        # regularHomePageKey = json.dumps({"keyboard":[[Btn().dailyLearnWords]],"resize_keyboard":True})
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
        aboutMsg =f"با درود و سلام به شما <i>{self.firstName}</i> عزیز 🌺🌸\nاین ربات امکان یادگیری تمامی واژه های جدید و مورد تاکید کتاب <b>'Großes Übungsbuch Wortschatz'</b>  را در چهارچوب تکرار و تمرین به روش لایتنر به صورت روزمره و در ساختار تقویم با امکان یادآوری به شما و انتخاب پاسخ به آلمانی، به مترادف، به انگلیسی و به فارسی را با استفاده از منابع معتبر زبان آلمانی میسر می کند، به گونه ای که تسلط کامل در حداقل یک ماه نسبت به یک واژه حاصل می شود و واژه از حافظه کوتاه مدت شما درحافظه بلند مدتتان قرار می گیرد." 
        # firstHomePageKey = json.dumps({"keyboard":[[Btn().startLearning],[Btn().aboutBotNew,Btn().uILangNKeyEditNew]],"resize_keyboard":True}) 
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
        reviewMsg = "روش مرور واژگان را براساس یکی از گزینه ها، {} عزیز🌺🌸 انتخاب کن".format(self.firstName)
        # reviewKey = json.dumps({"keyboard":[[Btn().chapterNSection],[Btn().leitnerBoxParts],[Btn().weakWords],[Btn().getBack]],"resize_keyboard":True})  
        reviewKey = Keys().revKeys
        self.bot.sendMessage(self.id,reviewMsg,"none",reviewKey)
        
        #🔎
        ###در صورت زدن دکمه «سرفصل و فصل» در بخش آغازین و اصلی این  دکمه ها و پیام نخستین واژه می آیند 
    def sendWordsChapterContentKeyAndMessageFirstOLdWord(self,content,chapter,word,answer,counter,length,section,page,link):
        oldWordsMsg = f".سرفصل : {content}\nفصل : {chapter}\n\n<b>{word}</b>\n\n{answer.center(63)}\n\n.برگ:{page}                         {section}: {length}/{counter+1}{link}."
        reviewNextKey = json.dumps({"keyboard":[[Btn().nextWordChapNS],[Btn().getBack]],"resize_keyboard":True}) 
        reviewNextKey = Keys().revChapNexKeys
        self.bot.sendMessage(self.id,oldWordsMsg,"none",reviewNextKey)

    def sendWordsChapterContentKeyAndMessageFirstOLdWordOneLength(self,content,chapter,word,answer,counter,length,section,page,link):
        oldWordsMsg = f".سرفصل : {content}\nفصل : {chapter}\n\n<b>{word}</b>\n\n{answer.center(63)}\n\n.برگ:{page}                         {section}: {length}/{counter+1}{link}."
        # backToHomePage = json.dumps({"keyboard":[[Btn().getBack]],"resize_keyboard":True}) 
        backToHomePage = Keys().getBackKeys
        self.bot.sendMessage(self.id,oldWordsMsg,"none",backToHomePage)




    #سرفصل و فصل- کیبورد حاوی قبلی و بعدی  
    def sendWordsChapterContentKeyAndMessagMiddleOLdWord(self,content,chapter,word,answer,counter,length,section,page,link):
        oldWordsMsg = f".سرفصل : {content}\nفصل : {chapter}\n\n<b>{word}</b>\n\n{answer.center(63)}\n\n.برگ:{page}                         {section}: {length}/{counter+1}{link}."
        # reviewMiddleKeys = json.dumps({"keyboard":[[Btn().beforeWordChapNS,Btn().nextWordChapNS],[Btn().getBack]],"resize_keyboard":True}) 
        reviewMiddleKeys = Keys().revChapMidKeys
        self.bot.sendMessage(self.id,oldWordsMsg,"none",reviewMiddleKeys)
    
    #سرفصل و فصل- کیبورد حاوی قبلی و آخرین واژه  
    def sendWordsChapterContentKeyAndMessagLastOLdWord(self,content,chapter,word,answer,counter,length,section,page,link):
        oldWordsMsg = f".سرفصل : {content}\nفصل : {chapter}\n\n<b>{word}</b>\n\n{answer.center(63)}\n\n.برگ:{page}                         {section}: {length}/{counter+1}{link}."
        # reviewBeforeKey = json.dumps({"keyboard":[[Btn().beforeWordChapNS],[Btn().getBack]],"resize_keyboard":True}) 
        reviewBeforeKey = Keys().revChapBefKeys
        self.bot.sendMessage(self.id,oldWordsMsg,"none",reviewBeforeKey)


    #🔭
    ###در صورت زدن دکمه «بخش ها» در بخش آغازین و اصلی این  دکمه ها و پیام نخستین واژه می آیند 
    def sendBakhshhaKeyAndMessageFirstWord(self,counter,length,section,word,answer,page,content,chapter,link):
        oldWordsMsg = f". {section}: {length}/{counter+1}\n<b>{word}</b>\n\n{answer.center(63)}\n\n.سرفصل : {content}\nفصل : {chapter}  \n {link}\nبرگ:{page}"
        # reviewNextKey = json.dumps({"keyboard":[[Btn().nextWordLeitBP],[Btn().getBack]],"resize_keyboard":True}) 
        reviewNextKey = Keys().revLeitNexKeys
        self.bot.sendMessage(self.id,oldWordsMsg,"none",reviewNextKey)
    # وقتی طول آریه یکی است
    def sendBakhshhaKeyAndMessageFirstWordOneLength(self,counter,length,section,word,answer,page,content,chapter,link):
        oldWordsMsg = f". {section}: {length}/{counter+1}\n<b>{word}</b>\n\n{answer.center(63)}\n\n.سرفصل : {content}\nفصل : {chapter}  \n {link}\nبرگ:{page}"
        # backToHomePage = json.dumps({"keyboard":[[Btn().getBack]],"resize_keyboard":True})
        backToHomePage = Keys().getBackKeys 
        self.bot.sendMessage(self.id,oldWordsMsg,"none",backToHomePage)


        #بخش ها- کیبورد حاوی قبلی و بعدی 
    def sendBakhshhaKeyAndMessageMiddleWord(self,counter,length,section,word,answer,page,content,chapter,link):
        oldWordsMsg = f". {section}: {length}/{counter+1}\n<b>{word}</b>\n\n{answer.center(63)}\n\n.سرفصل : {content}\nفصل : {chapter}  \n {link}\nبرگ:{page}"
        #اگر واژه ای بعد از این هنوز موجود باشد
        # reviewBackNextKey = json.dumps({"keyboard":[[Btn().beforeWordLeitBP,Btn().nextWordLeitBP],[Btn().getBack]],"resize_keyboard":True}) 
        reviewBackNextKey = Keys().revLeitMidKeys
        self.bot.sendMessage(self.id,oldWordsMsg,"none",reviewBackNextKey)

        #بخش ها- کیبورد حاوی قبلی  
    def sendBakhshhaKeyAndMessageLastWord(self,counter,length,section,word,answer,page,content,chapter,link):
        oldWordsMsg = f". {section}: {length}/{counter+1}\n<b>{word}</b>\n\n{answer.center(63)}\n\n.سرفصل : {content}\nفصل : {chapter}  \n {link}\nبرگ:{page}"
        #اگر واژه ای بعد از این دیگر موجود نباشد
        # reviewBackKey = json.dumps({"keyboard":[[Btn().beforeWordLeitBP],[Btn().getBack]],"resize_keyboard":True}) 
        reviewBackKey = Keys().revLeitBefKeys
        self.bot.sendMessage(self.id,oldWordsMsg,"none",reviewBackKey)

    #🔬
    ###در صورت زدن دکمه «واژگان ناتوان» در بخش آغازین و اصلی این  دکمه ها و پیام نخستین واژه می آیند 
    def sendWeakWordsKeyAndMessageFirstOLdWord(self,durationDays,counter,length,section,word,answer,content,chapter,page,link):
        oldWordsMsg = f".شمار روزها : {durationDays}         {section}:{counter+1}/{length}.\n\n<b>{word}</b>\n\n{answer.center(63)}\n\n.سرفصل : {content}\nفصل : {chapter} \n {link}\n{page}:برگ"
        # برگ:{page}
        # {page}:برگ
        # reviewNextKey = json.dumps({"keyboard":[[Btn().nextWordWW],[Btn().getBack]],"resize_keyboard":True}) 
        reviewNextKey = Keys().revWeakNexKeys
        self.bot.sendMessage(self.id,oldWordsMsg,"none",reviewNextKey)
    #اگر طول آرایه یک بود
    def sendWeakWordsKeyAndMessageFirstOLdWordOneLength(self,durationDays,counter,length,section,word,answer,content,chapter,page,link):
        oldWordsMsg = f".شمار روزها : {durationDays}         {section}:{counter+1}/{length}.\n\n<b>{word}</b>\n\n{answer.center(63)}\n\n.سرفصل : {content}\nفصل : {chapter} \n {link}\n{page}:برگ"
        # برگ:{page}
        # {page}:برگ
        # backToHomePage = json.dumps({"keyboard":[[Btn().getBack]],"resize_keyboard":True}) 
        backToHomePage = Keys().getBackKeys
        self.bot.sendMessage(self.id,oldWordsMsg,"none",backToHomePage)


 
    def sendWeakWordsKeyAndMessageNoWord(self):
        noWeakWordMsg = f" واژه ناتوانی نداری <i> {self.firstName}</i> عزیز 🌺🌸"
        # برگ:{page}
        # {page}:برگ
        # regularHomePageKey = json.dumps({"keyboard":[[Btn().reviewWords],[Btn().wordsNum,Btn().wayEdit,Btn().account],[Btn().timeLearnEdit,Btn().reportActivity],[Btn().deleteBot,Btn().aboutBot,Btn().uILangNKeyEdit],[Btn().opinion]],"resize_keyboard":True})
        regularHomePageKey = Keys().secondMenu
        self.bot.sendMessage(self.id,noWeakWordMsg,"none",regularHomePageKey)   

    def sendWeakWordsKeyAndMessageNoWordOtherReview(self):
        noWeakWordMsg = f" واژه ای تا این لحظه و دم <i> {self.firstName}</i> عزیز 🌺🌸تمرین و  کار نکرد ه ای! "
        # برگ:{page}
        # {page}:برگ
        # regularHomePageKey = json.dumps({"keyboard":[[BtnA().admin,Btn().reviewWords],[Btn().wordsNum,Btn().wayEdit,Btn().account],[Btn().timeLearnEdit,Btn().reportActivity],[Btn().deleteBot,Btn().aboutBot,Btn().uILangNKeyEdit],[Btn().opinion]],"resize_keyboard":True})
        regularHomePageKey = Keys().secondMenu
        self.bot.sendMessage(self.id,noWeakWordMsg,"none",regularHomePageKey)


    #واژگان ناتوان- کیبورد حاوی قبلی و بعدی  
    def sendWeakWordsKeyAndMessagMiddleOLdWord(self,durationDays,counter,length,section,word,answer,content,chapter,page,link):
        oldWordsMsg = f".شمار روزها : {durationDays}         {section}:{counter+1}/{length}.\n\n<b>{word}</b>\n\n{answer.center(63)}\n\n.سرفصل : {content}\nفصل : {chapter} \n {link}\n{page}:برگ"
        # reviewNextKey = json.dumps({"keyboard":[[Btn().beforeWordWW,Btn().nextWordWW],[Btn().getBack]],"resize_keyboard":True}) 
        reviewNextKey = Keys().revWeakMidKeys
        self.bot.sendMessage(self.id,oldWordsMsg,"none",reviewNextKey)
    #واژگان ناتوان- کیبورد حاوی قبلی و آخرین واژه  
    def sendWeakWordsKeyAndMessagLastOLdWord(self,durationDays,counter,length,section,word,answer,content,chapter,page,link):
        oldWordsMsg = f".شمار روزها : {durationDays}         {section}:{counter+1}/{length}.\n\n<b>{word}</b>\n\n{answer.center(63)}\n\n.سرفصل : {content}\nفصل : {chapter} \n {link}\n{page}:برگ"
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
        waysMsg = "روش یادگیری واژه های کتاب را {} عزیز 🌺🌸 انتخاب کن.".format(self.firstName)
        # wayKey = json.dumps({"keyboard":[[BtnS().deutsch,BtnS().english],[BtnS().synonym,BtnS().persian],[Btn().getBack]],"resize_keyboard":True}) 
        wayKey = Keys().ways 
        self.bot.sendMessage(self.id,waysMsg,"none",wayKey)
        



     #    یا پارسی  این دکمه ها و پیام می آیند  deutsch , english , synonym  در صورت زدن یکی از دکمه های  
    def sendDESPAllKeyAndMessageYesNo(self,way): 
        waysWarningMsg = f"آیا مطمئن و استیگان نسبت به انتخاب روش جدید <b>{self.msg}</b>داری {self.firstName} عزیز🌺🌸 زیرا در صورت انتخاب سابقه قبلی شما به <b>{way}</b> در مورد واژه های کار شده از بین می رود؟"
        # yesNoKey = json.dumps({"keyboard":[[Btn().noDot,Btn().yesDot]],"resize_keyboard":True})
        yesNoKey = Keys().yNDot 
        self.bot.sendMessage(self.id,waysWarningMsg,"none",yesNoKey)


   #    یا پارسی و یکسان بودن با روش قبلی این دکمه ها و پیام می آیند  deutsch , english , synonym  در صورت زدن یکی از دکمه های  
    def sendDESPAllSameKeyAndMessageFAVA(self): 
        waysWarningMsg = f"روش شما در همین هنگام <b>{self.msg}</b> هست نیازی به دگرسانی و تغییر نیست."
        # regularHomePageKey = json.dumps({"keyboard":[[Btn().reviewWords],[Btn().wordsNum,Btn().wayEdit,Btn().account],[Btn().timeLearnEdit,Btn().reportActivity],[Btn().deleteBot,Btn().aboutBot,Btn().uILangNKeyEdit],[Btn().opinion]],"resize_keyboard":True})
        regularHomePageKey = Keys().secondMenu
        self.bot.sendMessage(self.id,waysWarningMsg,"none",regularHomePageKey)

    #در صورت زدن دکمه «بله» به فهرست آغازین و اصلی منتقل شده و این  دکمه ها و پیام می آیند 
    def sendBaleKeyAndMessageFAVA(self): 
        waysChangedMsg = "دگرسانی و تغییر📝 روش 🛣 به <b>{}</b> انجام شد.".format(self.msg)
        # regularHomePageKey = json.dumps({"keyboard":[[Btn().reviewWords],[Btn().wordsNum,Btn().wayEdit,Btn().account],[Btn().timeLearnEdit,Btn().reportActivity],[Btn().deleteBot,Btn().aboutBot,Btn().uILangNKeyEdit],[Btn().opinion]],"resize_keyboard":True})
        regularHomePageKey = Keys().secondMenu
        self.bot.sendMessage(self.id,waysChangedMsg,"none",regularHomePageKey)

   #در صورت زدن دکمه «خیر» به فهرست آغازین و اصلی منتقل شده و این  دکمه ها و پیام می آیند 
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
        wortZahlMsg = "چه تعداد و شمار واژه نو {} عزیز 🌺🌸 در روز می خواهی؟".format(self.firstName)        
        # wortZahlKey = json.dumps({"keyboard":[[BtnS().three],[BtnS().two],[BtnS().one],[Btn().getBack]],"resize_keyboard":True})
        wortZahlKey = Keys().numWords
        self.bot.sendMessage(self.id,wortZahlMsg,"none",wortZahlKey)
    #در صورت زدن دکمه «۳» یا «۵» یا «۷»این  دکمه ها و پیام می آیند 
    def send357AllVMessageFAVA(self):
        changedWordNum = "شمار و تعداد واژه های نو به {} تغییر و دگرش یافت.".format(self.msg)
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
        timeLearningMsg = "ساعت آغاز یادگیری روزانه ات را {} عزیز 🌺🌸 جهت مراجعه و سرزدن ربات انتخاب کن.".format(self.firstName)
        # hoursKey = json.dumps({"keyboard":[[BtnS().clock1,BtnS().clock2,BtnS().clock3,BtnS().clock4,BtnS().clock5,BtnS().clock6,BtnS().clock7,BtnS().clock8],[BtnS().clock9,BtnS().clock10,BtnS().clock11,BtnS().clock12,BtnS().clock13,BtnS().clock14,BtnS().clock15,BtnS().clock16],[BtnS().clock17,BtnS().clock18,BtnS().clock19,BtnS().clock20,BtnS().clock21,BtnS().clock22,BtnS().clock23],[Btn().getBack]],"resize_keyboard":True}) 
        hoursKey = Keys().hKeys
        self.bot.sendMessage(self.id,timeLearningMsg,"none",hoursKey)
    #در صورت زدن دکمه «۱..۲۳» این  دکمه ها و پیام می آیند 
    def send1_23MessageYesNo(self,year,monthAlpha,day,weekDay,hourMin,askedYear,askedMonthAlpha,askedDay,askedWeekDay,askedHourMin):
        dash = "___________________________________"
        timeLearningWarningMsg = f"آیا مطمئن و اُستیگان هستی  {self.firstName} عزیز 🌺🌸 از دگرسانی 👈یادگیری واژگان روزانه👉 به ساعت و زمان {self.msg} در تاریخ {askedWeekDay}  {askedDay} {askedMonthAlpha} {askedYear} \n{dash}\nدر حال حاضر 👈یادگیری واژگان روزانه👉 بعدی و پسین در تاریخ {weekDay}  {day} {monthAlpha} {year} ,<b> در ساعت و زمان {hourMin}</b> می باشد.\n @DeutschOhal "
        

        # yesNoKey = json.dumps({"keyboard":[[Btn().noDash,Btn().yesDash]],"resize_keyboard":True}) 
        yesNoKey = Keys().yNDash
        self.bot.sendMessage(self.id,timeLearningWarningMsg,"none",yesNoKey)


    #در صورت همسان بودن زمان یادگیری روزانه با قبلی  این  دکمه ها و پیام می آیند 
    def sendYesMessageSameFAVA(self,year,monthAlpha,day,weekDay,hourMin):
        dash = "___________________________________"
        # "روش شما در همین هنگام هم  {} هست نیازی تغییر و دگرسانی نیست".format(self.msg)

        timeLearningChangedMsg = f"زمان یادگیری روزانه شما در همین هنگام هم  {self.msg} هست نیازی به دگرسانی و تغییر نیست\n{dash}\n👈یادگیری واژگان روزانه👉 بعدی و پسین در تاریخ {weekDay}  {day} {monthAlpha} {year} ,<b> در ساعت و زمان {hourMin}</b> \n @DeutschOhal"
        # regularHomePageKey = json.dumps({"keyboard":[[Btn().reviewWords],[Btn().wordsNum,Btn().wayEdit,Btn().account],[Btn().timeLearnEdit,Btn().reportActivity],[Btn().deleteBot,Btn().aboutBot,Btn().uILangNKeyEdit],[Btn().opinion]],"resize_keyboard":True})
        regularHomePageKey = Keys().secondMenu
        self.bot.sendMessage(self.id,timeLearningChangedMsg,"none",regularHomePageKey)


    #در صورت زدن دکمه «بله» این  دکمه ها و پیام می آیند 
    def sendYesMessageFAVA(self,year,monthAlpha,day,weekDay,hourMin):
        dash = "___________________________________"
        timeLearningChangedMsg = f"ساعت یادگیری روزانه به<b> {hourMin}</b> ویرایش شد.\n{dash}\n👈یادگیری واژگان روزانه👉 بعدی و پسین در تاریخ {weekDay}  {day} {monthAlpha} {year} ,<b> در ساعت و زمان {hourMin}</b>\n@DeutschOhal"
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
        reportPageMsg = "انتخاب {}".format(self.msg)
        # reportKey = json.dumps({"keyboard":[[Btn().reportWeakWords,Btn().reportWordsPartions],[Btn().getBack]],"resize_keyboard":True})
        reportKey = Keys().reportKeys
        self.bot.sendMessage(self.id,reportPageMsg,"none",reportKey)

    #در صورت زدن دکمه «گزارش واژگان در بخش ها📈»  این  دکمه ها و پیام می آیند 
    def sendReportAllWordsMessageBBFA(self,num,reportWordsSectionsPercentage):
        num = f"<b>{num}</b>"
        dash = "___________________________________" 
        reportWordsSectionsMsg = f"گزارش تمامی واژگان کار شده ات در بخش ها، {self.firstName} عزیز 🌺🌸 تا امروز : \n {dash}\n\nشمار تمامی واژگان کار شده تا امروز : {num} \n{dash}\n\nشمار و درصد تمامی واژه ها در تمامی بخش های جعبه لایتنر : \n\n {reportWordsSectionsPercentage}\n\n@DeutschOhal "
        # backToHomePage = json.dumps({"keyboard":[[Btn().getBack]],"resize_keyboard":True})
        backToHomePage = Keys().getBackKeys
        self.bot.sendMessage(self.id,reportWordsSectionsMsg,"none",backToHomePage)
    #در صورت زدن دکمه «گزارش ناتوانی در واژگان📉»  این  دکمه ها و پیام می آیند 
    # wWDS,wWPGS
    def sendReportWeakWordMessageBBFA(self,wWDS,wWPGS):
        dash = "___________________________________"
        reportWordsSectionsMsg = f"گزارش ناتوان ترین واژگان در یادگیری، {self.firstName} عزیز 🌺🌸 تا امروز \n (ناتوان ترین واژگان به معنی و چَم واژگانی  می باشد که بیش از یک ماه است که هنوز، یادگیری کامل نشده اند) \n {dash}\n فهرست به ترتیب واژگانی که بیش از یک ماه یادگیریشان به درازا کشیده با بیان شمارِ روز و بخش\n\n<b>{wWDS.center(63)}</b>\n{dash}\nفهرست واژگان ناتوان به ترتیب درصد در بخش های جعبه لایتنر\n\n{wWPGS}\n@DeutschOhal"
        # backToHomePage = json.dumps({"keyboard":[[Btn().getBack]],"resize_keyboard":True})
        backToHomePage = Keys().getBackKeys
        self.bot.sendMessage(self.id,reportWordsSectionsMsg,"none",backToHomePage)

    #در صورت زدن دکمه «بازگشت به فهرست آغازین🏡»  این  دکمه ها و پیام می آیند 
     #FIXME حذف این تابع از کیبورد و جایگزینی در آنالیز AYVK.sendKeyAndMessageFAVA()
    def sendBBFAMessageFAVA(self):
        self.obj_AYVK.sendKeyAndMessageFAVA()

    def reportWeakWords(self,wWDS,wWPGS): 
        dash = "___________________________________"   
        reportMsg = f"\n گزارش ناتوان ترین واژگان در یادگیری ,{self.firstName} عزیز 🌺🌸 تاامروز \n{dash.center(73)} \n\n فهرست به ترتیب واژگانی که بیش از یک ماه یادگیرشان به درازا کشیده با بیان شمار روز\n \n {wWDS}\n{dash.center(73)}\n\n فهرست واژگان ناتوان به ترتیب درصد بخش های جعبه لایتنر\n\n {wWPGS}\n @DeutschOhal"
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
         languageMsg = "زبان دلخواهت انتخاب کن {} عزیز 🌺🌸 برای پیام ها و فهرست ربات".format(self.firstName)
         
        #  languagesKey = json.dumps({"keyboard":[[BtnS().keyNMsgDe],[BtnS().keyNMsgEn],[BtnS().keyNMsgPer],[Btn().getBack]],"resize_keyboard":True}) 
         languagesKey = Keys().lanKeys
         self.bot.sendMessage(self.id,languageMsg,"none",languagesKey)
    
        #در صورت انتخاب و زدن <پوسته فارسی> به فهرست آغازین و اصلی منتقل شده و این  دکمه ها و پیام می آیند 
    def sendBaleKeyAndMessageFAVA(self): 
        languageSelectedMsg = f"برای ربات {self.msg} انتخاب شد."
        # regularHomePageKey = json.dumps({"keyboard":[[Btn().reviewWords],[Btn().wordsNum,Btn().wayEdit,Btn().account],[Btn().timeLearnEdit,Btn().reportActivity],[Btn().deleteBot,Btn().aboutBot,Btn().uILangNKeyEdit],[Btn().opinion]],"resize_keyboard":True})
        regularHomePageKey = Keys().secondMenu
        self.bot.sendMessage(self.id,languageSelectedMsg,"none",regularHomePageKey)
        




        # self.obj_Start.sendKeyAndMessagesUI()
    #    یا کیبورد و پیام پارسی⌨💬 این دکمه ها و پیام از فهرست آغازین و اصلی  می آیند  deutsch Menu, english Menu  در صورت زدن یکی از دکمه های  
    def sendKeyAndMessageFNVA2(self):
        languageSelectedMsg = f"برای ربات {self.msg}انتخاب شد."
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
        aboutMsg =f"با درود و سلام به شما <i>{self.firstName}</i> عزیز 🌺🌸\nاین ربات امکان یادگیری تمامی واژه های جدید و مورد تاکید کتاب <b>'Großes Übungsbuch Wortschatz'</b>  را در چهارچوب تکرار و تمرین به روش لایتنر به صورت روزمره و در ساختار تقویم با امکان یادآوری به شما و انتخاب پاسخ به آلمانی، به مترادف، به انگلیسی و به فارسی را با استفاده از منابع معتبر زبان آلمانی میسر می کند، به گونه ای که تسلط کامل در حداقل یک ماه نسبت به یک واژه حاصل می شود و واژه از حافظه کوتاه مدت شما درحافظه بلند مدتتان قرار می گیرد." 
        # regularHomePageKey = json.dumps({"keyboard":[[Btn().reviewWords],[Btn().wordsNum,Btn().wayEdit,Btn().account],[Btn().timeLearnEdit,Btn().reportActivity],[Btn().deleteBot,Btn().aboutBot,Btn().uILangNKeyEdit],[Btn().opinion]],"resize_keyboard":True})
        regularHomePageKey = Keys().secondMenu
        self.bot.sendMessage(self.id,aboutMsg,"none",regularHomePageKey)

#FIXME copy these 4 method to every user language
    def sendKeyAndMessageSendingSugession(self):
        aboutMsg =f" هرگونه نظر، انتقاد و یا پیشنهادی داری، <i>{self.firstName}</i> عزیز 🌺🌸برای ما بفرست."
        # backToHomePage = json.dumps({"keyboard":[[Btn().getBack]],"resize_keyboard":True})
        backToHomePage = Keys().getBackKeys
        self.bot.sendMessage(self.id,aboutMsg,"none",backToHomePage)

    def sendKeyAndMessageDeliverOpinion(self,opId):
        aboutMsg =f"نظرت، <i>{self.firstName}</i> عزیز 🌺🌸 با شماره پی گیری <b>{opId}</b> ثبت شد."
        # regularHomePageKey = json.dumps({"keyboard":[[Btn().reviewWords],[Btn().wordsNum,Btn().wayEdit,Btn().account],[Btn().timeLearnEdit,Btn().reportActivity],[Btn().deleteBot,Btn().aboutBot,Btn().uILangNKeyEdit],[Btn().opinion]],"resize_keyboard":True})
        regularHomePageKey = Keys().secondMenu
        self.bot.sendMessage(self.id,aboutMsg,"none",regularHomePageKey)

    def sendKeyAndMessageUsingBotKeys(self):
        aboutMsg =f"متنی وارد نشد! در صورت تمایل به فرستادن نظر، <b>بدون استفاده از کیبورد ربات </b>، متن  را وارد کرده و سپس بفرستید."
        # regularHomePageKey = json.dumps({"keyboard":[[Btn().reviewWords],[Btn().wordsNum,Btn().wayEdit,Btn().account],[Btn().timeLearnEdit,Btn().reportActivity],[Btn().deleteBot,Btn().aboutBot,Btn().uILangNKeyEdit],[Btn().opinion]],"resize_keyboard":True})
        regularHomePageKey = Keys().secondMenu
        self.bot.sendMessage(self.id,aboutMsg,"none",regularHomePageKey)

    def sendKeyAndMessageOutOfRangeMsg(self):
        aboutMsg =f"شمار کاراکترها و واژه های متن فرستاده شده بیش از حد است! متنتان را کوتاه تر یا در چند بخش بفرستید."
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
        deleteBotWarnMsg = "آیا مطمئن و اُستیگان هستی {} عزیز 🌺🌸 ازحذف و زدایش ربات؟ زیرا موجب از بین رفتن سابقه شما می شود و دیگر پیامی برایتان ارسال نمی شود.".format(self.firstName)
        # yesNoKey = json.dumps({"keyboard":[[Btn().no,Btn().yesDelete]],"resize_keyboard":True})
        yesNoKey = Keys().yNKeys 
        self.bot.sendMessage(self.id,deleteBotWarnMsg,"none",yesNoKey)
    #در صورت زدن دکمه «بله» به بخش فهرست نخستین🛎 و اولیه منتقل شده و   این دکمه ها و پیام می آیند    
    def sendYesKeyAndMessageFNVA(self):
        deleteBotMsg = "ربات حذف و زدایش شد."
        # firstHomePageKey = json.dumps({"keyboard":[[Btn().startLearning],[Btn().aboutBotNew,Btn().uILangNKeyEditNew]],"resize_keyboard":True}) 
        firstHomePageKey = Keys().firstMenu
        self.bot.sendMessage(self.id,deleteBotMsg,"none",firstHomePageKey)

    #در صورت زدن دکمه «خیر» به بخش فهرست آغازین و اصلی منتقل شده و   این دکمه ها و پیام می آیند    
    #FIXME حذف این تابع از کیبورد و جایگزینی در آنالیز AYVK.sendKeyAndMessageFAVA()
    def sendNoKeyAndMessageFAVA(self):
        self.obj_AYVK.sendKeyAndMessageFAVA()


#تمامی کیبوردها و پیام های بخش «دگرسانی زبان» در فهرست آعازین واصلی


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
        enterPanelMsg = "میز گردانش ⚙️ سرپرست وادمین"
        # adminDesktop = json.dumps({"keyboard":[[BtnA().changeUserType,BtnA().sendToAll,BtnA().reportToday,BtnA().reportAll],[BtnA().apply],[Btn().getBack]],"resize_keyboard":True})  
        adminDesktop = AKeys().adminKeys
        self.bot.sendMessage(self.id,enterPanelMsg,"none",adminDesktop)

    def adminSendGMessageGPanellAppleyChanges(self,outputAll):
        enterPanelMsg = f"{outputAll}\nورزانش و اعمال ، کارها و عملیات انجام شد."
        # adminDesktop = json.dumps({"keyboard":[[BtnA().changeUserType,BtnA().sendToAll,BtnA().reportToday,BtnA().reportAll],[BtnA().apply],[Btn().getBack]],"resize_keyboard":True})
        adminDesktop = AKeys().adminKeys  
        self.bot.sendMessage(self.id,enterPanelMsg,"none",adminDesktop)


     #در صورت زدن دکمه «گزارش تکاپو فراگیر»  این دکمه ها و پیام می آیند  
    def adminSendGTFaraMessageGPanel(self,guestsNum,usersNum,guestInfos,userInfos,monthAlpha,year,day,weekDay):
        dash = "___________________________________" 
        fileW = open("TFaraMessageGPanel.txt", "w",encoding='utf-8') 
        data = f"   \n\n  <b>  داده های کاربران :\n</b>  {userInfos}\n {dash}\n<b>  داده های مهمانان :\n</b> {guestInfos} \n {dash}"
        # data = f"\n      {userInfos}\n {dash}\n   {guestInfos} \n {dash}"
        # data = f"{userInfos} \n{dash}\n {guestInfos}"
        fileW.write(data) 
        fileW.close() 
        file = open("TFaraMessageGPanel.txt", "rb")
        openedfile ={'document': file}
        dateGri = datetime.datetime.today().date().strftime("%Y-(%B %m)-%d")
        all = guestsNum + usersNum
        # reportAllActionMsg = f"   \n\n  <b>  داده های کاربران :\n</b>  {userInfos}\n {dash}\n<b>  داده های مهمانان :\n</b> {guestInfos} \n {dash} \nشمار کاربران : <b>{usersNum}</b>\nشمار مهمانان : <b>{guestsNum}</b>\n شمار افراد کنشگر فراگیر : <b>{all}</b> \n {dash} \n امروز: <b>{weekDay}  {day} {monthAlpha} {year} \n {dateGri}</b>     "
        reportAllActionMsg = f"   \n\n  شمار کاربران : {usersNum}\nشمار مهمانان : {guestsNum}\n شمار افراد کنشگر فراگیر : {all} \n {dash} \n امروز: {weekDay}  {day} {monthAlpha} {year} \n {dateGri}     "
        self.bot.sendDocument(self.id,openedfile,reportAllActionMsg,disable_notification=True)
        file.close()
        if os.path.exists("TFaraMessageGPanel.txt"):
            os.remove("TFaraMessageGPanel.txt")
        else:
            print("The file does not exist") 
        

    def adminOpinionsTypes(self):
        enterPanelMsg = "تمامی گونه های گزارش نظرات"
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
        reportAllActionMsg = f"  \nشمار نظرات : {opinionsNum}\nشمار کاربران فرستنده نظر : {suguestersNum} \n {dash} \nToday: {weekDay} {day} {monthAlpha} {year} \n {dateGri}"
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
        reportAllActionMsg = f"   \n\n     نام ها و شناسه های کاربری امروز :\n {activeUsersInfos} \n {dash} \n نام ها و شناسه های میهمان امروز :\n {activeGuestsInfo}\n {dash} \n شمار کاربران کنشگر امروز : <b>{todayActiveUsersNum}</b> \n  شمار میهمانان کنشگر امروز : <b>{todayActiveGuestsNum}</b> \n شمار همه گی کنشگران امروز : <b>{all}</b> \n  {dash} \n  شمار تراکنش های امروز : <b>{numTodayAllTransactions}</b> \n {dash} \n امروز:<b> {weekDay}  {day} {monthAlpha} {year}  \n {dateGri}</b>"
        # adminDesktop = json.dumps({"keyboard":[[BtnA().changeUserType,BtnA().sendToAll,BtnA().reportToday,BtnA().reportAll],[BtnA().apply],[Btn().getBack]],"resize_keyboard":True}) 
        adminDesktop = AKeys().adminKeys 
        # BtnA().changeUserType,BtnA().sendToAll,BtnA().reportToday,BtnA().reportAll,BtnA().apply
        self.bot.sendMessage(self.id,reportAllActionMsg,"none",adminDesktop)

     #در صورت زدن دکمه «پیام به همه»  این دکمه ها و پیام می آیند   
    def adminSendPBHMessageBBMSVA(self):
        adminMessageToAllEnterMsg = "پیام مورد نظر خود را برای گسیل به تمامی کاربران وارد کنید"
        # adminSendingKey = json.dumps({"keyboard":[[BtnA().getBackToDesk]],"resize_keyboard":True})
        adminSendingKey = AKeys().getBackDesk
        self.bot.sendMessage(self.id,adminMessageToAllEnterMsg,"none",adminSendingKey)
     #در صورت فرستادن پیام از روش کیبورد مبایل(نه ربات)   این دکمه ها و پیام می آیند   
    def adminSendGosilMessageYesNo(self,msg):
        adminMessageToAllWarningMsg = f"{msg}\n\nآیا مطمئن و اُستیگان از فرستادن این 👆 متن برای همه کاربران هستید؟" 
        # yesNoKey = json.dumps({"keyboard":[[BtnA().noDoubleComma,BtnA().yesSendIt]],"resize_keyboard":True}) 
        yesNoKey = AKeys().yNDoubleKomma
        self.bot.sendMessage(self.id,adminMessageToAllWarningMsg,"none",yesNoKey)

    # بیشتر شدن کاراکترها بیشتر از 4050
    def adminSendGMessageGPanellCharMore(self,msg):
        length = len(msg)
        msgMore4050 = f"شمار کاراکتر های پیام  {length} تا است که بیش از 4050 تا بوده و قابل فرستادن نیست !!!"
        # adminDesktop = json.dumps({"keyboard":[[BtnA().changeUserType,BtnA().sendToAll,BtnA().reportToday,BtnA().reportAll],[BtnA().apply],[Btn().getBack]],"resize_keyboard":True}) 
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
        backToAdminDesk = "میز گردانش ⚙️ سرپرست و ادمین"
        # adminDesktop = json.dumps({"keyboard":[[BtnA().changeUserType,BtnA().sendToAll,BtnA().reportToday,BtnA().reportAll],[BtnA().apply],[Btn().getBack]],"resize_keyboard":True}) 
        adminDesktop = AKeys().adminKeys 
        self.bot.sendMessage(self.id,backToAdminDesk,"none",adminDesktop)
    
     #در صورت زدن دکمه «بله،گسیل شود!»  این دکمه ها و پیام می آیند   
    def adminSendYeslMessageGPanel(self):
        adminMessageToAllSentMsg = "پیام شما به همه کاربران فرستاده شد"
        # adminDesktop = json.dumps({"keyboard":[[BtnA().changeUserType,BtnA().sendToAll,BtnA().reportToday,BtnA().reportAll],[BtnA().apply],[Btn().getBack]],"resize_keyboard":True}) 
        adminDesktop = AKeys().adminKeys 
        self.bot.sendMessage(self.id,adminMessageToAllSentMsg,"none",adminDesktop)
   
     #در صورت زدن دکمه «خیر»  این دکمه ها و پیام می آیند   
    def adminSendNolMessageGPanel(self):
        backToAdminDesk = "میز گردانش ⚙️ سرپرست و ادمین"
        # adminDesktop = json.dumps({"keyboard":[[BtnA().changeUserType,BtnA().sendToAll,BtnA().reportToday,BtnA().reportAll],[BtnA().apply],[Btn().getBack]],"resize_keyboard":True}) 
        adminDesktop = AKeys().adminKeys 
        self.bot.sendMessage(self.id,backToAdminDesk,"none",adminDesktop)
   
     #در صورت زدن دکمه «دگرسانی گونه کاربر»  این دکمه ها و پیام می آیند   
    def adminSendDGKlMessageGBBMSVA(self):
        dGKGUIdeMsg = "شناسه کاربری 12... یا نام کاربری @... کاربر دلخواهتان را  وارد کنید »"
        # adminSendingKey = json.dumps({"keyboard":[[BtnA().send],[BtnA().getBackToDesk]],"resize_keyboard":True})
        adminSendingKey = AKeys().sendChangeUser
        self.bot.sendMessage(self.id,dGKGUIdeMsg,"none",adminSendingKey)
   
     #در صورت زدن دکمه «گسیل» و فرستادن شناسه کاربری یا نام کاربری اشتباه این دکمه ها و پیام می آیند   
    def adminSendWrongGMessageGBBMSVA(self):
        dGKGUIdeMsg = "شناسه کاربری یا نام کاربری کاربر را درست وارد کنید"
        # adminSendingKey = json.dumps({"keyboard":[[BtnA().send],[BtnA().getBackToDesk]],"resize_keyboard":True})
        adminSendingKey = AKeys().sendChangeUser
        self.bot.sendMessage(self.id,dGKGUIdeMsg,"none",adminSendingKey)
   
     #در صورت زدن دکمه «گسیل» و وارد کردن نام درست کاربری یا شناسه کاربری   این دکمه ها و پیام می آیند   
    def adminSendًRightGMessageGPanel(self):
        successfulChangedMsg = "کاربر {} از کاربر ساده به کاربر ویژه دگرگون شد.".format(self.msg)
        # adminSendingKey = json.dumps({"keyboard":[[BtnA().send],[BtnA().getBackToDesk]],"resize_keyboard":True})
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
         languageMsg = "زبان دلخواهت انتخاب کن {} عزیز 🌺🌸 برای پیام ها و فهرست ربات".format(self.firstName)
        #  languagesKey = json.dumps({"keyboard":[[BtnS().keyNMsgDe],[BtnS().keyNMsgEn],[BtnS().keyNMsgPer]],"resize_keyboard":True}) 
         languagesKey = SKeys(Btn(),MNV()).uI
         self.bot.sendMessage(self.id,languageMsg,"none",languagesKey)

   #    یا کیبورد و پیام پارسی⌨💬 این دکمه ها و پیام از فهرست نخستین🛎 و اولیه  می آیند  deutsch Menu, english Menu  در صورت زدن یکی از دکمه های  
    def sendKeyAndMessageFNVAUIselected(self):
        languageSelectedMsg = f"برای ربات {self.msg}انتخاب شد."
        # firstHomePageKey = json.dumps({"keyboard":[[BtnA().admin,Btn().startLearning],[Btn().aboutBotNew,Btn().uILangNKeyEditNew]],"resize_keyboard":True}) 
        firstHomePageKey = AKeys().firstMenu
        self.bot.sendMessage(self.id,languageSelectedMsg,"none",firstHomePageKey)
    

    def sendKeyAndMessageFNVAUINakhostin(self):
         languageSelectedMsg = "فهرست نخستین🛎"
        #  firstHomePageKey = json.dumps({"keyboard":[[BtnA().admin,Btn().startLearning],[Btn().aboutBotNew,Btn().uILangNKeyEditNew]],"resize_keyboard":True}) 
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
        msgNextTrainingTimeDate = f"حساب کاربریت <i>{self.firstName}</i> عزیز 🌺🌸 \n{ent}\n{output}\n{dash}\n{outpuTodayDateNTime}\n@DeutschOhal"
        # regularHomePageKey = json.dumps({"keyboard":[[BtnA().admin,Btn().reviewWords],[Btn().wordsNum,Btn().wayEdit,Btn().account],[Btn().timeLearnEdit,Btn().reportActivity],[Btn().deleteBot,Btn().aboutBot,Btn().uILangNKeyEdit],[Btn().opinion]],"resize_keyboard":True})
        regularHomePageKey = AKeys().secondMenu
        self.bot.sendMessage(self.id,msgNextTrainingTimeDate,"none",regularHomePageKey)
        
    
    #در صورت زدن دکمه ((آعاز یادگیری واژه های کتاب)) این دکمه ها و پیام می آیند
    def sendAYVKKeyAndMessage327(self):
        wortZahlMsg = "چه تعداد و شمار واژه نو {} عزیز 🌺🌸 در روز می خواهی؟".format(self.firstName)        
        # wortZahlKey = json.dumps({"keyboard":[[BtnS().threeNew],[BtnS().twoNew],[BtnS().oneNew],[BtnS().fiveNew,BtnS().tenNew,BtnS().fifteenNew,BtnS().twentyNew]],"resize_keyboard":True})
        wortZahlKey = AKeys().wordsNumNew
        self.bot.sendMessage(self.id,wortZahlMsg,"none",wortZahlKey)
    #در صورت زدن یکی از دکمه های ۳ یا ۵  یا ۷ این دکمه ها و پیام می آیند
    def send357KeyAndMessageDESP(self):
        waysMsg = "روش یادگیری واژه های کتاب را {} عزیز 🌺🌸 انتخاب کن.".format(self.firstName)
        # wayKey = json.dumps({"keyboard":[[BtnS().deutschNew,BtnS().englishNew,BtnS().synonymNew],[BtnS().allTogetherNew,BtnS().persianNew]],"resize_keyboard":True}) 
        wayKey = AKeys().waysNew
        self.bot.sendMessage(self.id,waysMsg,"none",wayKey)

  
   #    یا پارسی این دکمه و پیام می آیند  deutsch , english , synonym  در صورت زدن یکی از دکمه های  
    def sendDESPKeyAndMessageLampGuid(self,way,wKind,numW,numAll,standardizedWord,content,chapter,wordsPage,linkWord):
        dash = "___________________________________"
        guide = f" راهنمایی🔔: واژه را مطالعه کنید و {way} آن را بگویید و به خاطر بسپارید پس از آن جهت دیدن پاسخ درست و مقایسه  با پاسخ خود روی 💡 تلنگر بزنید. "
        #  <p align="right">This is some text in a paragraph.</p> 
        # newWordsMsg = f".{numW}/{numAll}                                         {wKind}.\n<b>{standardizedWord.center(63)}</b>\n.سرفصل : {content}\nفصل : {chapter} \nبرگ:{wordsPage}.\n{dash}\n{guide}"

        newWordsMsg = f".{numW}/{numAll}                                         {wKind}.\n<b>{standardizedWord}</b>\n.سرفصل : {content}\nفصل : {chapter} \nبرگ:{wordsPage}.\n{dash} \n{linkWord}{guide} "


        # {content}\n{cotentNChap} \nبرگ:{wordsPage}
        # antwortKey = json.dumps({"keyboard":[[BtnS().lamp]],"resize_keyboard":True}) 
        antwortKey = SKeys(Btn(),MNV()).lampKeys
        self.bot.sendMessage(self.id,newWordsMsg,"none",antwortKey)


                               
   #    یا پارسی این دکمه و پیام می آیند  deutsch , english , synonym  در صورت زدن یکی از دکمه های  
    def sendDESPKeyAndMessageLamp(self,wKind,numW,numAll,standardizedWord,content,chapter,wordsPage,linkWord):
        newWordsMsg = f".{numW}/{numAll}                                         {wKind}.\n<b>{standardizedWord}</b>\n.سرفصل : {content}\nفصل : {chapter} \nبرگ:{wordsPage}.\n {linkWord}."
        # {content}\n{cotentNChap} \nبرگ:{wordsPage}
        # antwortKey = json.dumps({"keyboard":[[BtnS().lamp]],"resize_keyboard":True}) 
        antwortKey = SKeys(Btn(),MNV()).lampKeys
        self.bot.sendMessage(self.id,newWordsMsg,"none",antwortKey)



   #در صورت زدن دکمه 💡 این دکمه و پیام می آید 
    def sendLampKeyAndMessageVXGuide(self,way,icon,standardizedAnswer,answerLink):
               #63 blank space
        dash = "___________________________________"
        guide = f"راهنمایی🔔: با بررسی پاسخ فرستاده شده و پاسخ خود ،درستی یا نادرستی پاسخ خود را با انتخاب ✅ یا ❌ برگزینید."

        pa = f"{icon}{way} پاسخ به "
        lenngthPa = len(pa)
        pa = pa.center(72 - lenngthPa)
        # print(f"len(pa) = {len(pa)}")       
        newWordsMsg = f"<b>{pa}</b>\n{standardizedAnswer}\n{dash}\n \n{answerLink}{guide}"
        # rwKey = json.dumps({"keyboard":[[BtnS().crossCheck,BtnS().check]],"resize_keyboard":True}) 
        rwKey = SKeys(Btn(),MNV()).rW
        self.bot.sendMessage(self.id,newWordsMsg,"none",rwKey)


   #در صورت زدن دکمه 💡 این دکمه و پیام می آید 
    def sendLampKeyAndMessageVX(self,way,icon,standardizedAnswer,answerLink):
               #63 blank space
        pa = f"{icon}{way} پاسخ به "
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
        # print(f"nRWords = {nRWords},nWorkedWords = {nWorkedWords}")
        percentageRight = self.obj_dbContatct.Percentage().percentage(nRWords,nWorkedWords)
        percentageWrong = self.obj_dbContatct.Percentage().percentage(nWWrong,nWorkedWords)
        graphRight = self.obj_dbContatct.Graph().graph(nRWords,nWorkedWords)
        graphWrong = self.obj_dbContatct.Graph().graph(nWWrong,nWorkedWords)
        guide = f"🔔 برای مرور واژهای کار شده می توانید پس از انتخاب ({Btn().getBack}) ،({Btn().reviewWords}) را انتخاب کنید. "
        daliyReport = f"<i>گزارش کارکردت، {self.firstName} عزیز 🌺🌸 در امروز:</i>\n{dash.center(14)}\nشمار وا‌ژه های کار شده : <b>{nWorkedWords}</b>\nشمار واژه های درست : <b>{nRWords}</b>\nشمار واژه های نادرست : <b>{nWWrong}</b>\n{dash.center(14)}\n<i>درصد درستی و نادرستی واژه ها :</i>\nدرستی <b>{graphRight} % {percentageRight} </b>\nنادرستی <b>{graphWrong} % {percentageWrong}</b> \n{dash.center(14)}\nفهرست واژه های نادرست امروز به همراه نشانی برگ در کتاب :\n <b>{wrongWordsNpages}</b>\n{dash.center(14)}\n👈یادگیری واژگان روزانه👉 بعدی و پسین در تاریخ <b> {weekDay} {day} {month} {year} </b>, در ساعت و زمان <b>{houNMTraining}</b> به وقت ایران، مصادف با <b>{dateGriNextTraining}</b>\n{dash}\n<i>بخش و شمار تمامی واژه ها در جعبه لایتنر :</i>\nشمار واژه ها در بخش نخست :<b>{wordsSectionPosition[0]} </b>\nشمار واژه ها در بخش دوم :<b> {wordsSectionPosition[1]} </b>\nشمار واژه ها در بخش سوم : <b>{wordsSectionPosition[2]} </b>\nشمار واژه ها در بخش چهارم :<b> {wordsSectionPosition[3]}</b> \nشمار واژه ها در بخش پنجم :‌<b>{wordsSectionPosition[4]}</b> \nشمار واژه ها در بخش ششم :<b>‌{wordsSectionPosition[5]}</b>\n{dash}\nواژه های یادگیری شده به صورت کامل :<b>‌{wordsSectionPosition[6]}</b>\n{dash} \n<i>{guide}</i>\n@DeutschOhal\n"
        # print(f"daily report = {daliyReport}")
        # backToHomePage = json.dumps({"keyboard":[[Btn().getBack]],"resize_keyboard":True})
        backToHomePage = Keys().getBackKeys
        self.bot.sendMessage(self.id,daliyReport,"none",backToHomePage)
       
    # فرستادن تاریخ و زمان یادگیری واژگان بعدی پسین
    def sendNextTrainingDateTimeKeyAndMessageBBFA(self,weekDay,day,monthAlpha,year,hourMin):
        # y = "یادگیری واژگان روزانه"
        
        msgNextTrainingTimeDate = f"👈یادگیری واژگان روزانه👉 بعدی و پسین‌ات {self.firstName} عزیز 🌺🌸 در تاریخ  <b> {weekDay} {day} {monthAlpha} {year} </b>, در ساعت و زمان  <b>{hourMin} </b> می باشد.\n@DeutschOhal"
        # msgNextTrainingTimeDate = "g"
        # regularHomePageKey = json.dumps({"keyboard":[[BtnA().admin,Btn().reviewWords],[Btn().wordsNum,Btn().wayEdit,Btn().account],[Btn().timeLearnEdit,Btn().reportActivity],[Btn().deleteBot,Btn().aboutBot,Btn().uILangNKeyEdit],[Btn().opinion]],"resize_keyboard":True})
        regularHomePageKey = AKeys().secondMenu
        self.bot.sendMessage(self.id,msgNextTrainingTimeDate,"none",regularHomePageKey)






     #در صورت زدن  دکمه بازگشت به فهرست آغازین🏡 به بخش فهرست آغازین و اصلی منتقل شده و این دکمه ها و پیام می آیند 
#FIXME حذف این تابع از کیبورد و جایگزینی در آنالیز AYVK.sendKeyAndMessageFAVA()
    def sendKeyAndMessageFAVA(self):
        fehrestAghazinMsg = "فهرست آغازین"
        # regularHomePageKey = json.dumps({"keyboard":[[BtnA().admin,Btn().reviewWords],[Btn().wordsNum,Btn().wayEdit,Btn().account],[Btn().timeLearnEdit,Btn().reportActivity],[Btn().deleteBot,Btn().aboutBot,Btn().uILangNKeyEdit],[Btn().opinion]],"resize_keyboard":True})
        regularHomePageKey = AKeys().secondMenu
        self.bot.sendMessage(self.id,fehrestAghazinMsg,"none",regularHomePageKey)

    def sendKeyAndMessageUserMustWait(self):
        fehrestAghazinMsg = "تا تاریخ بعدی "
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
        msgWarning = "⛔️😡😡⛔️از فرستادن Spam خودداری کنید⛔️😡😡⛔️"
        # antwortKey = json.dumps({"keyboard":[[BtnS().lamp]],"resize_keyboard":True}) 
        # antwortKey = SKeys(Btn(),MNV()).lampKeys
        antwortKey = ""
        self.bot.sendMessage(self.id,msgWarning,"none",antwortKey)
        #spam warning هنگامه آخرین واژه BtnS().crossCheck,"✅ پیام خطا به جهت فرستادن تکراری 
    def sendWarningKeyAndMessageBBFA(self):
        msgWarning = "⛔️😡😡⛔️از فرستادن Spam خودداری کنید⛔️😡😡⛔️"
        # backToHomePage = json.dumps({"keyboard":[[Btn().getBack]],"resize_keyboard":True})
        # backToHomePage = Keys().getBackKeys
        backToHomePage =""
        self.bot.sendMessage(self.id,msgWarning,"none",backToHomePage)
     
    #spam warning  پیام خطا به جهت فرستادن تکراری برای کاربری که هنوز نام نویسی نشده 
    def sendWarningRepeatedKeyAndMessageToAdminGuest(self):
        msgWarning = "⛔️😡😡⛔️از فرستادن Spam  خودداری کنید⛔️😡😡⛔️"
        # firstHomePageKey = json.dumps({"keyboard":[[BtnA().admin,Btn().startLearning],[Btn().aboutBotNew,Btn().uILangNKeyEditNew]],"resize_keyboard":True}) 
        # firstHomePageKey = AKeys().firstMenu
        firstHomePageKey =""
        self.bot.sendMessage(self.id,msgWarning,"none",firstHomePageKey)


    #spam warning  پیام خطا به جهت فرستادن تکراری برای کاربر  
    def sendWarningRepeatedKeyAndMessageToAdmin(self):
        msgWarning = "⛔️😡😡⛔️از فرستادن Spam  خودداری کنید⛔️😡😡⛔️"
        # regularHomePageKey = json.dumps({"keyboard":[[BtnA().admin,Btn().reviewWords],[Btn().wordsNum,Btn().wayEdit,Btn().account],[Btn().timeLearnEdit,Btn().reportActivity],[Btn().deleteBot,Btn().aboutBot,Btn().uILangNKeyEdit],[Btn().opinion]],"resize_keyboard":True})
        # regularHomePageKey = AKeys().secondMenu
        regularHomePageKey =""  
        self.bot.sendMessage(self.id,msgWarning,"none",regularHomePageKey) 

     
    #none keyboard warning  پیام خطا به جهت عدم استفاده از کیبورد ربات برای ادمین عضو شده  
    def sendWarningNoneKeyboardToAdmin(self):
        msgWarning = "فقط از کیبورد ربات استفاده کنید!"
        # regularHomePageKey = json.dumps({"keyboard":[[BtnA().admin,Btn().reviewWords],[Btn().wordsNum,Btn().wayEdit,Btn().account],[Btn().timeLearnEdit,Btn().reportActivity],[Btn().deleteBot,Btn().aboutBot,Btn().uILangNKeyEdit],[Btn().opinion]],"resize_keyboard":True})
        regularHomePageKey = AKeys().secondMenu
        # regularHomePageKey=""
        self.bot.sendMessage(self.id,msgWarning,"none",regularHomePageKey) 

       
    #none keyboard warning  پیام خطا به جهت عدم استفاده از کیبورد ربات برای ادمین میهمان   
    def sendWarningNoneKeyboardToAdminGuest(self):
        msgWarning = "فقط از کیبورد ربات استفاده کنید!"
        # firstHomePageKey = json.dumps({"keyboard":[[BtnA().admin,Btn().startLearning],[Btn().aboutBotNew,Btn().uILangNKeyEditNew]],"resize_keyboard":True}) 
        firstHomePageKey = AKeys().firstMenu
        # firstHomePageKey =""
        self.bot.sendMessage(self.id,msgWarning,"none",firstHomePageKey) 

class AdminAutomaticMessage:
    def __init__(self,id,firstName):
        self.id = id
        self.bot = pybotc.Bot("config.cfg")
        self.firstName = firstName
    def sendKeyAndMessageDailyLearn(self):
        msg = f"آغاز یادگیری و تمرین واژگان، <i>{self.firstName}</i> عزیز 🌺🌸 روی یادگیری واژگان روزانه تلنگر بزن ! "
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
        aboutMsg =f"با درود و سلام به شما <i>{self.firstName}</i> عزیز 🌺🌸\nاین ربات امکان یادگیری تمامی واژه های جدید و مورد تاکید کتاب <b>'Großes Übungsbuch Wortschatz'</b>  را در چهارچوب تکرار و تمرین به روش لایتنر به صورت روزمره و در ساختار تقویم با امکان یادآوری به شما و انتخاب پاسخ به آلمانی، به مترادف، به انگلیسی و به فارسی را با استفاده از منابع معتبر زبان آلمانی میسر می کند، به گونه ای که تسلط کامل در حداقل یک ماه نسبت به یک واژه حاصل می شود و واژه از حافظه کوتاه مدت شما درحافظه بلند مدتتان قرار می گیرد." 
        # firstHomePageKey = json.dumps({"keyboard":[[BtnA().admin,Btn().startLearning],[Btn().aboutBotNew,Btn().uILangNKeyEditNew]],"resize_keyboard":True})
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
        reviewMsg = "روش مرور واژگان را براساس یکی از گزینه ها، {} عزیز🌺🌸 انتخاب کن".format(self.firstName)
        # reviewKey = json.dumps({"keyboard":[[Btn().chapterNSection],[Btn().leitnerBoxParts],[Btn().weakWords],[Btn().getBack]],"resize_keyboard":True})  
        reviewKey = Keys().revKeys
        self.bot.sendMessage(self.id,reviewMsg,"none",reviewKey)
        
        #🔎
        ###در صورت زدن دکمه «سرفصل و فصل» در بخش آغازین و اصلی این  دکمه ها و پیام نخستین واژه می آیند 
    def sendWordsChapterContentKeyAndMessageFirstOLdWord(self,content,chapter,word,answer,counter,length,section,page,link):
        oldWordsMsg = f".سرفصل : {content}\nفصل : {chapter}\n\n<b>{word}</b>\n\n{answer.center(63)}\n\n.برگ:{page}                         {section}: {length}/{counter+1}{link}."
        # reviewNextKey = json.dumps({"keyboard":[[Btn().nextWordChapNS],[Btn().getBack]],"resize_keyboard":True}) 
        reviewNextKey = Keys().revChapNexKeys
        self.bot.sendMessage(self.id,oldWordsMsg,"none",reviewNextKey)
        ## وقتی طول آرایه یکی بود
    # def sendWordsChapterContentKeyAndMessageFirstOLdWordOneLength(self,content,chapter,word,answer,counter,length,section,page,link):
    #     oldWordsMsg = f".سرفصل : {content}\nفصل : {chapter}\n\n<b>{word}</b>\n\n{answer.center(63)}\n\n.برگ:{page}                         {section}: {length}/{counter+1}{link}."
    #     keys = MNV().review(ways,length,msg)
        
        # reviewNextKey = json.dumps({"keyboard":[[Btn().getBack]],"resize_keyboard":True}) 
        backToHomePage = Keys().getBackKeys
        self.bot.sendMessage(self.id,oldWordsMsg,"none",backToHomePage)


    #سرفصل و فصل- کیبورد حاوی قبلی و بعدی  
    def sendWordsChapterContentKeyAndMessagMiddleOLdWord(self,content,chapter,word,answer,counter,length,section,page,link):
        oldWordsMsg = f".سرفصل : {content}\nفصل : {chapter}\n\n<b>{word}</b>\n\n{answer.center(63)}\n\n.برگ:{page}                         {section}: {length}/{counter+1}{link}."
        # reviewMiddleKeys = json.dumps({"keyboard":[[Btn().beforeWordChapNS,Btn().nextWordChapNS],[Btn().getBack]],"resize_keyboard":True}) 
        reviewMiddleKeys = Keys().revChapMidKeys
        self.bot.sendMessage(self.id,oldWordsMsg,"none",reviewMiddleKeys)
    
    #سرفصل و فصل- کیبورد حاوی قبلی و آخرین واژه  
    def sendWordsChapterContentKeyAndMessagLastOLdWord(self,content,chapter,word,answer,counter,length,section,page,link):
        oldWordsMsg = f".سرفصل : {content}\nفصل : {chapter}\n\n<b>{word}</b>\n\n{answer.center(63)}\n\n.برگ:{page}                         {section}: {length}/{counter+1}{link}."
        # reviewNextKey = json.dumps({"keyboard":[[Btn().beforeWordChapNS],[Btn().getBack]],"resize_keyboard":True}) 
        reviewBeforeKey = Keys().revChapBefKeys
        self.bot.sendMessage(self.id,oldWordsMsg,"none",reviewBeforeKey)


    #🔭
    ###در صورت زدن دکمه «بخش ها» در بخش آغازین و اصلی این  دکمه ها و پیام نخستین واژه می آیند 
    def sendBakhshhaKeyAndMessageFirstWord(self,counter,length,section,word,answer,page,content,chapter,link):
        oldWordsMsg = f". {section}: {length}/{counter+1}\n<b>{word}</b>\n\n{answer.center(63)}\n\n.سرفصل : {content}\nفصل : {chapter}  \n {link}\nبرگ:{page}"
        # reviewNextKey = json.dumps({"keyboard":[[Btn().nextWordLeitBP],[Btn().getBack]],"resize_keyboard":True}) 
        reviewNextKey = Keys().revLeitNexKeys
        self.bot.sendMessage(self.id,oldWordsMsg,"none",reviewNextKey)

    def sendBakhshhaKeyAndMessageFirstWordOneLength(self,counter,length,section,word,answer,page,content,chapter,link):
        oldWordsMsg = f". {section}: {length}/{counter+1}\n<b>{word}</b>\n\n{answer.center(63)}\n\n.سرفصل : {content}\nفصل : {chapter} {link}\nبرگ:{page}"
        # reviewNextKey = json.dumps({"keyboard":[[Btn().getBack]],"resize_keyboard":True}) 
        backToHomePage = Keys().getBackKeys
        self.bot.sendMessage(self.id,oldWordsMsg,"none",backToHomePage)



        #بخش ها- کیبورد حاوی قبلی و بعدی 
    def sendBakhshhaKeyAndMessageMiddleWord(self,counter,length,section,word,answer,page,content,chapter,link):
        oldWordsMsg = f". {section}: {length}/{counter+1}\n<b>{word}</b>\n\n{answer.center(63)}\n\n.سرفصل : {content}\nفصل : {chapter}  \n {link}\nبرگ:{page}"
        #اگر واژه ای بعد از این هنوز موجود باشد
        # reviewBackNextKey = json.dumps({"keyboard":[[Btn().beforeWordLeitBP,Btn().nextWordLeitBP],[Btn().getBack]],"resize_keyboard":True}) 
        reviewBackNextKey = Keys().revLeitMidKeys
        self.bot.sendMessage(self.id,oldWordsMsg,"none",reviewBackNextKey)

        #بخش ها- کیبورد حاوی قبلی  
    def sendBakhshhaKeyAndMessageLastWord(self,counter,length,section,word,answer,page,content,chapter,link):
        oldWordsMsg = f". {section}: {length}/{counter+1}\n<b>{word}</b>\n\n{answer.center(63)}\n\n.سرفصل : {content}\nفصل : {chapter}  \n {link}\nبرگ:{page}"
        #اگر واژه ای بعد از این دیگر موجود نباشد
        # reviewBackKey = json.dumps({"keyboard":[[Btn().beforeWordLeitBP],[Btn().getBack]],"resize_keyboard":True}) 
        reviewBackKey = Keys().revLeitBefKeys
        self.bot.sendMessage(self.id,oldWordsMsg,"none",reviewBackKey)

    #🔬
    ###در صورت زدن دکمه «واژگان ناتوان» در بخش آغازین و اصلی این  دکمه ها و پیام نخستین واژه می آیند 
    def sendWeakWordsKeyAndMessageFirstOLdWord(self,durationDays,counter,length,section,word,answer,content,chapter,page,link):
        oldWordsMsg = f".شمار روزها : {durationDays}         {section}:{counter+1}/{length}.\n\n<b>{word}</b>\n\n{answer.center(63)}\n\n.سرفصل : {content}\nفصل : {chapter} \n {link}\n{page}:برگ"
        # برگ:{page}
        # {page}:برگ
        # reviewNextKey = json.dumps({"keyboard":[[Btn().nextWordWW],[Btn().getBack]],"resize_keyboard":True}) 
        reviewNextKey = Keys().revWeakNexKeys
        self.bot.sendMessage(self.id,oldWordsMsg,"none",reviewNextKey)

    #وقتی طول آرایه یکی باشد
    def sendWeakWordsKeyAndMessageFirstOLdWordOneLength(self,durationDays,counter,length,section,word,answer,content,chapter,page,link):
        oldWordsMsg = f".شمار روزها : {durationDays}         {section}:{counter+1}/{length}.\n\n<b>{word}</b>\n\n{answer.center(63)}\n\n.سرفصل : {content}\nفصل : {chapter} \n {link}\n{page}:برگ"
        # برگ:{page}
        # {page}:برگ
        # backToHomePage = json.dumps({"keyboard":[[Btn().getBack]],"resize_keyboard":True}) 
        backToHomePage = Keys().getBackKeys
        self.bot.sendMessage(self.id,oldWordsMsg,"none",backToHomePage)



# {self.firstName}
    def sendWeakWordsKeyAndMessageNoWord(self):
        noWeakWordMsg = f" واژه ناتوانی نداری <i> {self.firstName}</i> عزیز 🌺🌸"
        # برگ:{page}
        # {page}:برگ
        # regularHomePageKey = json.dumps({"keyboard":[[BtnA().admin,Btn().reviewWords],[Btn().wordsNum,Btn().wayEdit,Btn().account],[Btn().timeLearnEdit,Btn().reportActivity],[Btn().deleteBot,Btn().aboutBot,Btn().uILangNKeyEdit],[Btn().opinion]],"resize_keyboard":True})
        regularHomePageKey = AKeys().secondMenu
        self.bot.sendMessage(self.id,noWeakWordMsg,"none",regularHomePageKey)
  
    # {self.firstName}
    def sendWeakWordsKeyAndMessageNoWordOtherReview(self):
        noWeakWordMsg = f" واژه ای تا این لحظه و دم <i> {self.firstName}</i> عزیز 🌺🌸تمرین و  کار نکرد ه ای! "
        # برگ:{page}
        # {page}:برگ
        # regularHomePageKey = json.dumps({"keyboard":[[BtnA().admin,Btn().reviewWords],[Btn().wordsNum,Btn().wayEdit,Btn().account],[Btn().timeLearnEdit,Btn().reportActivity],[Btn().deleteBot,Btn().aboutBot,Btn().uILangNKeyEdit],[Btn().opinion]],"resize_keyboard":True})
        regularHomePageKey = AKeys().secondMenu
        self.bot.sendMessage(self.id,noWeakWordMsg,"none",regularHomePageKey)


    #واژگان ناتوان- کیبورد حاوی قبلی و بعدی  
    def sendWeakWordsKeyAndMessagMiddleOLdWord(self,durationDays,counter,length,section,word,answer,content,chapter,page,link):
        oldWordsMsg = f".شمار روزها : {durationDays}         {section}:{counter+1}/{length}.\n\n<b>{word}</b>\n\n{answer.center(63)}\n\n.سرفصل : {content}\nفصل : {chapter} \n {link}\n{page}:برگ"
        # reviewNextKey = json.dumps({"keyboard":[[Btn().beforeWordWW,Btn().nextWordWW],[Btn().getBack]],"resize_keyboard":True}) 
        reviewNextKey = Keys().revWeakMidKeys
        self.bot.sendMessage(self.id,oldWordsMsg,"none",reviewNextKey)
    #واژگان ناتوان- کیبورد حاوی قبلی و آخرین واژه  
    def sendWeakWordsKeyAndMessagLastOLdWord(self,durationDays,counter,length,section,word,answer,content,chapter,page,link):
        oldWordsMsg = f".شمار روزها : {durationDays}         {section}:{counter+1}/{length}.\n\n<b>{word}</b>\n\n{answer.center(63)}\n\n.سرفصل : {content}\nفصل : {chapter} \n {link}\n{page}:برگ"
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
        waysMsg = "روش یادگیری واژه های کتاب را {} عزیز 🌺🌸 انتخاب کن.".format(self.firstName)
        # wayKey = json.dumps({"keyboard":[[BtnS().deutsch,BtnS().english,BtnS().synonym],[BtnS().allTogether,BtnS().persian],[Btn().getBack]],"resize_keyboard":True}) 
        wayKey = AKeys().ways
        self.bot.sendMessage(self.id,waysMsg,"none",wayKey)



     #    یا پارسی  این دکمه ها و پیام می آیند  deutsch , english , synonym  در صورت زدن یکی از دکمه های  
    def sendDESPAllKeyAndMessageYesNo(self,way): 
        waysWarningMsg = f"آیا مطمئن و استیگان نسبت به انتخاب روش جدید <b>{self.msg}</b>داری {self.firstName} عزیز🌺🌸 زیرا در صورت انتخاب سابقه قبلی شما به <b>{way}</b> در مورد واژه های کار شده از بین می رود؟"
        # yesNoKey = json.dumps({"keyboard":[[Btn().noDot,Btn().yesDot]],"resize_keyboard":True}) 
        yesNoKey = Keys().yNDot
        self.bot.sendMessage(self.id,waysWarningMsg,"none",yesNoKey)


   #    یا پارسی و یکسان بودن با روش قبلی این دکمه ها و پیام می آیند  deutsch , english , synonym  در صورت زدن یکی از دکمه های  
    def sendDESPAllSameKeyAndMessageFAVA(self): 
        waysWarningMsg = f"روش شما در همین هنگام <b>{self.msg}</b> هست نیازی به دگرسانی و تغییر نیست."
        # regularHomePageKey = json.dumps({"keyboard":[[BtnA().admin,Btn().reviewWords],[Btn().wordsNum,Btn().wayEdit,Btn().account],[Btn().timeLearnEdit,Btn().reportActivity],[Btn().deleteBot,Btn().aboutBot,Btn().uILangNKeyEdit],[Btn().opinion]],"resize_keyboard":True})
        regularHomePageKey = AKeys().secondMenu
        self.bot.sendMessage(self.id,waysWarningMsg,"none",regularHomePageKey)

    #در صورت زدن دکمه «بله» به فهرست آغازین و اصلی منتقل شده و این  دکمه ها و پیام می آیند 
    def sendBaleKeyAndMessageFAVA(self): 
        waysChangedMsg = "دگرسانی و تغییر📝 روش 🛣 به <b>{}</b> انجام شد.".format(self.msg)
        # regularHomePageKey = json.dumps({"keyboard":[[BtnA().admin,Btn().reviewWords],[Btn().wordsNum,Btn().wayEdit,Btn().account],[Btn().timeLearnEdit,Btn().reportActivity],[Btn().deleteBot,Btn().aboutBot,Btn().uILangNKeyEdit],[Btn().opinion]],"resize_keyboard":True})
        regularHomePageKey = AKeys().secondMenu
        self.bot.sendMessage(self.id,waysChangedMsg,"none",regularHomePageKey)

   #در صورت زدن دکمه «خیر» به فهرست آغازین و اصلی منتقل شده و این  دکمه ها و پیام می آیند 
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
        wortZahlMsg = "چه تعداد و شمار واژه نو {} عزیز 🌺🌸 در روز می خواهی؟".format(self.firstName)        
        # wortZahlKey = json.dumps({"keyboard":[[BtnS().three],[BtnS().two],[BtnS().one],[BtnS().five,BtnS().ten,BtnS().fifteen,BtnS().twenty],[Btn().getBack]],"resize_keyboard":True})
        wortZahlKey = AKeys().wordsNum
        self.bot.sendMessage(self.id,wortZahlMsg,"none",wortZahlKey)

    #در صورت زدن دکمه «۳» یا «۵» یا «۷»این  دکمه ها و پیام می آیند 
    def send357AllVMessageFAVA(self):
        changedWordNum = "شمار و تعداد واژه های نو به {} تغییر و دگرش یافت.".format(self.msg)
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
        timeLearningMsg = "ساعت آغاز یادگیری روزانه ات را {} عزیز 🌺🌸 جهت مراجعه و سرزدن ربات انتخاب کن.".format(self.firstName)
        # hoursKey = json.dumps({"keyboard":[[BtnS().clock1,BtnS().clock2,BtnS().clock3,BtnS().clock4,BtnS().clock5,BtnS().clock6,BtnS().clock7,BtnS().clock8],[BtnS().clock9,BtnS().clock10,BtnS().clock11,BtnS().clock12,BtnS().clock13,BtnS().clock14,BtnS().clock15,BtnS().clock16],[BtnS().clock17,BtnS().clock18,BtnS().clock19,BtnS().clock20,BtnS().clock21,BtnS().clock22,BtnS().clock23],[Btn().getBack]],"resize_keyboard":True}) 
        hoursKey = Keys().hKeys
        self.bot.sendMessage(self.id,timeLearningMsg,"none",hoursKey)
    #در صورت زدن دکمه «۱..۲۳» این  دکمه ها و پیام می آیند 
    def send1_23MessageYesNo(self,year,monthAlpha,day,weekDay,hourMin,askedYear,askedMonthAlpha,askedDay,askedWeekDay,askedHourMin):
        dash = "___________________________________"
        timeLearningWarningMsg = f"آیا مطمئن و اُستیگان هستی  {self.firstName} عزیز 🌺🌸 از دگرسانی 👈یادگیری واژگان روزانه👉 به ساعت و زمان {self.msg} در تاریخ {askedWeekDay}  {askedDay} {askedMonthAlpha} {askedYear} \n{dash}\nدر حال حاضر 👈یادگیری واژگان روزانه👉 بعدی و پسین در تاریخ {weekDay}  {day} {monthAlpha} {year} ,<b> در ساعت و زمان {hourMin}</b> می باشد.\n @DeutschOhal "
        

        # yesNoKey = json.dumps({"keyboard":[[Btn().noDash,Btn().yesDash]],"resize_keyboard":True}) 
        yesNoKey = Keys().yNDash
        self.bot.sendMessage(self.id,timeLearningWarningMsg,"none",yesNoKey)


    #در صورت همسان بودن زمان یادگیری روزانه با قبلی  این  دکمه ها و پیام می آیند 
    def sendYesMessageSameFAVA(self,year,monthAlpha,day,weekDay,hourMin):
        dash = "___________________________________"
        # "روش شما در همین هنگام هم  {} هست نیازی تغییر و دگرسانی نیست".format(self.msg)

        timeLearningChangedMsg = f"زمان یادگیری روزانه شما در همین هنگام هم  {self.msg} هست نیازی به دگرسانی و تغییر نیست\n{dash}\n👈یادگیری واژگان روزانه👉 بعدی و پسین در تاریخ {weekDay}  {day} {monthAlpha} {year} ,<b> در ساعت و زمان {hourMin}</b> \n @DeutschOhal"
        # regularHomePageKey = json.dumps({"keyboard":[[BtnA().admin,Btn().reviewWords],[Btn().wordsNum,Btn().wayEdit,Btn().account],[Btn().timeLearnEdit,Btn().reportActivity],[Btn().deleteBot,Btn().aboutBot,Btn().uILangNKeyEdit],[Btn().opinion]],"resize_keyboard":True})
        regularHomePageKey = AKeys().secondMenu
        self.bot.sendMessage(self.id,timeLearningChangedMsg,"none",regularHomePageKey)


    #در صورت زدن دکمه «بله» این  دکمه ها و پیام می آیند 
    def sendYesMessageFAVA(self,year,monthAlpha,day,weekDay,hourMin):
        dash = "___________________________________"
        timeLearningChangedMsg = f"ساعت یادگیری روزانه به<b> {hourMin}</b> ویرایش شد.\n{dash}\n👈یادگیری واژگان روزانه👉 بعدی و پسین در تاریخ {weekDay}  {day} {monthAlpha} {year} ,<b> در ساعت و زمان {hourMin}</b>\n@DeutschOhal"
        # regularHomePageKey = json.dumps({"keyboard":[[BtnA().admin,Btn().reviewWords],[Btn().wordsNum,Btn().wayEdit,Btn().account],[Btn().timeLearnEdit,Btn().reportActivity],[Btn().deleteBot,Btn().aboutBot,Btn().uILangNKeyEdit],[Btn().opinion]],"resize_keyboard":True})
        regularHomePageKey = AKeys().secondMenu
        self.bot.sendMessage(self.id,timeLearningChangedMsg,"none",regularHomePageKey)
    #در صورت زدن دکمه «نه» به فهرست آغازین و اصلی این  دکمه ها و پیام می آیند 
    def sendNoMessageFAVA(self):
        fehrestAghazinMsg = "فهرست آغازین"
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
    #در صورت زدن دکمه «گزارش‌ کارکرد📊»  این  دکمه ها و پیام می آیند 
    def sendBVFMessageReports(self):
        reportPageMsg = "انتخاب {}".format(self.msg)
        # reportKey = json.dumps({"keyboard":[[Btn().reportWeakWords,Btn().reportWordsPartions],[Btn().getBack]],"resize_keyboard":True})
        reportKey = Keys().reportKeys
        self.bot.sendMessage(self.id,reportPageMsg,"none",reportKey)

    #در صورت زدن دکمه «گزارش واژگان در بخش ها📈»  این  دکمه ها و پیام می آیند 
    def sendReportAllWordsMessageBBFA(self,num,reportWordsSectionsPercentage):
        dash = "___________________________________" 
        reportWordsSectionsMsg = f"گزارش تمامی واژگان کار شده ات در بخش ها، {self.firstName} عزیز 🌺🌸 تا امروز : \n {dash}\n\nشمار تمامی واژگان کار شده تا امروز : {num} \n{dash}\n\nشمار و درصد تمامی واژه ها در تمامی بخش های جعبه لایتنر : \n\n {reportWordsSectionsPercentage}\n\n@DeutschOhal "
        # backToHomePage = json.dumps({"keyboard":[[Btn().getBack]],"resize_keyboard":True})
        backToHomePage = Keys().getBackKeys
        self.bot.sendMessage(self.id,reportWordsSectionsMsg,"none",backToHomePage)
    #در صورت زدن دکمه «گزارش ناتوانی در واژگان📉»  این  دکمه ها و پیام می آیند 
    # wWDS,wWPGS
    def sendReportWeakWordMessageBBFA(self,wWDS,wWPGS):
        dash = "___________________________________"
        reportWordsSectionsMsg = f"گزارش ناتوان ترین واژگان در یادگیری، {self.firstName} عزیز 🌺🌸 تا امروز \n (ناتوان ترین واژگان به معنی و چَم واژگانی  می باشد که بیش از یک ماه است که هنوز، یادگیری کامل نشده اند) \n {dash}\n فهرست به ترتیب واژگانی که بیش از یک ماه یادگیریشان به درازا کشیده با بیان شمارِ روز و بخش\n\n<b>{wWDS.center(63)}</b>\n{dash}\nفهرست واژگان ناتوان به ترتیب درصد در بخش های جعبه لایتنر\n\n{wWPGS}\n@DeutschOhal"
        # backToHomePage = json.dumps({"keyboard":[[Btn().getBack]],"resize_keyboard":True})
        backToHomePage = Keys().getBackKeys
        self.bot.sendMessage(self.id,reportWordsSectionsMsg,"none",backToHomePage)

    #در صورت زدن دکمه «بازگشت به فهرست آغازین🏡»  این  دکمه ها و پیام می آیند 
    #FIXME حذف این تابع از کیبورد و جایگزینی در آنالیز AYVK.sendKeyAndMessageFAVA()
    def sendBBFAMessageFAVA(self):
        self.obj_AYVK.sendKeyAndMessageFAVA()

    def reportWeakWords(self,wWDS,wWPGS): 
        dash = "___________________________________"   
        reportMsg = f"\n گزارش ناتوان ترین واژگان در یادگیری ,{self.firstName} عزیز 🌺🌸 تاامروز \n{dash.center(73)} \n\n فهرست به ترتیب واژگانی که بیش از یک ماه یادگیرشان به درازا کشیده با بیان شمار روز\n \n {wWDS}\n{dash.center(73)}\n\n فهرست واژگان ناتوان به ترتیب درصد بخش های جعبه لایتنر\n\n {wWPGS}\n @DeutschOhal"
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
         languageMsg = "زبان دلخواهت انتخاب کن {} عزیز 🌺🌸 برای پیام ها و فهرست ربات".format(self.firstName)
         
        #  languagesKey = json.dumps({"keyboard":[[BtnS().keyNMsgDe],[BtnS().keyNMsgEn],[BtnS().keyNMsgPer],[Btn().getBack]],"resize_keyboard":True}) 
         languagesKey = Keys().lanKeys
         self.bot.sendMessage(self.id,languageMsg,"none",languagesKey)
    
        #در صورت انتخاب و زدن <پوسته فارسی> به فهرست آغازین و اصلی منتقل شده و این  دکمه ها و پیام می آیند 
    def sendBaleKeyAndMessageFAVA(self): 
        languageSelectedMsg = f"برای ربات {self.msg}انتخاب شد."
        # regularHomePageKey = json.dumps({"keyboard":[[BtnA().admin,Btn().reviewWords],[Btn().wordsNum,Btn().wayEdit,Btn().account],[Btn().timeLearnEdit,Btn().reportActivity],[Btn().deleteBot,Btn().aboutBot,Btn().uILangNKeyEdit],[Btn().opinion]],"resize_keyboard":True})
        regularHomePageKey = AKeys().secondMenu
        self.bot.sendMessage(self.id,languageSelectedMsg,"none",regularHomePageKey)




        # self.obj_Start.sendKeyAndMessagesUI()
    #    یا کیبورد و پیام پارسی⌨💬 این دکمه ها و پیام از فهرست آغازین و اصلی  می آیند  deutsch Menu, english Menu  در صورت زدن یکی از دکمه های  
    def sendKeyAndMessageFNVA2(self):
        languageSelectedMsg = f"برای ربات {self.msg}انتخاب شد."
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
        aboutMsg =f"با درود و سلام به شما <i>{self.firstName}</i> عزیز 🌺🌸\nاین ربات امکان یادگیری تمامی واژه های جدید و مورد تاکید کتاب <b>'Großes Übungsbuch Wortschatz'</b>  را در چهارچوب تکرار و تمرین به روش لایتنر به صورت روزمره و در ساختار تقویم با امکان یادآوری به شما و انتخاب پاسخ به آلمانی، به مترادف، به انگلیسی و به فارسی را با استفاده از منابع معتبر زبان آلمانی میسر می کند، به گونه ای که تسلط کامل در حداقل یک ماه نسبت به یک واژه حاصل می شود و واژه از حافظه کوتاه مدت شما درحافظه بلند مدتتان قرار می گیرد." 
        # regularHomePageKey = json.dumps({"keyboard":[[BtnA().admin,Btn().reviewWords],[Btn().wordsNum,Btn().wayEdit,Btn().account],[Btn().timeLearnEdit,Btn().reportActivity],[Btn().deleteBot,Btn().aboutBot,Btn().uILangNKeyEdit],[Btn().opinion]],"resize_keyboard":True})
        regularHomePageKey = AKeys().secondMenu
        self.bot.sendMessage(self.id,aboutMsg,"none",regularHomePageKey)

#FIXME copy these 4 method to every admin language
    def sendKeyAndMessageSendingSugession(self):
        aboutMsg =f" هرگونه نظر، انتقاد و یا پیشنهادی داری، <i>{self.firstName}</i> عزیز 🌺🌸برای ما بفرست."
        # backToHomePage = json.dumps({"keyboard":[[Btn().getBack]],"resize_keyboard":True})
        backToHomePage = Keys().getBackKeys
        self.bot.sendMessage(self.id,aboutMsg,"none",backToHomePage)

    def sendKeyAndMessageDeliverOpinion(self,opId):
        aboutMsg =f"نظرت، <i>{self.firstName}</i> عزیز 🌺🌸 با شماره پی گیری <b>{opId}</b> ثبت شد."
        # regularHomePageKey = json.dumps({"keyboard":[[Btn().reviewWords],[Btn().wordsNum,Btn().wayEdit,Btn().account],[Btn().timeLearnEdit,Btn().reportActivity],[Btn().deleteBot,Btn().aboutBot,Btn().uILangNKeyEdit],[Btn().opinion]],"resize_keyboard":True})
        regularHomePageKey = AKeys().secondMenu
        self.bot.sendMessage(self.id,aboutMsg,"none",regularHomePageKey)

    def sendKeyAndMessageUsingBotKeys(self):
        aboutMsg =f"متنی وارد نشد! در صورت تمایل به فرستادن نظر، <b>بدون استفاده از کیبورد ربات </b>، متن  را وارد کرده و سپس بفرستید."
        # regularHomePageKey = json.dumps({"keyboard":[[Btn().reviewWords],[Btn().wordsNum,Btn().wayEdit,Btn().account],[Btn().timeLearnEdit,Btn().reportActivity],[Btn().deleteBot,Btn().aboutBot,Btn().uILangNKeyEdit],[Btn().opinion]],"resize_keyboard":True})
        regularHomePageKey = Keys().secondMenu
        self.bot.sendMessage(self.id,aboutMsg,"none",regularHomePageKey)

    def sendKeyAndMessageOutOfRangeMsg(self):
        aboutMsg =f"شمار کاراکترها و واژه های متن فرستاده شده بیش از حد است! متنتان را کوتاه تر یا در چند بخش بفرستید."
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
        deleteBotWarnMsg = "آیا مطمئن و اُستیگان هستی {} عزیز 🌺🌸 ازحذف و زدایش ربات؟ زیرا موجب از بین رفتن سابقه شما می شود و دیگر پیامی برایتان ارسال نمی شود.".format(self.firstName)
        # yesNoKey = json.dumps({"keyboard":[[Btn().no,Btn().yesDelete]],"resize_keyboard":True})
        yesNoKey = Keys().yNKeys 
        self.bot.sendMessage(self.id,deleteBotWarnMsg,"none",yesNoKey)
    #در صورت زدن دکمه «بله» به بخش فهرست نخستین🛎 و اولیه منتقل شده و   این دکمه ها و پیام می آیند    
    def sendYesKeyAndMessageFNVA(self):
        deleteBotMsg = "ربات حذف و زدایش شد."
        # firstHomePageKey = json.dumps({"keyboard":[[BtnA().admin,Btn().startLearning],[Btn().aboutBotNew,Btn().uILangNKeyEditNew]],"resize_keyboard":True})
        firstHomePageKey = AKeys().firstMenu
        self.bot.sendMessage(self.id,deleteBotMsg,"none",firstHomePageKey)

    #در صورت زدن دکمه «خیر» به بخش فهرست آغازین و اصلی منتقل شده و   این دکمه ها و پیام می آیند  
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

