#my class
import sys
sys.path.append( "../")
from mainV2.base.ButtonsA import ButtonSame as ABtnS

from mainV2.KeysNMsgs import KeysNMsgsPer as Sending
from mainV2.KeysNMsgs import KeysNMsgsEn as KNMEn
from mainV2.KeysNMsgs import KeysNMsgsDe as KNMDe
from mainV2.base.Buttons import ButtonPer as Btn
from mainV2.base.Buttons import ButtonSame as BtnS
from mainV2.base.ButtonsA import ButtonAdminPer as BtnA 
from mainV2.base.Txt import MessageNVarPer as MNV

from mainV2.picLeitner import VidSet as VS


from mainV2.set import dbContact
import datetime

from abc import ABC,abstractclassmethod





# self.obj_Btn.aboutBot
#شناسایی گونه کاربر
class KindOfUser:
    def __init__(self,id,firstName,msg,callBackQuery_id,msgId,data,last_name=None,username=None):
         
        self.id = id
        self.firstName = firstName
        self.msg = msg
        self.data = data
        self.lastName = last_name
        self.username = username

        self.verifyCallBackQuery_id = callBackQuery_id
        self.verifyMsg = msg
        # print(id,firstName,msg,last_name,username)
        self.obj_UserInfo = Karbar(id,firstName,msg,callBackQuery_id,msgId,data,last_name,username)
        self.obj_AdminInfo = Admin(id,firstName,msg,callBackQuery_id,msgId,data,last_name,username)


    def identifyUserAndMsg(self):
        if self.id == 73543260  and self.verifyMsg is not None and self.verifyCallBackQuery_id is None:
            self.obj_AdminInfo.msgAnlizer()
        elif self.id == 73543260  and self.verifyMsg is None and self.verifyCallBackQuery_id is not None:
            self.obj_AdminInfo.dataAnalizer()
        elif self.verifyMsg is not None and self.verifyCallBackQuery_id is None:
            self.obj_UserInfo.msgAnlizer()
        elif self.verifyMsg is None and self.verifyCallBackQuery_id is not None:
            self.obj_UserInfo.dataAnalizer()




#فرستادن پیام و کیبورد interface
class AnlaizeAbstract(ABC):
      @abstractclassmethod
      def msgAnlizer(self):
          pass

# کلاس کاربر
class Karbar(AnlaizeAbstract):
    def __init__(self,id,firstName,msg,callBackQuery_id,msgId,data,last_name=None,username=None):
        self.id = id
        self.msg = msg
        self.firstName=firstName
        self.last_name = last_name
        self.callBackQuery_id = callBackQuery_id  
        self.msgId = msgId
        self.data = data
        self.obj_Btn = Btn()
        self.username = username
        self.obj_KNM = Sending
        self.obj_DbC= dbContact


    def msgAnlizer (self):
        try:
            userIdentify = self.obj_DbC.User(self.id,self.firstName,self.last_name,self.username).userIdentify()
            channel = "@DeutschOhal"
            # channel = "@testasd147"
            channelMemVeri = self.obj_DbC.Report(self.id).channelMemberVerification(channel)
            if userIdentify and channelMemVeri is False:
                self.obj_KNM.Start(self.id,self.firstName,self.msg).memberChannel(channel)
            else: 
            
                try:    
                    repeat = 0  


                    # افزودن پیام در چهارچوب زمان به پیام های دیرین
                    self.obj_DbC.Msg(self.id).addMsgs(self.msg)
                    
                    #پیشگیری از پیام تکراری
                    #done AdminErrorMsgs class in karbar side and rename sendWarningRepeatedKeyAndMessageToNoneUser to NoneAdmin
                    if self.obj_DbC.Msg().isTheLastOneRepeatedMsg(self.id,"User") is True:
                        # type of keybaord home
                        if userIdentify is False:                  
                            self.obj_KNM.ErrorMsgs(self.id,self.firstName,self.msg).sendWarningRepeatedKeyAndMessageToNoneUser()
                            repeat = 1        
                        elif userIdentify is True:
                            self.obj_KNM.ErrorMsgs(self.id,self.firstName,self.msg).sendWarningRepeatedKeyAndMessageToUser()    
                            repeat = 1  
                    if self.obj_DbC.Msg(self.id,self.msg).noneKeyboardMsgs(self.msg,"User") and repeat == 0  :
                    
                        if userIdentify is False:
                        #done پیام استفاده از کیبورد
                            self.obj_KNM.ErrorMsgs(self.id,self.firstName,self.msg).sendWarningNoneKeyboardToGuest()
                            
                        elif userIdentify:
                            self.obj_KNM.ErrorMsgs(self.id,self.firstName,self.msg).sendWarningNoneKeyboardToUser()
                        
                    elif repeat == 0  :
                            ####################### در فهرست نخستین و اولیه ######################

                            #در فهرست نخستین و اولیه
                            if self.msg == BtnS().start :
                                if userIdentify is False :
                                    
                                    # self.obj_Start.sendKeyAndMessagesUI()
                                    # self.obj_DbC.User(self.id,self.firstName,self.last_name,self.username).registerByClick()
                                    self.obj_KNM.Start(self.id,self.firstName,self.msg).sendKeyAndMessagesUI()

                                else:
                                    self.obj_KNM.AghazYadgiriVazhehayeKetab(self.id,self.firstName,self.msg).sendKeyAndMessageFAVA()
                            
                                
                            #در فهرست نخستین و اولیه
                            if self.msg ==Btn().uILangNKeyEditNew:
                                if userIdentify is False:
                                    
                                    self.obj_KNM.DegarsaniZaban1(self.id,self.firstName,self.msg).sendKeyAndMessageUI1()
                                    #  self.obj_DegarsaniZaban1.sendKeyAndMessageUI1() 

                                else:
                                    self.obj_KNM.AghazYadgiriVazhehayeKetab(self.id,self.firstName,self.msg).sendKeyAndMessageFAVA()

                            

                        
                            #در فهرست نخستین و اولیه
                            if self.msg == BtnS().keyNMsgPer:        
                                self.obj_DbC.UILanguage(self.id).saveUIL(self.msg)
                                if userIdentify is False:
                                        self.obj_KNM.Start(self.id,self.firstName,self.msg).sendKeyAndMessageFNVAUIselected()
                                else:
                                        self.obj_KNM.AghazYadgiriVazhehayeKetab(self.id,self.firstName,self.msg).sendKeyAndMessageFAVA()

                            if self.msg == BtnS().keyNMsgEn:        
                                self.obj_DbC.UILanguage(self.id).saveUIL(self.msg)
                                if userIdentify is False:
                                        KNMEn.Start(self.id,self.firstName,self.msg).sendKeyAndMessageFNVAUIselected()
                                else:
                                        KNMEn.AghazYadgiriVazhehayeKetab(self.id,self.firstName,self.msg).sendKeyAndMessageFAVA()

                            if self.msg == BtnS().keyNMsgDe:        
                                self.obj_DbC.UILanguage(self.id).saveUIL(self.msg)
                                if userIdentify is False:
                                        KNMDe.Start(self.id,self.firstName,self.msg).sendKeyAndMessageFNVAUIselected()
                                else:
                                        KNMDe.AghazYadgiriVazhehayeKetab(self.id,self.firstName,self.msg).sendKeyAndMessageFAVA()
                                ############
                                ##  save to database
                                ###########
                                

                                # break 
                            #در فهرست نخستین و اولیه
                            if self.msg == Btn().startLearning :
                                if userIdentify is False: 
                                            self.obj_DbC.Report(self.id).firstLeitnerBoxStatistics(self.msg) 
                                            # self.obj_DbC.User(self.id,self.firstName,self.last_name,self.username).updateNoneUserToSimple()
                                            #بطور ویژه از باتان برای مشخص کردن زبان استفاده شد
                                            self.obj_DbC.UILanguage(self.id).saveUIL(BtnS().keyNMsgPer)
                                    

                                            self.obj_KNM.AghazYadgiriVazhehayeKetab(self.id,self.firstName,self.msg).sendAYVKKeyAndMessage327()
                                else:
                                    self.obj_KNM.AghazYadgiriVazhehayeKetab(self.id,self.firstName,self.msg).sendKeyAndMessageFAVA()
                                            
                                            #در فهرست نخستین و اولیه
                            if self.msg == BtnS().oneNew or self.msg == BtnS().twoNew or self.msg == BtnS().threeNew:
                                if userIdentify is False:
                                    withoutEmoj = int(self.msg.strip(" ♨️"))
                                    self.obj_DbC.ShomarVazhgan(self.id).saveWordNum(withoutEmoj)

                                    self.obj_DbC.User(self.id,self.firstName,self.last_name,self.username).updateNoneUserToSimple()
                                    # موقت تا مرور ساخته بشه شمارنده در اینجاصفر می کنیم
                                    self.obj_DbC.Counter(self.id).putZeroToCounter()
                                    withoutEmoj = ""
                                    #FIXME way of give user all language in appropriate way
                                    allWays =[BtnS().persianTextEn, BtnS().deutschText,BtnS().englishText,BtnS().synonymText]
                                    # print(f'allWays = {allWays}')

                                    self.obj_DbC.RaveshYadgiri(self.id).saveWay(allWays)
                                    #make package words 
                                    self.obj_DbC.Vazhegan(self.id,self.msg).mixWords()
                                    # self.obj_Vazhegan.mixWords()
                                    
                                    way,wKind,numW,numAll,word,content,chapter,wordsPage,linkWord = self.obj_DbC.Vazhegan(self.id,self.msg).wordNdetails()
                                                                        
                                    # print(f'way = {way}')
                                    reportNum = self.obj_DbC.Report(self.id).getReportNum()
                                    #standardized word
                                    standardizedWord = self.obj_DbC.Vazhegan(self.id).standardizeWord(word,reportNum)
                                    #نگاشتن تاریخ یادگیری و تمرین نوبت پسین  و بعدی در فردا
                                    self.obj_DbC.DateArrange().saveTomorrowNextTraining(self.id)

                                    wordCard = MNV(self.firstName).wordCard(wKind,numW,numAll,standardizedWord,content,chapter,wordsPage,linkWord)
                                    self.obj_KNM.Inline(self.id,self.data).dataWordWithGuide(way,wordCard,Btn().startLearning)

                                else:
                                    #########
                                    tomorrowNextTraining =self.obj_DbC.DateArrange().getTomorrowNextTraining(self.id)
                                    hourMin = tomorrowNextTraining.strftime("%H:%M")
                                    #گرفتن سال ، ماه نویسه ای ، روز
                                    # monthAlpha,year,month,day,monthAlphaFinglish,weekDayPer,weekDayFinglish
                                    monthAlpha,year,_,day,_,_,_ = self.obj_DbC.DateArrange(self.id).convertToKhorshidi(tomorrowNextTraining)
                                    # گرفتن نام روز در هفته به پارسی
                                    weekDay = self.obj_DbC.DateArrange(self.id).getWeekDay(tomorrowNextTraining)
                                    ########
                                    self.obj_KNM.AghazYadgiriVazhehayeKetab(self.id,self.firstName,self.msg).sendNextTrainingDateTimeKeyAndMessageBBFA(weekDay,day,monthAlpha,year,hourMin)



                        #FIXME
                            #در فهرست نخستین و اولیه
                            # if self.msg ==BtnS().persianNew or self.msg == BtnS().deutschNew or self.msg ==BtnS().englishNew or self.msg ==BtnS().synonymNew:
                                if userIdentify is False:
                                        self.obj_DbC.User(self.id,self.firstName,self.last_name,self.username).updateNoneUserToSimple()
                                        # موقت تا مرور ساخته بشه شمارنده در اینجاصفر می کنیم
                                        self.obj_DbC.Counter(self.id).putZeroToCounter()
                                        # withoutEmoj = ""
                                        # dictMsg ={BtnS().persianNew:BtnS().persianText, BtnS().deutschNew:BtnS().deutschText,BtnS().englishNew:BtnS().englishText,BtnS().synonymNew:BtnS().synonymText}
                                        # for field,value in dictMsg.items():
                                        #     if self.msg == field: 
                                        #         withoutEmoj = value

                                        # self.obj_DbC.RaveshYadgiri(self.id).saveWay(withoutEmoj)
                                        #make package words 
                                        self.obj_DbC.Vazhegan(self.id,self.msg).mixWords()
                                        # self.obj_Vazhegan.mixWords()
                                    
                                        way,wKind,numW,numAll,word,content,chapter,wordsPage,linkWord = self.obj_DbC.Vazhegan(self.id,self.msg).wordNdetails()
                                                                        

                                        reportNum = self.obj_DbC.Report(self.id).getReportNum()
                                        #standardized word
                                        standardizedWord = self.obj_DbC.Vazhegan(self.id).standardizeWord(word,reportNum)
                                        #نگاشتن تاریخ یادگیری و تمرین نوبت پسین  و بعدی در فردا
                                        self.obj_DbC.DateArrange().saveTomorrowNextTraining(self.id)
                                        if   5<reportNum:
                                        # here 
                                          pass

                                        else:

                                            pass
                                else:
                                    #########
                                    tomorrowNextTraining =self.obj_DbC.DateArrange().getTomorrowNextTraining(self.id)
                                    hourMin = tomorrowNextTraining.strftime("%H:%M")
                                    #گرفتن سال ، ماه نویسه ای ، روز
                                    # monthAlpha,year,month,day,monthAlphaFinglish,weekDayPer,weekDayFinglish
                                    monthAlpha,year,_,day,_,_,_ = self.obj_DbC.DateArrange(self.id).convertToKhorshidi(tomorrowNextTraining)
                                    # گرفتن نام روز در هفته به پارسی
                                    weekDay = self.obj_DbC.DateArrange(self.id).getWeekDay(tomorrowNextTraining)
                                    ########
                                    self.obj_KNM.AghazYadgiriVazhehayeKetab(self.id,self.firstName,self.msg).sendNextTrainingDateTimeKeyAndMessageBBFA(weekDay,day,monthAlpha,year,hourMin)
                            ###must be vanish################

                            #در فهرست نخستین و اولیه
                            if self.msg == Btn().aboutBotNew:
                                if userIdentify is False:
                                    #  self.obj_DarbarehRobat1.sendKeyAndMessageDarbarehRobat1()
                                    self.obj_KNM.DarbarehRobat1(self.id,self.firstName,self.msg).sendKeyAndMessageDarbarehRobat1()
                                else:
                                    self.obj_KNM.AghazYadgiriVazhehayeKetab(self.id,self.firstName,self.msg).sendKeyAndMessageFAVA()
                                

                        ###################### دکمه های مشترک میان فهرست ها ###################
                            # if self.msg == BtnS().lamp:
                            #     if userIdentify is True:
                                
                            #             if self.obj_DbC.DateArrange().getRightWrongLampFlag(self.id) is True:

                            #                     #get way 
                            #                     way = self.obj_DbC.RaveshYadgiri(self.id).getWay()
                            #                     #planB
                                                
                            #                     # way = self.obj_DbC.RaveshYadgiri(self.id).wayOrWaysString(way)
                            #                     #planA
                            #                     #get icon
                            #                     icon = self.obj_DbC.RaveshYadgiri(self.id).getIconBook(way)
                            #                     #get word
                            #                     todayWords = self.obj_DbC.Vazhegan(self.id).getTodayWords()
                            #                     print(f"todayWords = {todayWords}")
                            #                     word =  self.obj_DbC.Vazhegan(self.id).getOneRightWord(todayWords) 
                            #                     print(f"word = {word}")
                            #                     #save answer to todayWordsNAnswer
                            #                     answerLink = self.obj_DbC.Vazhegan(self.id).audioAnswer(word,way)
                            #                     input = self.obj_DbC.Vazhegan(self.id).getOneAnswerPure(word)
                            #                     self.obj_DbC.Vazhegan(self.id).updateValueKeyAnswer(input)
                            #                     # 
                            #                     # get one answer
                            #                     answer = self.obj_DbC.Vazhegan(self.id).getOneAnswer(input)
                                                
                            #                     reportNum = self.obj_DbC.Report(self.id).getReportNum()

                            #                     standardizedAnswer = self.obj_DbC.Vazhegan(self.id).standardizeAnswer(way,answer,reportNum)
                            #                     #FIXME reportnum doesn't work
                            #                     if   5<reportNum:
                            #                         #send keyboar and message
                            #                         self.obj_KNM.AghazYadgiriVazhehayeKetab(self.id,self.firstName,self.msg).sendLampKeyAndMessageVX(way,icon,standardizedAnswer,answerLink) 
                            #                     else:
                            #                         self.obj_KNM.AghazYadgiriVazhehayeKetab(self.id,self.firstName,self.msg).sendLampKeyAndMessageVXGuide(way,icon,standardizedAnswer,answerLink)


                            #             else:
                            #                     #########
                            #                     tomorrowNextTraining =self.obj_DbC.DateArrange().getTomorrowNextTraining(self.id)
                            #                     hourMin = tomorrowNextTraining.strftime("%H:%M")
                            #                     #گرفتن سال ، ماه نویسه ای ، روز
                            #                     # monthAlpha,year,month,day
                            #                     monthAlpha,year,_,day = self.obj_DbC.DateArrange(self.id).convertToKhorshidi(tomorrowNextTraining)
                            #                     # گرفتن نام روز در هفته به پارسی
                            #                     weekDay = self.obj_DbC.DateArrange(self.id).getWeekDay(tomorrowNextTraining)
                            #                     ########
                            #                     self.obj_KNM.AghazYadgiriVazhehayeKetab(self.id,self.firstName,self.msg).sendNextTrainingDateTimeKeyAndMessageBBFA(weekDay,day,monthAlpha,year,hourMin)   
                            #     else:
                            #         self.obj_KNM.Start(self.id,self.firstName,self.msg).sendKeyAndMessageFNVAUINakhostin()



                            # if self.msg == BtnS().crossCheck or self.msg == BtnS().check:
                            #     if userIdentify is True:
                            #             if self.obj_DbC.DateArrange().getRightWrongLampFlag(self.id) is True:
                            #                     msgArray = self.obj_DbC.Msg().getMessagesToday(self.id)
                            #                     # msgArray = self.obj_DbC.Msg(self.id,self.msg).getMsgArray()
                            #                     lengthMsgArray = len(msgArray)
                            #                     counter = self.obj_DbC.Counter(self.id).getCounter()
                            #                     #درصورت اسپم بودن و تکرار ی و  در عین حال آخرین  واژه هم بودن
                            #                     if (msgArray[lengthMsgArray-1] == msgArray[lengthMsgArray-2] or msgArray[lengthMsgArray-2] == BtnS().check or msgArray[lengthMsgArray-2] == BtnS().crossCheck) and  self.obj_DbC.Counter(self.id).lastWordVerification() == False:
                            #                         self.obj_KNM.ErrorMsgs(self.id,self.firstName,self.msg).sendWarningKeyAndMessageBBFA()
                            #                     #شرط تکراری نبودن
                            #                     elif (msgArray[lengthMsgArray-1] == msgArray[lengthMsgArray-2] or msgArray[lengthMsgArray-2] == BtnS().check or msgArray[lengthMsgArray-2] == BtnS().crossCheck) and counter == 0:
                            #                         self.obj_KNM.ErrorMsgs(self.id,self.firstName,self.msg).sendWarningKeyAndMessageBBFA()
                            #                     elif  msgArray[lengthMsgArray-1] == msgArray[lengthMsgArray-2] or msgArray[lengthMsgArray-2] == BtnS().check or msgArray[lengthMsgArray-2] == BtnS().crossCheck:
                            #                         self.obj_KNM.AghazYadgiriVazhehayeKetab(self.id,self.firstName,self.msg).sendWarningKeyAndMessageLamp() 
                                                    
                            #                     #آزمون آخرین بودن یا نبودن واژه 
                            #                     elif self.obj_DbC.Counter(self.id).lastWordVerification() == True:
                            #                     # if self.obj_Counter.lastWordVerification() == True:
                            #                         input = bool
                            #                         if self.msg == BtnS().check  :
                            #                             input = True
                            #                         elif self.msg == BtnS().crossCheck :
                            #                             input = False
                            #                         self.obj_DbC.Vazhegan(self.id).updateValueKey(input)
                            #                         self.obj_DbC.Counter(self.id).addOneToCounter()
                            #                         # self.obj_Counter.addOneToCounter()
                            #                         ##############
                            #                         if self.obj_DbC.IdentifyWordsSection(self.id,self.msg).findUserNWord() == False :
                            #                             if input is False:
                            #                                 self.obj_DbC.IdentifyWordsSection(self.id,self.msg).makeWordSection(1)
                            #                             elif input is True:
                            #                                 self.obj_DbC.IdentifyWordsSection(self.id,self.msg).makeWordSection(1)
                            #                                 self.obj_DbC.IdentifyWordsSection(self.id,self.msg).moveToNextLevel(1)
                            #                         elif self.obj_DbC.IdentifyWordsSection(self.id,self.msg).findUserNWord() ==True:
                            #                                 self.obj_DbC.IdentifyWordsSection(self.id,self.msg).moveToNextLevel(1)
                            #                         #################  report part  
                            #                         if self.obj_DbC.Counter(self.id).lastWordVerification() == False:    


                            #                             # # گرفتن نام روز در هفته به پارسی
                            #                             # weekDay = self.obj_DbC.DateArrange(self.id).getWeekDay(tomorrowNextTraining)
                            #                             all,right,wrong,wrongWordsNpages,weekDay,day,monthAlpha,year,houNMTraining,dateGriNextTraining,wordsSectionPosition = self.obj_DbC.Report(self.id).dailyReport()
                            #                             self.obj_KNM.AghazYadgiriVazhehayeKetab(self.id,self.firstName,self.msg).sendLastVXKeyAndMessageBBFA(all,right,wrong,wrongWordsNpages,weekDay,day,monthAlpha,year,houNMTraining,dateGriNextTraining,wordsSectionPosition)
                            #                             # self.obj_DbC.Vazhegan(self.id).eraseTodayWords()
                            #                         #فرستادن واژه
                            #                         else:
                                                    
                            #                             way,wKind,numW,numAll,word,content,chapter,wordsPage,linkWord = self.obj_DbC.Vazhegan(self.id).wordNdetails()



                            #                             reportNum = self.obj_DbC.Report(self.id).getReportNum()
                            #                             standardizedWord = self.obj_DbC.Vazhegan(self.id).standardizeWord(word,reportNum)
                            #                             if   5<reportNum:

                            #                             # here 
                            #                             # send message and keyboard
                            #                                 self.obj_KNM.AghazYadgiriVazhehayeKetab(self.id,self.firstName,self.msg).sendDESPKeyAndMessageLamp(wKind,numW,numAll,standardizedWord,content,chapter,wordsPage,linkWord)
                            #                             # self.obj_DbC.Vazhegan(self.id).eraseTodayWords()
                            #                             else:
                            #                                 self.obj_KNM.AghazYadgiriVazhehayeKetab(self.id,self.firstName,self.msg).sendDESPKeyAndMessageLampGuid(way,wKind,numW,numAll,standardizedWord,content,chapter,wordsPage,linkWord)


                            #                     elif self.obj_DbC.Counter(self.id).lastWordVerification() == False:
                            #                     # elif self.obj_Counter.lastWordVerification() == False:
                            #                         self.obj_DbC.Counter(self.id).putZeroToCounter()
                            #                         # self.obj_Counter.putZeroToCounter() 
                            #                         self.obj_KNM.AghazYadgiriVazhehayeKetab(self.id,self.firstName,self.msg).sendDESPKeyAndMessageLamp(wKind,numW,numAll,word,content,chapter,wordsPage,linkWord)  
                            #                         # self.obj_AghazYadgiriVazhehayeKetab.sendLastVXKeyAndMessageBBFA(all,right,wrong)
                            #             else:
                            #                     #########
                            #                     tomorrowNextTraining =self.obj_DbC.DateArrange().getTomorrowNextTraining(self.id)
                            #                     hourMin = tomorrowNextTraining.strftime("%H:%M")
                            #                     #گرفتن سال ، ماه نویسه ای ، روز
                            #                     # monthAlpha,year,month,day
                            #                     monthAlpha,year,_,day = self.obj_DbC.DateArrange(self.id).convertToKhorshidi(tomorrowNextTraining)
                            #                     # گرفتن نام روز در هفته به پارسی
                            #                     weekDay = self.obj_DbC.DateArrange(self.id).getWeekDay(tomorrowNextTraining)
                            #                     ########
                            #                     self.obj_KNM.AghazYadgiriVazhehayeKetab(self.id,self.firstName,self.msg).sendNextTrainingDateTimeKeyAndMessageBBFA(weekDay,day,monthAlpha,year,hourMin)  


                            #     else:
                            #             self.obj_KNM.Start(self.id,self.firstName,self.msg).sendKeyAndMessageFNVAUINakhostin()
                    

                                # if userIdentify is True:

                                # else:
                                #     self.obj_KNM.Start(self.id,self.firstName,self.msg).sendKeyAndMessageFNVAUIselected()
                        ###################### در فهرست آغازین و اصلی ###################
                            if self.msg == Btn().dailyLearnWords:
                                if userIdentify is True:
                                        self.obj_DbC.Report(self.id).firstLeitnerBoxStatistics(self.msg)
                                        if self.obj_DbC.DateArrange().getAutomateMsgFlag(self.id) is True:
                                                    self.obj_DbC.DateArrange().saveTrueRightWrongLampFlag(self.id)
                                                    #make package words 
                                                    self.obj_DbC.Vazhegan(self.id,self.msg).mixWords()
                                                    
                                                    way,wKind,numW,numAll,word,content,chapter,wordsPage,wordLink = self.obj_DbC.Vazhegan(self.id).wordNdetails()
                                
                                                    # here 
                                                    # send message and keyboard
                                                    # self.obj_KNM.AghazYadgiriVazhehayeKetab(self.id,self.firstName,self.msg).sendDESPKeyAndMessageLamp(wKind,numW,numAll,word,cotentNChap,wordsPage)
                                                    #planA
                                                    way = self.obj_DbC.RaveshYadgiri(self.id).getWay()
                                                    #planB
                                                
                                                    # way = self.obj_DbC.RaveshYadgiri(self.id).wayOrWaysString(wayPure)


                                                    reportNum = self.obj_DbC.Report(self.id).getReportNum()
                                                    standardizedWord = self.obj_DbC.Vazhegan(self.id).standardizeWord(word,reportNum)
                                                    # print(f"reportNum = {reportNum}")
                                                    if reportNum is None:
                                                        self.obj_DbC.Report(self.id).addReportNumField()
                                                        reportNum = self.obj_DbC.Report(self.id).getReportNum()
                                                        standardizedWord = self.obj_DbC.Vazhegan(self.id).standardizeWord(word,reportNum)
                                                        if   5<reportNum:

                                                            wordCard = MNV(self.firstName).wordCard(wKind,numW,numAll,standardizedWord,content,chapter,wordsPage,wordLink)
                                                            
                                                            self.obj_KNM.Inline(self.id,self.data).dataWord(way,wordCard,Btn().dailyLearnWords)
                                                    
                                                        else:
                                                            wordCard = MNV(self.firstName).wordCard(wKind,numW,numAll,standardizedWord,content,chapter,wordsPage,wordLink)
                                                            wordCardWithGuide = MNV(self.firstName).wordCardWithGuide(way,wKind,numW,numAll,standardizedWord,content,chapter,wordsPage,wordLink)
                                                            self.obj_KNM.Inline(self.id,self.data).dataWordWithGuide(way,wordCardWithGuide,Btn().dailyLearnWords)

                                                    else:
                                                        if   5<reportNum:

                                                            
                                                            wordCard = MNV(self.firstName).wordCard(wKind,numW,numAll,standardizedWord,content,chapter,wordsPage,wordLink)
                                                            self.obj_KNM.Inline(self.id,self.data).dataWord(way,wordCard,Btn().dailyLearnWords)

                                                        
                                                        else:
                                                            wordCardWithGuide = MNV(self.firstName).wordCardWithGuide(way,wKind,numW,numAll,standardizedWord,content,chapter,wordsPage,wordLink)
                                                            # wordCard = MNV(self.firstName).wordCard(wKind,numW,numAll,standardizedWord,content,chapter,wordsPage,wordLink)
                                                            self.obj_KNM.Inline(self.id,self.data).dataWordWithGuide(way,wordCardWithGuide,Btn().dailyLearnWords)
                                        else:
                                                #########
                                                tomorrowNextTraining =self.obj_DbC.DateArrange().getTomorrowNextTraining(self.id)
                                                hourMin = tomorrowNextTraining.strftime("%H:%M")
                                                #گرفتن سال ، ماه نویسه ای ، روز
                                                # monthAlpha,year,month,day,monthAlphaFinglish,weekDayPer,weekDayFinglish
                                                monthAlpha,year,_,day,_,_,_ = self.obj_DbC.DateArrange(self.id).convertToKhorshidi(tomorrowNextTraining)
                                                # گرفتن نام روز در هفته به پارسی
                                                weekDay = self.obj_DbC.DateArrange(self.id).getWeekDay(tomorrowNextTraining)
                                                ########
                                                self.obj_KNM.AghazYadgiriVazhehayeKetab(self.id,self.firstName,self.msg).sendNextTrainingDateTimeKeyAndMessageBBFA(weekDay,day,monthAlpha,year,hourMin)  

                                else:
                                        self.obj_KNM.Start(self.id,self.firstName,self.msg).sendKeyAndMessageFNVAUINakhostin()



                            #در فهرست آغازین و اصلی  
                            if self.msg == Btn().reviewWords:
                                if userIdentify is True:
                                        self.obj_KNM.MorureVazhehhayeGozashteh(self.id,self.firstName,self.msg).sendMVGKeyAndMessageTMVG()
                                else:
                                        self.obj_KNM.Start(self.id,self.firstName,self.msg).sendKeyAndMessageFNVAUINakhostin()

                                    

                            #در فهرست آغازین و اصلی .....#Btn().reviewWords
                            if self.msg == Btn().chapterNSection:
                                    if userIdentify is True:
                                            ##############
                                            self.obj_DbC.Counter(self.id).putZeroToCounter()
                                            # self.obj_Counter.putZeroToCounter()
                                            words = self.obj_DbC.Review(self.id).sortChapterContentBase()
                                            # print(f"words = {words}")
                                            self.obj_DbC.Review(self.id).saveReviewWords(words)
                                            try:
                                                way,content,chapter,word,counter,length,section,page,link = self.obj_DbC.Review(self.id).reviewChapterContentWordsNDetails()
                                                standardizedWord = self.obj_DbC.Vazhegan(self.id).standardizeWordReview(word,self.msg)
                                                msgCHNS = MNV(self.firstName).chapterNSectionRev(content,chapter,standardizedWord,counter,length,section,page,link)
                                                lengthIF = len(self.obj_DbC.Review(self.id).getReviewWords())
                                                # chapterNSectionWaysCBArray
                                                chNSWCB = [BtnS().deutschChapNSCB,BtnS().englishChapNSCB,BtnS().synonymChapNSCB,BtnS().persianEnChapNSCB]
                                                if lengthIF == 1:
                                                    self.obj_KNM.Inline(self.id,self.firstName,self.msg).reviewOne(chNSWCB,way,length,msgCHNS,self.msg)
                                                else:
                                                    self.obj_KNM.Inline(self.id,self.firstName,self.msg).reviewMoreThanOne(counter,chNSWCB,way,length,msgCHNS,self.msg)

                                                counterIF = self.obj_DbC.Counter(self.id).getCounter()
                                                # print(f"counterIF = {counterIF}")

                                            except:
                                                self.obj_KNM.MorureVazhehhayeGozashteh(self.id,self.firstName,self.msg).sendWeakWordsKeyAndMessageNoWordOtherReview()
                                            # here
                                            ###############   
                                    else:
                                            self.obj_KNM.Start(self.id,self.firstName,self.msg).sendKeyAndMessageFNVAUINakhostin()
                                        
                            if self.msg == Btn().nextWordChapNS:
                                    if userIdentify is True:
                                        if self.obj_DbC.Counter(self.id).getCounter()+1 != len(self.obj_DbC.Review(self.id).getReviewWords()):
                                            self.obj_DbC.Counter(self.id).addOneToCounter()
                                        # self.obj_Counter.addOneToCounter()
                                        counterIF = self.obj_DbC.Counter(self.id).getCounter()+1
                                        # print(f"counterIF = {counterIF}")
                                        lengthIF = len(self.obj_DbC.Review(self.id).getReviewWords())
                                        # print(f"lengthIF = {lengthIF}")
                                        if counterIF>lengthIF:
                                                self.obj_DbC.Counter(self.id).putValueToCounter(lengthIF-1)
                                                # self.obj_Counter.putValueToCounter(lengthIF-1)
                                        if counterIF != lengthIF:
                                            content,chapter,word,answer,counter,length,section,page,link = self.obj_DbC.Review(self.id).reviewChapterContentWordsNDetails()
                                            self.obj_KNM.MorureVazhehhayeGozashteh(self.id,self.firstName,self.msg).sendWordsChapterContentKeyAndMessagMiddleOLdWord(content,chapter,word,answer,counter,length,section,page,link)
                                            
                                            
                                        elif counterIF == lengthIF:
                                        #if last:
                                            
                                            content,chapter,word,answer,counter,length,section,page,link = self.obj_DbC.Review(self.id).reviewChapterContentWordsNDetails()
                                            self.obj_KNM.MorureVazhehhayeGozashteh(self.id,self.firstName,self.msg).sendWordsChapterContentKeyAndMessagLastOLdWord(content,chapter,word,answer,counter,length,section,page,link) 
                                    else:
                                        self.obj_KNM.Start(self.id,self.firstName,self.msg).sendKeyAndMessageFNVAUINakhostin()


                                # if userIdentify is True:

                                # else:
                                #     self.obj_KNM.Start(self.id,self.firstName,self.msg).sendKeyAndMessageFNVAUIselected()
                            if self.msg == Btn().beforeWordChapNS:
                                if userIdentify is True:
                                        self.obj_DbC.Counter(self.id).subtractOneToCounter()
                                        # self.obj_Counter.subtractOneToCounter()
                                        content,chapter,word,answer,counter,length,section,page,link = self.obj_DbC.Review(self.id).reviewChapterContentWordsNDetails()
                                        counterIF = self.obj_DbC.Counter(self.id).getCounter()+1
                                        lengthIF = len(self.obj_DbC.Review(self.id).getReviewWords())
                                        # print(f"lengthIF = {lengthIF}")
                                        if counterIF == 1:
                                            self.obj_KNM.MorureVazhehhayeGozashteh(self.id,self.firstName,self.msg).sendWordsChapterContentKeyAndMessageFirstOLdWord(content,chapter,word,answer,counter,length,section,page,link)
                                        elif counterIF != 1:
                                            self.obj_KNM.MorureVazhehhayeGozashteh(self.id,self.firstName,self.msg).sendWordsChapterContentKeyAndMessagMiddleOLdWord(content,chapter,word,answer,counter,length,section,page,link)
                                else:
                                    self.obj_KNM.Start(self.id,self.firstName,self.msg).sendKeyAndMessageFNVAUINakhostin()


                            #🔭
                            #در فهرست آغازین و اصلی .....#Btn().reviewWords 
                            if self.msg == Btn().leitnerBoxParts:
                                if userIdentify is True:
                                            ##############
                                        self.obj_DbC.Counter(self.id).putZeroToCounter()
                                        # self.obj_Counter.putZeroToCounter()
                                        words = self.obj_DbC.Review(self.id).sortSectionBase()
                                        # words = self.obj_Vazhegan.getAllWordsSection()

                                        # print(f"words = {words}")
                                        self.obj_DbC.Review(self.id).saveReviewWords(words)
                                        try:
                                            way,counter,length,section,word,page,content,chapter,link = self.obj_DbC.Review(self.id).reviewBakhshhaWordsNDetails()
                                            standardizedWord = self.obj_DbC.Vazhegan(self.id).standardizeWordReview(word,self.msg)
                                            wordDetails = MNV(self.firstName).leitnerBoxrRev(content,chapter,standardizedWord,counter,length,section,page,link)
                                            
                                            lengthIF = len(self.obj_DbC.Review(self.id).getReviewWords())
                                            lBWCB = [BtnS().deutschLeitBPCB,BtnS().englishLeitBPCB,BtnS().synonymLeitBPCB,BtnS().persianEnLeitBPCB]     
                                            if lengthIF == 1:
                                                self.obj_KNM.Inline(self.id,self.firstName,self.msg).reviewOne(lBWCB,way,length,wordDetails,self.msg)
                                            else:
                                                self.obj_KNM.Inline(self.id,self.firstName,self.msg).reviewMoreThanOne(counter,lBWCB,way,length,wordDetails,self.msg)
                                            counterIF = self.obj_DbC.Counter(self.id).getCounter()
                                            # print(f"counterIF = {counterIF}")
                                            # here
                                        except:
                                            self.obj_KNM.MorureVazhehhayeGozashteh(self.id,self.firstName,self.msg).sendWeakWordsKeyAndMessageNoWordOtherReview()

                                        ###############
                                else:
                                    self.obj_KNM.Start(self.id,self.firstName,self.msg).sendKeyAndMessageFNVAUINakhostin()

                                # if userIdentify is True:

                                # else:
                                #     self.obj_KNM.Start(self.id,self.firstName,self.msg).sendKeyAndMessageFNVAUIselected()

                            if self.msg == Btn().nextWordLeitBP:
                                if userIdentify is True:
                                        #if one more is not last
                                        if self.obj_DbC.Counter(self.id).getCounter()+1 != len(self.obj_DbC.Review(self.id).getReviewWords()):
                                            self.obj_DbC.Counter(self.id).addOneToCounter()
                                        # self.obj_Counter.addOneToCounter()
                                        ###
                                        counterIF = self.obj_DbC.Counter(self.id).getCounter()+1
                                        # print(f"counterIF = {counterIF}")
                                        lengthIF = len(self.obj_DbC.Review(self.id).getReviewWords())
                                        # print(f"lengthIF = {lengthIF}")
                                        if counterIF>lengthIF:
                                            self.obj_DbC.Counter(self.id).putValueToCounter(length-1)
                                            # self.obj_Counter.putValueToCounter(lengthIF-1)
                                        #هنوز واژه در آراینه داریم و آخری نیست
                                        if counterIF != lengthIF:
                                            counter,length,section,word,answer,page,content,chapter,link = self.obj_DbC.Review(self.id).reviewBakhshhaWordsNDetails()
                                            self.obj_KNM.MorureVazhehhayeGozashteh(self.id,self.firstName,self.msg).sendBakhshhaKeyAndMessageMiddleWord(counter,length,section,word,answer,page,content,chapter,link)
                                        ###
                                        elif counterIF == lengthIF:
                                            counter,length,section,word,answer,page,content,chapter,link = self.obj_DbC.Review(self.id).reviewBakhshhaWordsNDetails()
                                            self.obj_KNM.MorureVazhehhayeGozashteh(self.id,self.firstName,self.msg).sendBakhshhaKeyAndMessageLastWord(counter,length,section,word,answer,page,content,chapter,link)    
                                else:
                                        self.obj_KNM.Start(self.id,self.firstName,self.msg).sendKeyAndMessageFNVAUINakhostin()




                            if self.msg == Btn().beforeWordLeitBP:
                                    if userIdentify is True:
                                            self.obj_DbC.Counter(self.id).subtractOneToCounter()
                                            # self.obj_Counter.subtractOneToCounter()
                                            counter,length,section,word,answer,page,content,chapter,link = self.obj_DbC.Review(self.id).reviewBakhshhaWordsNDetails()
                                            counterIF = self.obj_DbC.Counter(self.id).getCounter()+1
                                            lengthIF = len(self.obj_DbC.Review(self.id).getReviewWords())
                                            # print(f"lengthIF = {lengthIF}")
                                            if counterIF == 1:
                                                self.obj_KNM.MorureVazhehhayeGozashteh(self.id,self.firstName,self.msg).sendBakhshhaKeyAndMessageFirstWord(counter,length,section,word,answer,page,content,chapter,link)
                                            elif counterIF != 1:
                                                self.obj_KNM.MorureVazhehhayeGozashteh(self.id,self.firstName,self.msg).sendBakhshhaKeyAndMessageMiddleWord(counter,length,section,word,answer,page,content,chapter,link)
                                    else:
                                        self.obj_KNM.Start(self.id,self.firstName,self.msg).sendKeyAndMessageFNVAUINakhostin()




                            #🔬    
                            #در فهرست آغازین و اصلی .....#Btn().reviewWords 
                            if self.msg == Btn().weakWords:

                                        if userIdentify is True:    

                                                        ##############
                                                self.obj_DbC.Counter(self.id).putZeroToCounter()
                                                
                                                words = self.obj_DbC.Review(self.id).weakWordsNDuraionSorted()
                                                # print(f"words = {words}")
                                                if words != False:

                                                    self.obj_DbC.Review(self.id).saveReviewWords(words)
                                                    ###
                                                    way,durationDays,counter,length,section,word,content,chapter,page,link = self.obj_DbC.Review(self.id).reviewWeakWordsNDetails()
                                                    standardizedWord = self.obj_DbC.Vazhegan(self.id).standardizeWordReview(word,self.msg)
                                                    wordDetails = MNV(self.firstName).weakWordsRev(durationDays,counter,length,section,standardizedWord,content,chapter,page,link)

                                    
                                                    lengthIF = len(self.obj_DbC.Review(self.id).getReviewWords())
                                                    wWCB = [BtnS().deutschWWCB,BtnS().englishWWCB,BtnS().synonymWWCB,BtnS().persianEnWWCB]                                        
                                                    if lengthIF == 1:
                                                        self.obj_KNM.Inline(self.id,self.firstName,self.msg).reviewOne(wWCB,way,length,wordDetails,self.msg)
                                                    else:
                                                        self.obj_KNM.Inline(self.id,self.firstName,self.msg).reviewMoreThanOne(counter,wWCB,way,length,wordDetails,self.msg)


                                                    counterIF = self.obj_DbC.Counter(self.id).getCounter()
                                                    # print(f"counterIF = {counterIF}")

                                                    ### 
                                                    
                                                
                                                else:
                                                    self.obj_KNM.MorureVazhehhayeGozashteh(self.id,self.firstName,self.msg).sendWeakWordsKeyAndMessageNoWord()
                                                ###############
                                        else:
                                                self.obj_KNM.Start(self.id,self.firstName,self.msg).sendKeyAndMessageFNVAUINakhostin()



                            if self.msg == Btn().nextWordWW:
                                    if userIdentify is True:
                                            ###
                                            #if one more is not last
                                            if self.obj_DbC.Counter(self.id).getCounter()+1 != len(self.obj_DbC.Review(self.id).getReviewWords()):
                                                self.obj_DbC.Counter(self.id).addOneToCounter()
                                            # self.obj_Counter.addOneToCounter()
                                            ###
                                            counterIF = self.obj_DbC.Counter(self.id).getCounter()+1
                                            # print(f"counterIF = {counterIF}")
                                            lengthIF = len(self.obj_DbC.Review(self.id).getReviewWords())
                                            # print(f"lengthIF = {lengthIF}")
                                            if counterIF>lengthIF:
                                                self.obj_DbC.Counter(self.id).putValueToCounter(lengthIF-1)
                                                # self.obj_Counter.putValueToCounter(lengthIF-1)
                                            #هنوز واژه در آرایه داریم و آخری نیست
                                            if counterIF != lengthIF:
                                                durationDays,counter,length,section,word,answer,content,chapter,page,link = self.obj_DbC.Review(self.id).reviewWeakWordsNDetails()
                                                self.obj_KNM.MorureVazhehhayeGozashteh(self.id,self.firstName,self.msg).sendWeakWordsKeyAndMessagMiddleOLdWord(durationDays,counter,length,section,word,answer,content,chapter,page,link)
                                            ###
                                            elif counterIF == lengthIF:
                                                durationDays,counter,length,section,word,answer,content,chapter,page,link = self.obj_DbC.Review(self.id).reviewWeakWordsNDetails()
                                                self.obj_KNM.MorureVazhehhayeGozashteh(self.id,self.firstName,self.msg).sendWeakWordsKeyAndMessagLastOLdWord(durationDays,counter,length,section,word,answer,content,chapter,page,link) 
                                            ###
                                    else:
                                        self.obj_KNM.Start(self.id,self.firstName,self.msg).sendKeyAndMessageFNVAUINakhostin()



                                

                            if self.msg == Btn().beforeWordWW:
                                if userIdentify is True:    
                                            ###
                                            self.obj_DbC.Counter(self.id).subtractOneToCounter()
                                            # self.obj_Counter.subtractOneToCounter()
                                            durationDays,counter,length,section,word,answer,content,chapter,page,link = self.obj_DbC.Review(self.id).reviewWeakWordsNDetails()
                                            counterIF = self.obj_DbC.Counter(self.id).getCounter()+1
                                            lengthIF = len(self.obj_DbC.Review(self.id).getReviewWords())
                                            # print(f"lengthIF = {lengthIF}")
                                            if counterIF == 1:
                                                self.obj_KNM.MorureVazhehhayeGozashteh(self.id,self.firstName,self.msg).sendWeakWordsKeyAndMessageFirstOLdWord(durationDays,counter,length,section,word,answer,content,chapter,page,link)
                                            elif counterIF != 1:
                                                self.obj_KNM.MorureVazhehhayeGozashteh(self.id,self.firstName,self.msg).sendWeakWordsKeyAndMessagMiddleOLdWord(durationDays,counter,length,section,word,answer,content,chapter,page,link)
                                else:
                                            self.obj_KNM.Start(self.id,self.firstName,self.msg).sendKeyAndMessageFNVAUINakhostin()


                            #در فهرست آغازین و اصلی 
                            if self.msg == Btn().wayEdit:    
                                    if userIdentify is True:
                                        way = self.obj_DbC.RaveshYadgiri(self.id,self.msg).getWay()
                                        self.obj_KNM.VirayeshRavesh(self.id,self.firstName,self.msg).wayMenu(way)
                                        # self.obj_KNM.VirayeshRavesh(self.id,self.firstName,self.msg).send357KeyAndMessageDESP()
                                    else:
                                        self.obj_KNM.Start(self.id,self.firstName,self.msg).sendKeyAndMessageFNVAUINakhostin()
                                      
                            ##در فهرست آغازین و اصلی 
                            if self.msg ==BtnS().persian or self.msg == BtnS().deutsch or self.msg ==BtnS().english or self.msg ==BtnS().synonym:
                                    if userIdentify is True:
                                    # ذخیره کردن به صورت موقت 
                                            withoutEmoj = ""
                                            dictMsg ={BtnS().persian:"persian", BtnS().deutsch:"deutsch",BtnS().english:"english",BtnS().synonym:"synonym"}
                                            for field,value in dictMsg.items():
                                                if self.msg == field: 
                                                    withoutEmoj = value
                                            self.obj_DbC.RaveshYadgiri(self.id,withoutEmoj).saveTemportyWay() 
                                            #درصورت یکسان بودن با روشی که پیش از این انتخاب کرده بود
                                            way = self.obj_DbC.RaveshYadgiri(self.id,self.msg).getWay()
                                            #planB
                                            
                                            # if withoutEmoj in way :
                                            #planA
                                            if withoutEmoj == way:
                                                self.obj_KNM.VirayeshRavesh(self.id,self.firstName,self.msg).sendDESPAllSameKeyAndMessageFAVA()
                                                # print("same")
                                            else:
                                                self.obj_KNM.VirayeshRavesh(self.id,self.firstName,self.msg).sendDESPAllKeyAndMessageYesNo(way)
                                    else:
                                            self.obj_KNM.Start(self.id,self.firstName,self.msg).sendKeyAndMessageFNVAUINakhostin()
                                
                            
                            
                            #در فهرست آغازین و اصلی .....#Btn().wayEdit
                            if self.msg == Btn().yesDot :
                                if userIdentify is True:
                                        tempWay = self.obj_DbC.RaveshYadgiri(self.id,self.msg).getTemporaryWay()  
                                        self.obj_DbC.RaveshYadgiri(self.id,self.msg).saveWayByTemporary()
                                        # حذف تمامی سکشن های مرتبط 
                                        self.obj_DbC.IdentifyWordsSection(self.id,self.msg).deleteAllSections()  
                                        self.obj_KNM.VirayeshRavesh(self.id,self.firstName,tempWay).sendBaleKeyAndMessageFAVA()
                                else:
                                    self.obj_KNM.Start(self.id,self.firstName,self.msg).sendKeyAndMessageFNVAUINakhostin() 
                            elif self.msg == Btn().noDot:
                                if userIdentify is True:
                                        self.obj_KNM.VirayeshRavesh(self.id,self.firstName,self.msg).sendKheyrKeyAndMessageFAVA()
                                else:
                                    self.obj_KNM.Start(self.id,self.firstName,self.msg).sendKeyAndMessageFNVAUINakhostin()        

                            



                            #در فهرست آغازین و اصلی 
                            if self.msg ==Btn().wordsNum:
                                if userIdentify is True:
                                    # self.obj_VirayeshShomarVazheha.sendVShVMessage357()
                                    self.obj_KNM.VirayeshShomarVazheha(self.id,self.firstName,self.msg).sendVShVMessage357()
                                else:
                                    self.obj_KNM.Start(self.id,self.firstName,self.msg).sendKeyAndMessageFNVAUINakhostin()

                            #در فهرست آغازین و اصلی .....#Btn().wordsNum
                            if self.msg == BtnS().one or self.msg == BtnS().two or self.msg == BtnS().three:
                                if userIdentify is True:
                                    withoutEmoj = int(self.msg.strip("-"))
                                    self.obj_DbC.ShomarVazhgan(self.id).saveWordNum(withoutEmoj)   
                                    self.obj_KNM.VirayeshShomarVazheha(self.id,self.firstName,self.msg).send357AllVMessageFAVA()
                                else:
                                    self.obj_KNM.Start(self.id,self.firstName,self.msg).sendKeyAndMessageFNVAUINakhostin()



                            #در فهرست آغازین و اصلی 
                            if self.msg == Btn().timeLearnEdit:
                                    if userIdentify is True:
                                            self.obj_KNM.VireyeshZamanYadgiriRuzaneh(self.id,self.firstName,self.msg).sendVZYRVMessage1_23()
                                    else:
                                            self.obj_KNM.Start(self.id,self.firstName,self.msg).sendKeyAndMessageFNVAUINakhostin()

                            #در فهرست آغازین و اصلی .....#Btn().timeLearnEdit
                            if self.msg == BtnS().clock1 or self.msg == BtnS().clock2 or self.msg == BtnS().clock3 or self.msg == BtnS().clock4 or self.msg == BtnS().clock5 or self.msg == BtnS().clock6 or self.msg == BtnS().clock7 or self.msg == BtnS().clock8 or self.msg == BtnS().clock9 or self.msg == BtnS().clock10 or self.msg == BtnS().clock11 or self.msg == BtnS().clock12 or self.msg == BtnS().clock13 or self.msg == BtnS().clock14 or self.msg == BtnS().clock15 or self.msg == BtnS().clock16 or self.msg == BtnS().clock17 or self.msg == BtnS().clock18 or self.msg == BtnS().clock19 or self.msg == BtnS().clock20 or self.msg == BtnS().clock21 or self.msg == BtnS().clock22 or self.msg == BtnS().clock23:
                                    if userIdentify is True:
                                        dictMsg ={BtnS().clock1:1,BtnS().clock2:2, BtnS().clock3: 3,BtnS().clock4:4,BtnS().clock5:5,BtnS().clock6:6,BtnS().clock7:7, BtnS().clock8: 8,BtnS().clock9:9,BtnS().clock10:10,BtnS().clock11:11,BtnS().clock12:12,BtnS().clock13:13,BtnS().clock14:14,BtnS().clock15:15,BtnS().clock16:16,BtnS().clock17:17,BtnS().clock18:18,BtnS().clock19:19,BtnS().clock20:20,BtnS().clock21:21,BtnS().clock22:22,BtnS().clock23:23}
                                        for field,value in dictMsg.items():
                                            if self.msg == field: 
                                                pureHour = value
                                        # arr = self.msg.split(" ")
                                        # pureHour = int(arr[0])
                                        # print(pureHour)

                                        tomorrowNextTraining = self.obj_DbC.DateArrange().getTomorrowNextTraining(self.id)
                                        hourTraining = int(tomorrowNextTraining.strftime("%H"))
                                        # print(f"hourTraining = {hourTraining}")       
                                        #########

                                        hourMin = tomorrowNextTraining.strftime("%H:%M")
                                        #گرفتن سال ، ماه نویسه ای ، روز
                                        # monthAlpha,year,month,day,monthAlphaFinglish,weekDayPer,weekDayFinglish
                                        monthAlpha,year,_,day,_,_,_ = self.obj_DbC.DateArrange(self.id).convertToKhorshidi(tomorrowNextTraining)
                                        # گرفتن نام روز در هفته به پارسی
                                        weekDay = self.obj_DbC.DateArrange(self.id).getWeekDay(tomorrowNextTraining)
                                        ########
                                        #پیام در صورت تکراری بودن ساعت و زمان داده شده
                                        if pureHour == hourTraining:
                                            self.obj_KNM.VireyeshZamanYadgiriRuzaneh(self.id,self.firstName,self.msg).sendYesMessageSameFAVA(year,monthAlpha,day,weekDay,hourMin)
                                        else:
                                            self.obj_DbC.DateArrange(self.id).saveTemporaryNextTrainingsHour(pureHour)
                                            askedNextTraining =  self.obj_DbC.DateArrange(self.id).askedNextTraining(pureHour)
                                            askedHourMin = askedNextTraining.strftime("%H:%M")
                                            #گرفتن سال ، ماه نویسه ای ، روز
                                            # monthAlpha,year,month,day,monthAlphaFinglish,weekDayPer,weekDayFinglish
                                            askedMonthAlpha,askedYear,_,askedDay,_,_,_ = self.obj_DbC.DateArrange(self.id).convertToKhorshidi(askedNextTraining)
                                            # گرفتن نام روز در هفته به پارسی
                                            askedWeekDay = self.obj_DbC.DateArrange(self.id).getWeekDay(askedNextTraining)

                                            self.obj_KNM.VireyeshZamanYadgiriRuzaneh(self.id,self.firstName,self.msg).send1_23MessageYesNo(year,monthAlpha,day,weekDay,hourMin,askedYear,askedMonthAlpha,askedDay,askedWeekDay,askedHourMin)
                                    else:
                                        self.obj_KNM.Start(self.id,self.firstName,self.msg).sendKeyAndMessageFNVAUINakhostin()




                            
                            #در فهرست آغازین و اصلی .....#1..23#Btn().timeLearnEdit
                            if self.msg == Btn().yesDash :


                                if userIdentify is True:
                                    temp = self.obj_DbC.DateArrange(self.id).getTemporaryNextTrainingsHour()
                                    # print(f"temp = {temp}")
                                    # self.obj_DbC.DateArrange(self.id).saveNextTrainingsHourbyTemp(temp)
                                    self.obj_DbC.DateArrange(self.id).checkIsValue24(temp)
                                    tomorrowNextTraining =self.obj_DbC.DateArrange().getTomorrowNextTraining(self.id)

                                    hourMin = tomorrowNextTraining.strftime("%H:%M")
                                    #گرفتن سال ، ماهنویسه ای ، روز
                                    # monthAlpha,year,month,day,monthAlphaFinglish,weekDayPer,weekDayFinglish
                                    monthAlpha,year,_,day,_,_,_ = self.obj_DbC.DateArrange(self.id).convertToKhorshidi(tomorrowNextTraining) 
                                    # گرفتن نام روز در هفته به پارسی
                                    weekDay = self.obj_DbC.DateArrange(self.id).getWeekDay(tomorrowNextTraining)
                                    self.obj_KNM.VireyeshZamanYadgiriRuzaneh(self.id,self.firstName).sendYesMessageFAVA(year,monthAlpha,day,weekDay,hourMin)

                                else:
                                    self.obj_KNM.Start(self.id,self.firstName,self.msg).sendKeyAndMessageFNVAUINakhostin()

                            elif self.msg == Btn().noDash:
                                if userIdentify is True:
                                    self.obj_KNM.VireyeshZamanYadgiriRuzaneh(self.id,self.firstName,self.msg).sendNoMessageFAVA()
                                else:
                                    self.obj_KNM.Start(self.id,self.firstName,self.msg).sendKeyAndMessageFNVAUINakhostin()

                            #در فهرست آغازین و اصلی        
                            if self.msg == Btn().reportActivity:
                                if userIdentify is True:
                                    self.obj_KNM.BarayandVaFarjam(self.id,self.firstName,self.msg).sendBVFMessageReports()
                                    # self.obj_bot.sendMessage(self.id,"test","none",self.reportKey)
                                else:
                                    self.obj_KNM.Start(self.id,self.firstName,self.msg).sendKeyAndMessageFNVAUINakhostin()    
                            #در فهرست آغازین و اصلی .....#"برآیند و فرجام" 
                            if self.msg == Btn().reportWordsPartions:
                                    if userIdentify is True:
                                        ############
                                        num = len(self.obj_DbC.Vazhegan(self.id).getAllWordsSection())
                                        msg2 = self.obj_DbC.Report(self.id).reportWordsSectionsPercentage()
                                        self.obj_KNM.BarayandVaFarjam(self.id,self.firstName,self.msg).sendReportAllWordsMessageBBFA(num,msg2)
                                    else:
                                        self.obj_KNM.Start(self.id,self.firstName,self.msg).sendKeyAndMessageFNVAUINakhostin() 



                            #در فهرست آغازین و اصلی .....#"برآیند و فرجام" 
                            if self.msg == Btn().reportWeakWords:
                                if userIdentify is True:
                                    ############
                                    #گزارش بخش ها ،روزها،واژه

                                    wWDS = self.obj_DbC.Report(self.id).weakWordDuraionSection()
                                    

                                    #درصد،گراف،بخش
                                    wWPGS = self.obj_DbC.Report(self.id).weakWordsPercentageGraphSection()
                                    # فرستادن کیبورد و پیام
                                    self.obj_KNM.BarayandVaFarjam(self.id,self.firstName,self.msg).sendReportWeakWordMessageBBFA(wWDS,wWPGS)
                                    ###########
                                else:
                                    self.obj_KNM.Start(self.id,self.firstName,self.msg).sendKeyAndMessageFNVAUINakhostin()




                            #در فهرست آغازین و اصلی 
                            if self.msg ==Btn().uILangNKeyEdit:
                                if userIdentify is True:
                                    self.obj_KNM.DegarsaniZaban2(self.id,self.firstName,self.msg).sendKeyAndMessageUI2() 
                                    #  self.obj_DegarsaniZaban2.sendKeyAndMessageUI2() 
                                else:
                                    self.obj_KNM.Start(self.id,self.firstName,self.msg).sendKeyAndMessageFNVAUINakhostin()





                            #حساب کاربری🙂
                            if self.msg == Btn().account:
                                if userIdentify is True:
                                    outpuTodayDateNTime,output = self.obj_DbC.Report(self.id).getAccoutDetails()

                                    self.obj_KNM.AghazYadgiriVazhehayeKetab(self.id,self.firstName,self.msg).sendAccountInfoKeyAndMessageBBFA(outpuTodayDateNTime,output)
                                
                                else:
                                    self.obj_KNM.AdminStart(self.id,self.firstName,self.msg).sendKeyAndMessageFNVAUINakhostin()
                            #در فهرست آغازین و اصلی 
                            if self.msg == self.obj_Btn.aboutBot:
                                if userIdentify is True:
                                    self.obj_KNM.DarbarehRobat2(self.id,self.firstName,self.msg).sendKeyAndMessageDarbarehRobat2()
                                else:
                                    self.obj_KNM.Start(self.id,self.firstName,self.msg).sendKeyAndMessageFNVAUINakhostin()    
                            #در فهرست آغازین و اصلی 
                            if self.msg == Btn().deleteBot:
                                if userIdentify is True:
                                    self.obj_KNM.HazfRobot(self.id,self.firstName,self.msg).sendHRKeyAndMessageYesNo()     
                                else:
                                    self.obj_KNM.Start(self.id,self.firstName,self.msg).sendKeyAndMessageFNVAUINakhostin()



                            #در فهرست آغازین و اصلی .....#Btn().deleteBot
                            if self.msg == Btn().yesDelete :
                                if userIdentify is True:
                                        # حذف تمامی سکشن های مرتبط 
                                        self.obj_DbC.IdentifyWordsSection(self.id,self.msg).deleteAllSections() 
                                        # حذف ربات 🗑
                                        self.obj_DbC.DeleteBot(self.id).deleteBot()
                                        self.obj_KNM.HazfRobot(self.id,self.firstName,self.msg).sendYesKeyAndMessageFNVA()
                                
                                else:
                                    self.obj_KNM.Start(self.id,self.firstName,self.msg).sendKeyAndMessageFNVAUINakhostin()
                            
                            elif self.msg == Btn().no:
                                if userIdentify is True:
                                        self.obj_KNM.AghazYadgiriVazhehayeKetab(self.id,self.firstName,self.msg).sendKeyAndMessageFAVA()
                                else:
                                    self.obj_KNM.Start(self.id,self.firstName,self.msg).sendKeyAndMessageFNVAUINakhostin()    
                                    
                                                            #در فهرست آغازین و اصلی 
                            if self.msg == Btn().getBack:
                                if userIdentify is True:    
                                    self.obj_KNM.AghazYadgiriVazhehayeKetab(self.id,self.firstName,self.msg).sendKeyAndMessageFAVA()
                                else:
                                    self.obj_KNM.Start(self.id,self.firstName,self.msg).sendKeyAndMessageFNVAUINakhostin()
                            
                            #FIXME self.msg == Btn().opinion
                            if self.msg == Btn().opinion:
                                if userIdentify is True: 
                                    # self.obj_DbC.Msg().opinion(self.msg) 
                                    self.obj_KNM.DarbarehRobat2(self.id,self.firstName,self.msg).sendKeyAndMessageSendingSugession()
                                    pass
                                else:
                                    self.obj_KNM.Start(self.id,self.firstName,self.msg).sendKeyAndMessageFNVAUINakhostin()

                            #FIXME  self.obj_DbC.Msg(self.id,self.msg).isSecondTodEndMsg() is True   
                            if self.obj_DbC.Msg(self.id,self.msg).isSecondTodEndMsg() is True:
                                if userIdentify is True: 
                                    output,opId = self.obj_DbC.Msg(self.id,self.msg).saveOpinion(self.msg)
                                    #در صورتی که متن وارد شده باشد و برای فرستادن رسید از این ایف استفاده می شود
                                    if output is False and opId == "outOfRange":
                                        self.obj_KNM.DarbarehRobat2(self.id,self.firstName,self.msg).sendKeyAndMessageOutOfRangeMsg()
                                    #درصورت فرستادن متن سالم و درست
                                    elif output is True:
                                        self.obj_KNM.DarbarehRobat2(self.id,self.firstName,self.msg).sendKeyAndMessageDeliverOpinion(opId)
                                    #در صورت زدن دکمه بازگشت به فهرست آغازین
                                    elif output is False and opId == "getBack":
                                        # self.obj_KNM.AghazYadgiriVazhehayeKetab(self.id,self.firstName,self.msg).sendKeyAndMessageFAVA()
                                        pass
                                    #درصورت استفاده از کیبورد ربات به غیر از بازگشت به فهرست آغازین
                                    elif output is False and opId == "botKeyboard":
                                        
                                        self.obj_KNM.DarbarehRobat2(self.id,self.firstName,self.msg).sendKeyAndMessageUsingBotKeys()
                                        
                                        
                                else:
                                    self.obj_KNM.Start(self.id,self.firstName,self.msg).sendKeyAndMessageFNVAUINakhostin()
                                
                except:
                    print("we go issue to send message")
        except:
            print("userIdentify or channelmemberVerification problem")

    def dataAnalizer(self):
        
        try:
            self.obj_DbC.Msg(self.id).addMsgs(self.data)
            # print(f'self.data = {self.data}')
            if self.data ==BtnS().wordCB:
                            self.obj_DbC.Vazhegan(self.id,self.msg).mixWords()
                            way,wKind,numW,numAll,word,content,chapter,wordsPage,linkWord = self.obj_DbC.Vazhegan(self.id,self.msg).wordNdetails()
                            reportNum = self.obj_DbC.Report(self.id).getReportNum()
                            standardizedWord = self.obj_DbC.Vazhegan(self.id).standardizeWordReview(word,self.data)
                            # wayPer = way
                            # print(way)
                            if   5<reportNum:

                                wordCard = MNV(self.firstName).wordCard(wKind,numW,numAll,standardizedWord,content,chapter,wordsPage,linkWord)
                                self.obj_KNM.Inline(self.id,self.msgId,self.firstName).dataWordQuery(way,wordCard)
                           
                            else:
                                # print(way)
                                wordCardWithGuide = MNV(self.firstName).wordCardWithGuide(way,wKind,numW,numAll,standardizedWord,content,chapter,wordsPage,linkWord)
                                # print(way)
                                self.obj_KNM.Inline(self.id,self.msgId,self.firstName).dataWordWithGuideQuery(way,wordCardWithGuide)

            if self.data == BtnS().synonymText or self.data == BtnS().deutschText or self.data == BtnS().englishText or self.data == BtnS().persianTextEn:

                    # if userIdentify is True:
                            
                    #                 if self.obj_DbC.DateArrange().getRightWrongLampFlag(self.id) is True:

                                            #get way 
                                            way = self.obj_DbC.RaveshYadgiri(self.id).getWay()
                                            print(f"self.id = {self.id}\nway = {way}")
                                            # way = self.data
                                            #planB
                                            
                                            # way = self.obj_DbC.RaveshYadgiri(self.id).wayOrWaysString(way)
                                            #planA
                                            #get icon
                                            # FIXME icon
                                            icon = self.obj_DbC.RaveshYadgiri(self.id).getIconBook(self.data)
                                            #get word
                                            todayWords = self.obj_DbC.Vazhegan(self.id).getTodayWords()
                                            # print(f"todayWords = {todayWords}")
                                            word =  self.obj_DbC.Vazhegan(self.id).getOneRightWord(todayWords) 
                                            # print(f"word = {word}")
                                            #save answer to todayWordsNAnswer
                                            answerLink = self.obj_DbC.Vazhegan(self.id).audioAnswer(word,self.data)
                                            # print(f'answerLink = {answerLink}')
                                            input = self.obj_DbC.Vazhegan(self.id).getOneAnswerPure(word,self.data)
                                            self.obj_DbC.Vazhegan(self.id).updateValueKeyAnswer(input)
                                            # 
                                            # get one answer
                                            answer = self.obj_DbC.Vazhegan(self.id).getOneAnswer(input)
                                            
                                            reportNum = self.obj_DbC.Report(self.id).getReportNum()
                                            #FIXME standardizedAnswer
                                            standardizedAnswer = self.obj_DbC.Vazhegan(self.id).standardizeAnswer(self.data,answer,reportNum)
                                            #FIXME reportnum doesn't work

                                            print(f"icon = {icon}\n todayWords ={todayWords}\nword = {word}\nanswerLink = {answerLink}\ninput = {input}\nanswer = {answer}\nreportNum = {reportNum}\nstandardizedAnswer = {standardizedAnswer}")
                                            if   5<reportNum:
                                                #send keyboar and message
                                                answerCard = MNV(self.firstName).answerCard(self.data,icon,standardizedAnswer,answerLink)
                                                self.obj_KNM.Inline(self.id,self.msgId,self.firstName).answerWord(self.data,way,answerCard)
                                            else:
                                                answerWordWithGuide = MNV(self.firstName).answerCardWithGuide(self.data,icon,standardizedAnswer,answerLink)    
                                                self.obj_KNM.Inline(self.id,self.msgId,self.firstName).answerWordWithGuide(self.data,way,answerWordWithGuide)

            if self.data == BtnS().crossCheckCB or self.data == BtnS().checkCB:
                            # if userIdentify is True:
                                    # if self.obj_DbC.DateArrange().getRightWrongLampFlag(self.id) is True:
                                            msgArray = self.obj_DbC.Msg().getMessagesToday(self.id)
                                            # msgArray = self.obj_DbC.Msg(self.id,self.msg).getMsgArray()
                                            lengthMsgArray = len(msgArray)
                                            counter = self.obj_DbC.Counter(self.id).getCounter()
                                            #درصورت اسپم بودن و تکرار ی و  در عین حال آخرین  واژه هم بودن
                                            if (msgArray[lengthMsgArray-1] == msgArray[lengthMsgArray-2] or msgArray[lengthMsgArray-2] == BtnS().check or msgArray[lengthMsgArray-2] == BtnS().crossCheck) and  self.obj_DbC.Counter(self.id).lastWordVerification() == False:
                                                self.obj_KNM.ErrorMsgs(self.id,self.firstName,self.msg).sendWarningKeyAndMessageBBFA()
                                            #شرط تکراری نبودن
                                            elif (msgArray[lengthMsgArray-1] == msgArray[lengthMsgArray-2] or msgArray[lengthMsgArray-2] == BtnS().check or msgArray[lengthMsgArray-2] == BtnS().crossCheck) and counter == 0:
                                                self.obj_KNM.ErrorMsgs(self.id,self.firstName,self.msg).sendWarningKeyAndMessageBBFA()
                                            elif  msgArray[lengthMsgArray-1] == msgArray[lengthMsgArray-2] or msgArray[lengthMsgArray-2] == BtnS().check or msgArray[lengthMsgArray-2] == BtnS().crossCheck:
                                                pass
                                                # self.obj_KNM.AghazYadgiriVazhehayeKetab(self.id,self.firstName,self.msg).sendWarningKeyAndMessageLamp() 
                                                
                                            #آزمون آخرین بودن یا نبودن واژه 
                                            elif self.obj_DbC.Counter(self.id).lastWordVerification() == True:
                                                input = bool
                                                if self.data == BtnS().checkCB  :
                                                    input = True
                                                elif self.data == BtnS().crossCheckCB :
                                                    input = False
                                                self.obj_DbC.Vazhegan(self.id).updateValueKey(input)
                                                self.obj_DbC.Counter(self.id).addOneToCounter()
                                                ##############
                                                if self.obj_DbC.IdentifyWordsSection(self.id,self.data).findUserNWord() == False :
                                                    if input is False:
                                                        self.obj_DbC.IdentifyWordsSection(self.id,self.data).makeWordSection(1)
                                                    elif input is True:
                                                        self.obj_DbC.IdentifyWordsSection(self.id,self.data).makeWordSection(1)
                                                        self.obj_DbC.IdentifyWordsSection(self.id,self.data).moveToNextLevel(1)
                                                elif self.obj_DbC.IdentifyWordsSection(self.id,self.data).findUserNWord() ==True:
                                                        self.obj_DbC.IdentifyWordsSection(self.id,self.data).moveToNextLevel(1)
                                                #################  report part  
                                                if self.obj_DbC.Counter(self.id).lastWordVerification() == False:    
                                                    #save last leitner values
                                                    self.obj_DbC.Report(self.id).lastLeitnerBoxStatistics(self.data)
                                                    #TODO get firstName,language,id,first,last karbar
                                                    lan = self.obj_DbC.UILanguage(self.id).getUIL()
                                                    first,last = self.obj_DbC.Report(self.id).getLeitnerBoxStatistics()
                                                    print(f"{first = } {last = } {lan = } {self.id = } {self.firstName = }")
                                                    cardNum = self.obj_DbC.ShomarVazhgan(self.id).getWordNum()

                                                    all,right,wrong,wrongWordsNpages,weekDay,day,monthAlpha,year,houNMTraining,dateGriNextTraining,wordsSectionPosition = self.obj_DbC.Report(self.id).dailyReport()
                                                    # print(self.msgId,self.id)
                                                    reportMsg = MNV(self.firstName).reportMsg(all,right,wrong,wrongWordsNpages,weekDay,day,monthAlpha,year,houNMTraining,dateGriNextTraining,wordsSectionPosition)
                                                    self.obj_KNM.Inline(self.id,self.msgId,self.firstName).report(reportMsg)

                                                    vidPNName = VS.ReleaseVideo().releaseVideo(self.id,cardNum,self.firstName,lan,first,last)
                                                    print(f"{vidPNName = }")
                                                    self.obj_KNM.Inline(self.id,self.firstName,self.msgId).sendVideoReport(vidPNName)

                                                else:
                                                   
                                                    way,wKind,numW,numAll,word,content,chapter,wordsPage,linkWord = self.obj_DbC.Vazhegan(self.id).wordNdetails()
                                                    # print(f"way = {way}")
                                                    reportNum = self.obj_DbC.Report(self.id).getReportNum()
                                                    standardizedWord = self.obj_DbC.Vazhegan(self.id).standardizeWord(word,reportNum)
                                                    if   5<reportNum:

                                                    # here 
                                                    # send message and keyboard
                                                        wordCardWithGuide = MNV(self.firstName).wordCardWithGuide(way,wKind,numW,numAll,standardizedWord,content,chapter,wordsPage,linkWord)
                                                        self.obj_KNM.Inline(self.id,self.msgId,self.firstName).dataWordQuery(way,wordCardWithGuide)
                                                   
                                                    else:
                                                        wordCard = MNV(self.firstName).wordCard(wKind,numW,numAll,standardizedWord,content,chapter,wordsPage,linkWord)
                                                        self.obj_KNM.Inline(self.id,self.msgId,self.firstName).dataWordWithGuideQuery(way,wordCard)


                                            elif self.obj_DbC.Counter(self.id).lastWordVerification() == False:
                                                self.obj_DbC.Counter(self.id).putZeroToCounter()
                                                wordCardWithGuide = MNV(self.firstName).wordCardWithGuide(way,wKind,numW,numAll,standardizedWord,content,chapter,wordsPage,linkWord)
                                                self.obj_KNM.Inline(self.id,self.msgId,self.firstName).dataWordQuery(way,wordCardWithGuide)

            if self.data == BtnS().deutschChapNSCB or self.data == BtnS().englishChapNSCB or self.data ==BtnS().synonymChapNSCB or self.data == BtnS().persianEnChapNSCB:
                        waysArray = [{BtnS().deutschChapNSCB:BtnS().deutschText},{ BtnS().englishChapNSCB:BtnS().englishText},{BtnS().synonymChapNSCB:BtnS().synonymText},{BtnS().persianEnChapNSCB:BtnS().persianTextEn}]
                        answerWay = ''
                        for z in waysArray:
                            for x,y in z.items():
                                if self.data == x:
                                    answerWay = y
                        ways,pureAnswer,counter,length,answerLink = self.obj_DbC.Review(self.id).reviewANSWERChapterContentNDetails(answerWay)
                        # reviewAnswerChapNSec(ways,counter,length,self.data)
                        icon = self.obj_DbC.RaveshYadgiri(self.id).getIconBook(answerWay)
                        standardizedAnswer = self.obj_DbC.Vazhegan(self.id).standardizeAnswer(answerWay,pureAnswer,6)
                        # standardizedAnswer = ""
                        answerOutput = MNV(self.firstName).answerCard(answerWay,icon,standardizedAnswer,answerLink)
                        chapterNSectionCB = [BtnS().deutschChapNSCB,BtnS().englishChapNSCB,BtnS().synonymChapNSCB,BtnS().persianEnChapNSCB,BtnS().wordChapNSCB]
                        self.obj_KNM.Inline(self.id,self.msgId,self.firstName).reviewAnswer(chapterNSectionCB,answerWay,ways,counter,length,answerOutput,chapterNSectionCB[4])


                                
            if self.data == Btn().nextWordChapNS or self.data == Btn().beforeWordChapNS or self.data == BtnS().wordChapNSCB:
                        counterIF = self.obj_DbC.Counter(self.id).getCounter()+1
                        lengthIF = len(self.obj_DbC.Review(self.id).getReviewWords())
                        if self.data == Btn().nextWordChapNS:
                                if self.obj_DbC.Counter(self.id).getCounter()+1 != len(self.obj_DbC.Review(self.id).getReviewWords()):
                                        self.obj_DbC.Counter(self.id).addOneToCounter()
                                if counterIF>lengthIF:
                                        self.obj_DbC.Counter(self.id).putValueToCounter(lengthIF-1)
                        elif self.data == Btn().beforeWordChapNS:
                                self.obj_DbC.Counter(self.id).subtractOneToCounter()
                        way,content,chapter,word,counter,length,section,page,link = self.obj_DbC.Review(self.id).reviewChapterContentWordsNDetails()
                        standardizedWord = self.obj_DbC.Vazhegan(self.id).standardizeWordReview(word,self.data)
                        msgCHNS = MNV(self.firstName).chapterNSectionRev(content,chapter,standardizedWord,counter,length,section,page,link)
                        waysArrayCB = [BtnS().deutschChapNSCB,BtnS().englishChapNSCB,BtnS().synonymChapNSCB,BtnS().persianEnChapNSCB]
                        if lengthIF == 1:
                                self.obj_KNM.Inline(self.id,self.msgId,self.firstName).reviewOne(waysArrayCB,way,length,msgCHNS,self.data)
                        else:
                                self.obj_KNM.Inline(self.id,self.msgId,self.firstName).reviewMoreThanOne(counter,waysArrayCB,way,length,msgCHNS,self.data)


            if self.data == BtnS().deutschLeitBPCB or self.data == BtnS().englishLeitBPCB or self.data ==BtnS().synonymLeitBPCB or self.data == BtnS().persianEnLeitBPCB:
                        # print(f"self.data = {self.data}")
                        waysArray = [{BtnS().deutschLeitBPCB:BtnS().deutschText},{ BtnS().englishLeitBPCB:BtnS().englishText},{BtnS().synonymLeitBPCB:BtnS().synonymText},{BtnS().persianEnLeitBPCB:BtnS().persianTextEn}]
                        answerWay = ''
                        for z in waysArray:
                            for x,y in z.items():
                                if self.data == x:
                                    answerWay = y
                        ways,pureAnswer,counter,length,answerLink = self.obj_DbC.Review(self.id).reviewANSWERChapterContentNDetails(answerWay)
                        # reviewAnswerChapNSec(ways,counter,length,self.data)
                        icon = self.obj_DbC.RaveshYadgiri(self.id).getIconBook(answerWay)
                        standardizedAnswer = self.obj_DbC.Vazhegan(self.id).standardizeAnswer(answerWay,pureAnswer,6)
                        # standardizedAnswer = ""
                        answerOutput = MNV(self.firstName).answerCard(answerWay,icon,standardizedAnswer,answerLink)
                        
                        leitnerBoxCB = [BtnS().deutschLeitBPCB,BtnS().englishLeitBPCB,BtnS().synonymLeitBPCB,BtnS().persianEnLeitBPCB,BtnS().wordLeitBPCB]
                        self.obj_KNM.Inline(self.id,self.msgId,self.firstName).reviewAnswer(leitnerBoxCB,answerWay,ways,counter,length,answerOutput,leitnerBoxCB[4])


            if self.data == Btn().nextWordLeitBP or self.data == Btn().beforeWordLeitBP or self.data == BtnS().wordLeitBPCB:
                        counterIF = self.obj_DbC.Counter(self.id).getCounter()+1
                        lengthIF = len(self.obj_DbC.Review(self.id).getReviewWords())
                        if self.data == Btn().nextWordLeitBP:
                                if self.obj_DbC.Counter(self.id).getCounter()+1 != len(self.obj_DbC.Review(self.id).getReviewWords()):
                                        self.obj_DbC.Counter(self.id).addOneToCounter()
                                if counterIF>lengthIF:
                                        self.obj_DbC.Counter(self.id).putValueToCounter(lengthIF-1)
                        elif self.data == Btn().beforeWordLeitBP:
                                self.obj_DbC.Counter(self.id).subtractOneToCounter()
                        way,content,chapter,word,counter,length,section,page,link = self.obj_DbC.Review(self.id).reviewChapterContentWordsNDetails()
                        standardizedWord = self.obj_DbC.Vazhegan(self.id).standardizeWordReview(word,self.data)
                        msgCHNS = MNV(self.firstName).leitnerBoxrRev(content,chapter,standardizedWord,counter,length,section,page,link)
                        waysArrayCB = [BtnS().deutschLeitBPCB,BtnS().englishLeitBPCB,BtnS().synonymLeitBPCB,BtnS().persianEnLeitBPCB]
                        if lengthIF == 1:
                                self.obj_KNM.Inline(self.id,self.msgId,self.firstName).reviewOne(waysArrayCB,way,length,msgCHNS,self.data)
                        else:
                                self.obj_KNM.Inline(self.id,self.msgId,self.firstName).reviewMoreThanOne(counter,waysArrayCB,way,length,msgCHNS,self.data)

            if self.data == BtnS().deutschWWCB or self.data == BtnS().englishWWCB or self.data ==BtnS().synonymWWCB or self.data == BtnS().persianEnWWCB:
                        waysArray = [{BtnS().deutschWWCB:BtnS().deutschText},{ BtnS().englishWWCB:BtnS().englishText},{BtnS().synonymWWCB:BtnS().synonymText},{BtnS().persianEnWWCB:BtnS().persianTextEn}]
                        answerWay = ''
                        for z in waysArray:
                            for x,y in z.items():
                                if self.data == x:
                                    answerWay = y


                        # print(answerWay)
                        #FIXME this name must be fixed reviewANSWERChapterContentNDetails
                        ways,pureAnswer,counter,length,answerLink = self.obj_DbC.Review(self.id).reviewANSWERChapterContentNDetails(answerWay)
                        # print(f"pureAnswer = {pureAnswer}")
                        # reviewAnswerChapNSec(ways,counter,length,self.data)
                        icon = self.obj_DbC.RaveshYadgiri(self.id).getIconBook(answerWay)
                        standardizedAnswer = self.obj_DbC.Vazhegan(self.id).standardizeAnswer(answerWay,pureAnswer,6)
                        # standardizedAnswer = ""
                        answerOutput = MNV(self.firstName).answerCard(answerWay,icon,standardizedAnswer,answerLink)
                        
                        weakWordCB = [BtnS().deutschWWCB,BtnS().englishWWCB,BtnS().synonymWWCB,BtnS().persianEnWWCB,BtnS().wordWWCB]
                        self.obj_KNM.Inline(self.id,self.msgId,self.firstName).reviewAnswer(weakWordCB,answerWay,ways,counter,length,answerOutput,weakWordCB[4])

            if self.data == Btn().nextWordWW or self.data == Btn().beforeWordWW or self.data == BtnS().wordWWCB:
                        counterIF = self.obj_DbC.Counter(self.id).getCounter()+1
                        lengthIF = len(self.obj_DbC.Review(self.id).getReviewWords())
                        if self.data == Btn().nextWordWW:
                                if self.obj_DbC.Counter(self.id).getCounter()+1 != len(self.obj_DbC.Review(self.id).getReviewWords()):
                                        self.obj_DbC.Counter(self.id).addOneToCounter()
                                if counterIF>lengthIF:
                                        self.obj_DbC.Counter(self.id).putValueToCounter(lengthIF-1)
                        elif self.data == Btn().beforeWordWW:
                                self.obj_DbC.Counter(self.id).subtractOneToCounter()
                        way,durationDays,counter,length,section,word,content,chapter,page,link = self.obj_DbC.Review(self.id).reviewWeakWordsNDetails()
                            ####-----####
                        standardizedWord = self.obj_DbC.Vazhegan(self.id).standardizeWordReview(word,self.data)
                        wordDetails = MNV(self.firstName).weakWordsRev(durationDays,counter,length,section,standardizedWord,content,chapter,page,link)

        
                        lengthIF = len(self.obj_DbC.Review(self.id).getReviewWords())
                        wWCB = [BtnS().deutschWWCB,BtnS().englishWWCB,BtnS().synonymWWCB,BtnS().persianEnWWCB]                                        
                        if lengthIF == 1:
                            self.obj_KNM.Inline(self.id,self.msgId,self.firstName).reviewOne(wWCB,way,length,wordDetails,self.data)
                        else:
                            self.obj_KNM.Inline(self.id,self.msgId,self.firstName).reviewMoreThanOne(counter,wWCB,way,length,wordDetails,self.data)
            
            if self.data == MNV().endReview:
                    self.obj_KNM.Inline(self.id,self.msgId,self.firstName).getBack(MNV().endReview)
            if self.data == Btn().addWay:
                    way = self.obj_DbC.RaveshYadgiri(self.id,self.msg).getWay()
                    self.obj_KNM.Inline(self.id,self.msgId,self.firstName).addWay(way)
            if self.data == Btn().subtractWay:
                    way = self.obj_DbC.RaveshYadgiri(self.id).getWay()
                    self.obj_KNM.Inline(self.id,self.msgId,self.firstName).subtractWay(way)

            if self.data == BtnS().addEnglish or self.data == BtnS().addDeutsch or self.data == BtnS().addSynonym or self.data == BtnS().addPersian:
                    addedWay = self.obj_DbC.RaveshYadgiri(self.id).addWay(self.data)
                    self.obj_KNM.Inline(self.id,self.msgId,self.firstName).addedWayBefore(addedWay)
                    
            if self.data == BtnS().subtractEnglish or self.data == BtnS().subtractDeutsch or self.data == BtnS().subtractSynonym or self.data == BtnS().subtractPersian:
                    subtractingWay = self.obj_DbC.RaveshYadgiri(self.id).subtractWay(self.data)
                    self.obj_KNM.Inline(self.id,self.msgId,self.firstName).subtractedWayBefre(subtractingWay)
            if self.data == MNV().endEditWay:
                    self.obj_KNM.Inline(self.id,self.msgId,self.firstName).getBack(MNV().endEditWay)
            if self.data == MNV().secondMenu:
                    self.obj_KNM.Inline(self.id,self.msgId,self.firstName).getBack(MNV().secondMenu)

            if self.data in Btn().changeWay:
                way = self.obj_DbC.RaveshYadgiri(self.id,self.data).getWay()
                self.obj_KNM.Inline(self.id,self.msgId,self.firstName).changeWayBefore(way)
            if self.data in BtnS().changeBtns:
                add,subtract = self.obj_DbC.RaveshYadgiri(self.id,self.data).changeWay(self.data)
                self.obj_KNM.Inline(self.id,self.msgId,self.firstName).changeWay(add,subtract)

        except:
            pass

#کلاس ادمین و سرپرست
class Admin(AnlaizeAbstract):
    def __init__(self,id,firstName,msg,callBackQuery_id,msgId,data,last_name=None,username=None):

        self.id = id
        self.msg = msg
        self.firstName=firstName
        self.last_name = last_name
        self.callBackQuery_id = callBackQuery_id  
        self.msgId = msgId
        self.data = data
        self.username = username
        #keyboard
        self.obj_KNM = Sending
        #dbContact
        self.obj_DbC= dbContact


    def msgAnlizer (self):
 

        try:    
                repeat = 0
                # self.obj_DbC.User(self.id,self.firstName,self.last_name,self.username).updateIdentity()
                userIdentify =  self.obj_DbC.User(self.id,self.firstName,self.last_name,self.username).userIdentify()
                    # افزودن پیام در چهارچوب زمان به پیام های دیرین
                self.obj_DbC.Msg(self.id).addMsgs(self.msg)
                #done must change sendWarningRepeatedKeyAndMessageToNoneUser to NoneAdmin 
                #پیشگیری از پیام تکراری
                if self.obj_DbC.Msg().isTheLastOneRepeatedMsg(self.id,"Admin") is True:
                    # type of keybaord home
                    if userIdentify is False:                  
                        self.obj_KNM.AdminErrorMsgs(self.id,self.firstName,self.msg).sendWarningRepeatedKeyAndMessageToAdminGuest() 
                        repeat = 1     
                    elif userIdentify is True:
                        self.obj_KNM.AdminErrorMsgs(self.id,self.firstName,self.msg).sendWarningRepeatedKeyAndMessageToAdmin() 
                        repeat = 1  
                        
                #FIXME need id and better to have msg
                if  self.obj_DbC.Msg(self.id,self.msg).noneKeyboardMsgs(self.msg,"Admin") and repeat == 0:
                    
                    #done پیام استفاده از کیبورد
                    if userIdentify is False:
                        
                        self.obj_KNM.AdminErrorMsgs(self.id,self.firstName,self.msg).sendWarningNoneKeyboardToAdminGuest()
                        
                    elif userIdentify is True:
                        
                        self.obj_KNM.AdminErrorMsgs(self.id,self.firstName,self.msg).sendWarningNoneKeyboardToAdmin()
                            
                elif repeat == 0  : 
                        #######################          گردانش ⚙️          ######################
                        if self.msg == BtnA().admin:
                            
                                self.obj_KNM.AdminGardanesh(self.id,self.firstName,self.msg).adminSendGMessageGPanell()  
                        
                        if self.msg == BtnA().apply:
                            # self.obj_DbC.Admin(self.id).changeAWordSection()
                            # output1 = "done"
                            # self.obj_DbC.Sections(73543260).changeWord()
                            # self.obj_DbC.Sections(73543260).changeWord2()
                            # self.obj_DbC.Sections(73543260).changeWord3()
                            # self.obj_DbC.Sections(73543260).changeWord4()
                            # self.obj_DbC.Sections(73543260).changeWord5()
                            # self.obj_DbC.Sections(73543260).changeWord6()
                            # self.obj_DbC.Sections(73543260).changeWord7()
                            # self.obj_DbC.Sections(73543260).changeWord8()
                            # self.obj_DbC.Sections(73543260).changeWord9()
                            # self.obj_DbC.Sections(73543260).changeWord10()
                            # self.obj_DbC.Sections(73543260).changeWord11()
                            # self.obj_DbC.Sections(73543260).changeWord12()
                            # self.obj_DbC.Sections(73543260).changeWordPersianMeaning()
                            # self.obj_DbC
                            # self.obj_DbC.UILanguage().erase()
                            id = 73543260
                            output2 = self.obj_DbC.Admin(self.id).afterOneMinNexTrain(id)
                            now  = datetime.datetime.now()
                            output = f"output2={output2} \nnow       = {now}"
                            self.obj_KNM.AdminGardanesh(self.id,self.firstName,self.msg).adminSendGMessageGPanellAppleyChanges(output) 
                            pass


                        if self.msg == BtnA().reportAll:
                            
                                nowDate = datetime.datetime.now()
                                #گرفتن سال ، ماه نویسه ای ، روز
                                # monthAlpha,year,month,day,monthAlphaFinglish,weekDayPer,weekDayFinglish
                                monthAlpha,year,_,day,_,_,_ = self.obj_DbC.DateArrange(self.id).convertToKhorshidi(nowDate) 
                                # print(_)
                                # day = self.obj_DbC.DateArrange(self.id).convertToKhorshidi() 
                                # گرفتن نام روز در هفته به پارسی
                                weekDay = self.obj_DbC.DateArrange(self.id).getWeekDay(nowDate)
                                guestsNum = self.obj_DbC.Admin(self.id).guestsNum()
                                usersNum = self.obj_DbC.Admin(self.id).usersNum()
                                guestInfos = self.obj_DbC.Admin(self.id).getAllGuestsInfoNguestStartDay()
                                userInfos = self.obj_DbC.Admin(self.id).getAllUsersInfoNuserStartDay()

                                self.obj_KNM.AdminGardanesh(self.id,self.firstName,self.msg).adminSendGTFaraMessageGPanel(guestsNum,usersNum,guestInfos,userInfos,monthAlpha,year,day,weekDay)

                        if self.msg == BtnA().opinionsA:
                                self.obj_KNM.AdminGardanesh(self.id,self.firstName,self.msg).adminOpinionsTypes()


                        if self.msg == BtnA().opUserBase:
                                nowDate = datetime.datetime.now()
                                # monthAlpha,year,month,day,monthAlphaFinglish,weekDayPer,weekDayFinglish
                                monthAlpha,year,_,day,_,_,_ = self.obj_DbC.DateArrange(self.id).convertToKhorshidi(nowDate) 
                                weekDay = self.obj_DbC.DateArrange(self.id).getWeekDay(nowDate)
                                guestsNum = self.obj_DbC.Admin(self.id).guestsNum()
                                usersNum = self.obj_DbC.Admin(self.id).usersNum()
                                suguestersNum,opinionsNum,opinions = self.obj_DbC.Admin(self.id).takeOpinionsBaseOnEachUser()
                                self.obj_KNM.AdminGardanesh(self.id,self.firstName,self.msg).adminSendAllOpinionUserBase(opinions,opinionsNum,suguestersNum,weekDay,day,monthAlpha,year)


                        if self.msg == BtnA().reportToday:
                                #done گزارش تکاپو اضافه کردن میهمانان به آن
                                nowtime = datetime.datetime.now()
                                #گرفتن سال ، ماه نویسه ای ، روز
                                # monthAlpha,year,month,day,monthAlphaFinglish,weekDayPer,weekDayFinglish
                                monthAlpha,year,_,day,_,_,_ = self.obj_DbC.DateArrange(self.id).convertToKhorshidi(nowtime) 
                                # print(_)
                                # day = self.obj_DbC.DateArrange(self.id).convertToKhorshidi() 
                                # گرفتن نام روز در هفته به پارسی
                                weekDay = self.obj_DbC.DateArrange(self.id).getWeekDay(nowtime)
                                # getTodayActiveUsersNum  getNumTodayAllTransactions getActiveUsersInfos
                                todayActiveUsersNum = self.obj_DbC.Admin(self.id).getTodayActiveUsersNum()
                                todayActiveGuestsNum = self.obj_DbC.Admin(self.id).getTodayActiveGuestsNum()
                                activeUsersInfos = self.obj_DbC.Admin(self.id).getActiveUsersInfo()
                                activeGuestsInfo = self.obj_DbC.Admin(self.id).getActiveGuestsInfo()
                                numTodayAllTransactions = len(self.obj_DbC.Admin(self.id).getMessagesTodayOfAll())
                                self.obj_KNM.AdminGardanesh(self.id,self.firstName,self.msg).adminSendGTEmruzMessageGPanel(todayActiveUsersNum,todayActiveGuestsNum,activeUsersInfos,activeGuestsInfo,numTodayAllTransactions,monthAlpha,year,day,weekDay)

                        if self.msg == BtnA().sendToAll:
                            self.obj_KNM.AdminGardanesh(self.id,self.firstName,self.msg).adminSendPBHMessageBBMSVA()

                        if self.obj_DbC.Admin(self.id).verifySendToAllMsg() is True and self.obj_DbC.Admin(self.id).msgKeyBotComparison(self.msg) is True:
                            if len(self.msg) < 4050:
                                self.obj_DbC.Admin(self.id).saveTempSendToAll(self.msg)
                                msg = self.obj_DbC.Admin(self.id).getTempSendToAll()
                                self.obj_KNM.AdminGardanesh(self.id,self.firstName,self.msg).adminSendGosilMessageYesNo(msg)
                            else:
                                self.obj_KNM.AdminGardanesh(self.id,self.firstName,self.msg).adminSendGMessageGPanellCharMore(self.msg)

                        if self.msg == BtnA().yesSendIt:
                            self.obj_KNM.AdminGardanesh(self.id,self.firstName,self.msg). adminSendGMessageGPanellCode()
                        if self.msg == "lightnessnoor":
                            ids = self.obj_DbC.Admin(self.id).getUserIds()
                            msg = self.obj_DbC.Admin(self.id).getTempSendToAll()
                            for id in ids:
                                self.obj_KNM.AdminGardanesh(self.id,self.firstName,self.msg).adminSendMsgToAll(id,msg)
                            self.obj_KNM.AdminGardanesh(self.id,self.firstName,self.msg).adminSendYeslMessageGPanel()
                        
                        if self.msg == BtnA().noDoubleComma:
                            self.obj_KNM.AdminGardanesh(self.id,self.firstName,self.msg).adminSendGMessageGPanell()  

                        if self.msg == BtnA().getBackToDesk:
                            self.obj_KNM.AdminGardanesh(self.id,self.firstName,self.msg).adminSendGMessageGPanell()       

                        ####################### در فهرست نخستین و اولیه ######################


                        #در فهرست نخستین و اولیه
                        if self.msg == BtnS().start :
                            if userIdentify is False:
                                    
                                # self.obj_Start.sendKeyAndMessagesUI()
                                self.obj_KNM.AdminStart(self.id,self.firstName,self.msg).sendKeyAndMessagesUI()

                            else:
                                self.obj_KNM.AdminAghazYadgiriVazhehayeKetab(self.id,self.firstName,self.msg).sendKeyAndMessageFAVA()
                        
                            # 📝 زبان پیام و کیبورد ⌨
                        #در فهرست نخستین و اولیه
                        if self.msg ==Btn().uILangNKeyEditNew:
                            if userIdentify is False:
                                    
                                    self.obj_KNM.AdminDegarsaniZaban1(self.id,self.firstName,self.msg).sendKeyAndMessageUI1()
                                #  self.obj_DegarsaniZaban1.sendKeyAndMessageUI1() 

                            else:
                                self.obj_KNM.AdminAghazYadgiriVazhehayeKetab(self.id,self.firstName,self.msg).sendKeyAndMessageFAVA()
                        
                        #در فهرست نخستین و اولیه
                        if self.msg == BtnS().keyNMsgPer:        
                            self.obj_DbC.UILanguage(self.id).saveUIL(self.msg)
                            if userIdentify is False:
                                    self.obj_KNM.AdminStart(self.id,self.firstName,self.msg).sendKeyAndMessageFNVAUIselected()
                            else:
                                    self.obj_KNM.AdminAghazYadgiriVazhehayeKetab(self.id,self.firstName,self.msg).sendKeyAndMessageFAVA()

                        if self.msg == BtnS().keyNMsgEn:        
                            self.obj_DbC.UILanguage(self.id).saveUIL(self.msg)
                            if userIdentify is False:
                                    KNMEn.AdminStart(self.id,self.firstName,self.msg).sendKeyAndMessageFNVAUIselected()
                            else:
                                    KNMEn.AdminAghazYadgiriVazhehayeKetab(self.id,self.firstName,self.msg).sendKeyAndMessageFAVA()

                        if self.msg == BtnS().keyNMsgDe:        
                            self.obj_DbC.UILanguage(self.id).saveUIL(self.msg)
                            if userIdentify is False:
                                    KNMDe.AdminStart(self.id,self.firstName,self.msg).sendKeyAndMessageFNVAUIselected()
                            else:
                                    KNMDe.AdminAghazYadgiriVazhehayeKetab(self.id,self.firstName,self.msg).sendKeyAndMessageFAVA()

                            ############
                            ##  save to database
                            ###########
                            

                            # break 
                        #در فهرست نخستین و اولیه
                        if self.msg == Btn().startLearning :
                            if userIdentify is False:  
                                        self.obj_DbC.Report(self.id).firstLeitnerBoxStatistics(self.msg)
                                        # self.obj_DbC.User(self.id,self.firstName,self.last_name,self.username).updateNoneUserToSimple()
                                        #بطور ویژه از باتان برای مشخص کردن زبان استفاده شد
                                        self.obj_DbC.UILanguage(self.id).saveUIL(BtnS().keyNMsgPer)
                                    

                                        self.obj_KNM.AdminAghazYadgiriVazhehayeKetab(self.id,self.firstName,self.msg).sendAYVKKeyAndMessage327()
                            else:
                                self.obj_KNM.AdminAghazYadgiriVazhehayeKetab(self.id,self.firstName,self.msg).sendKeyAndMessageFAVA()
                                        
                                            #در فهرست نخستین و اولیه
                        if self.msg == BtnS().oneNew or self.msg == BtnS().twoNew or self.msg == BtnS().threeNew or self.msg == ABtnS().fiveNew  or self.msg == ABtnS().tenNew or self.msg == ABtnS().fifteenNew or self.msg == ABtnS().twentyNew :
                            if userIdentify is False:
                                withoutEmoj = int(self.msg.strip(" ♨️"))
                                self.obj_DbC.ShomarVazhgan(self.id).saveWordNum(withoutEmoj)

                                self.obj_DbC.User(self.id,self.firstName,self.last_name,self.username).updateNoneUserToSimple()
                                # موقت تا مرور ساخته بشه شمارنده در اینجاصفر می کنیم
                                self.obj_DbC.Counter(self.id).putZeroToCounter()
                                withoutEmoj = ""
                                #FIXME way of give user all language in appropriate way
                                allWays =[BtnS().persianTextEn, BtnS().deutschText,BtnS().englishText,BtnS().synonymText]
                                # print(f'allWays = {allWays}')

                                self.obj_DbC.RaveshYadgiri(self.id).saveWay(allWays)
                                #make package words 
                                self.obj_DbC.Vazhegan(self.id,self.msg).mixWords()
                                # self.obj_Vazhegan.mixWords()
                                
                                way,wKind,numW,numAll,word,content,chapter,wordsPage,linkWord = self.obj_DbC.Vazhegan(self.id,self.msg).wordNdetails()
                                                                    
                                # print(f'way = {way}')
                                reportNum = self.obj_DbC.Report(self.id).getReportNum()
                                #standardized word
                                standardizedWord = self.obj_DbC.Vazhegan(self.id).standardizeWord(word,reportNum)
                                #نگاشتن تاریخ یادگیری و تمرین نوبت پسین  و بعدی در فردا
                                self.obj_DbC.DateArrange().saveTomorrowNextTraining(self.id)
                                # if   5<reportNum:

                                #     wordCardWithGuide = MNV(self.firstName).wordCardWithGuide(way,wKind,numW,numAll,standardizedWord,content,chapter,wordsPage,linkWord)
                                #     self.obj_KNM.AdminInline(self.id,self.data).dataWord(way,wordCardWithGuide,Btn().startLearning)

                                # else:
                                wordCard = MNV(self.firstName).wordCard(wKind,numW,numAll,standardizedWord,content,chapter,wordsPage,linkWord)
                                self.obj_KNM.AdminInline(self.id,self.data).dataWordWithGuide(way,wordCard,Btn().startLearning)

                            else:
                                #########
                                tomorrowNextTraining =self.obj_DbC.DateArrange().getTomorrowNextTraining(self.id)
                                hourMin = tomorrowNextTraining.strftime("%H:%M")
                                #گرفتن سال ، ماه نویسه ای ، روز
                                # monthAlpha,year,month,day,monthAlphaFinglish,weekDayPer,weekDayFinglish
                                monthAlpha,year,_,day,_,_,_ = self.obj_DbC.DateArrange(self.id).convertToKhorshidi(tomorrowNextTraining)
                                # گرفتن نام روز در هفته به پارسی
                                weekDay = self.obj_DbC.DateArrange(self.id).getWeekDay(tomorrowNextTraining)
                                ########
                                self.obj_KNM.AghazYadgiriVazhehayeKetab(self.id,self.firstName,self.msg).sendNextTrainingDateTimeKeyAndMessageBBFA(weekDay,day,monthAlpha,year,hourMin)
                        
                        if self.msg == ABtnS().allTogetherNew or self.msg ==BtnS().persianNew or self.msg == BtnS().deutschNew or self.msg ==BtnS().englishNew or self.msg ==BtnS().synonymNew:
                            if userIdentify is False:
            
                                    self.obj_DbC.User(self.id,self.firstName,self.last_name,self.username).updateNoneUserToSimple()
                                    # موقت تا مرور ساخته بشه شمارنده در اینجاصفر می کنیم
                                    self.obj_DbC.Counter(self.id).putZeroToCounter()
                                    withoutEmoj = ""
                                    dictMsg ={ABtnS().allTogetherNew:"all together",BtnS().persianNew:"persian", BtnS().deutschNew:"deutsch",BtnS().englishNew:"english",BtnS().synonymNew:"synonym"}
                                    for field,value in dictMsg.items():
                                        if self.msg == field: 
                                            withoutEmoj = value
                                        ##  save to database
                                    self.obj_DbC.RaveshYadgiri(self.id).saveWay(withoutEmoj)
                                    #make package words 
                                    self.obj_DbC.Vazhegan(self.id,self.msg).mixWords()
                                    # self.obj_Vazhegan.mixWords()

                                    way,wKind,numW,numAll,word,content,chapter,wordsPage,linkWord = self.obj_DbC.Vazhegan(self.id).wordNdetails()



                                    ####
                                    
                                    reportNum = self.obj_DbC.Report(self.id).getReportNum()
                                    standardizedWord = self.obj_DbC.Vazhegan(self.id).standardizeWord(word,reportNum)
                                    #نگاشتن تاریخ یادگیری و تمرین نوبت پسین  و بعدی در فردا
                                    self.obj_DbC.DateArrange().saveTomorrowNextTraining(self.id)
                                    if   5<reportNum:
                                    # here 
                                    # send message and keyboard
                                        self.obj_KNM.AdminAghazYadgiriVazhehayeKetab(self.id,self.firstName,self.msg).sendDESPKeyAndMessageLamp(wKind,numW,numAll,standardizedWord,content,chapter,wordsPage,linkWord)
                                    # self.obj_DbC.Vazhegan(self.id).eraseTodayWords()
                                    else:
                                            self.obj_KNM.AdminAghazYadgiriVazhehayeKetab(self.id,self.firstName,self.msg).sendDESPKeyAndMessageLampGuid(way,wKind,numW,numAll,standardizedWord,content,chapter,wordsPage,linkWord)
                            else:
                                
                                #########
                                tomorrowNextTraining =self.obj_DbC.DateArrange().getTomorrowNextTraining(self.id)
                                hourMin = tomorrowNextTraining.strftime("%H:%M")
                                #گرفتن سال ، ماه نویسه ای ، روز
                                # monthAlpha,year,month,day,monthAlphaFinglish,weekDayPer,weekDayFinglish
                                monthAlpha,year,_,day,_,_,_ = self.obj_DbC.DateArrange(self.id).convertToKhorshidi(tomorrowNextTraining)
                                # گرفتن نام روز در هفته به پارسی
                                weekDay = self.obj_DbC.DateArrange(self.id).getWeekDay(tomorrowNextTraining)
                                ########
                                self.obj_KNM.AdminAghazYadgiriVazhehayeKetab(self.id,self.firstName,self.msg).sendNextTrainingDateTimeKeyAndMessageBBFA(weekDay,day,monthAlpha,year,hourMin)


                        #در فهرست نخستین و اولیه
                        if self.msg == Btn().aboutBotNew:
                            if userIdentify is False:
                                #  self.obj_DarbarehRobat1.sendKeyAndMessageDarbarehRobat1()
                                    self.obj_KNM.AdminDarbarehRobat1(self.id,self.firstName,self.msg).sendKeyAndMessageDarbarehRobat1()
                            else:
                                self.obj_KNM.AdminAghazYadgiriVazhehayeKetab(self.id,self.firstName,self.msg).sendKeyAndMessageFAVA()
                            


                    ###################### دکمه های مشترک میان فهرست ها ###################
                        # if self.msg == BtnS().lamp:
                        #     if userIdentify is True:
                            
                        #             if self.obj_DbC.DateArrange().getRightWrongLampFlag(self.id) is True:
                        #                     #get way 
                        #                     way = self.obj_DbC.RaveshYadgiri(self.id).getWay()
                        #                     #planB
                                            
                        #                     # way = self.obj_DbC.RaveshYadgiri(self.id).wayOrWaysString(way)
                        #                     #planA
                        #                     #get icon
                        #                     icon = self.obj_DbC.RaveshYadgiri(self.id).getIconBook(way)
                        #                     #get word
                        #                     todayWords = self.obj_DbC.Vazhegan(self.id).getTodayWords()
                        #                     print(f"todayWords = {todayWords}")
                        #                     word =  self.obj_DbC.Vazhegan(self.id).getOneRightWord(todayWords) 
                        #                     print(f"word = {word}")

                        #                     answerLink = self.obj_DbC.Vazhegan(self.id).audioAnswer(word,way)
                        #                     #save answer to todayWordsNAnswer
                                            
                        #                     input = self.obj_DbC.Vazhegan(self.id).getOneAnswerPure(word)
                        #                     self.obj_DbC.Vazhegan(self.id).updateValueKeyAnswer(input)
                        #                     # self.obj_updateValueKey.updateValueKeyAnswer(input)
                        #                     # get one answer
                        #                     answer = self.obj_DbC.Vazhegan(self.id).getOneAnswer(input)
                        #                     reportNum = self.obj_DbC.Report(self.id).getReportNum()
                        #                     standardizedAnswer = self.obj_DbC.Vazhegan(self.id).standardizeAnswer(way,answer,reportNum)

                        #                     if   5<reportNum:
                        #                         #send keyboar and message
                        #                         self.obj_KNM.AdminAghazYadgiriVazhehayeKetab(self.id,self.firstName,self.msg).sendLampKeyAndMessageVX(way,icon,standardizedAnswer,answerLink) 
                        #                     else:
                        #                         self.obj_KNM.AdminAghazYadgiriVazhehayeKetab(self.id,self.firstName,self.msg).sendLampKeyAndMessageVXGuide(way,icon,standardizedAnswer,answerLink)


                        #             else:
                        #                     #########
                        #                     tomorrowNextTraining =self.obj_DbC.DateArrange().getTomorrowNextTraining(self.id)
                        #                     hourMin = tomorrowNextTraining.strftime("%H:%M")
                        #                     #گرفتن سال ، ماه نویسه ای ، روز
                        #                     # monthAlpha,year,month,day
                        #                     monthAlpha,year,_,day = self.obj_DbC.DateArrange(self.id).convertToKhorshidi(tomorrowNextTraining)
                        #                     # گرفتن نام روز در هفته به پارسی
                        #                     weekDay = self.obj_DbC.DateArrange(self.id).getWeekDay(tomorrowNextTraining)
                        #                     ########
                        #                     self.obj_KNM.AdminAghazYadgiriVazhehayeKetab(self.id,self.firstName,self.msg).sendNextTrainingDateTimeKeyAndMessageBBFA(weekDay,day,monthAlpha,year,hourMin)   
                        #     else:
                        #             self.obj_KNM.AdminStart(self.id,self.firstName,self.msg).sendKeyAndMessageFNVAUINakhostin()



                        # if self.msg == BtnS().crossCheck or self.msg == BtnS().check:
                        #     if userIdentify is True:
                        #             if self.obj_DbC.DateArrange().getRightWrongLampFlag(self.id) is True:
                                            
                        #                     msgArray = self.obj_DbC.Msg().getMessagesToday(self.id)
                        #                     lengthMsgArray = len(msgArray)
                        #                     counter = self.obj_DbC.Counter(self.id).getCounter()
                        #                     #درصورت اسپم بودن و تکرار ی و  در عین حال آخرین  واژه هم بودن
                        #                     if (msgArray[lengthMsgArray-1] == msgArray[lengthMsgArray-2] or msgArray[lengthMsgArray-2] == BtnS().check or msgArray[lengthMsgArray-2] == BtnS().crossCheck) and  self.obj_DbC.Counter(self.id).lastWordVerification() == False:
                        #                         self.obj_KNM.AdminErrorMsgs(self.id,self.firstName,self.msg).sendWarningKeyAndMessageBBFA()
                        #                     #شرط تکراری نبودن
                        #                     elif (msgArray[lengthMsgArray-1] == msgArray[lengthMsgArray-2] or msgArray[lengthMsgArray-2] == BtnS().check or msgArray[lengthMsgArray-2] == BtnS().crossCheck) and counter == 0:
                        #                         self.obj_KNM.AdminErrorMsgs(self.id,self.firstName,self.msg).sendWarningKeyAndMessageBBFA()
                        #                     elif  msgArray[lengthMsgArray-1] == msgArray[lengthMsgArray-2] or msgArray[lengthMsgArray-2] == BtnS().check or msgArray[lengthMsgArray-2] == BtnS().crossCheck:
                        #                         self.obj_KNM.AdminAghazYadgiriVazhehayeKetab(self.id,self.firstName,self.msg).sendWarningKeyAndMessageLamp() 
                                                
                        #                     #آزمون آخرین بودن یا نبودن واژه 
                        #                     elif self.obj_DbC.Counter(self.id).lastWordVerification() == True:
                        #                     # if self.obj_Counter.lastWordVerification() == True:
                        #                         input = bool
                        #                         if self.msg == BtnS().check  :
                        #                             input = True
                        #                         elif self.msg == BtnS().crossCheck :
                        #                             input = False
                        #                         self.obj_DbC.Vazhegan(self.id).updateValueKey(input)
                        #                         self.obj_DbC.Counter(self.id).addOneToCounter()
                        #                         # self.obj_Counter.addOneToCounter()
                        #                         ##############
                        #                         if self.obj_DbC.IdentifyWordsSection(self.id,self.msg).findUserNWord() == False :
                        #                             if input is False:
                        #                                 self.obj_DbC.IdentifyWordsSection(self.id,self.msg).makeWordSection(1)
                        #                             elif input is True:
                        #                                 self.obj_DbC.IdentifyWordsSection(self.id,self.msg).makeWordSection(1)
                        #                                 self.obj_DbC.IdentifyWordsSection(self.id,self.msg).moveToNextLevel(1)
                        #                         elif self.obj_DbC.IdentifyWordsSection(self.id,self.msg).findUserNWord() ==True:
                        #                                 self.obj_DbC.IdentifyWordsSection(self.id,self.msg).moveToNextLevel(1)
                        #                         #################  report part  
                        #                         if self.obj_DbC.Counter(self.id).lastWordVerification() == False:    

                        #                             all,right,wrong,wrongWordsNpages,weekDay,day,monthAlpha,year,houNMTraining,dateGriNextTraining,wordsSectionPosition = self.obj_DbC.Report(self.id).dailyReport()
                        #                             self.obj_KNM.AdminAghazYadgiriVazhehayeKetab(self.id,self.firstName,self.msg).sendLastVXKeyAndMessageBBFA(all,right,wrong,wrongWordsNpages,weekDay,day,monthAlpha,year,houNMTraining,dateGriNextTraining,wordsSectionPosition)
                        #                             # self.obj_DbC.Vazhegan(self.id).eraseTodayWords()
                        #                         #فرستادن واژه
                        #                         else:
                        #                             way,wKind,numW,numAll,word,content,chapter,wordsPage,linkWord = self.obj_DbC.Vazhegan(self.id).wordNdetails()
                        #                             reportNum = self.obj_DbC.Report(self.id).getReportNum()
                        #                             standardizedWord = self.obj_DbC.Vazhegan(self.id).standardizeWord(word,reportNum)
                        #                             if   5<reportNum:

                        #                             # here 
                        #                             # send message and keyboard
                        #                                 self.obj_KNM.AdminAghazYadgiriVazhehayeKetab(self.id,self.firstName,self.msg).sendDESPKeyAndMessageLamp(wKind,numW,numAll,standardizedWord,content,chapter,wordsPage,linkWord)
                        #                             # self.obj_DbC.Vazhegan(self.id).eraseTodayWords()
                        #                             else:
                        #                                 self.obj_KNM.AdminAghazYadgiriVazhehayeKetab(self.id,self.firstName,self.msg).sendDESPKeyAndMessageLampGuid(way,wKind,numW,numAll,standardizedWord,content,chapter,wordsPage,linkWord)


                        #                     elif self.obj_DbC.Counter(self.id).lastWordVerification() == False:
                        #                     # elif self.obj_Counter.lastWordVerification() == False:
                        #                         self.obj_DbC.Counter(self.id).putZeroToCounter()
                        #                         # self.obj_Counter.putZeroToCounter() 
                        #                         self.obj_KNM.AdminAghazYadgiriVazhehayeKetab(self.id,self.firstName,self.msg).sendDESPKeyAndMessageLamp(wKind,numW,numAll,word,content,chapter,wordsPage,linkWord)  
                        #                         # self.obj_AghazYadgiriVazhehayeKetab.sendLastVXKeyAndMessageBBFA(all,right,wrong)
                        #             else:
                        #                     #########
                        #                     tomorrowNextTraining =self.obj_DbC.DateArrange().getTomorrowNextTraining(self.id)
                        #                     hourMin = tomorrowNextTraining.strftime("%H:%M")
                        #                     #گرفتن سال ، ماه نویسه ای ، روز
                        #                     # monthAlpha,year,month,day
                        #                     monthAlpha,year,_,day = self.obj_DbC.DateArrange(self.id).convertToKhorshidi(tomorrowNextTraining)
                        #                     # گرفتن نام روز در هفته به پارسی
                        #                     weekDay = self.obj_DbC.DateArrange(self.id).getWeekDay(tomorrowNextTraining)
                        #                     ########
                        #                     self.obj_KNM.AdminAghazYadgiriVazhehayeKetab(self.id,self.firstName,self.msg).sendNextTrainingDateTimeKeyAndMessageBBFA(weekDay,day,monthAlpha,year,hourMin)  


                        #     else:
                        #             self.obj_KNM.AdminStart(self.id,self.firstName,self.msg).sendKeyAndMessageFNVAUINakhostin()
                    

                    ###################### در فهرست آغازین و اصلی ###################
                        if self.msg == Btn().dailyLearnWords:
                            if userIdentify is True:
                                    self.obj_DbC.Report(self.id).firstLeitnerBoxStatistics(self.msg)
                                    if self.obj_DbC.DateArrange().getAutomateMsgFlag(self.id) is True:
                                                self.obj_DbC.DateArrange().saveTrueRightWrongLampFlag(self.id)
                                                #make package words 
                                                self.obj_DbC.Vazhegan(self.id,self.msg).mixWords()
                                                
                                                way,wKind,numW,numAll,word,content,chapter,wordsPage,wordLink = self.obj_DbC.Vazhegan(self.id).wordNdetails()
                            
                                                # here 
                                                # send message and keyboard
                                                # self.obj_KNM.AghazYadgiriVazhehayeKetab(self.id,self.firstName,self.msg).sendDESPKeyAndMessageLamp(wKind,numW,numAll,word,cotentNChap,wordsPage)
                                                #planA
                                                # way = self.obj_DbC.RaveshYadgiri(self.id).getWay()
                                                #planB
                                               
                                                # way = self.obj_DbC.RaveshYadgiri(self.id).wayOrWaysString(wayPure)


                                                reportNum = self.obj_DbC.Report(self.id).getReportNum()
                                                standardizedWord = self.obj_DbC.Vazhegan(self.id).standardizeWord(word,reportNum)
                                                # print(f"reportNum = {reportNum}")
                                                if reportNum is None:
                                                    self.obj_DbC.Report(self.id).addReportNumField()
                                                    reportNum = self.obj_DbC.Report(self.id).getReportNum()
                                                    standardizedWord = self.obj_DbC.Vazhegan(self.id).standardizeWord(word,reportNum)
                                                    if   5<reportNum:

                                                        wordCard = MNV(self.firstName).wordCard(wKind,numW,numAll,standardizedWord,content,chapter,wordsPage,wordLink)
                                                        
                                                        self.obj_KNM.AdminInline(self.id,self.data).dataWord(way,wordCard,Btn().dailyLearnWords)
                                                   
                                                    else:
                                                        
                                                        wordCardWithGuide = MNV(self.firstName).wordCardWithGuide(way,wKind,numW,numAll,standardizedWord,content,chapter,wordsPage,wordLink)
                                                        self.obj_KNM.AdminInline(self.id,self.data).dataWordWithGuide(way,wordCardWithGuide,Btn().dailyLearnWords)

                                                else:
                                                    if   5<reportNum:

                                                        
                                                        wordCard = MNV(self.firstName).wordCard(wKind,numW,numAll,standardizedWord,content,chapter,wordsPage,wordLink)
                                                        self.obj_KNM.AdminInline(self.id,self.data).dataWord(way,wordCard,Btn().dailyLearnWords)
                                                     
                                                    else:
                                                        wordCardWithGuide = MNV(self.firstName).wordCardWithGuide(way,wKind,numW,numAll,standardizedWord,content,chapter,wordsPage,wordLink)
                                                        self.obj_KNM.AdminInline(self.id,self.data).dataWordWithGuide(way,wordCardWithGuide,Btn().dailyLearnWords)
                                                      
                                    else:
                                            #########
                                            tomorrowNextTraining =self.obj_DbC.DateArrange().getTomorrowNextTraining(self.id)
                                            hourMin = tomorrowNextTraining.strftime("%H:%M")
                                            #گرفتن سال ، ماه نویسه ای ، روز
                                            # monthAlpha,year,month,day,monthAlphaFinglish,weekDayPer,weekDayFinglish
                                            monthAlpha,year,_,day,_,_,_ = self.obj_DbC.DateArrange(self.id).convertToKhorshidi(tomorrowNextTraining)
                                            # گرفتن نام روز در هفته به پارسی
                                            weekDay = self.obj_DbC.DateArrange(self.id).getWeekDay(tomorrowNextTraining)
                                            ########
                                            self.obj_KNM.AdminAghazYadgiriVazhehayeKetab(self.id,self.firstName,self.msg).sendNextTrainingDateTimeKeyAndMessageBBFA(weekDay,day,monthAlpha,year,hourMin)  

                            else:
                                    self.obj_KNM.AdminStart(self.id,self.firstName,self.msg).sendKeyAndMessageFNVAUINakhostin()





                        #در فهرست آغازین و اصلی  
                        if self.msg == Btn().reviewWords:
                            if userIdentify is True:
                                    self.obj_KNM.AdminMorureVazhehhayeGozashteh(self.id,self.firstName,self.msg).sendMVGKeyAndMessageTMVG()
                            else:
                                    self.obj_KNM.AdminStart(self.id,self.firstName,self.msg).sendKeyAndMessageFNVAUINakhostin()

                                

                        #در فهرست آغازین و اصلی .....#Btn().reviewWords
                        if self.msg == Btn().chapterNSection:
                                if userIdentify is True:
                                        ##############
                                        self.obj_DbC.Counter(self.id).putZeroToCounter()
                                        # self.obj_Counter.putZeroToCounter()
                                        words = self.obj_DbC.Review(self.id).sortChapterContentBase()
                                        # print(f"words = {words}")
                                        self.obj_DbC.Review(self.id).saveReviewWords(words)
                                        try:
                                            way,content,chapter,word,counter,length,section,page,link = self.obj_DbC.Review(self.id).reviewChapterContentWordsNDetails()
                                            standardizedWord = self.obj_DbC.Vazhegan(self.id).standardizeWordReview(word,self.msg)
                                            msgCHNS = MNV(self.firstName).chapterNSectionRev(content,chapter,standardizedWord,counter,length,section,page,link)
                                            lengthIF = len(self.obj_DbC.Review(self.id).getReviewWords())
                                            # chapterNSectionWaysCBArray
                                            chNSWCB = [BtnS().deutschChapNSCB,BtnS().englishChapNSCB,BtnS().synonymChapNSCB,BtnS().persianEnChapNSCB]
                                            if lengthIF == 1:
                                                self.obj_KNM.AdminInline(self.id,self.firstName).reviewOne(chNSWCB,way,length,msgCHNS,self.msg)
                                            else:
                                                self.obj_KNM.AdminInline(self.id,self.firstName).reviewMoreThanOne(counter,chNSWCB,way,length,msgCHNS,self.msg)

                                            counterIF = self.obj_DbC.Counter(self.id).getCounter()
                                            # print(f"counterIF = {counterIF}")

                                        except:
                                            self.obj_KNM.MorureVazhehhayeGozashteh(self.id,self.firstName,self.msg).sendWeakWordsKeyAndMessageNoWordOtherReview()
                                        # here
                                        ###############   
                                else:
                                        self.obj_KNM.AdminStart(self.id,self.firstName,self.msg).sendKeyAndMessageFNVAUINakhostin()
                                    
                        if self.msg == Btn().nextWordChapNS:
                                if userIdentify is True:
                                    if self.obj_DbC.Counter(self.id).getCounter()+1 != len(self.obj_DbC.Review(self.id).getReviewWords()):
                                        self.obj_DbC.Counter(self.id).addOneToCounter()
                                    # self.obj_Counter.addOneToCounter()
                                    counterIF = self.obj_DbC.Counter(self.id).getCounter()+1
                                    # print(f"counterIF = {counterIF}")
                                    lengthIF = len(self.obj_DbC.Review(self.id).getReviewWords())
                                    # print(f"lengthIF = {lengthIF}")
                                    if counterIF>lengthIF:
                                            self.obj_DbC.Counter(self.id).putValueToCounter(lengthIF-1)
                                            # self.obj_Counter.putValueToCounter(lengthIF-1)
                                    if counterIF != lengthIF:
                                        content,chapter,word,answer,counter,length,section,page,link = self.obj_DbC.Review(self.id).reviewChapterContentWordsNDetails()
                                        self.obj_KNM.AdminMorureVazhehhayeGozashteh(self.id,self.firstName,self.msg).sendWordsChapterContentKeyAndMessagMiddleOLdWord(content,chapter,word,answer,counter,length,section,page,link)
                                        
                                        
                                    elif counterIF == lengthIF:
                                    #if last:
                                        
                                        content,chapter,word,answer,counter,length,section,page,link = self.obj_DbC.Review(self.id).reviewChapterContentWordsNDetails()
                                        self.obj_KNM.AdminMorureVazhehhayeGozashteh(self.id,self.firstName,self.msg).sendWordsChapterContentKeyAndMessagLastOLdWord(content,chapter,word,answer,counter,length,section,page,link) 
                                else:
                                    self.obj_KNM.AdminStart(self.id,self.firstName,self.msg).sendKeyAndMessageFNVAUINakhostin()


                            # if userIdentify is True:

                            # else:
                            #     self.obj_KNM.Start(self.id,self.firstName,self.msg).sendKeyAndMessageFNVAUIselected()
                        if self.msg == Btn().beforeWordChapNS:
                            if userIdentify is True:
                                    self.obj_DbC.Counter(self.id).subtractOneToCounter()
                                    # self.obj_Counter.subtractOneToCounter()
                                    content,chapter,word,answer,counter,length,section,page,link = self.obj_DbC.Review(self.id).reviewChapterContentWordsNDetails()
                                    counterIF = self.obj_DbC.Counter(self.id).getCounter()+1
                                    lengthIF = len(self.obj_DbC.Review(self.id).getReviewWords())
                                    # print(f"lengthIF = {lengthIF}")
                                    if counterIF == 1:
                                        self.obj_KNM.AdminMorureVazhehhayeGozashteh(self.id,self.firstName,self.msg).sendWordsChapterContentKeyAndMessageFirstOLdWord(content,chapter,word,answer,counter,length,section,page,link)
                                    elif counterIF != 1:
                                        self.obj_KNM.AdminMorureVazhehhayeGozashteh(self.id,self.firstName,self.msg).sendWordsChapterContentKeyAndMessagMiddleOLdWord(content,chapter,word,answer,counter,length,section,page,link)
                            else:
                                self.obj_KNM.AdminStart(self.id,self.firstName,self.msg).sendKeyAndMessageFNVAUINakhostin()


                        #🔭
                        #در فهرست آغازین و اصلی .....#Btn().reviewWords 
                        if self.msg == Btn().leitnerBoxParts:
                                if userIdentify is True:
                                            ##############
                                        self.obj_DbC.Counter(self.id).putZeroToCounter()
                                        # self.obj_Counter.putZeroToCounter()
                                        words = self.obj_DbC.Review(self.id).sortSectionBase()
                                        # words = self.obj_Vazhegan.getAllWordsSection()

                                        # print(f"words = {words}")
                                        self.obj_DbC.Review(self.id).saveReviewWords(words)
                                        try:
                                            way,counter,length,section,word,page,content,chapter,link = self.obj_DbC.Review(self.id).reviewBakhshhaWordsNDetails()
                                            standardizedWord = self.obj_DbC.Vazhegan(self.id).standardizeWordReview(word,self.msg)
                                            wordDetails = MNV(self.firstName).leitnerBoxrRev(content,chapter,standardizedWord,counter,length,section,page,link)
                                            
                                            lengthIF = len(self.obj_DbC.Review(self.id).getReviewWords())
                                            lBWCB = [BtnS().deutschLeitBPCB,BtnS().englishLeitBPCB,BtnS().synonymLeitBPCB,BtnS().persianEnLeitBPCB]     
                                            if lengthIF == 1:
                                                self.obj_KNM.AdminInline(self.id,self.firstName,self.msg).reviewOne(lBWCB,way,length,wordDetails,self.msg)
                                            else:
                                                self.obj_KNM.AdminInline(self.id,self.firstName,self.msg).reviewMoreThanOne(counter,lBWCB,way,length,wordDetails,self.msg)
                                            counterIF = self.obj_DbC.Counter(self.id).getCounter()
                                            # print(f"counterIF = {counterIF}")
                                            # here
                                        except:
                                            self.obj_KNM.MorureVazhehhayeGozashteh(self.id,self.firstName,self.msg).sendWeakWordsKeyAndMessageNoWordOtherReview()

                                        ###############
                                else:
                                    self.obj_KNM.AdminStart(self.id,self.firstName,self.msg).sendKeyAndMessageFNVAUINakhostin()

                                # if userIdentify is True:

                                # else:
                                #     self.obj_KNM.Start(self.id,self.firstName,self.msg).sendKeyAndMessageFNVAUIselected()

                        if self.msg == Btn().nextWordLeitBP:
                            if userIdentify is True:
                                    #if one more is not last
                                    if self.obj_DbC.Counter(self.id).getCounter()+1 != len(self.obj_DbC.Review(self.id).getReviewWords()):
                                        self.obj_DbC.Counter(self.id).addOneToCounter()
                                    # self.obj_Counter.addOneToCounter()
                                    ###
                                    counterIF = self.obj_DbC.Counter(self.id).getCounter()+1
                                    # print(f"counterIF = {counterIF}")
                                    lengthIF = len(self.obj_DbC.Review(self.id).getReviewWords())
                                    # print(f"lengthIF = {lengthIF}")
                                    if counterIF>lengthIF:
                                        self.obj_DbC.Counter(self.id).putValueToCounter(length-1)
                                        # self.obj_Counter.putValueToCounter(lengthIF-1)
                                    #هنوز واژه در آراینه داریم و آخری نیست
                                    if counterIF != lengthIF:
                                        counter,length,section,word,answer,page,content,chapter,link = self.obj_DbC.Review(self.id).reviewBakhshhaWordsNDetails()
                                        self.obj_KNM.AdminMorureVazhehhayeGozashteh(self.id,self.firstName,self.msg).sendBakhshhaKeyAndMessageMiddleWord(counter,length,section,word,answer,page,content,chapter,link)
                                    ###
                                    elif counterIF == lengthIF:
                                        counter,length,section,word,answer,page,content,chapter,link = self.obj_DbC.Review(self.id).reviewBakhshhaWordsNDetails()
                                        self.obj_KNM.AdminMorureVazhehhayeGozashteh(self.id,self.firstName,self.msg).sendBakhshhaKeyAndMessageLastWord(counter,length,section,word,answer,page,content,chapter,link)    
                            else:
                                    self.obj_KNM.AdminStart(self.id,self.firstName,self.msg).sendKeyAndMessageFNVAUINakhostin()




                        if self.msg == Btn().beforeWordLeitBP:
                                if userIdentify is True:
                                        self.obj_DbC.Counter(self.id).subtractOneToCounter()
                                        # self.obj_Counter.subtractOneToCounter()
                                        counter,length,section,word,answer,page,content,chapter,link = self.obj_DbC.Review(self.id).reviewBakhshhaWordsNDetails()
                                        counterIF = self.obj_DbC.Counter(self.id).getCounter()+1
                                        lengthIF = len(self.obj_DbC.Review(self.id).getReviewWords())
                                        # print(f"lengthIF = {lengthIF}")
                                        
                                        if counterIF == 1:
                                            self.obj_KNM.AdminMorureVazhehhayeGozashteh(self.id,self.firstName,self.msg).sendBakhshhaKeyAndMessageFirstWord(counter,length,section,word,answer,page,content,chapter,link)
                                        elif counterIF != 1:
                                            self.obj_KNM.AdminMorureVazhehhayeGozashteh(self.id,self.firstName,self.msg).sendBakhshhaKeyAndMessageMiddleWord(counter,length,section,word,answer,page,content,chapter,link)
                                else:
                                    self.obj_KNM.AdminStart(self.id,self.firstName,self.msg).sendKeyAndMessageFNVAUINakhostin()




                        #🔬    
                        #در فهرست آغازین و اصلی .....#Btn().reviewWords 
                        if self.msg == Btn().weakWords:

                                    if userIdentify is True:    

                                                    ##############
                                            self.obj_DbC.Counter(self.id).putZeroToCounter()
                                            
                                            words = self.obj_DbC.Review(self.id).weakWordsNDuraionSorted()
                                            # print(f"words = {words}")
                                            if words != False:

                                                self.obj_DbC.Review(self.id).saveReviewWords(words)
                                                ###
                                                way,durationDays,counter,length,section,word,content,chapter,page,link = self.obj_DbC.Review(self.id).reviewWeakWordsNDetails()
                                                standardizedWord = self.obj_DbC.Vazhegan(self.id).standardizeWordReview(word,self.msg)
                                                wordDetails = MNV(self.firstName).weakWordsRev(durationDays,counter,length,section,standardizedWord,content,chapter,page,link)

                                
                                                lengthIF = len(self.obj_DbC.Review(self.id).getReviewWords())
                                                wWCB = [BtnS().deutschWWCB,BtnS().englishWWCB,BtnS().synonymWWCB,BtnS().persianEnWWCB]                                        
                                                if lengthIF == 1:
                                                    self.obj_KNM.AdminInline(self.id,self.firstName,self.msg).reviewOne(wWCB,way,length,wordDetails,self.msg)
                                                else:
                                                    self.obj_KNM.AdminInline(self.id,self.firstName,self.msg).reviewMoreThanOne(counter,wWCB,way,length,wordDetails,self.msg)


                                                counterIF = self.obj_DbC.Counter(self.id).getCounter()
                                                # print(f"counterIF = {counterIF}")

                                                ### 
                                                
                                            
                                            else:
                                                self.obj_KNM.AdminMorureVazhehhayeGozashteh(self.id,self.firstName,self.msg).sendWeakWordsKeyAndMessageNoWord()
                                            ###############
                                    else:
                                            self.obj_KNM.AdminStart(self.id,self.firstName,self.msg).sendKeyAndMessageFNVAUINakhostin()



                        if self.msg == Btn().nextWordWW:
                                if userIdentify is True:
                                        ###
                                        #if one more is not last
                                        if self.obj_DbC.Counter(self.id).getCounter()+1 != len(self.obj_DbC.Review(self.id).getReviewWords()):
                                            self.obj_DbC.Counter(self.id).addOneToCounter()
                                        # self.obj_Counter.addOneToCounter()
                                        ###
                                        counterIF = self.obj_DbC.Counter(self.id).getCounter()+1
                                        # print(f"counterIF = {counterIF}")
                                        lengthIF = len(self.obj_DbC.Review(self.id).getReviewWords())
                                        # print(f"lengthIF = {lengthIF}")
                                        if counterIF>lengthIF:
                                            self.obj_DbC.Counter(self.id).putValueToCounter(lengthIF-1)
                                            # self.obj_Counter.putValueToCounter(lengthIF-1)
                                        #هنوز واژه در آراینه داریم و آخری نیست
                                        if counterIF != lengthIF:
                                            durationDays,counter,length,section,word,answer,content,chapter,page,link = self.obj_DbC.Review(self.id).reviewWeakWordsNDetails()
                                            self.obj_KNM.AdminMorureVazhehhayeGozashteh(self.id,self.firstName,self.msg).sendWeakWordsKeyAndMessagMiddleOLdWord(durationDays,counter,length,section,word,answer,content,chapter,page,link)
                                        ###
                                        elif counterIF == lengthIF:
                                            durationDays,counter,length,section,word,answer,content,chapter,page = self.obj_DbC.Review(self.id).reviewWeakWordsNDetails()
                                            self.obj_KNM.AdminMorureVazhehhayeGozashteh(self.id,self.firstName,self.msg).sendWeakWordsKeyAndMessagLastOLdWord(durationDays,counter,length,section,word,answer,content,chapter,page,link) 
                                        ###
                                else:
                                    self.obj_KNM.AdminStart(self.id,self.firstName,self.msg).sendKeyAndMessageFNVAUINakhostin()



                            

                        if self.msg == Btn().beforeWordWW:
                                if userIdentify is True:    
                                        ###
                                        self.obj_DbC.Counter(self.id).subtractOneToCounter()
                                        # self.obj_Counter.subtractOneToCounter()
                                        durationDays,counter,length,section,word,answer,content,chapter,page,link = self.obj_DbC.Review(self.id).reviewWeakWordsNDetails()
                                        counterIF = self.obj_DbC.Counter(self.id).getCounter()+1
                                        lengthIF = len(self.obj_DbC.Review(self.id).getReviewWords())
                                        # print(f"lengthIF = {lengthIF}")
                                        if counterIF == 1:
                                            self.obj_KNM.AdminMorureVazhehhayeGozashteh(self.id,self.firstName,self.msg).sendWeakWordsKeyAndMessageFirstOLdWord(durationDays,counter,length,section,word,answer,content,chapter,page,link)
                                        elif counterIF != 1:
                                            self.obj_KNM.AdminMorureVazhehhayeGozashteh(self.id,self.firstName,self.msg).sendWeakWordsKeyAndMessagMiddleOLdWord(durationDays,counter,length,section,word,answer,content,chapter,page,link)
                                else:
                                            self.obj_KNM.AdminStart(self.id,self.firstName,self.msg).sendKeyAndMessageFNVAUINakhostin()


                        #در فهرست آغازین و اصلی 
                        if self.msg == Btn().wayEdit:    
                                if userIdentify is True:
                                        way = self.obj_DbC.RaveshYadgiri(self.id,self.msg).getWay()
                                        self.obj_KNM.AdminVirayeshRavesh(self.id,self.firstName,self.msg).wayMenu(way)
                                        # self.obj_KNM.AdminVirayeshRavesh(self.id,self.firstName,self.msg).send357KeyAndMessageDESP()
                                else:
                                        self.obj_KNM.AdminStart(self.id,self.firstName,self.msg).sendKeyAndMessageFNVAUINakhostin()
                                   
                        ##در فهرست آغازین و اصلی 
                        if self.msg == ABtnS().allTogether or self.msg ==BtnS().persian or self.msg == BtnS().deutsch or self.msg ==BtnS().english or self.msg ==BtnS().synonym:
                                if userIdentify is True:
                                # ذخیره کردن به صورت موقت 
                                        withoutEmoj = ""
                                        dictMsg ={ABtnS().allTogether:"all together",BtnS().persian:"persian", BtnS().deutsch:"deutsch",BtnS().english:"english",BtnS().synonym:"synonym"}
                                        for field,value in dictMsg.items():
                                            if self.msg == field: 
                                                withoutEmoj = value
                                        self.obj_DbC.RaveshYadgiri(self.id,withoutEmoj).saveTemportyWay() 
                                        #درصورت یکسان بودن با روشی که پیش از این انتخاب کرده بود
                                        way = self.obj_DbC.RaveshYadgiri(self.id,self.msg).getWay()
                                        #planB
                                        
                                        # if withoutEmoj in way :
                                        #planA
                                        if withoutEmoj == way:
                                            self.obj_KNM.AdminVirayeshRavesh(self.id,self.firstName,self.msg).sendDESPAllSameKeyAndMessageFAVA()
                                            # print("same")
                                        else:
                                            self.obj_KNM.AdminVirayeshRavesh(self.id,self.firstName,self.msg).sendDESPAllKeyAndMessageYesNo(way)
                                else:
                                        self.obj_KNM.AdminStart(self.id,self.firstName,self.msg).sendKeyAndMessageFNVAUINakhostin()
                            
                        
                        
                        #در فهرست آغازین و اصلی .....#Btn().wayEdit
                        if self.msg == Btn().yesDot :
                            if userIdentify is True:
                                    tempWay = self.obj_DbC.RaveshYadgiri(self.id,self.msg).getTemporaryWay()  
                                    self.obj_DbC.RaveshYadgiri(self.id,self.msg).saveWayByTemporary()
                                    # حذف تمامی سکشن های مرتبط 
                                    self.obj_DbC.IdentifyWordsSection(self.id,self.msg).deleteAllSections()  
                                    self.obj_KNM.AdminVirayeshRavesh(self.id,self.firstName,tempWay).sendBaleKeyAndMessageFAVA()
                            else:
                                self.obj_KNM.Start(self.id,self.firstName,self.msg).sendKeyAndMessageFNVAUINakhostin() 
                        elif self.msg == Btn().noDot:
                            if userIdentify is True:
                                    self.obj_KNM.AdminVirayeshRavesh(self.id,self.firstName,self.msg).sendKheyrKeyAndMessageFAVA()
                            else:
                                self.obj_KNM.AdminStart(self.id,self.firstName,self.msg).sendKeyAndMessageFNVAUINakhostin()        

                        



                        #در فهرست آغازین و اصلی 
                        if self.msg ==Btn().wordsNum:
                            if userIdentify is True:
                                # self.obj_VirayeshShomarVazheha.sendVShVMessage357()

                                self.obj_KNM.AdminVirayeshShomarVazheha(self.id,self.firstName,self.msg).sendVShVMessage357()
                            else:
                                self.obj_KNM.AdminStart(self.id,self.firstName,self.msg).sendKeyAndMessageFNVAUINakhostin()

                        #در فهرست آغازین و اصلی .....#Btn().wordsNum
                        if self.msg == BtnS().one or self.msg == BtnS().two or self.msg == BtnS().three or self.msg == ABtnS().five or self.msg == ABtnS().ten or self.msg == ABtnS().fifteen or self.msg == ABtnS().twenty:
                            if userIdentify is True:   
                                    withoutEmoj = int(self.msg.strip("-"))
                                    self.obj_DbC.ShomarVazhgan(self.id).saveWordNum(withoutEmoj)
                                    self.obj_KNM.AdminVirayeshShomarVazheha(self.id,self.firstName,self.msg).send357AllVMessageFAVA()
                            else:
                                    self.obj_KNM.AdminStart(self.id,self.firstName,self.msg).sendKeyAndMessageFNVAUINakhostin()



                        #در فهرست آغازین و اصلی 
                        if self.msg == Btn().timeLearnEdit:
                                if userIdentify is True:
                                        self.obj_KNM.AdminVireyeshZamanYadgiriRuzaneh(self.id,self.firstName,self.msg).sendVZYRVMessage1_23()
                                else:
                                        self.obj_KNM.AdminStart(self.id,self.firstName,self.msg).sendKeyAndMessageFNVAUINakhostin()

                        #در فهرست آغازین و اصلی .....#Btn().timeLearnEdit
                        if self.msg == BtnS().clock1 or self.msg == BtnS().clock2 or self.msg == BtnS().clock3 or self.msg == BtnS().clock4 or self.msg == BtnS().clock5 or self.msg == BtnS().clock6 or self.msg == BtnS().clock7 or self.msg == BtnS().clock8 or self.msg == BtnS().clock9 or self.msg == BtnS().clock10 or self.msg == BtnS().clock11 or self.msg == BtnS().clock12 or self.msg == BtnS().clock13 or self.msg == BtnS().clock14 or self.msg == BtnS().clock15 or self.msg == BtnS().clock16 or self.msg == BtnS().clock17 or self.msg == BtnS().clock18 or self.msg == BtnS().clock19 or self.msg == BtnS().clock20 or self.msg == BtnS().clock21 or self.msg == BtnS().clock22 or self.msg == BtnS().clock23:
                                if userIdentify is True:
                                    dictMsg ={BtnS().clock1:1,BtnS().clock2:2, BtnS().clock3: 3,BtnS().clock4:4,BtnS().clock5:5,BtnS().clock6:6,BtnS().clock7:7, BtnS().clock8: 8,BtnS().clock9:9,BtnS().clock10:10,BtnS().clock11:11,BtnS().clock12:12,BtnS().clock13:13,BtnS().clock14:14,BtnS().clock15:15,BtnS().clock16:16,BtnS().clock17:17,BtnS().clock18:18,BtnS().clock19:19,BtnS().clock20:20,BtnS().clock21:21,BtnS().clock22:22,BtnS().clock23:23}
                                    for field,value in dictMsg.items():
                                        if self.msg == field: 
                                            pureHour = value
                                    # arr = self.msg.split(" ")
                                    # pureHour = int(arr[0])
                                    # print(pureHour)

                                    tomorrowNextTraining = self.obj_DbC.DateArrange().getTomorrowNextTraining(self.id)
                                    hourTraining = int(tomorrowNextTraining.strftime("%H"))
                                    # print(f"hourTraining = {hourTraining}")       
                                    #########

                                    hourMin = tomorrowNextTraining.strftime("%H:%M")
                                    #گرفتن سال ، ماه نویسه ای ، روز
                                    # monthAlpha,year,month,day,monthAlphaFinglish,weekDayPer,weekDayFinglish
                                    monthAlpha,year,_,day,_,_,_ = self.obj_DbC.DateArrange(self.id).convertToKhorshidi(tomorrowNextTraining)
                                    # گرفتن نام روز در هفته به پارسی
                                    weekDay = self.obj_DbC.DateArrange(self.id).getWeekDay(tomorrowNextTraining)
                                    ########
                                    #پیام در صورت تکراری بودن ساعت و زمان داده شده
                                    if pureHour == hourTraining:
                                        self.obj_KNM.AdminVireyeshZamanYadgiriRuzaneh(self.id,self.firstName,self.msg).sendYesMessageSameFAVA(year,monthAlpha,day,weekDay,hourMin)
                                    else:
                                        self.obj_DbC.DateArrange(self.id).saveTemporaryNextTrainingsHour(pureHour)
                                        askedNextTraining =  self.obj_DbC.DateArrange(self.id).askedNextTraining(pureHour)
                                        askedHourMin = askedNextTraining.strftime("%H:%M")
                                        #گرفتن سال ، ماه نویسه ای ، روز
                                        # monthAlpha,year,month,day,monthAlphaFinglish,weekDayPer,weekDayFinglish
                                        askedMonthAlpha,askedYear,_,askedDay,_,_,_ = self.obj_DbC.DateArrange(self.id).convertToKhorshidi(askedNextTraining)
                                        # گرفتن نام روز در هفته به پارسی
                                        askedWeekDay = self.obj_DbC.DateArrange(self.id).getWeekDay(askedNextTraining)

                                        self.obj_KNM.AdminVireyeshZamanYadgiriRuzaneh(self.id,self.firstName,self.msg).send1_23MessageYesNo(year,monthAlpha,day,weekDay,hourMin,askedYear,askedMonthAlpha,askedDay,askedWeekDay,askedHourMin)
                                else:
                                        self.obj_KNM.AdminStart(self.id,self.firstName,self.msg).sendKeyAndMessageFNVAUINakhostin()




                        
                        #در فهرست آغازین و اصلی .....#1..23#Btn().timeLearnEdit
                        if self.msg == Btn().yesDash :


                            if userIdentify is True:
                                temp = self.obj_DbC.DateArrange(self.id).getTemporaryNextTrainingsHour()
                                # print(f"temp = {temp}")
                                # self.obj_DbC.DateArrange(self.id).saveNextTrainingsHourbyTemp(temp)
                                self.obj_DbC.DateArrange(self.id).checkIsValue24(temp)
                                tomorrowNextTraining =self.obj_DbC.DateArrange().getTomorrowNextTraining(self.id)

                                hourMin = tomorrowNextTraining.strftime("%H:%M")
                                #گرفتن سال ، ماهنویسه ای ، روز
                                # monthAlpha,year,month,day,monthAlphaFinglish,weekDayPer,weekDayFinglish
                                monthAlpha,year,_,day,_,_,_ = self.obj_DbC.DateArrange(self.id).convertToKhorshidi(tomorrowNextTraining) 
                                # گرفتن نام روز در هفته به پارسی
                                weekDay = self.obj_DbC.DateArrange(self.id).getWeekDay(tomorrowNextTraining)
                                self.obj_KNM.AdminVireyeshZamanYadgiriRuzaneh(self.id,self.firstName).sendYesMessageFAVA(year,monthAlpha,day,weekDay,hourMin)

                            else:
                                self.obj_KNM.Start(self.id,self.firstName,self.msg).sendKeyAndMessageFNVAUINakhostin()

                        elif self.msg == Btn().noDash:
                            if userIdentify is True:
                                self.obj_KNM.AdminVireyeshZamanYadgiriRuzaneh(self.id,self.firstName,self.msg).sendNoMessageFAVA()
                            else:
                                self.obj_KNM.Start(self.id,self.firstName,self.msg).sendKeyAndMessageFNVAUINakhostin()

                        #در فهرست آغازین و اصلی        
                        if self.msg == Btn().reportActivity:
                            if userIdentify is True:
                                self.obj_KNM.AdminBarayandVaFarjam(self.id,self.firstName,self.msg).sendBVFMessageReports()
                                # self.obj_bot.sendMessage(self.id,"test","none",self.reportKey)
                            else:
                                self.obj_KNM.AdminStart(self.id,self.firstName,self.msg).sendKeyAndMessageFNVAUINakhostin()    
                        #در فهرست آغازین و اصلی .....#"برآیند و فرجام" 
                        if self.msg == Btn().reportWordsPartions:
                                if userIdentify is True:
                                    ############
                                    num = len(self.obj_DbC.Vazhegan(self.id).getAllWordsSection())
                                    msg2 = self.obj_DbC.Report(self.id).reportWordsSectionsPercentage()
                                    self.obj_KNM.AdminBarayandVaFarjam(self.id,self.firstName,self.msg).sendReportAllWordsMessageBBFA(num,msg2)
                                else:
                                    self.obj_KNM.AdminStart(self.id,self.firstName,self.msg).sendKeyAndMessageFNVAUINakhostin() 



                        #در فهرست آغازین و اصلی .....#"برآیند و فرجام" 
                        if self.msg == Btn().reportWeakWords:
                            if userIdentify is True:
                                    ############
                                #گزارش بخش ها ،روزها،واژه

                                wWDS = self.obj_DbC.Report(self.id).weakWordDuraionSection()
                                

                                #درصد،گراف،بخش
                                wWPGS = self.obj_DbC.Report(self.id).weakWordsPercentageGraphSection()
                                # فرستادن کیبورد و پیام
                                self.obj_KNM.AdminBarayandVaFarjam(self.id,self.firstName,self.msg).sendReportWeakWordMessageBBFA(wWDS,wWPGS)
                                    ###########
                            else:
                                self.obj_KNM.AdminStart(self.id,self.firstName,self.msg).sendKeyAndMessageFNVAUINakhostin()




                        #در فهرست آغازین و اصلی 
                        if self.msg ==Btn().uILangNKeyEdit:
                            if userIdentify is True:
                                    self.obj_KNM.AdminDegarsaniZaban2(self.id,self.firstName,self.msg).sendKeyAndMessageUI2() 
                                #  self.obj_DegarsaniZaban2.sendKeyAndMessageUI2() 
                            else:
                                self.obj_KNM.AdminStart(self.id,self.firstName,self.msg).sendKeyAndMessageFNVAUINakhostin()




                        
                        #حساب کاربری🙂
                        if self.msg == Btn().account:
                            if userIdentify is True:
                                outpuTodayDateNTime,output = self.obj_DbC.Report(self.id).getAccoutDetails()

                                self.obj_KNM.AdminAghazYadgiriVazhehayeKetab(self.id,self.firstName,self.msg).sendAccountInfoKeyAndMessageBBFA(outpuTodayDateNTime,output)
                                # self.obj_KNM.AdminAghazYadgiriVazhehayeKetab().
                            else:
                                self.obj_KNM.AdminStart(self.id,self.firstName,self.msg).sendKeyAndMessageFNVAUINakhostin()


                        #در فهرست آغازین و اصلی 
                        if self.msg == Btn().aboutBot:
                            if userIdentify is True:
                                    self.obj_KNM.AdminDarbarehRobat2(self.id,self.firstName,self.msg).sendKeyAndMessageDarbarehRobat2()
                            else:
                                self.obj_KNM.AdminStart(self.id,self.firstName,self.msg).sendKeyAndMessageFNVAUINakhostin()    
                        #در فهرست آغازین و اصلی 
                        if self.msg == Btn().deleteBot:
                            if userIdentify is True:
                                    self.obj_KNM.AdminHazfRobot(self.id,self.firstName,self.msg).sendHRKeyAndMessageYesNo()     
                            else:
                                self.obj_KNM.AdminStart(self.id,self.firstName,self.msg).sendKeyAndMessageFNVAUINakhostin()



                        #در فهرست آغازین و اصلی .....#Btn().deleteBot
                        if self.msg == Btn().yesDelete :
                            if userIdentify is True:
                                    # حذف تمامی سکشن های مرتبط 
                                    self.obj_DbC.IdentifyWordsSection(self.id,self.msg).deleteAllSections() 
                                    # حذف ربات 🗑
                                    self.obj_DbC.DeleteBot(self.id).deleteBot()
                                    self.obj_KNM.AdminHazfRobot(self.id,self.firstName,self.msg).sendYesKeyAndMessageFNVA()
                            
                            else:
                                self.obj_KNM.AdminStart(self.id,self.firstName,self.msg).sendKeyAndMessageFNVAUINakhostin()
                        
                        elif self.msg == Btn().no:
                            if userIdentify is True:
                                    self.obj_KNM.AdminAghazYadgiriVazhehayeKetab(self.id,self.firstName,self.msg).sendKeyAndMessageFAVA()
                            else:
                                self.obj_KNM.AdminStart(self.id,self.firstName,self.msg).sendKeyAndMessageFNVAUINakhostin()    
                                
                                                        #در فهرست آغازین و اصلی 
                        if self.msg == Btn().getBack:
                            if userIdentify is True:    
                                    self.obj_KNM.AdminAghazYadgiriVazhehayeKetab(self.id,self.firstName,self.msg).sendKeyAndMessageFAVA()
                            else:
                                self.obj_KNM.AdminStart(self.id,self.firstName,self.msg).sendKeyAndMessageFNVAUINakhostin()

                        #FIXME Admin self.msg == Btn().opinion
                        if self.msg == Btn().opinion:
                            if userIdentify is True: 
                                # self.obj_DbC.Msg().opinion(self.msg) 
                                self.obj_KNM.AdminDarbarehRobat2(self.id,self.firstName,self.msg).sendKeyAndMessageSendingSugession()
                                
                            else:
                                self.obj_KNM.AdminStart(self.id,self.firstName,self.msg).sendKeyAndMessageFNVAUINakhostin()

                        #FIXME  self.obj_DbC.Msg(self.id,self.msg).isSecondTodEndMsg() is True   
                        if self.obj_DbC.Msg(self.id,self.msg).isSecondTodEndMsg() is True:
                            if userIdentify is True: 
                                output,opId = self.obj_DbC.Msg(self.id,self.msg).saveOpinion(self.msg)
                                #در صورتی که متن وارد شده باشد و برای فرستادن رسید از این ایف استفاده می شود
                                if output is False and opId == "outOfRange":
                                    self.obj_KNM.AdminDarbarehRobat2(self.id,self.firstName,self.msg).sendKeyAndMessageOutOfRangeMsg()
                                #درصورت فرستادن متن سالم و درست
                                elif output is True:
                                    self.obj_KNM.AdminDarbarehRobat2(self.id,self.firstName,self.msg).sendKeyAndMessageDeliverOpinion(opId)
                                #در صورت زدن دکمه بازگشت به فهرست آغازین
                                elif output is False and opId == "getBack":
                                    # self.obj_KNM.AghazYadgiriVazhehayeKetab(self.id,self.firstName,self.msg).sendKeyAndMessageFAVA()
                                    pass
                                #درصورت استفاده از کیبورد ربات به غیر از بازگشت به فهرست آغازین
                                elif output is False and opId == "botKeyboard":
                                    
                                    self.obj_KNM.AdminDarbarehRobat2(self.id,self.firstName,self.msg).sendKeyAndMessageUsingBotKeys()
                                    
                                    
                            else:
                                self.obj_KNM.AdminStart(self.id,self.firstName,self.msg).sendKeyAndMessageFNVAUINakhostin()

                    



        except:
                    print("we go issue to send message")

    def dataAnalizer(self):
            
            try:
                print(self.data)
                self.obj_DbC.Msg(self.id).addMsgs(self.data)
                if self.data ==BtnS().wordCB:
                    # if userIdentify is True:
                                self.obj_DbC.Vazhegan(self.id,self.msg).mixWords()
                                way,wKind,numW,numAll,word,content,chapter,wordsPage,linkWord = self.obj_DbC.Vazhegan(self.id,self.msg).wordNdetails()
                                reportNum = self.obj_DbC.Report(self.id).getReportNum()
                                standardizedWord = self.obj_DbC.Vazhegan(self.id).standardizeWord(word,reportNum)
                                if   5<reportNum:

                                    wordCard = MNV(self.firstName).wordCard(wKind,numW,numAll,standardizedWord,content,chapter,wordsPage,linkWord)
                                    self.obj_KNM.AdminInline(self.id,self.firstName,self.msgId).dataWordQuery(way,wordCard)
                            
                                else:
                                    wordCardWithGuide = MNV(self.firstName).wordCardWithGuide(way,wKind,numW,numAll,standardizedWord,content,chapter,wordsPage,linkWord)
                                    self.obj_KNM.AdminInline(self.id,self.firstName,self.msgId).dataWordWithGuideQuery(way,wordCardWithGuide)
                    # else:
                    #         self.obj_KNM.AdminStart(self.id,self.firstName,self.msg).sendKeyAndMessageFNVAUINakhostin()
                if self.data == BtnS().synonymText or self.data == BtnS().deutschText or self.data == BtnS().englishText or self.data == BtnS().persianTextEn:

                        # if userIdentify is True:
                                
                        #                 if self.obj_DbC.DateArrange().getRightWrongLampFlag(self.id) is True:

                                                #get way 
                                                way = self.obj_DbC.RaveshYadgiri(self.id).getWay()
                                                # way = self.data
                                                #planB
                                                
                                                # way = self.obj_DbC.RaveshYadgiri(self.id).wayOrWaysString(way)
                                                #planA
                                                #get icon
                                                # FIXME icon
                                                icon = self.obj_DbC.RaveshYadgiri(self.id).getIconBook(self.data)
                                                #get word
                                                todayWords = self.obj_DbC.Vazhegan(self.id).getTodayWords()
                                                # print(f"todayWords = {todayWords}")
                                                word =  self.obj_DbC.Vazhegan(self.id).getOneRightWord(todayWords) 
                                                # print(f"word = {word}")
                                                #save answer to todayWordsNAnswer
                                                answerLink = self.obj_DbC.Vazhegan(self.id).audioAnswer(word,self.data)
                                                # print(f'answerLink = {answerLink}')
                                                input = self.obj_DbC.Vazhegan(self.id).getOneAnswerPure(word,self.data)
                                                self.obj_DbC.Vazhegan(self.id).updateValueKeyAnswer(input)
                                                # 
                                                # get one answer
                                                answer = self.obj_DbC.Vazhegan(self.id).getOneAnswer(input)
                                                
                                                reportNum = self.obj_DbC.Report(self.id).getReportNum()
                                                #FIXME standardizedAnswer
                                                standardizedAnswer = self.obj_DbC.Vazhegan(self.id).standardizeAnswer(self.data,answer,reportNum)
                                                #FIXME reportnum doesn't work


                                                if   5<reportNum:
                                                    #send keyboar and message
                                                    answerCard = MNV(self.firstName).answerCard(self.data,icon,standardizedAnswer,answerLink)
                                                    self.obj_KNM.AdminInline(self.id,self.firstName,self.msgId).answerWord(self.data,way,answerCard)
                                                    # self.obj_KNM.AghazYadgiriVazhehayeKetab(self.id,self.firstName,self.msg).sendLampKeyAndMessageVX(way,icon,standardizedAnswer,answerLink) 
                                                else:
                                                    # self.obj_KNM.AghazYadgiriVazhehayeKetab(self.id,self.firstName,self.msg).sendLampKeyAndMessageVXGuide(way,icon,standardizedAnswer,answerLink)
                                                    answerWordWithGuide = MNV(self.firstName).answerCardWithGuide(self.data,icon,standardizedAnswer,answerLink)     
                                                    self.obj_KNM.AdminInline(self.id,self.firstName,self.msgId).answerWordWithGuide(self.data,way,answerWordWithGuide)

                        # else:
                        #             self.obj_KNM.AdminStart(self.id,self.firstName,self.msg).sendKeyAndMessageFNVAUINakhostin()
                if self.data == BtnS().crossCheckCB or self.data == BtnS().checkCB:
                                # if userIdentify is True:
                                        # if self.obj_DbC.DateArrange().getRightWrongLampFlag(self.id) is True:
                                                msgArray = self.obj_DbC.Msg().getMessagesToday(self.id)
                                                # msgArray = self.obj_DbC.Msg(self.id,self.msg).getMsgArray()
                                                lengthMsgArray = len(msgArray)
                                                counter = self.obj_DbC.Counter(self.id).getCounter()
                                                #درصورت اسپم بودن و تکرار ی و  در عین حال آخرین  واژه هم بودن
                                                if (msgArray[lengthMsgArray-1] == msgArray[lengthMsgArray-2] or msgArray[lengthMsgArray-2] == BtnS().check or msgArray[lengthMsgArray-2] == BtnS().crossCheck) and  self.obj_DbC.Counter(self.id).lastWordVerification() == False:
                                                    self.obj_KNM.ErrorMsgs(self.id,self.firstName,self.msg).sendWarningKeyAndMessageBBFA()
                                                #شرط تکراری نبودن
                                                elif (msgArray[lengthMsgArray-1] == msgArray[lengthMsgArray-2] or msgArray[lengthMsgArray-2] == BtnS().check or msgArray[lengthMsgArray-2] == BtnS().crossCheck) and counter == 0:
                                                    self.obj_KNM.ErrorMsgs(self.id,self.firstName,self.msg).sendWarningKeyAndMessageBBFA()
                                                elif  msgArray[lengthMsgArray-1] == msgArray[lengthMsgArray-2] or msgArray[lengthMsgArray-2] == BtnS().check or msgArray[lengthMsgArray-2] == BtnS().crossCheck:
                                                    pass
                                                    # self.obj_KNM.AghazYadgiriVazhehayeKetab(self.id,self.firstName,self.msg).sendWarningKeyAndMessageLamp() 
                                                    
                                                #آزمون آخرین بودن یا نبودن واژه 
                                                elif self.obj_DbC.Counter(self.id).lastWordVerification() == True:
                                                    input = bool
                                                    if self.data == BtnS().checkCB  :
                                                        input = True
                                                    elif self.data == BtnS().crossCheckCB :
                                                        input = False
                                                    self.obj_DbC.Vazhegan(self.id).updateValueKey(input)
                                                    self.obj_DbC.Counter(self.id).addOneToCounter()
                                                    ##############
                                                    if self.obj_DbC.IdentifyWordsSection(self.id,self.data).findUserNWord() == False :
                                                        if input is False:
                                                            self.obj_DbC.IdentifyWordsSection(self.id,self.data).makeWordSection(1)
                                                        elif input is True:
                                                            self.obj_DbC.IdentifyWordsSection(self.id,self.data).makeWordSection(1)
                                                            self.obj_DbC.IdentifyWordsSection(self.id,self.data).moveToNextLevel(1)
                                                    elif self.obj_DbC.IdentifyWordsSection(self.id,self.data).findUserNWord() ==True:
                                                            self.obj_DbC.IdentifyWordsSection(self.id,self.data).moveToNextLevel(1)
                                                    #################  report part  
                                                    if self.obj_DbC.Counter(self.id).lastWordVerification() == False:    
                                                        #save last leitner values
                                                        self.obj_DbC.Report(self.id).lastLeitnerBoxStatistics(self.data)
                                                        #TODO get firstName,language,id,first,last karbar
                                                        lan = self.obj_DbC.UILanguage(self.id).getUIL()
                                                        first,last = self.obj_DbC.Report(self.id).getLeitnerBoxStatistics()
                                                        print(f"{first = } {last = } {lan = } {self.id = } {self.firstName = }")
                                                        cardNum = self.obj_DbC.ShomarVazhgan(self.id).getWordNum()

                                                        all,right,wrong,wrongWordsNpages,weekDay,day,monthAlpha,year,houNMTraining,dateGriNextTraining,wordsSectionPosition = self.obj_DbC.Report(self.id).dailyReport()
                                                        # print(self.msgId,self.id)
                                                        reportMsg = MNV(self.firstName).reportMsg(all,right,wrong,wrongWordsNpages,weekDay,day,monthAlpha,year,houNMTraining,dateGriNextTraining,wordsSectionPosition)
                                                        self.obj_KNM.AdminInline(self.id,self.firstName,self.msgId).report(reportMsg)

                                                        vidPNName = VS.ReleaseVideo().releaseVideo(self.id,cardNum,self.firstName,lan,first,last)
                                                        print(f"{vidPNName = }")
                                                        self.obj_KNM.AdminInline(self.id,self.firstName,self.msgId).sendVideoReport(vidPNName)

                                                    else:
                                                    
                                                        way,wKind,numW,numAll,word,content,chapter,wordsPage,linkWord = self.obj_DbC.Vazhegan(self.id).wordNdetails()
                                                        reportNum = self.obj_DbC.Report(self.id).getReportNum()
                                                        standardizedWord = self.obj_DbC.Vazhegan(self.id).standardizeWord(word,reportNum)
                                                        if   5<reportNum:

                                                        # here 
                                                        # send message and keyboard
                                                            # wordCardWithGuide = MNV(self.firstName).wordCardWithGuide(way,wKind,numW,numAll,standardizedWord,content,chapter,wordsPage,wordLink)
                                                            # wordCard = MNV(self.firstName).wordCard(wKind,numW,numAll,standardizedWord,content,chapter,wordsPage,wordLink)
                                                            wordCard = MNV(self.firstName).wordCard(wKind,numW,numAll,standardizedWord,content,chapter,wordsPage,linkWord)
                                                            self.obj_KNM.AdminInline(self.id,self.firstName,self.msgId).dataWordQuery(way,wordCard)
                                                            # self.obj_KNM.AdminInline(self.id,self.firstName,self.msgId).dataWordQuery(way,wordCardWithGuide)
                                                    
                                                        else:
                                                            # wordCard = MNV(self.firstName).wordCard(wKind,numW,numAll,standardizedWord,content,chapter,wordsPage,wordLink)
                                                            wordCardWithGuide = MNV(self.firstName).wordCardWithGuide(way,wKind,numW,numAll,standardizedWord,content,chapter,wordsPage,linkWord)
                                                            self.obj_KNM.AdminInline(self.id,self.firstName,self.msgId).dataWordWithGuideQuery(way,wordCardWithGuide)


                                                elif self.obj_DbC.Counter(self.id).lastWordVerification() == False:
                                                    self.obj_DbC.Counter(self.id).putZeroToCounter()
                                                    wordCard = MNV(self.firstName).wordCard(wKind,numW,numAll,standardizedWord,content,chapter,wordsPage,linkWord)
                                                    self.obj_KNM.AdminInline(self.id,self.firstName,self.msgId).dataWordQuery(way,wordCard)


                 #FIXME fix from here all admin keyboards
                if self.data == BtnS().deutschChapNSCB or self.data == BtnS().englishChapNSCB or self.data ==BtnS().synonymChapNSCB or self.data == BtnS().persianEnChapNSCB:
                            waysArray = [{BtnS().deutschChapNSCB:BtnS().deutschText},{ BtnS().englishChapNSCB:BtnS().englishText},{BtnS().synonymChapNSCB:BtnS().synonymText},{BtnS().persianEnChapNSCB:BtnS().persianTextEn}]
                            answerWay = ''
                            for z in waysArray:
                                for x,y in z.items():
                                    if self.data == x:
                                        answerWay = y
                            ways,pureAnswer,counter,length,answerLink = self.obj_DbC.Review(self.id).reviewANSWERChapterContentNDetails(answerWay)
                            # reviewAnswerChapNSec(ways,counter,length,self.data)
                            icon = self.obj_DbC.RaveshYadgiri(self.id).getIconBook(answerWay)
                            standardizedAnswer = self.obj_DbC.Vazhegan(self.id).standardizeAnswer(answerWay,pureAnswer,6)
                            # standardizedAnswer = ""
                            answerOutput = MNV(self.firstName).answerCard(answerWay,icon,standardizedAnswer,answerLink)
                            chapterNSectionCB = [BtnS().deutschChapNSCB,BtnS().englishChapNSCB,BtnS().synonymChapNSCB,BtnS().persianEnChapNSCB,BtnS().wordChapNSCB]
                            self.obj_KNM.AdminInline(self.id,self.firstName,self.msgId).reviewAnswer(chapterNSectionCB,answerWay,ways,counter,length,answerOutput,chapterNSectionCB[4])
                                   
                if self.data == Btn().nextWordChapNS or self.data == Btn().beforeWordChapNS or self.data == BtnS().wordChapNSCB:
                            counterIF = self.obj_DbC.Counter(self.id).getCounter()+1
                            lengthIF = len(self.obj_DbC.Review(self.id).getReviewWords())
                            if self.data == Btn().nextWordChapNS:
                                    if self.obj_DbC.Counter(self.id).getCounter()+1 != len(self.obj_DbC.Review(self.id).getReviewWords()):
                                            self.obj_DbC.Counter(self.id).addOneToCounter()
                                    if counterIF>lengthIF:
                                            self.obj_DbC.Counter(self.id).putValueToCounter(lengthIF-1)
                            elif self.data == Btn().beforeWordChapNS:
                                    self.obj_DbC.Counter(self.id).subtractOneToCounter()
                            way,content,chapter,word,counter,length,section,page,link = self.obj_DbC.Review(self.id).reviewChapterContentWordsNDetails()
                            standardizedWord = self.obj_DbC.Vazhegan(self.id).standardizeWordReview(word,self.data)
                            msgCHNS = MNV(self.firstName).chapterNSectionRev(content,chapter,standardizedWord,counter,length,section,page,link)
                            waysArrayCB = [BtnS().deutschChapNSCB,BtnS().englishChapNSCB,BtnS().synonymChapNSCB,BtnS().persianEnChapNSCB]
                            if lengthIF == 1:
                                    self.obj_KNM.AdminInline(self.id,self.firstName,self.msgId).reviewOne(waysArrayCB,way,length,msgCHNS,self.data)
                            else:
                                    self.obj_KNM.AdminInline(self.id,self.firstName,self.msgId).reviewMoreThanOne(counter,waysArrayCB,way,length,msgCHNS,self.data)
                if self.data == BtnS().deutschLeitBPCB or self.data == BtnS().englishLeitBPCB or self.data ==BtnS().synonymLeitBPCB or self.data == BtnS().persianEnLeitBPCB:
                            print(f"self.data = {self.data}")
                            waysArray = [{BtnS().deutschLeitBPCB:BtnS().deutschText},{ BtnS().englishLeitBPCB:BtnS().englishText},{BtnS().synonymLeitBPCB:BtnS().synonymText},{BtnS().persianEnLeitBPCB:BtnS().persianTextEn}]
                            answerWay = ''
                            for z in waysArray:
                                for x,y in z.items():
                                    if self.data == x:
                                        answerWay = y
                            ways,pureAnswer,counter,length,answerLink = self.obj_DbC.Review(self.id).reviewANSWERChapterContentNDetails(answerWay)
                            # reviewAnswerChapNSec(ways,counter,length,self.data)
                            icon = self.obj_DbC.RaveshYadgiri(self.id).getIconBook(answerWay)
                            standardizedAnswer = self.obj_DbC.Vazhegan(self.id).standardizeAnswer(answerWay,pureAnswer,6)
                            # standardizedAnswer = ""
                            answerOutput = MNV(self.firstName).answerCard(answerWay,icon,standardizedAnswer,answerLink)
                            
                            leitnerBoxCB = [BtnS().deutschLeitBPCB,BtnS().englishLeitBPCB,BtnS().synonymLeitBPCB,BtnS().persianEnLeitBPCB,BtnS().wordLeitBPCB]
                            self.obj_KNM.AdminInline(self.id,self.firstName,self.msgId).reviewAnswer(leitnerBoxCB,answerWay,ways,counter,length,answerOutput,leitnerBoxCB[4])


                if self.data == Btn().nextWordLeitBP or self.data == Btn().beforeWordLeitBP or self.data == BtnS().wordLeitBPCB:
                            counterIF = self.obj_DbC.Counter(self.id).getCounter()+1
                            lengthIF = len(self.obj_DbC.Review(self.id).getReviewWords())
                            if self.data == Btn().nextWordLeitBP:
                                    if self.obj_DbC.Counter(self.id).getCounter()+1 != len(self.obj_DbC.Review(self.id).getReviewWords()):
                                            self.obj_DbC.Counter(self.id).addOneToCounter()
                                    if counterIF>lengthIF:
                                            self.obj_DbC.Counter(self.id).putValueToCounter(lengthIF-1)
                            elif self.data == Btn().beforeWordLeitBP:
                                    self.obj_DbC.Counter(self.id).subtractOneToCounter()
                            way,content,chapter,word,counter,length,section,page,link = self.obj_DbC.Review(self.id).reviewChapterContentWordsNDetails()
                            standardizedWord = self.obj_DbC.Vazhegan(self.id).standardizeWordReview(word,self.data)
                            msgCHNS = MNV(self.firstName).leitnerBoxrRev(content,chapter,standardizedWord,counter,length,section,page,link)
                            waysArrayCB = [BtnS().deutschLeitBPCB,BtnS().englishLeitBPCB,BtnS().synonymLeitBPCB,BtnS().persianEnLeitBPCB]
                            if lengthIF == 1:
                                    self.obj_KNM.AdminInline(self.id,self.firstName,self.msgId).reviewOne(waysArrayCB,way,length,msgCHNS,self.data)
                            else:
                                    self.obj_KNM.AdminInline(self.id,self.firstName,self.msgId).reviewMoreThanOne(counter,waysArrayCB,way,length,msgCHNS,self.data)

                if self.data == BtnS().deutschWWCB or self.data == BtnS().englishWWCB or self.data ==BtnS().synonymWWCB or self.data == BtnS().persianEnWWCB:
                            waysArray = [{BtnS().deutschWWCB:BtnS().deutschText},{ BtnS().englishWWCB:BtnS().englishText},{BtnS().synonymWWCB:BtnS().synonymText},{BtnS().persianEnWWCB:BtnS().persianTextEn}]
                            answerWay = ''
                            for z in waysArray:
                                for x,y in z.items():
                                    if self.data == x:
                                        answerWay = y


                            # print(answerWay)
                            #FIXME this name must be fixed reviewANSWERChapterContentNDetails
                            ways,pureAnswer,counter,length,answerLink = self.obj_DbC.Review(self.id).reviewANSWERChapterContentNDetails(answerWay)
                            # print(f"pureAnswer = {pureAnswer}")
                            # reviewAnswerChapNSec(ways,counter,length,self.data)
                            icon = self.obj_DbC.RaveshYadgiri(self.id).getIconBook(answerWay)
                            standardizedAnswer = self.obj_DbC.Vazhegan(self.id).standardizeAnswer(answerWay,pureAnswer,6)
                            # standardizedAnswer = ""
                            answerOutput = MNV(self.firstName).answerCard(answerWay,icon,standardizedAnswer,answerLink)
                            
                            weakWordCB = [BtnS().deutschWWCB,BtnS().englishWWCB,BtnS().synonymWWCB,BtnS().persianEnWWCB,BtnS().wordWWCB]
                            self.obj_KNM.AdminInline(self.id,self.firstName,self.msgId).reviewAnswer(weakWordCB,answerWay,ways,counter,length,answerOutput,weakWordCB[4])

                if self.data == Btn().nextWordWW or self.data == Btn().beforeWordWW or self.data == BtnS().wordWWCB:
                            counterIF = self.obj_DbC.Counter(self.id).getCounter()+1
                            lengthIF = len(self.obj_DbC.Review(self.id).getReviewWords())
                            if self.data == Btn().nextWordWW:
                                    if self.obj_DbC.Counter(self.id).getCounter()+1 != len(self.obj_DbC.Review(self.id).getReviewWords()):
                                            self.obj_DbC.Counter(self.id).addOneToCounter()
                                    if counterIF>lengthIF:
                                            self.obj_DbC.Counter(self.id).putValueToCounter(lengthIF-1)
                            elif self.data == Btn().beforeWordWW:
                                    self.obj_DbC.Counter(self.id).subtractOneToCounter()
                            way,durationDays,counter,length,section,word,content,chapter,page,link = self.obj_DbC.Review(self.id).reviewWeakWordsNDetails()
                                ####-----####
                            standardizedWord = self.obj_DbC.Vazhegan(self.id).standardizeWordReview(word,self.data)
                            wordDetails = MNV(self.firstName).weakWordsRev(durationDays,counter,length,section,standardizedWord,content,chapter,page,link)

            
                            lengthIF = len(self.obj_DbC.Review(self.id).getReviewWords())
                            wWCB = [BtnS().deutschWWCB,BtnS().englishWWCB,BtnS().synonymWWCB,BtnS().persianEnWWCB]                                        
                            if lengthIF == 1:
                                self.obj_KNM.AdminInline(self.id,self.firstName,self.msgId).reviewOne(wWCB,way,length,wordDetails,self.data)
                            else:
                                self.obj_KNM.AdminInline(self.id,self.firstName,self.msgId).reviewMoreThanOne(counter,wWCB,way,length,wordDetails,self.data)
                if self.data == MNV().endReview:
                             self.obj_KNM.AdminInline(self.id,self.firstName,self.msgId).getBack(MNV().endReview)
                if self.data == Btn().addWay:
                        way = self.obj_DbC.RaveshYadgiri(self.id,self.msg).getWay()
                        self.obj_KNM.AdminInline(self.id,self.firstName,self.msgId).addWay(way)
                if self.data == Btn().subtractWay:
                        way = self.obj_DbC.RaveshYadgiri(self.id).getWay()
                        self.obj_KNM.AdminInline(self.id,self.firstName,self.msgId).subtractWay(way)

                if self.data == BtnS().addEnglish or self.data == BtnS().addDeutsch or self.data == BtnS().addSynonym or self.data == BtnS().addPersian:
                        addedWay = self.obj_DbC.RaveshYadgiri(self.id).addWay(self.data)
                        self.obj_KNM.AdminInline(self.id,self.firstName,self.msgId).addedWayBefore(addedWay)
                        
                if self.data == BtnS().subtractEnglish or self.data == BtnS().subtractDeutsch or self.data == BtnS().subtractSynonym or self.data == BtnS().subtractPersian:
                        subtractingWay = self.obj_DbC.RaveshYadgiri(self.id).subtractWay(self.data)
                        self.obj_KNM.AdminInline(self.id,self.firstName,self.msgId).subtractedWayBefre(subtractingWay)
                if self.data == MNV().endEditWay:
                        self.obj_KNM.AdminInline(self.id,self.firstName,self.msgId).getBack(MNV().endEditWay)
                if self.data == MNV().secondMenu:
                        self.obj_KNM.AdminInline(self.id,self.firstName,self.msgId).getBack(MNV().secondMenu)

                if self.data in Btn().changeWay:
                        way = self.obj_DbC.RaveshYadgiri(self.id,self.msg).getWay()
                        self.obj_KNM.AdminInline(self.id,self.firstName,self.msgId).changeWayBefore(way)
                if self.data in BtnS().changeBtns:
                    add,subtract = self.obj_DbC.RaveshYadgiri(self.id,self.data).changeWay(self.data)
                    self.obj_KNM.AdminInline(self.id,self.firstName,self.msgId).changeWay(add,subtract)

            except:
                pass

