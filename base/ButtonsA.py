import sys
sys.path.append("../")
from mainV2.base.Buttons import ButtonSame as BtnS

class ButtonAdminPer:
    def __init__(self):

        self.getBackToDesk = "بازگشت به میز سرپرست و ادمین"
        self.admin = "گردانش ⚙️"
        self.apply = "ورزانش و اعمال"
        self.reportAll = "گزارش تکاپو فراگیر"
        self.reportToday = "گزارش تکاپو امروز"
        self.changeUserType = "دگرسانی گونه کاربر"
        self.sendToAll = "پیام به همه"
        self.noDoubleComma = ",, خیر ,,"
        self.yesSendIt = "بله،گسیل شود!"
        self.send = "گسیل"
        self.opinionsA = "نظرات"
        self.opUserBase = "نظرات کاربر محور"
        self.todayOpinions = "نظرات امروز"
        self.newOpinions = "نظرات به ترتیب جدیدترین"
        self.oldOpinions ="نظرات به ترتیب قدیمی ترین"
        self.opinionTrackNum ="نظرات براساس کد پیگیری"
        self.arrButtonAdminPer = [self.opinionTrackNum,self.oldOpinions,self.newOpinions,self.todayOpinions,self.opinionsA,self.opUserBase,self.getBackToDesk,self.admin,self.apply,self.reportAll,self.reportToday,self.changeUserType,self.sendToAll,self.noDoubleComma,self.yesSendIt,self.send]
        self.avoidMsgs = [self.opinionTrackNum,self.oldOpinions,self.newOpinions,self.todayOpinions,self.opinionsA,self.opUserBase,self.getBackToDesk ,self.admin,self.apply ,self.reportAll,self.reportToday,self.changeUserType,self.sendToAll,self.noDoubleComma,self.yesSendIt,self.send]


class ButtonAdminDe:
    def __init__(self):

        self.getBackToDesk = "Zurück zum Admin-Desk"
        self.admin = "Admin ⚙️"
        self.apply = "anwenden"
        self.reportAll = "Bericht über alle Fortschritte"
        self.reportToday = "Bericht über den heutigen Fortschritt"
        self.changeUserType = "Eingabe von Benutzeränderungen"
        self.sendToAll = "Nachricht an alle"
        self.noDoubleComma = ",, Nein ,,"
        self.yesSendIt = "Ja, sende es!"
        self.send = "Senden"
        self.opinionsA = "Vorschläge"
        self.opUserBase = "Nutzerbasis Vorschläge"
        self.todayOpinions = "Heute Vorschläge"
        self.newOpinions = "Kommentare in der letzten Reihenfolge"
        self.oldOpinions ="Kommentare in der ältesten Reihenfolge"
        self.opinionTrackNum ="Kommentare basieren auf Tracking-Code"
        self.arrButtonAdminDe = [self.opinionTrackNum,self.oldOpinions,self.newOpinions,self.todayOpinions,self.opinionsA,self.opUserBase,self.getBackToDesk,self.admin,self.apply,self.reportAll,self.reportToday,self.changeUserType,self.sendToAll,self.noDoubleComma,self.yesSendIt,self.send]
        self.avoidMsgs = [self.opinionTrackNum,self.oldOpinions,self.newOpinions,self.todayOpinions,self.opinionsA,self.opUserBase,self.getBackToDesk ,self.admin,self.apply ,self.reportAll,self.reportToday,self.changeUserType,self.sendToAll,self.noDoubleComma,self.yesSendIt,self.send]

class ButtonAdminEn:
    def __init__(self):
        
        self.getBackToDesk = "Back to Admin desk"
        self.admin = "Admin ⚙️"
        self.apply = "Apply"
        self.reportAll = "Reporting all Progress"
        self.reportToday = "Reporting Today's Progress"
        self.changeUserType = "User change typing"
        self.sendToAll = "Message to All"
        self.noDoubleComma = ",, No ,,"
        self.yesSendIt ="Yes, send It!"
        self.send = "Send"
        self.opinionsA = "Sugesstions"
        self.opUserBase = "User base Sugesstions"
        self.todayOpinions = "Today Sugesstions"
        self.newOpinions = "Sugesstions in the latest order"
        self.oldOpinions ="Sugesstions in the oldest order"
        self.opinionTrackNum ="Sugesstions based on tracking code"
        self.arrButtonAdminEn = [self.opinionTrackNum,self.oldOpinions,self.newOpinions,self.todayOpinions,self.opinionsA,self.opUserBase,self.getBackToDesk,self.admin,self.apply,self.reportAll,self.reportToday,self.changeUserType,self.sendToAll,self.noDoubleComma,self.yesSendIt,self.send]
        self.avoidMsgs = [self.opinionTrackNum,self.oldOpinions,self.newOpinions,self.todayOpinions,self.opinionsA,self.opUserBase,self.getBackToDesk ,self.admin,self.apply ,self.reportAll,self.reportToday,self.changeUserType,self.sendToAll,self.noDoubleComma,self.yesSendIt,self.send]

class ButtonSame:
    def __init__(self):

        self.fiveNew = "5 ♨️"
        self.tenNew = "10 ♨️"
        self.fifteenNew = "15 ♨️"
        self.twentyNew = "20 ♨️"
        self.allTogetherNew = "all together📒📕📘📔 ♨️"
        self.five = "-5-"
        self.ten = "-10-"
        self.fifteen = "-15-"
        self.twenty = "-20-"
        self.allTogether ="all together📒📕📘📔"
        self.avoidMsgs = [ self.fiveNew,self.tenNew,self.fifteenNew,self.twentyNew , self.allTogetherNew ,self.five,self.ten,self.fifteen,self.twenty,self.allTogether] 