
import sys
sys.path.append( "../")
from mainV2.base.Buttons import ButtonSame as BtnS
from mainV2.base.Buttons import ButtonPer as PerBtn
from mainV2.base.Buttons import ButtonEn as EnBtn
from mainV2.base.Buttons import ButtonDe as DeBtn
from mainV2.set import dbContact
import datetime
class PublicMsgNVar:
    def __init__(self):
        self.gudwbot = "@gudwbot"
class MessageNVarPer:
    def __init__(self,firstName=None):
        # self.uILanguage = "Per"
        self.firstName = firstName
        self.dash = "___________________________________"
        self.secondMenu = "فهرست آغازین"
        self.endReview = "پایان مرور"
        self.endEditWay = "پایان ویرایش روش"


    def leitnerChanges(self):
        msg = f"دگرسانی و تغییرات جعبه لایتنرت!"
        return msg
    
    def todayDate(self,dateImport):
        # now = datetime.datetime.now()
        # monthAlpha,year,month,day,monthAlphaFinglish,weekDay,weekDayFinglish
        monthAlpha,year,_,day,_,weekDayPer,_= dbContact.DateArrange().convertToKhorshidi(dateImport)
            ## fix persian text
        todayNDateSplit = f" امروز : {weekDayPer} {day} {monthAlpha} {year}"

        return todayNDateSplit
    def dear(self):
        return "عزیز،"

    def wayStrCorrection(self,way):
        # print(ways)
        # self.wayEdit = ways
        try:
            wayEdit = [n for n in way if n !=BtnS().persianTextEn]
            # self.wayEdit.remove(BtnS().persianTextEn)
            wayEdit.append(BtnS().persianText)
        except:
            pass
        # print(way)
        wayStr = str(wayEdit)
        wayStr = wayStr.replace("[","")
        wayStr = wayStr.replace("]","")
        wayStr = wayStr.replace("'","")
        wayStr = wayStr.replace(","," یا")
        return wayStr
        
    def wordGuide(self,way):
        wayStr = self.wayStrCorrection(way)
        guide = f"راهنمایی🔔: واژه را مطالعه کنید و تلفظ و گویش  آن را با تلنگر بر صوت و آوای 🔉 آن در پایین گوش کنید سپس  {wayStr} آن را بگویید و به خاطر بسپارید، پس از آن جهت دیدن پاسخ درست و مقایسه  با پاسخ خود روی دکمه <b>{wayStr}</b> تلنگر بزنید."
        return guide

    def answerGuide(self,specificWay):
        guide = f"راهنمایی🔔: با بررسی  {specificWay} واژه، پاسخ خود و صوت و آوای 🔉 آن در پایین، درستی یا نادرستی پاسخ خود را با انتخاب دکمه ✅ یا ❌ برگزینید." 
        return guide

    def answerInTopOfCard(self,data,icon):
        if data == BtnS().persianTextEn:
            data = BtnS().persianText
            answer = f"پاسخ به {data}{icon}"
            lenngthAnswer = len(answer)
            answerInTopOfCard = answer.center(45 - lenngthAnswer) 
        else:
            answer = f"{icon}{data} پاسخ به "
            lenngthAnswer = len(answer)
            answerInTopOfCard = answer.center(72 - lenngthAnswer) 
 
        return answerInTopOfCard
    
    def wordCard(self,wKind,numW,numAll,standardizedWord,content,chapter,wordsPage,wordLink):
        newWordsMsg = f".{numW}/{numAll}                                         {wKind}.\n<b>{standardizedWord}</b>\n.Chapter : {content}\nSection : {chapter} \n{wordLink} برگ:{wordsPage}."
        return newWordsMsg

    def wordCardWithGuide(self,way,wKind,numW,numAll,standardizedWord,content,chapter,wordsPage,wordLink):
        print(way)
        newWordsMsg = f".{wordLink}{numW}/{numAll}                                         {wKind}.<b>{standardizedWord.center(63)}</b>\n.Chapter : {content}\nSection : {chapter} \nبرگ:{wordsPage}.\n{self.dash}\n{self.wordGuide(way)}"  
        print(way)
        return newWordsMsg
 
    def answerCard(self,data,icon,standardizedAnswer,answerLink):
        answerCard = f"<b>{self.answerInTopOfCard(data,icon)}</b>\n{answerLink} {standardizedAnswer.center(63)}."
        return answerCard

    def answerCardWithGuide(self,data,icon,standardizedAnswer,answerLink):
        guide = self.answerGuide(data)
        answerInTopOfCard = self.answerInTopOfCard(data,icon)
        newWordsMsg = f"<b>{answerInTopOfCard}</b>\n{standardizedAnswer.center(63)}\n{self.dash}\n{answerLink}{guide}"
        return newWordsMsg

    def reportMsg(self,nWorkedWords,nRWords,nWWrong,wrongWordsNpages,weekDay,day,month,year,houNMTraining,dateGriNextTraining,wordsSectionPosition):
        print(f"nRWords = {nRWords},nWorkedWords = {nWorkedWords}")
        percentageRight = dbContact.Percentage().percentage(nRWords,nWorkedWords)
        percentageWrong = dbContact.Percentage().percentage(nWWrong,nWorkedWords)
        graphRight = dbContact.Graph().graph(nRWords,nWorkedWords)
        graphWrong = dbContact.Graph().graph(nWWrong,nWorkedWords)
        guide = f"🔔 برای مرور واژهای کار شده می توانید پس از انتخاب ({PerBtn().getBack}) ،({PerBtn().reviewWords}) را انتخاب کنید. "

        daliyReport = f"<i>گزارش کارکردت، {self.firstName} عزیز 🌺🌸 در امروز:</i>\n{self.dash.center(14)}\nشمار وا‌ژه های کار شده : <b>{nWorkedWords}</b>\nشمار واژه های درست : <b>{nRWords}</b>\nشمار واژه های نادرست : <b>{nWWrong}</b>\n{self.dash.center(14)}\n<i>درصد درستی و نادرستی واژه ها :</i>\nدرستی <b>{graphRight} % {percentageRight} </b>\nنادرستی <b>{graphWrong} % {percentageWrong}</b> \n{self.dash.center(14)}\nفهرست واژه های نادرست امروز به همراه نشانی برگ در کتاب :\n <b>{wrongWordsNpages}</b>\n{self.dash.center(14)}\n👈یادگیری واژگان روزانه👉 بعدی و پسین در تاریخ <b> {weekDay} {day} {month} {year} </b>, در ساعت و زمان <b>{houNMTraining}</b> به وقت ایران، مصادف با <b>{dateGriNextTraining}</b>\n{self.dash}\n<i>بخش و شمار تمامی واژه ها در جعبه لایتنر :</i>\nشمار واژه ها در بخش نخست :<b>{wordsSectionPosition[0]} </b>\nشمار واژه ها در بخش دوم :<b> {wordsSectionPosition[1]} </b>\nشمار واژه ها در بخش سوم : <b>{wordsSectionPosition[2]} </b>\nشمار واژه ها در بخش چهارم :<b> {wordsSectionPosition[3]}</b> \nشمار واژه ها در بخش پنجم :‌<b>{wordsSectionPosition[4]}</b> \nشمار واژه ها در بخش ششم :<b>‌{wordsSectionPosition[5]}</b>\n{self.dash}\nشمار واژگان به صورت کامل یادگیری شده :<b>‌{wordsSectionPosition[6]}</b>\n{self.dash} \n<i>{guide}</i>\n@DeutschOhal\n"
        return daliyReport

    def chapterNSectionRev(self,content,chapter,word,counter,length,section,page,link):
        output = f"{link}.Chapter : {content}\nSection : {chapter}\n<b>{word.center(63)}</b>\n.برگ:{page}                         {section}: {length}/{counter+1}."
        
        return output

    def leitnerBoxrRev(self,content,chapter,word,counter,length,section,page,link):
        output = f".{link} {section}: {length}/{counter+1}\n<b>{word.center(63)}</b>\n.سرSection : {content}\nSection : {chapter}\nبرگ:{page}"
        return output


        # durationDays,counter,length,section,word,content,chapter,page,link
    def weakWordsRev(self,durationDays,counter,length,section,word,content,chapter,page,link):
        output = f"{link}.شمار روزها : {durationDays}         {section}:{counter+1}/{length}.\n<b>{word.center(63)}</b>\n.سرفصل : {content}\nفصل : {chapter}\n{page}:برگ"
        return output
        
    def addedWaytxt(self,way):
        print(way)
        if way == BtnS().persianText:
            output = f"روش {way} {self.firstName}  عزیز 🌺🌸 افزوده شد."
        else:
            output = f"روش  {self.firstName} {way} عزیز 🌺🌸 افزوده شد."
        return output

    def addWayBeforeTxt(self):
        output = f" روش دلخواهت جهت افزایش را {self.firstName} عزیز 🌺🌸 انتخاب کن."    
        return output
    
    def subtractWayTxt(self):
        output = f" روش دلخواهت جهت کاستن را {self.firstName} عزیز 🌺🌸 انتخاب کن."
        return output

    def subtractedWayBeforeTxt(self,way):
        if way == BtnS().persianText:
            output = f"روش {way} {self.firstName} عزیز 🌺🌸 کاسته شد."        
        else:
            output = f"روش {self.firstName} {way} عزیز 🌺🌸 کاسته شد."
        return output

    def pickOptionTxt(self):
        output = f"گزینه دلخواهت  {self.firstName} عزیز 🌺🌸 را انتخاب کن."
        return output

    def changeWayBeforeTxt(self,way):
        print(way)
        allWays = [BtnS().persianTextEn,BtnS().englishText,BtnS().deutschText,BtnS().synonymText]
        if isinstance(way,list):
            optionWay = [z for z in allWays if z not in way]
            optionWayStr = str(optionWay)
        else:
            optionWayStr = str(way)
        optionWayStr = optionWayStr.replace("[","")
        optionWayStr = optionWayStr.replace("]","")
        optionWayStr = optionWayStr.replace("'","")
        optionWayStr = optionWayStr.replace(","," یا")
        length = len(way)
        if length == 3:
            output = f"چنانچه تمایل داری {self.firstName} عزیز 🌺🌸 روش {optionWayStr} جهت دگرسانی به یکی از روش های دیگر  انتخاب کن."
        elif length == 1:
            output = f"چنانچه تمایل داری {self.firstName} عزیز 🌺🌸 روش های {optionWayStr} جهت دگرسانی به روش  دیگر  انتخاب کن."
        elif length <3 or length >1:
            output = f"چنانچه تمایل داری {self.firstName} عزیز 🌺🌸 روش های {optionWayStr} جهت دگرسانی به یکی از روش  های دیگر  انتخاب کن."
        return output

    def changeWayTxt(self,add,subtract):
        msg = f"دگرسانی  {self.firstName} عزیز 🌺🌸 از روش  {subtract}  به {add}  انجام شد."
        return msg

    def memberInCannel(self,chat_id):
        # output = f"ابتدا می بایست در کانال {chat_id}  {self.firstName} عزیز 🌺🌸 عضو شوی."
        output = f"برای ادامه دادن جهت استفاده از ربات، می بایست در کانال {chat_id} عضو شوی {self.firstName} عزیز 🌺🌸 ."
        return output


class MessageNVarDe:
    def __init__(self,firstName=None):
        # self.uILanguage = "En"
        self.firstName = firstName
        self.dash = "___________________________________"
        self.secondMenu = "Startseite"
        self.endReview = "Überprüfung beendet"
        self.endEditWay = "Die Bearbeitungsmethode ist beendet"


    def leitnerChanges(self):
        msg = f"Liebe/Lieber \nÄnderungen deiner Leitner Box!"
        return msg

    def wayStrCorrection(self,way):
        # print(ways)
        # self.wayEdit = ways
        try:
            wayEdit = [n for n in way if n !=BtnS().persianTextEn]
            # self.wayEdit.remove(BtnS().persianTextEn)
            wayEdit.append(BtnS().persianText)
        except:
            pass
        # print(way)
        wayStr = str(wayEdit)
        wayStr = wayStr.replace("[","")
        wayStr = wayStr.replace("]","")
        wayStr = wayStr.replace("'","")
        wayStr = wayStr.replace(","," oder")
        return wayStr
        
    def wordGuide(self,way):
        wayStr = self.wayStrCorrection(way)
        guide = f"Tipp🔔: Lesen Sie das Wort und hören Sie sich seine Aussprache an, indem Sie auf den Ton und das 🔉 unten tippen. Sagen Sie dann {wayStr} des Wortes und merken Sie sich das Wort, um die richtige Antwort zu sehen und mit Ihrer Antwort zu vergleichen. Tippen Sie auf  <b> {wayStr} </b> die Schaltfläche."
        return guide

    def answerGuide(self,specificWay):
        guide = f"Tipps 🔔: Geben Sie das Wort {specificWay}, Ihre Antwort und den Ton unten 🔉 an, rechts oder falsch. Wählen Sie Ihre Antwort aus, indem Sie auf die Schaltfläche ✅ oder ❌ klicken."
        return guide

    def answerInTopOfCard(self,data,icon):
        if data == BtnS().persianTextEn:
            data = BtnS().persianText
            answer = f"Antworte in {data}{icon}"
            lenngthAnswer = len(answer)
            answerInTopOfCard = answer.center(45 - lenngthAnswer) 
        else:
            answer = f"Antworte in {icon}{data}"
            lenngthAnswer = len(answer)
            answerInTopOfCard = answer.center(72 - lenngthAnswer) 
 
        return answerInTopOfCard
    
    def wordCard(self,wKind,numW,numAll,standardizedWord,content,chapter,wordsPage,wordLink):
        newWordsMsg = f".{numW}/{numAll}                                         {wKind}.\n<b>{standardizedWord}</b>\n.Kapitel : {content}\nAbschnitt : {chapter} \n{wordLink} Seite:{wordsPage}."
        return newWordsMsg

    def wordCardWithGuide(self,way,wKind,numW,numAll,standardizedWord,content,chapter,wordsPage,wordLink):
        print(way)
        newWordsMsg = f".{wordLink}{numW}/{numAll}                                         {wKind}.<b>{standardizedWord.center(63)}</b>\n.Kapitel : {content}\nAbschnitt : {chapter} \nSeite:{wordsPage}.\n{self.dash}\n{self.wordGuide(way)}"  
        print(way)
        return newWordsMsg
 
    def answerCard(self,data,icon,standardizedAnswer,answerLink):
        answerCard = f"<b>{self.answerInTopOfCard(data,icon)}</b>\n{answerLink} {standardizedAnswer.center(63)}."
        return answerCard

    def answerCardWithGuide(self,data,icon,standardizedAnswer,answerLink):
        guide = self.answerGuide(data)
        answerInTopOfCard = self.answerInTopOfCard(data,icon)
        newWordsMsg = f"<b>{answerInTopOfCard}</b>\n{standardizedAnswer.center(63)}\n{self.dash}\n{answerLink}{guide}"
        return newWordsMsg

    def reportMsg(self,nWorkedWords,nRWords,nWWrong,wrongWordsNpages,weekDay,day,month,year,houNMTraining,dateGriNextTraining,wordsSectionPosition):
        print(f"nRWords = {nRWords},nWorkedWords = {nWorkedWords}")
        percentageRight = dbContact.Percentage().percentage(nRWords,nWorkedWords)
        percentageWrong = dbContact.Percentage().percentage(nWWrong,nWorkedWords)
        graphRight = dbContact.Graph().graph(nRWords,nWorkedWords)
        graphWrong = dbContact.Graph().graph(nWWrong,nWorkedWords)
        guide = f"🔔 Nachdem Sie auf'{DeBtn().getBack}' getippt haben, können Sie '{DeBtn().reviewWords}' auswählen, um die von Ihnen eingegebenen Wörter zu überprüfen."

        daliyReport = f"Liebe/Lieber <i>{self.firstName}</i>🌺🌸  Melde deine Aktivitäten heute:  \n{self.dash.center(14)}\n Anzahl der geübten Wörter: <b> {nWorkedWords} </b> \n Anzahl der richtigen Wörter: <b>{nRWords}</b>\n Anzahl der falschen Wörter: <b>{nWWrong}</b>\n{self.dash.center(14)}\n<i> Prozentsatz der richtigen und falschen Wörter: </i> \n Richtig <b> {graphRight}% {percentageRight} </b> \n falsch <b> {graphWrong}% {percentageWrong} </b> \n {self.dash.center(14)} \n Liste der heute falschen Wörter mit der Seitenadresse im Buch: \n <b> {wrongWordsNpages} </b> \n {self.dash.center(14)} \n The 👉Lern den Wortschatz täglich👈 Weiter am <b> {weekDay} {day} {month} {year} </b>, um <b>{houNMTraining}</b> In der Zeit des Iran, Fällt zusammen mit <b>{dateGriNextTraining}</b> \n{self.dash}\n<i>Partition und Anzahl aller Wörter in der Lightner-Box: </i>\nWortnummer in der 1. Partition: <b>{wordsSectionPosition[0]} </b> \n Wortnummer in der 2. Partition: <b> {wordsSectionPosition[1]} </b> \n Wortnummer in der 3. Partition: <b> {wordsSectionPosition[2]} </b> \n Wortnummer in der 4. Partition: <b> {wordsSectionPosition[3]} </b> \n Wortnummer in der 5. Partition: <b> {wordsSectionPosition[4]} </b> \n Wortnummer in der 6. Partition: <b> {wordsSectionPosition[5]} </b> \n {self.dash} \n Anzahl der vollständig erlernten Vokabeln: <b> {wordsSectionPosition[6]} </b> \n {self.dash} \n <i> {guide} </i> \n @DeutschOhal \n"
        return daliyReport

    def chapterNSectionRev(self,content,chapter,word,counter,length,section,page,link):
        output = f"{link}.Kapitel : {content}\nAbschnitt : {chapter}\n<b>{word.center(63)}</b>\n.Seite:{page}                         {section}: {length}/{counter+1}."
        
        
        return output

    def leitnerBoxrRev(self,content,chapter,word,counter,length,section,page,link):
        output = f".{link} {section}: {length}/{counter+1}\n<b>{word.center(63)}</b>\n.Kapitel : {content}\nAbschnitt : {chapter}\nSeite:{page}"
        return output


        # durationDays,counter,length,section,word,content,chapter,page,link
    def weakWordsRev(self,durationDays,counter,length,section,word,content,chapter,page,link):
        output = f"{link}.Tage Nummer : {durationDays}         {section}:{counter+1}/{length}.\n<b>{word.center(63)}</b>\n.Kapitel : {content}\nAbschnitt : {chapter}\nSeite:{page}"

        return output
        
    def addedWaytxt(self,way):
        print(way)
        output = f"Liebe/Lieber {self.firstName} 🌺🌸, {way} Methode, hinzugefügt."
        return output

    def addWayBeforeTxt(self):
        output = f"Liebe/Lieber {self.firstName} 🌺🌸, wähle deine Lieblingsmethode zum Erhöhen."
        return output
    
    def subtractWayTxt(self):
        output = f"Liebe/Lieber  {self.firstName} 🌺🌸, wähle deinen bevorzugten Weg, um ihn zu reduzieren."
        return output

    def subtractedWayBeforeTxt(self,way):
        output = f"Liebe/Lieber {self.firstName} 🌺🌸, die Methode {way} wurde reduziert."
        return output

    def pickOptionTxt(self):
        output = f"Liebe/Lieber {self.firstName} 🌺🌸, wählen Sie Ihre Lieblingsoption."
        return output

    def changeWayBeforeTxt(self,way):
        print(way)
        allWays = [BtnS().persianTextEn,BtnS().englishText,BtnS().deutschText,BtnS().synonymText]
        if isinstance(way,list):
            optionWay = [z for z in allWays if z not in way]
            optionWayStr = str(optionWay)
        else:
            optionWayStr = str(way)
        optionWayStr = optionWayStr.replace("[","")
        optionWayStr = optionWayStr.replace("]","")
        optionWayStr = optionWayStr.replace("'","")
        optionWayStr = optionWayStr.replace(","," oder")
        length = len(way)
        if length == 3:
            output = f"Liebe/Lieber {self.firstName} 🌺🌸, Wenn Sie Methoden {optionWayStr} auswählen möchten, um zu einer der anderen Methoden zu wechseln." 

        elif length == 1:
            output = f"Lieber/Lieber {self.firstName} 🌺🌸, Wenn Sie die Methode {optionWayStr} auswählen möchten, um die andere Methode zu ändern."

        elif length <3 or length >1:
            output = f"Liebe/Lieber 🌺🌸, {self.firstName} Wenn Sie Methoden {optionWayStr} auswählen möchten, um eine der anderen Methoden zu ändern."

        return output

    def changeWayTxt(self,add,subtract):
        msg = f"Liebe/Lieber {self.firstName} 🌺🌸, der Wechsel wurde von {subtract} zu {add} vorgenommen."
        return msg

    def memberInCannel(self,chat_id):
        output = f"Lieber {self.firstName} 🌺🌸, um den Roboter weiterhin verwenden zu können, müssen Sie den Kanal {chat_id} abonnieren."
        return output



class MessageNVarEn:
    def __init__(self,firstName=None):
        # self.uILanguage = "En"
        self.firstName = firstName
        self.dash = "___________________________________"
        self.secondMenu = "Home"
        self.endReview = "Review finished"
        self.endEditWay = "Edit Method is finished"

    def leitnerChanges(self):
        msg = f"Dear \nchanges of your leitner box!"
        return msg
        
    def wayStrCorrection(self,way):
        # print(ways)
        # self.wayEdit = ways
        try:
            wayEdit = [n for n in way if n !=BtnS().persianTextEn]
            # self.wayEdit.remove(BtnS().persianTextEn)
            wayEdit.append(BtnS().persianText)
        except:
            pass
        # print(way)
        wayStr = str(wayEdit)
        wayStr = wayStr.replace("[","")
        wayStr = wayStr.replace("]","")
        wayStr = wayStr.replace("'","")
        wayStr = wayStr.replace(","," or")
        return wayStr
        
    def wordGuide(self,way):
        wayStr = self.wayStrCorrection(way)
        guide = f"Tip🔔: Read the word and listen to its  pronunciation by tap on the sound and its 🔉 at the bottom, then say {wayStr} of word and remember it, then to see the correct answer and compare with the your answer. Tap the <b> {wayStr} </b> button."
        return guide

    def answerGuide(self,specificWay):
        guide = f"Tips 🔔: Specify {specificWay} word, your answer, and its sound 🔉 at the bottom, right or wrong, choose your answer by selecting the ✅ or ❌ button."
        return guide

    def answerInTopOfCard(self,data,icon):
        if data == BtnS().persianTextEn:
            data = BtnS().persianText
            answer = f"Answer into {data}{icon}"
            lenngthAnswer = len(answer)
            answerInTopOfCard = answer.center(45 - lenngthAnswer) 
        else:
            answer = f"Answer into {icon}{data}"
            lenngthAnswer = len(answer)
            answerInTopOfCard = answer.center(72 - lenngthAnswer) 
 
        return answerInTopOfCard
    
    def wordCard(self,wKind,numW,numAll,standardizedWord,content,chapter,wordsPage,wordLink):
        newWordsMsg = f".{numW}/{numAll}                                         {wKind}.\n<b>{standardizedWord}</b>\n.Chapter : {content}\nAbschnitt : {chapter} \n{wordLink} Page:{wordsPage}."
        return newWordsMsg

    def wordCardWithGuide(self,way,wKind,numW,numAll,standardizedWord,content,chapter,wordsPage,wordLink):
        print(way)
        newWordsMsg = f".{wordLink}{numW}/{numAll}                                         {wKind}.<b>{standardizedWord.center(63)}</b>\n.Chapter : {content}\nSection : {chapter} \nPage:{wordsPage}.\n{self.dash}\n{self.wordGuide(way)}"  
        print(way)
        return newWordsMsg
 
    def answerCard(self,data,icon,standardizedAnswer,answerLink):
        answerCard = f"<b>{self.answerInTopOfCard(data,icon)}</b>\n{answerLink} {standardizedAnswer.center(63)}."
        return answerCard

    def answerCardWithGuide(self,data,icon,standardizedAnswer,answerLink):
        guide = self.answerGuide(data)
        answerInTopOfCard = self.answerInTopOfCard(data,icon)
        newWordsMsg = f"<b>{answerInTopOfCard}</b>\n{standardizedAnswer.center(63)}\n{self.dash}\n{answerLink}{guide}"
        return newWordsMsg

    def reportMsg(self,nWorkedWords,nRWords,nWWrong,wrongWordsNpages,weekDay,day,month,year,houNMTraining,dateGriNextTraining,wordsSectionPosition):
        print(f"nRWords = {nRWords},nWorkedWords = {nWorkedWords}")
        percentageRight = dbContact.Percentage().percentage(nRWords,nWorkedWords)
        percentageWrong = dbContact.Percentage().percentage(nWWrong,nWorkedWords)
        graphRight = dbContact.Graph().graph(nRWords,nWorkedWords)
        graphWrong = dbContact.Graph().graph(nWWrong,nWorkedWords)
        guide = f"🔔 After tap on '{EnBtn().getBack}' You can select '{EnBtn().reviewWords}' to review the words you have done."

        daliyReport = f" Dear {self.firstName}  🌺🌸 <i> Report your activities, Today: </i> \n {self.dash.center(14)} \n Number of Practiced Words: <b> {nWorkedWords} </b> \n Number of correct words: <b> {nRWords} </b> \n Number of incorrect words: <b> {nWWrong} </b> \n {self.dash.center(14)} \n <i> percentage of correct and incorrect Words: </i> \n  Correct <b> {graphRight}% {percentageRight} </b> \n  incorrect <b> {graphWrong}% {percentageWrong} </b> \n  {self.dash.center(14)} \n  List of incorrect words today with the page address in the book: \n  <b> {wrongWordsNpages} </b> \n  {self.dash.center(14)} \n The 👉Learn Vocabulary Daily👈 next on <b> { weekDay} {day} {month} {year} </b>, at <b> {houNMTraining} </b> In the time of Iran, Coincides with <b>{dateGriNextTraining}</b>\n {self.dash} \n <i> Partition and number of all words in the Lightner box: </i> \n  Words number in 1Th partition: <b> {wordsSectionPosition[0]} </b> \n  Words number in 2Th partition: <b> {wordsSectionPosition[1]} </b> \n  Words number in 3Th partition: <b> {wordsSectionPosition[2]} </b> \n  Words number in 4Th partition: <b> {wordsSectionPosition[3]} </b> \n  Words number in 5Th partition:  <b> {wordsSectionPosition[4]} </b> \n  Words number in 6Th partition: <b> {wordsSectionPosition[5]} </b> \n {self.dash} \n  Number of fully learned vocabulary: <b> {wordsSectionPosition[6]} </b> \n {self.dash} \n  <i> {guide} </i> \n @DeutschOhal \n"
        return daliyReport

    def chapterNSectionRev(self,content,chapter,word,counter,length,section,page,link):
        output = f"{link}.Chapter : {content}\nSection : {chapter}\n<b>{word.center(63)}</b>\n.Page:{page}                         {section}: {length}/{counter+1}."
        
        
        return output

    def leitnerBoxrRev(self,content,chapter,word,counter,length,section,page,link):
        output = f".{link} {section}: {length}/{counter+1}\n<b>{word.center(63)}</b>\n.Chapter : {content}\nSection : {chapter}\nPage:{page}"
        return output


        # durationDays,counter,length,section,word,content,chapter,page,link
    def weakWordsRev(self,durationDays,counter,length,section,word,content,chapter,page,link):
        output = f"{link}.Days Number : {durationDays}         {section}:{counter+1}/{length}.\n<b>{word.center(63)}</b>\n.Chapter : {content}\nSection : {chapter}\nPage:{page}"

        return output
        
    def addedWaytxt(self,way):
        print(way)
        output = f"Dear {self.firstName} 🌺🌸, {way} Method, added."
        return output

    def addWayBeforeTxt(self):
        output = f"Dear {self.firstName} 🌺🌸, Choose your favorite Method to increase."
        return output
    
    def subtractWayTxt(self):
        output = f"Dear {self.firstName} 🌺🌸, Choose your favorite Method to reduce it."
        return output

    def subtractedWayBeforeTxt(self,way):
        output = f"Dear {self.firstName} 🌺🌸, The Method {way} Has been reduced."
        return output

    def pickOptionTxt(self):
        output = f"Dear {self.firstName} 🌺🌸, Select your favorite option."
        return output

    def changeWayBeforeTxt(self,way):
        print(way)
        allWays = [BtnS().persianTextEn,BtnS().englishText,BtnS().deutschText,BtnS().synonymText]
        if isinstance(way,list):
            optionWay = [z for z in allWays if z not in way]
            optionWayStr = str(optionWay)
        else:
            optionWayStr = str(way)
        optionWayStr = optionWayStr.replace("[","")
        optionWayStr = optionWayStr.replace("]","")
        optionWayStr = optionWayStr.replace("'","")
        optionWayStr = optionWayStr.replace(","," or")
        length = len(way)
        if length == 3:
            output = f"Dear {self.firstName} 🌺🌸, If you wish select methods  {optionWayStr} to change to one of the other methods"
        elif length == 1:
            output = f"Dear {self.firstName} 🌺🌸, If you wish select method{optionWayStr} to change the other method."
        elif length <3 or length >1:
            output = f"Dear 🌺🌸, {self.firstName} If you wish Select methods {optionWayStr} to change one of the other methods."
        return output

    def changeWayTxt(self,add,subtract):
        msg = f"Dear {self.firstName} 🌺🌸, Changing was done from {subtract} to {add}."
        return msg

    def memberInCannel(self,chat_id):
        output = f"Dear {self.firstName} 🌺🌸,  To continue using the robot, you need to subscribe to channel {chat_id}."
        return output

