import json
import sys
sys.path.append("../")


from mainV2.base import Buttons

from mainV2.base.ButtonsA import ButtonSame as ABtnS

from mainV2.base.Buttons import ButtonSame as BtnS
from mainV2.base.Buttons import ButtonDe as DeBtn
from mainV2.base.ButtonsA import ButtonAdminDe as DeBtnA
from mainV2.base.Buttons import ButtonEn as EnBtn
from mainV2.base.ButtonsA import ButtonAdminEn as EnBtnA
from mainV2.base.Buttons import ButtonPer as PerBtn
from mainV2.base.ButtonsA import ButtonAdminPer as PerBtnA




class DeKeysA:
    def __init__(self):
        btn = DeBtn()
        btnA = DeBtnA()
        #6 times
        self.adminKeys = json.dumps ({"keyboard": [[btnA.changeUserType, btnA.sendToAll, btnA.reportToday, btnA.reportAll], [btnA.opinionsA,btnA.apply], [btn.getBack]]," resize_keyboard ": True}) 
        # new ##
        # opinions #
        self.opinionKeys = json.dumps ({"keyboard": [[btnA.todayOpinions,btnA.newOpinions],[btnA.oldOpinions,btnA.opinionTrackNum],[btnA.opUserBase], [btnA.getBackToDesk]]," resize_keyboard ": True}) 
        #2 times
        self.getBackDesk = json.dumps({"keyboard":[[btnA.getBackToDesk]],"resize_keyboard":True})
        #1 time
        self.yNDoubleKomma = json.dumps({"keyboard":[[btnA.noDoubleComma,btnA.yesSendIt]],"resize_keyboard":True}) 
        #3 times
        self.sendChangeUser =  json.dumps({"keyboard": [[btnA.send], [btnA.getBackToDesk]], "resize_keyboard": True})
        #4 times
        self.firstMenu = json.dumps ({"keyboard": [[btnA.admin, btn.startLearning], [btn.aboutBotNew, btn.uILangNKeyEditNew]], " resize_keyboard ": True}) 
        #16 times
        self.secondMenu = json.dumps({"keyboard":[[btnA.admin,btn.reviewWords],[btn.wordsNum,btn.wayEdit,btn.account],[btn.timeLearnEdit,btn.reportActivity],[btn.deleteBot,btn.aboutBot,btn.uILangNKeyEdit],[btn.opinion]],"resize_keyboard":True})
        #1 time
        self.wordsNumNew = json.dumps({"keyboard":[[BtnS().threeNew],[BtnS().twoNew],[BtnS().oneNew],[ABtnS().fiveNew,ABtnS().tenNew,ABtnS().fifteenNew,ABtnS().twentyNew]],"resize_keyboard":True})
        #1 time 
        self.waysNew = json.dumps({"keyboard":[[BtnS().deutschNew,BtnS().englishNew,BtnS().synonymNew],[ABtnS().allTogetherNew,BtnS().persianNew]],"resize_keyboard":True})  
        #1 time
        self.ways =  json.dumps({"keyboard":[[BtnS().deutsch,BtnS().english,BtnS().synonym],[ABtnS().allTogether,BtnS().persian],[btn.getBack]],"resize_keyboard":True})
        #1 time
        self.wordsNum = json.dumps({"keyboard":[[BtnS().three],[BtnS().two],[BtnS().one],[ABtnS().five,ABtnS().ten,ABtnS().fifteen,ABtnS().twenty],[btn.getBack]],"resize_keyboard":True})


class EnKeysA:
    def __init__(self):
        btn = EnBtn()
        btnA = EnBtnA()
        #6 times
        self.adminKeys = json.dumps ({"keyboard": [[btnA.changeUserType, btnA.sendToAll, btnA.reportToday, btnA.reportAll], [btnA.opinionsA,btnA.apply], [btn.getBack]]," resize_keyboard ": True}) 
        # new ##
        # opinions #
        self.opinionKeys = json.dumps ({"keyboard": [[btnA.todayOpinions,btnA.newOpinions],[btnA.oldOpinions,btnA.opinionTrackNum],[btnA.opUserBase], [btnA.getBackToDesk]]," resize_keyboard ": True}) 
        #2 times
        self.getBackDesk = json.dumps({"keyboard":[[btnA.getBackToDesk]],"resize_keyboard":True})
        #1 time
        self.yNDoubleKomma = json.dumps({"keyboard":[[btnA.noDoubleComma,btnA.yesSendIt]],"resize_keyboard":True}) 
        #3 times
        self.sendChangeUser =  json.dumps({"keyboard": [[btnA.send], [btnA.getBackToDesk]], "resize_keyboard": True})
        #4 times
        self.firstMenu = json.dumps ({"keyboard": [[btnA.admin, btn.startLearning], [btn.aboutBotNew, btn.uILangNKeyEditNew]], " resize_keyboard ": True}) 
        #16 times
        self.secondMenu = json.dumps({"keyboard":[[btnA.admin,btn.reviewWords],[btn.wordsNum,btn.wayEdit,btn.account],[btn.timeLearnEdit,btn.reportActivity],[btn.deleteBot,btn.aboutBot,btn.uILangNKeyEdit],[btn.opinion]],"resize_keyboard":True})
        #1 time
        self.wordsNumNew = json.dumps({"keyboard":[[BtnS().threeNew],[BtnS().twoNew],[BtnS().oneNew],[ABtnS().fiveNew,ABtnS().tenNew,ABtnS().fifteenNew,ABtnS().twentyNew]],"resize_keyboard":True})
        #1 time 
        self.waysNew = json.dumps({"keyboard":[[BtnS().deutschNew,BtnS().englishNew,BtnS().synonymNew],[ABtnS().allTogetherNew,BtnS().persianNew]],"resize_keyboard":True})  
        #1 time
        self.ways =  json.dumps({"keyboard":[[BtnS().deutsch,BtnS().english,BtnS().synonym],[ABtnS().allTogether,BtnS().persian],[btn.getBack]],"resize_keyboard":True})
        #1 time
        self.wordsNum = json.dumps({"keyboard":[[BtnS().three],[BtnS().two],[BtnS().one],[ABtnS().five,ABtnS().ten,ABtnS().fifteen,ABtnS().twenty],[btn.getBack]],"resize_keyboard":True})

class PerKeysA:
    def __init__(self):
        btn = PerBtn()
        btnA = PerBtnA()
        #6 times
        self.adminKeys = json.dumps ({"keyboard": [[btnA.changeUserType, btnA.sendToAll, btnA.reportToday, btnA.reportAll], [btnA.opinionsA,btnA.apply], [btn.getBack]]," resize_keyboard ": True}) 
        # new ##
        # opinions #
        self.opinionKeys = json.dumps ({"keyboard": [[btnA.todayOpinions,btnA.newOpinions],[btnA.oldOpinions,btnA.opinionTrackNum],[btnA.opUserBase], [btnA.getBackToDesk]]," resize_keyboard ": True})    


        #2 times
        self.getBackDesk = json.dumps({"keyboard":[[btnA.getBackToDesk]],"resize_keyboard":True})
        #1 time
        self.yNDoubleKomma = json.dumps({"keyboard":[[btnA.noDoubleComma,btnA.yesSendIt]],"resize_keyboard":True}) 
        #3 times
        self.sendChangeUser =  json.dumps({"keyboard": [[btnA.send], [btnA.getBackToDesk]], "resize_keyboard": True})
        #4 times
        self.firstMenu = json.dumps ({"keyboard": [[btnA.admin, btn.startLearning], [btn.aboutBotNew, btn.uILangNKeyEditNew]], " resize_keyboard ": True}) 
        #16 times
        self.secondMenu = json.dumps({"keyboard":[[btnA.admin,btn.reviewWords],[btn.wordsNum,btn.wayEdit,btn.account],[btn.timeLearnEdit,btn.reportActivity],[btn.deleteBot,btn.aboutBot,btn.uILangNKeyEdit],[btn.opinion]],"resize_keyboard":True})
        #1 time
        self.wordsNumNew = json.dumps({"keyboard":[[BtnS().threeNew],[BtnS().twoNew],[BtnS().oneNew],[ABtnS().fiveNew,ABtnS().tenNew,ABtnS().fifteenNew,ABtnS().twentyNew]],"resize_keyboard":True})
        #1 time 
        self.waysNew = json.dumps({"keyboard":[[BtnS().deutschNew,BtnS().englishNew,BtnS().synonymNew],[ABtnS().allTogetherNew,BtnS().persianNew]],"resize_keyboard":True})  
        #1 time
        self.ways =  json.dumps({"keyboard":[[BtnS().deutsch,BtnS().english,BtnS().synonym],[ABtnS().allTogether,BtnS().persian],[btn.getBack]],"resize_keyboard":True})
        #1 time
        self.wordsNum = json.dumps({"keyboard":[[BtnS().three],[BtnS().two],[BtnS().one],[ABtnS().five,ABtnS().ten,ABtnS().fifteen,ABtnS().twenty],[btn.getBack]],"resize_keyboard":True})
        ################################ inlineKeys ########################################
        self.dataWordLearn = json.dumps({'inline_keyboard': [[{'text': BtnS().persian,'callback_data':BtnS().persianText},{'text': BtnS().deutsch, 'callback_data':BtnS().deutschText},{'text': BtnS().synonym, 'callback_data':BtnS().synonymText},{'text': BtnS().english, 'callback_data':BtnS().englishText}],[{'text': BtnS().crossCheck, 'callback_data':BtnS().crossCheckCB},{'text': BtnS().check, 'callback_data':BtnS().checkCB}]],"resize_keyboard":True})