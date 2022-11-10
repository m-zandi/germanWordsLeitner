import json
import sys
sys.path.append("../")
from mainV2.base import Buttons
from mainV2.base.Buttons import ButtonSame as BtnS
from mainV2.base.Buttons import ButtonDe as DeBtn
from mainV2.base.Buttons import ButtonEn as EnBtn
from mainV2.base.Buttons import ButtonPer as PerBtn
from mainV2.base.Txt import MessageNVarPer as MNVPer
from mainV2.base.Txt import MessageNVarEn as MNVEn
from mainV2.base.Txt import MessageNVarDe as MNVDe

from mainV2.set import dbContact as DbC


class SKeys:
    def __init__(self,btn =None,mnv=None):
        #including comment once
        #2 times
        self.btn = btn
        self.mnv = mnv
        self.btnS = BtnS()
        self.uI = json.dumps({"keyboard":[[self.btnS.keyNMsgDe],[self.btnS.keyNMsgEn],[self.btnS.keyNMsgPer]],"resize_keyboard":True})
        #1 time
        self.waysNew = json.dumps({"keyboard":[[self.btnS.deutschNew],[self.btnS.englishNew],[self.btnS.synonymNew],[self.btnS.persianNew]],"resize_keyboard":True}) 
        #6 times
        # self.lampKeys = json.dumps({"keyboard":[[self.btnS.lamp]],"resize_keyboard":True})
        #4 times
        self.rW = json.dumps({"keyboard":[[self.btnS.crossCheck,self.btnS.check]],"resize_keyboard":True}) 
        self.removeKeyboard = json.dumps({"remove_keyboard": True})
        self.numWordsNew = json.dumps({"keyboard":[[self.btnS.threeNew,self.btnS.twoNew,self.btnS.oneNew],[btn.getBack]],"resize_keyboard":True})
        ################################ inlineKeys ########################################

    def wordKeys(self,ways):
        print(f"ways = {ways}")
        elements = []
        per = {'text': self.btnS.persianText,'callback_data':self.btnS.persianTextEn}
        de = {'text': self.btnS.deutschText, 'callback_data':self.btnS.deutschText}
        en = {'text': self.btnS.englishText, 'callback_data':self.btnS.englishText}
        syn = {'text': self.btnS.synonymText, 'callback_data':self.btnS.synonymText}

        identifyArray = [{self.btnS.persianTextEn:per},{self.btnS.deutschText:de},{self.btnS.synonymText:syn},{self.btnS.englishText:en}]
        for z in identifyArray:
            for x,y in z.items():
                if x in ways:
                    elements.append(y)
        print(f"elements = {elements}")
        output = json.dumps({'inline_keyboard': [elements],"resize_keyboard":True})
        return output

    def answerKeys(self,data,ways,wordBtn):
        print(f" data = {data}\n ways = {ways}")
        keys = ways
        keys.append(self.btnS.wordCB)
        elements = []
        keys.remove(data)
        print(f"keys = {keys}")
        per = {'text': self.btnS.persianText,'callback_data':self.btnS.persianTextEn}
        de = {'text': self.btnS.deutschText, 'callback_data':self.btnS.deutschText}
        en = {'text': self.btnS.englishText, 'callback_data':self.btnS.englishText}
        syn = {'text': self.btnS.synonymText, 'callback_data':self.btnS.synonymText}
        word = {'text': wordBtn , 'callback_data':self.btnS.wordCB}

        identifyArray = [{self.btnS.persianTextEn:per},{self.btnS.deutschText:de},{self.btnS.synonymText:syn},{self.btnS.englishText:en},{self.btnS.wordCB:word}]
        for z in identifyArray:
            for x,y in z.items():
                if x in keys:
                    elements.append(y)
        print(f"elements = {elements}")
        crsCheck= {'text': self.btnS.crossCheck, 'callback_data':self.btnS.crossCheckCB}
        check = {'text': self.btnS.check, 'callback_data':self.btnS.checkCB}
        output = json.dumps({'inline_keyboard': [elements,[crsCheck,check]],"resize_keyboard":True})

        return output

    def reviewOne(self,waysRevType,ways,length,btnGetBack,call_data):
        elements = []
        de = {'text': self.btnS.deutschText, 'callback_data':waysRevType[0]}
        en = {'text': self.btnS.englishText, 'callback_data':waysRevType[1]}
        syn = {'text': self.btnS.synonymText, 'callback_data':waysRevType[2]}
        per = {'text': self.btnS.persianText,'callback_data':waysRevType[3]}
        # wWCB = [self.btnS.deutschWWCB,self.btnS.englishWWCB,self.btnS.synonymWWCB,self.btnS.persianEnWWCB] 
        print(f"ways = {ways}")    
        identifyArray = [{self.btnS.persianTextEn:per},{self.btnS.deutschText:de},{self.btnS.synonymText:syn},{self.btnS.englishText:en}]       
        for z in identifyArray:
            for x,y in z.items():
                if x in ways:
                    elements.append(y)
        print(f"elements = {elements}")
        getBack = {'text': btnGetBack,'callback_data':call_data}
        output = json.dumps({'inline_keyboard': [elements,[getBack]],"resize_keyboard":True})
        return output

    def changeWayKeys(self,way,txtBtn,call_data):
        # getBack = [{'text': self.btn.getBack,'callback_data':MNVPer().secondMenu}]
        getBack = [{'text': txtBtn,'callback_data':call_data}]
        print(f"way = {way}")
        allChangeKeys = [(self.btnS.deutschPersian,self.btnS.deutschText,self.btnS.persianTextEn),(self.btnS.deutschEnlish,self.btnS.deutschText,self.btnS.englishText),(self.btnS.deutschSynonym,self.btnS.deutschText,self.btnS.synonymText),(self.btnS.persianDeutsch,self.btnS.persianTextEn,self.btnS.deutschText),(self.btnS.persianEnlish,self.btnS.persianTextEn,self.btnS.englishText),(self.btnS.perisanSynonym,self.btnS.persianTextEn,self.btnS.synonymText),(self.btnS.enlishDeutsch,self.btnS.englishText,self.btnS.deutschText),(self.btnS.englishPersian,self.btnS.englishText,self.btnS.persianTextEn),(self.btnS.englishSynonym,self.btnS.englishText,self.btnS.synonymText),(self.btnS.synonymDeutsch,self.btnS.synonymText,self.btnS.deutschText),(self.btnS.synonymPersian,self.btnS.synonymText,self.btnS.persianTextEn),(self.btnS.synonymEnlish,self.btnS.synonymText,self.btnS.englishText)]
        # allChangeKeys = self.btnS.allChangeKeys
        keysArray = []
        for z in allChangeKeys:
            if z[1] in way and z[2] in way:
                pass
            elif z[1] in way :
                keysArray.append({'text': z[0], 'callback_data':z[0]})
        print(f"keysArray = {keysArray}")

        arrA = []
        arrB = []
        for i in range(len(keysArray)):
                arrA.append(keysArray[i])
                # print(f'i = {i}')
                # print(array[i])
                if (i+1)%1 ==0  and len(keysArray) != 2:
                    # print(array[i])
                    arrB.append(arrA)
                    arrA =[]
                elif (i+1)%1 !=0 and (i+1) == len(keysArray) and len(keysArray) != 2:
                    # print(array[i])
                    arrB.append(arrA)
                    arrA =[]
                elif len(keysArray) == 2:
                    arrB = arrA
        print(f"arrB = {arrB}")
        arrB.append(getBack)
        output = json.dumps({'inline_keyboard': arrB,"resize_keyboard":True})  
        return output

    def beforeNextKeys(self,counter,length,typeRev):
        print(f"typeRev = {typeRev}")
        beforeChapNS = {'text': self.btn.beforeWordChapNS, 'callback_data':self.btn.beforeWordChapNS}
        nextChapNS = {'text': self.btn.nextWordChapNS,'callback_data':self.btn.nextWordChapNS}        

        beforeLeitBP = {'text': self.btn.beforeWordLeitBP, 'callback_data':self.btn.beforeWordLeitBP}
        nextLeitBP = {'text': self.btn.nextWordLeitBP,'callback_data':self.btn.nextWordLeitBP}

        beforeWW = {'text': self.btn.beforeWordWW, 'callback_data':self.btn.beforeWordWW}
        nextWW = {'text': self.btn.nextWordWW,'callback_data':self.btn.nextWordWW}
        
        # wordBCs = [{self.btnS.wordChapNSCB:self.btn.chapterNSection},{self.btnS.wordLeitBPCB:self.btn.leitnerBoxParts},{self.btnS.wordWWCB:self.btn.weakWords},{self.btn.nextWordChapNS:self.btn.chapterNSection},{self.btn.beforeWordChapNS:self.btn.chapterNSection},{self.btn.nextWordLeitBP:self.btn.leitnerBoxParts},{self.btn.beforeWordLeitBP:self.btn.leitnerBoxParts},{self.btn.nextWordWW:self.btn.weakWords},{self.btn.beforeWordWW:self.btn.weakWords}]

        counterIf = counter +1

        output = ""
        if counterIf == length and counterIf == 1:
            return False

        elif typeRev == self.btn.chapterNSection or typeRev == self.btnS.wordChapNSCB:
            if  counterIf == length:
                output = [beforeChapNS]
                # return [beforeChapNS]
            elif counterIf !=length and counterIf == 1:
                # return [nextChapNS]
                output = [nextChapNS]
            elif counterIf !=length and counterIf !=1:
                output = [beforeChapNS,nextChapNS]
                # return [beforeChapNS,nextChapNS]

        elif typeRev == self.btn.leitnerBoxParts or typeRev == self.btnS.wordLeitBPCB:
            if counterIf == length:
                # return [beforeLeitBP]
                output = [beforeLeitBP]
            elif counterIf !=length and counterIf == 1:
                output = [nextLeitBP]
                # return [nextLeitBP]
            elif counterIf !=length and counterIf !=1:
                output = [beforeLeitBP,nextLeitBP]
                # return [beforeLeitBP,nextLeitBP]
        
        elif typeRev == self.btn.weakWords or typeRev == self.btnS.wordWWCB:
            if counterIf == length:
                output = [beforeWW]
                # return [beforeWW]
            elif counterIf !=length and counterIf == 1:
                output = [nextWW]
                # return [nextWW]
            elif counterIf !=length and counterIf !=1:
                # return [beforeWW,nextWW]
                output = [beforeWW,nextWW]
        # outputLast = [output,[getBack]]
        # output.append(getBack)
        print(f'output beforeNextKeys = {output}')
        return output    

    def reviewMoreThanOne(self,counter,waysRevTypeCB,ways,length,msg):
        elements = []
        print(f'msg = {msg}')
        # print(f"chNSWCB = {waysRevTypeCB}")
        # print(f"chNSWCB[0] = {chNSWCB[0]}")
        # print(f"chNSWCB[1] = {chNSWCB[1]}")
        # print(f"chNSWCB[2] = {chNSWCB[2]}")
        # print(f"chNSWCB[3] = {chNSWCB[3]}")
        de = {'text': self.btnS.deutschText, 'callback_data':waysRevTypeCB[0]}
        en = {'text': self.btnS.englishText, 'callback_data':waysRevTypeCB[1]}
        syn = {'text': self.btnS.synonymText, 'callback_data':waysRevTypeCB[2]}
        per = {'text': self.btnS.persianText,'callback_data':waysRevTypeCB[3]}

        # nextArray = [{self.btn.chapterNSection:self.btn.nextWordChapNS},{self.btn.leitnerBoxParts:self.btn.nextWordLeitBP},{self.btn.weakWords:self.btn.nextWordWW}]
        # wordBCs = [{self.btnS.wordChapNSCB:self.btn.chapterNSection},{self.btnS.wordLeitBPCB:self.btn.leitnerBoxParts},{self.btnS.wordWWCB:self.btn.weakWords},{self.btn.nextWordChapNS:self.btn.chapterNSection},{self.btn.beforeWordChapNS:self.btn.chapterNSection},{self.btn.nextWordLeitBP:self.btn.leitnerBoxParts},{self.btn.beforeWordLeitBP:self.btn.leitnerBoxParts},{self.btn.nextWordWW:self.btn.weakWords},{self.btn.beforeWordWW:self.btn.weakWords}]
        wordBCs = [{self.btn.nextWordChapNS:self.btn.chapterNSection},{self.btn.beforeWordChapNS:self.btn.chapterNSection},{self.btn.nextWordLeitBP:self.btn.leitnerBoxParts},{self.btn.beforeWordLeitBP:self.btn.leitnerBoxParts},{self.btn.nextWordWW:self.btn.weakWords},{self.btn.beforeWordWW:self.btn.weakWords}]

        typeRev = ''
        for z in wordBCs:
            for x,y in z.items():
                if msg == x:
                    typeRev = y
            
        if typeRev == '':
            typeRev = msg
        print(f"typeRev = {typeRev}")
        nextBeforeKeys = self.beforeNextKeys(counter,length,typeRev)
        getBack = {'text': self.btn.getBack,'callback_data':self.mnv.endReview}
         ######
        identifyArray = [{self.btnS.persianTextEn:per},{self.btnS.deutschText:de},{self.btnS.synonymText:syn},{self.btnS.englishText:en}]
        for z in identifyArray:
            for x,y in z.items():
                if x in ways:
                    elements.append(y)
        print(f"elements = {elements}")
        # output = json.dumps({'inline_keyboard': [elements,[next]],"resize_keyboard":True})
        # output = json.dumps({'inline_keyboard': [elements],"resize_keyboard":True})
        output = json.dumps({'inline_keyboard': [elements,nextBeforeKeys,[getBack]],"resize_keyboard":True})
        print(output)

        return output    

    def reviewAnswer(self,reviewsKeysCB,ways,counter,length,data,wordType):
        print(f" data = {data}\n ways = {ways}")
        print(f"reviewsKeysCB[4] = {reviewsKeysCB[4]}")
        keys = ways
        if isinstance (keys,str):
            keys = [ways]
        keys.append(wordType)
        elements = []
        keys.remove(data)
        de = {'text': self.btnS.deutschText, 'callback_data':reviewsKeysCB[0]}
        en = {'text': self.btnS.englishText, 'callback_data':reviewsKeysCB[1]}
        syn = {'text': self.btnS.synonymText, 'callback_data':reviewsKeysCB[2]}
        per = {'text': self.btnS.persianText,'callback_data':reviewsKeysCB[3]}
        word = {'text': self.btn.word , 'callback_data':reviewsKeysCB[4]}
        identifyArray = [{self.btnS.persianTextEn:per},{self.btnS.deutschText:de},{self.btnS.synonymText:syn},{self.btnS.englishText:en},{reviewsKeysCB[4]:word}]
        for z in identifyArray:
            for x,y in z.items():
                if x in keys:
                    elements.append(y)
        print(f"elements = {elements}")
        print(f"typeRev = {wordType}")
        beforeNnext = self.beforeNextKeys(counter,length,wordType)
        getBack = {'text': self.btn.getBack,'callback_data':self.mnv.endReview}
        if beforeNnext is False :
            output = json.dumps({'inline_keyboard': [elements,[getBack]],"resize_keyboard":True})
        else:
            output = json.dumps({'inline_keyboard': [elements,beforeNnext,[getBack]],"resize_keyboard":True})
        print(output)
        return output


    def wayKeys(self,way):
        add = {'text': self.btn.addWay, 'callback_data':self.btn.addWay}
        change = {'text': self.btn.changeWay, 'callback_data':self.btn.changeWay}
        subtract = {'text': self.btn.subtractWay, 'callback_data':self.btn.subtractWay}
        getBack = {'text': self.btn.getBack,'callback_data':self.mnv.secondMenu}
        if isinstance(way,list): 
            length = len(way)
        else:
            length = 1
        # print(way,length)
        keysArray = ""
        if length == 4:
            keysArray = [subtract]
        elif length <4 and 1<length:
            keysArray = [subtract,change,add]
        elif length ==1:
            keysArray = [add,change]
        output = json.dumps({'inline_keyboard': [keysArray,[getBack]],"resize_keyboard":True})
        return output

    def addWayKeys(self,way):
        print(f"way = {way}")
        addPer =  {'text': self.btnS.addPersian, 'callback_data':self.btnS.addPersian}
        addEn = {'text': self.btnS.addEnglish, 'callback_data':self.btnS.addEnglish}
        addSyn = {'text': self.btnS.addSynonym, 'callback_data':self.btnS.addSynonym}
        addDe = {'text': self.btnS.addDeutsch, 'callback_data':self.btnS.addDeutsch}
        getBack = {'text': self.btn.getBack,'callback_data':self.mnv.endEditWay}
        allWaysWithAdd = [{self.btnS.persianTextEn:addPer},{self.btnS.deutschText:addDe},{self.btnS.englishText:addEn},{self.btnS.synonymText:addSyn}]
        allWays = [self.btnS.persianTextEn,self.btnS.deutschText,self.btnS.englishText,self.btnS.synonymText]
        keys = []
        remainWays = []
        print(f"allWays = {allWays}")
        if isinstance(way,list):
            for z in allWays:
                if z not in way:
                    remainWays.append(z)
            # remainWays = [x for x in way if x not in allWays]
        else:
            
            for x in allWays:
                print(x)
                if way !=x:
                    remainWays.append(x)
            # remainWays = way if way not in allWays
        print(f'remainWays = {remainWays}')
        for z in allWaysWithAdd:
            for x,y in z.items():
                if x in remainWays:
                    keys.append(y)
        print(keys)
        if len(keys)<3:
            output = json.dumps({'inline_keyboard': [keys,[getBack]],"resize_keyboard":True})
        elif len(keys) == 3:
            output = json.dumps({'inline_keyboard': [[keys[0],keys[1]],[keys[2]],[getBack]],"resize_keyboard":True})
        elif len(keys) == 4:
            output = json.dumps({'inline_keyboard': [[keys[0],keys[1]],[keys[2],keys[3]],[getBack]],"resize_keyboard":True})
        # json.dumps({'inline_keyboard': [elements,beforeNnext,[getBack]],"resize_keyboard":True})
        return output

    def subtractWayKeys(self,way):
        addPer =  {'text': self.btnS.subtractPersian, 'callback_data':self.btnS.subtractPersian}
        addEn = {'text': self.btnS.subtractEnglish, 'callback_data':self.btnS.subtractEnglish}
        addSyn = {'text': self.btnS.subtractSynonym, 'callback_data':self.btnS.subtractSynonym}
        addDe = {'text': self.btnS.subtractDeutsch, 'callback_data':self.btnS.subtractDeutsch}
        getBack = {'text': self.btn.getBack,'callback_data':self.mnv.endEditWay}
        allWaysWithAdd = [{self.btnS.persianTextEn:addPer},{self.btnS.deutschText:addDe},{self.btnS.englishText:addEn},{self.btnS.synonymText:addSyn}]
        keys = []
        for z in allWaysWithAdd:
            for x,y in z.items():
                if x in way:
                    keys.append(y)
        if len(keys)<3:
            output = json.dumps({'inline_keyboard': [keys,[getBack]],"resize_keyboard":True})
        elif len(keys) == 3:
            output = json.dumps({'inline_keyboard': [[keys[0],keys[1]],[keys[2]],[getBack]],"resize_keyboard":True})
        elif len(keys) == 4:
            output = json.dumps({'inline_keyboard': [[keys[0],keys[1]],[keys[2],keys[3]],[getBack]],"resize_keyboard":True})
        print(f'output = {output}')
        return output




class DeKeys:
    def __init__(self):
        #
        self.btn =DeBtn()
        #5 times
        self.mnv = MNVDe()
        self.btnS = BtnS()
        self.firstMenu = json.dumps({"keyboard": [[self.btn.startLearning], [self.btn.aboutBotNew, self.btn.uILangNKeyEditNew]], "resize_keyboard": True})
        #21 times
        self.secondMenu = json.dumps({"keyboard":[[self.btn.reviewWords],[self.btn.wordsNum,self.btn.wayEdit,self.btn.account],[self.btn.timeLearnEdit,self.btn.reportActivity],[self.btn.deleteBot,self.btn.aboutBot,self.btn.uILangNKeyEdit],[self.btn.opinion]],"resize_keyboard":True})
        #19 times
        self.getBackKeys = json.dumps({"keyboard":[[self.btn.getBack]],"resize_keyboard":True})
        #2 times
        self.dailyLearnKeys = json.dumps({"keyboard":[[self.btn.dailyLearnWords]],"resize_keyboard":True})
        #2 times 
        # self.revKeys = json.dumps({"keyboard": [[self.btn.chapterNSection], [self.btn.leitnerBoxParts], [self.btn.weakWords], [self.btn.getBack]], "resize_keyboard": True}) 
        self.revKeys = json.dumps({"keyboard": [[self.btn.chapterNSection,self.btn.leitnerBoxParts,self.btn.weakWords], [self.btn.getBack]], "resize_keyboard": True}) 

        #2 times
        self.revChapNexKeys = json.dumps({"keyboard":[[self.btn.nextWordChapNS],[self.btn.getBack]],"resize_keyboard":True}) 
        #2 times
        self.revChapMidKeys = json.dumps({"keyboard":[[self.btn.beforeWordChapNS,self.btn.nextWordChapNS],[self.btn.getBack]],"resize_keyboard":True})
        #2 times
        self.revChapBefKeys =  json.dumps({"keyboard":[[self.btn.beforeWordChapNS],[self.btn.getBack]],"resize_keyboard":True})
        #2 times
        self.revLeitNexKeys = json.dumps({"keyboard":[[self.btn.nextWordLeitBP],[self.btn.getBack]],"resize_keyboard":True}) 
        #2 times
        self.revLeitMidKeys = json.dumps({"keyboard":[[self.btn.beforeWordLeitBP,self.btn.nextWordLeitBP],[self.btn.getBack]],"resize_keyboard":True}) 
        #2 times
        self.revLeitBefKeys = json.dumps({"keyboard":[[self.btn.beforeWordLeitBP],[self.btn.getBack]],"resize_keyboard":True})
        #2 times
        self.revWeakNexKeys = json.dumps({"keyboard":[[self.btn.nextWordWW],[self.btn.getBack]],"resize_keyboard":True})
        #2 times
        self.revWeakMidKeys = json.dumps({"keyboard":[[self.btn.beforeWordWW,self.btn.nextWordWW],[self.btn.getBack]],"resize_keyboard":True}) 
        #2 times
        self.revWeakBefKeys = json.dumps({"keyboard":[[self.btn.beforeWordWW],[self.btn.getBack]],"resize_keyboard":True}) 
        #2 times
        self.yNDot = json.dumps({"keyboard":[[self.btn.yesDot, self.btn.noDot]],"resize_keyboard":True}) 
        #1 times
        self.ways = json.dumps({"keyboard":[[self.btnS.deutsch,self.btnS.english],[self.btnS.synonym,self.btnS.persian],[self.btn.getBack]],"resize_keyboard":True}) 
        #1 time
        self.numWords = json.dumps({"keyboard":[[self.btnS.three],[self.btnS.two],[self.btnS.one],[self.btn.getBack]],"resize_keyboard":True})
        #1 time
        self.hKeys = json.dumps({"keyboard":[[self.btnS.clock1,self.btnS.clock2,self.btnS.clock3,self.btnS.clock4,self.btnS.clock5,self.btnS.clock6,self.btnS.clock7,self.btnS.clock8],[self.btnS.clock9,self.btnS.clock10,self.btnS.clock11,self.btnS.clock12,self.btnS.clock13,self.btnS.clock14,self.btnS.clock15,self.btnS.clock16],[self.btnS.clock17,self.btnS.clock18,self.btnS.clock19,self.btnS.clock20,self.btnS.clock21,self.btnS.clock22,self.btnS.clock23],[self.btn.getBack]],"resize_keyboard":True})
        #2 times
        self.yNDash = json.dumps({"keyboard":[[self.btn.yesDash,self.btn.noDash]],"resize_keyboard":True}) 
        #2 times
        self.reportKeys = json.dumps ({"keyboard": [[self.btn.reportWeakWords,self.btn.reportWordsPartions], [self.btn.getBack]], "resize_keyboard": True})
        #2 times
        self.lanKeys = json.dumps({"keyboard":[[self.btnS.keyNMsgDe],[self.btnS.keyNMsgEn],[self.btnS.keyNMsgPer],[self.btn.getBack]],"resize_keyboard":True}) 
        #2 times
        self.yNKeys = json.dumps({"keyboard":[[self.btn.no, self.btn.yesDelete]],"resize_keyboard":True})

class EnKeys:
    def __init__(self):
        #
        self.btn =EnBtn()
        self.mnv = MNVEn()
        self.btnS = BtnS()
        #5 times
        
        self.firstMenu = json.dumps({"keyboard": [[self.btn.startLearning], [self.btn.aboutBotNew, self.btn.uILangNKeyEditNew]], "resize_keyboard": True})
        #21 times
        self.secondMenu = json.dumps({"keyboard":[[self.btn.reviewWords],[self.btn.wordsNum,self.btn.wayEdit,self.btn.account],[self.btn.timeLearnEdit,self.btn.reportActivity],[self.btn.deleteBot,self.btn.aboutBot,self.btn.uILangNKeyEdit],[self.btn.opinion]],"resize_keyboard":True})
        #19 times
        self.getBackKeys = json.dumps({"keyboard":[[self.btn.getBack]],"resize_keyboard":True})
        #2 times
        self.dailyLearnKeys = json.dumps({"keyboard":[[self.btn.dailyLearnWords]],"resize_keyboard":True})
        #2 times 
        # self.revKeys = json.dumps({"keyboard": [[self.btn.chapterNSection], [self.btn.leitnerBoxParts], [self.btn.weakWords], [self.btn.getBack]], "resize_keyboard": True}) 
        self.revKeys = json.dumps({"keyboard": [[self.btn.chapterNSection,self.btn.leitnerBoxParts,self.btn.weakWords], [self.btn.getBack]], "resize_keyboard": True}) 

        #2 times
        self.revChapNexKeys = json.dumps({"keyboard":[[self.btn.nextWordChapNS],[self.btn.getBack]],"resize_keyboard":True}) 
        #2 times
        self.revChapMidKeys = json.dumps({"keyboard":[[self.btn.beforeWordChapNS,self.btn.nextWordChapNS],[self.btn.getBack]],"resize_keyboard":True})
        #2 times
        self.revChapBefKeys =  json.dumps({"keyboard":[[self.btn.beforeWordChapNS],[self.btn.getBack]],"resize_keyboard":True})
        #2 times
        self.revLeitNexKeys = json.dumps({"keyboard":[[self.btn.nextWordLeitBP],[self.btn.getBack]],"resize_keyboard":True}) 
        #2 times
        self.revLeitMidKeys = json.dumps({"keyboard":[[self.btn.beforeWordLeitBP,self.btn.nextWordLeitBP],[self.btn.getBack]],"resize_keyboard":True}) 
        #2 times
        self.revLeitBefKeys = json.dumps({"keyboard":[[self.btn.beforeWordLeitBP],[self.btn.getBack]],"resize_keyboard":True})
        #2 times
        self.revWeakNexKeys = json.dumps({"keyboard":[[self.btn.nextWordWW],[self.btn.getBack]],"resize_keyboard":True})
        #2 times
        self.revWeakMidKeys = json.dumps({"keyboard":[[self.btn.beforeWordWW,self.btn.nextWordWW],[self.btn.getBack]],"resize_keyboard":True}) 
        #2 times
        self.revWeakBefKeys = json.dumps({"keyboard":[[self.btn.beforeWordWW],[self.btn.getBack]],"resize_keyboard":True}) 
        #2 times
        self.yNDot = json.dumps({"keyboard":[[self.btn.yesDot, self.btn.noDot]],"resize_keyboard":True}) 
        #1 times
        self.ways = json.dumps({"keyboard":[[self.btnS.deutsch,self.btnS.english],[self.btnS.synonym,self.btnS.persian],[self.btn.getBack]],"resize_keyboard":True}) 
        #1 time
        self.numWords = json.dumps({"keyboard":[[self.btnS.three],[self.btnS.two],[self.btnS.one],[self.btn.getBack]],"resize_keyboard":True})
        #1 time
        self.hKeys = json.dumps({"keyboard":[[self.btnS.clock1,self.btnS.clock2,self.btnS.clock3,self.btnS.clock4,self.btnS.clock5,self.btnS.clock6,self.btnS.clock7,self.btnS.clock8],[self.btnS.clock9,self.btnS.clock10,self.btnS.clock11,self.btnS.clock12,self.btnS.clock13,self.btnS.clock14,self.btnS.clock15,self.btnS.clock16],[self.btnS.clock17,self.btnS.clock18,self.btnS.clock19,self.btnS.clock20,self.btnS.clock21,self.btnS.clock22,self.btnS.clock23],[self.btn.getBack]],"resize_keyboard":True})
        #2 times
        self.yNDash = json.dumps({"keyboard":[[self.btn.yesDash,self.btn.noDash]],"resize_keyboard":True}) 
        #2 times
        self.reportKeys = json.dumps ({"keyboard": [[self.btn.reportWeakWords,self.btn.reportWordsPartions], [self.btn.getBack]], "resize_keyboard": True})
        #2 times
        self.lanKeys = json.dumps({"keyboard":[[self.btnS.keyNMsgDe],[self.btnS.keyNMsgEn],[self.btnS.keyNMsgPer],[self.btn.getBack]],"resize_keyboard":True}) 
        #2 times
        self.yNKeys = json.dumps({"keyboard":[[self.btn.no, self.btn.yesDelete]],"resize_keyboard":True})

        ################################ inlineKeys #############can be user for all languages ###########################
        # self.wayMenuAddChange = json.dumps({"keyboard":[[self.btn.changeWay],[self.btn.addWay]],"resize_keyboard":True})
    # def wayKeys(self,way):

    #     add = {'text': self.btn.addWay, 'callback_data':self.btn.addWay}
    #     change = {'text': self.btn.changeWay, 'callback_data':self.btn.changeWay}
    #     subtract = {'text': self.btn.subtractWay, 'callback_data':self.btn.subtractWay}
    #     getBack = {'text': self.btn.getBack,'callback_data':self.mnv.secondMenu}
    #     if isinstance(way,list): 
    #         length = len(way)
    #     else:
    #         length = 1
    #     # print(way,length)
    #     keysArray = ""
    #     if length == 4:
    #         keysArray = [subtract]
    #     elif length <4 and 1<length:
    #         keysArray = [subtract,change,add]
    #     elif length ==1:
    #         keysArray = [add,change]
    #     output = json.dumps({'inline_keyboard': [keysArray,[getBack]],"resize_keyboard":True})
    #     return output

    # def addWayKeys(self,way):
    #     print(f"way = {way}")
    #     addPer =  {'text': self.btnS.addPersian, 'callback_data':self.btnS.addPersian}
    #     addEn = {'text': self.btnS.addEnglish, 'callback_data':self.btnS.addEnglish}
    #     addSyn = {'text': self.btnS.addSynonym, 'callback_data':self.btnS.addSynonym}
    #     addDe = {'text': self.btnS.addDeutsch, 'callback_data':self.btnS.addDeutsch}
    #     getBack = {'text': self.btn.getBack,'callback_data':self.mnv.endEditWay}




    #     allWaysWithAdd = [{self.btnS.persianTextEn:addPer},{self.btnS.deutschText:addDe},{self.btnS.englishText:addEn},{self.btnS.synonymText:addSyn}]
    #     allWays = [self.btnS.persianTextEn,self.btnS.deutschText,self.btnS.englishText,self.btnS.synonymText]
    #     keys = []
    #     remainWays = []
    #     print(f"allWays = {allWays}")
    #     if isinstance(way,list):
    #         for z in allWays:
    #             if z not in way:
    #                 remainWays.append(z)
    #         # remainWays = [x for x in way if x not in allWays]
    #     else:
            
    #         for x in allWays:
    #             print(x)
    #             if way !=x:
    #                 remainWays.append(x)
    #         # remainWays = way if way not in allWays
    #     print(f'remainWays = {remainWays}')
    #     for z in allWaysWithAdd:
    #         for x,y in z.items():
    #             if x in remainWays:
    #                 keys.append(y)
    #     print(keys)
    #     if len(keys)<3:
    #         output = json.dumps({'inline_keyboard': [keys,[getBack]],"resize_keyboard":True})
    #     elif len(keys) == 3:
    #         output = json.dumps({'inline_keyboard': [[keys[0],keys[1]],[keys[2]],[getBack]],"resize_keyboard":True})
    #     elif len(keys) == 4:
    #         output = json.dumps({'inline_keyboard': [[keys[0],keys[1]],[keys[2],keys[3]],[getBack]],"resize_keyboard":True})
    #     # json.dumps({'inline_keyboard': [elements,beforeNnext,[getBack]],"resize_keyboard":True})
    #     return output

    # def subtractWayKeys(self,way):
        # addPer =  {'text': self.btnS.subtractPersian, 'callback_data':self.btnS.subtractPersian}
        # addEn = {'text': self.btnS.subtractEnglish, 'callback_data':self.btnS.subtractEnglish}
        # addSyn = {'text': self.btnS.subtractSynonym, 'callback_data':self.btnS.subtractSynonym}
        # addDe = {'text': self.btnS.subtractDeutsch, 'callback_data':self.btnS.subtractDeutsch}
        # getBack = {'text': self.btn.getBack,'callback_data':self.mnv.endEditWay}
        # allWaysWithAdd = [{self.btnS.persianTextEn:addPer},{self.btnS.deutschText:addDe},{self.btnS.englishText:addEn},{self.btnS.synonymText:addSyn}]
        # keys = []
        # for z in allWaysWithAdd:
        #     for x,y in z.items():
        #         if x in way:
        #             keys.append(y)
        # if len(keys)<3:
        #     output = json.dumps({'inline_keyboard': [keys,[getBack]],"resize_keyboard":True})
        # elif len(keys) == 3:
        #     output = json.dumps({'inline_keyboard': [[keys[0],keys[1]],[keys[2]],[getBack]],"resize_keyboard":True})
        # elif len(keys) == 4:
        #     output = json.dumps({'inline_keyboard': [[keys[0],keys[1]],[keys[2],keys[3]],[getBack]],"resize_keyboard":True})
        # print(f'output = {output}')
        # return output


        

    # def reviewAnswer(self,reviewsKeysCB,ways,counter,length,data,wordType):
        # print(f" data = {data}\n ways = {ways}")
        # keys = ways
        # if isinstance (keys,str):
        #     keys = [ways]
        # keys.append(wordType)
        # elements = []
        # keys.remove(data)
        # de = {'text': self.btnS.deutschText, 'callback_data':reviewsKeysCB[0]}
        # en = {'text': self.btnS.englishText, 'callback_data':reviewsKeysCB[1]}
        # syn = {'text': self.btnS.synonymText, 'callback_data':reviewsKeysCB[2]}
        # per = {'text': self.btnS.persianText,'callback_data':reviewsKeysCB[3]}
        # word = {'text': self.btn.word , 'callback_data':reviewsKeysCB[4]}
        # identifyArray = [{self.btnS.persianTextEn:per},{self.btnS.deutschText:de},{self.btnS.synonymText:syn},{self.btnS.englishText:en},{reviewsKeysCB[4]:word}]
        # for z in identifyArray:
        #     for x,y in z.items():
        #         if x in keys:
        #             elements.append(y)
        # print(f"elements = {elements}")
        # print(f"wordType = {wordType}")
        # beforeNnext = self.beforeNextKeys(counter,length,wordType)
        # getBack = {'text': self.btn.getBack,'callback_data':self.mnv.endReview}
        # if beforeNnext is False :
        #     output = json.dumps({'inline_keyboard': [elements,[getBack]],"resize_keyboard":True})
        # else:
        #     output = json.dumps({'inline_keyboard': [elements,beforeNnext,[getBack]],"resize_keyboard":True})
        # print(output)
        # return output

            
    # def beforeNextKeys(self,counter,length,typeRev):
    #     beforeChapNS = {'text': self.btn.beforeWordChapNS, 'callback_data':self.btn.beforeWordChapNS}
    #     nextChapNS = {'text': self.btn.nextWordChapNS,'callback_data':self.btn.nextWordChapNS}        

    #     beforeLeitBP = {'text': self.btn.beforeWordLeitBP, 'callback_data':self.btn.beforeWordLeitBP}
    #     nextLeitBP = {'text': self.btn.nextWordLeitBP,'callback_data':self.btn.nextWordLeitBP}

    #     beforeWW = {'text': self.btn.beforeWordWW, 'callback_data':self.btn.beforeWordWW}
    #     nextWW = {'text': self.btn.nextWordWW,'callback_data':self.btn.nextWordWW}
        

    #     counterIf = counter +1

    #     output = ""
    #     if counterIf == length and counterIf == 1:
    #         return False

    #     elif typeRev == self.btn.chapterNSection:
    #         if  counterIf == length:
    #             output = [beforeChapNS]
    #             # return [beforeChapNS]
    #         elif counterIf !=length and counterIf == 1:
    #             # return [nextChapNS]
    #             output = [nextChapNS]
    #         elif counterIf !=length and counterIf !=1:
    #             output = [beforeChapNS,nextChapNS]
    #             # return [beforeChapNS,nextChapNS]

    #     elif typeRev == self.btn.leitnerBoxParts:
    #         if counterIf == length:
    #             # return [beforeLeitBP]
    #             output = [beforeLeitBP]
    #         elif counterIf !=length and counterIf == 1:
    #             output = [nextLeitBP]
    #             # return [nextLeitBP]
    #         elif counterIf !=length and counterIf !=1:
    #             output = [beforeLeitBP,nextLeitBP]
    #             # return [beforeLeitBP,nextLeitBP]
        
    #     elif typeRev == self.btn.weakWords:
    #         if counterIf == length:
    #             output = [beforeWW]
    #             # return [beforeWW]
    #         elif counterIf !=length and counterIf == 1:
    #             output = [nextWW]
    #             # return [nextWW]
    #         elif counterIf !=length and counterIf !=1:
    #             # return [beforeWW,nextWW]
    #             output = [beforeWW,nextWW]
    #     # outputLast = [output,[getBack]]
    #     # output.append(getBack)
    #     return output

    # def reviewMoreThanOne(self,counter,waysRevTypeCB,ways,length,msg):
    #     elements = []
    #     print(f'msg = {msg}')
    #     # print(f"chNSWCB = {waysRevTypeCB}")
    #     # print(f"chNSWCB[0] = {chNSWCB[0]}")
    #     # print(f"chNSWCB[1] = {chNSWCB[1]}")
    #     # print(f"chNSWCB[2] = {chNSWCB[2]}")
    #     # print(f"chNSWCB[3] = {chNSWCB[3]}")
    #     de = {'text': self.btnS.deutschText, 'callback_data':waysRevTypeCB[0]}
    #     en = {'text': self.btnS.englishText, 'callback_data':waysRevTypeCB[1]}
    #     syn = {'text': self.btnS.synonymText, 'callback_data':waysRevTypeCB[2]}
    #     per = {'text': self.btnS.persianText,'callback_data':waysRevTypeCB[3]}


    #     wordBCs = [{self.btnS.wordChapNSCB:self.btn.chapterNSection},{self.btnS.wordLeitBPCB:self.btn.leitnerBoxParts},{self.btnS.wordWWCB:self.btn.weakWords},{self.btn.nextWordChapNS:self.btn.chapterNSection},{self.btn.beforeWordChapNS:self.btn.chapterNSection},{self.btn.nextWordLeitBP:self.btn.leitnerBoxParts},{self.btn.beforeWordLeitBP:self.btn.leitnerBoxParts},{self.btn.nextWordWW:self.btn.weakWords},{self.btn.beforeWordWW:self.btn.weakWords}]
    #     typeRev = ''
    #     for z in wordBCs:
    #         for x,y in z.items():
    #             if msg == x:
    #                 typeRev = y
    #     if typeRev == '':
    #         typeRev = msg
    #     print(f"typeRev = {typeRev}")
    #     nextBeforeKeys = self.beforeNextKeys(counter,length,typeRev)
    #     getBack = {'text': self.btn.getBack,'callback_data':self.mnv.endReview}





    #      ######
    #     identifyArray = [{self.btnS.persianTextEn:per},{self.btnS.deutschText:de},{self.btnS.synonymText:syn},{self.btnS.englishText:en}]
    #     for z in identifyArray:
    #         for x,y in z.items():
    #             if x in ways:
    #                 elements.append(y)
    #     print(f"elements = {elements}")
    #     # output = json.dumps({'inline_keyboard': [elements,[next]],"resize_keyboard":True})
    #     # output = json.dumps({'inline_keyboard': [elements],"resize_keyboard":True})
    #     output = json.dumps({'inline_keyboard': [elements,nextBeforeKeys,[getBack]],"resize_keyboard":True})
    #     print(output)

    #     return output





class PerKeys:
    def __init__(self):
        

        #
        self.btn =PerBtn()
        #5 times
        self.mnv = MNVPer()
        self.btnS = BtnS()
        
        self.firstMenu = json.dumps({"keyboard": [[self.btn.startLearning], [self.btn.aboutBotNew, self.btn.uILangNKeyEditNew]], "resize_keyboard": True})
        #21 times
        self.secondMenu = json.dumps({"keyboard":[[self.btn.reviewWords],[self.btn.wordsNum,self.btn.wayEdit,self.btn.account],[self.btn.timeLearnEdit,self.btn.reportActivity],[self.btn.deleteBot,self.btn.aboutBot,self.btn.uILangNKeyEdit],[self.btn.opinion]],"resize_keyboard":True})
        #19 times
        self.getBackKeys = json.dumps({"keyboard":[[self.btn.getBack]],"resize_keyboard":True})
        #2 times
        self.dailyLearnKeys = json.dumps({"keyboard":[[self.btn.dailyLearnWords]],"resize_keyboard":True})
        #2 times 
        # self.revKeys = json.dumps({"keyboard": [[self.btn.chapterNSection], [self.btn.leitnerBoxParts], [self.btn.weakWords], [self.btn.getBack]], "resize_keyboard": True}) 
        self.revKeys = json.dumps({"keyboard": [[self.btn.chapterNSection,self.btn.leitnerBoxParts,self.btn.weakWords], [self.btn.getBack]], "resize_keyboard": True}) 
        
        #2 times
        self.revChapNexKeys = json.dumps({"keyboard":[[self.btn.nextWordChapNS],[self.btn.getBack]],"resize_keyboard":True}) 
        #2 times
        self.revChapMidKeys = json.dumps({"keyboard":[[self.btn.beforeWordChapNS,self.btn.nextWordChapNS],[self.btn.getBack]],"resize_keyboard":True})
        #2 times
        self.revChapBefKeys =  json.dumps({"keyboard":[[self.btn.beforeWordChapNS],[self.btn.getBack]],"resize_keyboard":True})
        #2 times
        self.revLeitNexKeys = json.dumps({"keyboard":[[self.btn.nextWordLeitBP],[self.btn.getBack]],"resize_keyboard":True}) 
        #2 times
        self.revLeitMidKeys = json.dumps({"keyboard":[[self.btn.beforeWordLeitBP,self.btn.nextWordLeitBP],[self.btn.getBack]],"resize_keyboard":True}) 
        #2 times
        self.revLeitBefKeys = json.dumps({"keyboard":[[self.btn.beforeWordLeitBP],[self.btn.getBack]],"resize_keyboard":True})
        #2 times
        self.revWeakNexKeys = json.dumps({"keyboard":[[self.btn.nextWordWW],[self.btn.getBack]],"resize_keyboard":True})
        #2 times
        self.revWeakMidKeys = json.dumps({"keyboard":[[self.btn.beforeWordWW,self.btn.nextWordWW],[self.btn.getBack]],"resize_keyboard":True}) 
        #2 times
        self.revWeakBefKeys = json.dumps({"keyboard":[[self.btn.beforeWordWW],[self.btn.getBack]],"resize_keyboard":True}) 
        #2 times
        self.yNDot = json.dumps({"keyboard":[[self.btn.yesDot, self.btn.noDot]],"resize_keyboard":True}) 
        #1 times
        self.ways = json.dumps({"keyboard":[[self.btnS.deutsch,self.btnS.english],[self.btnS.synonym,self.btnS.persian],[self.btn.getBack]],"resize_keyboard":True}) 
        #1 time
        self.numWords = json.dumps({"keyboard":[[self.btnS.three],[self.btnS.two],[self.btnS.one],[self.btn.getBack]],"resize_keyboard":True})
        #1 time
        self.hKeys = json.dumps({"keyboard":[[self.btnS.clock1,self.btnS.clock2,self.btnS.clock3,self.btnS.clock4,self.btnS.clock5,self.btnS.clock6,self.btnS.clock7,self.btnS.clock8],[self.btnS.clock9,self.btnS.clock10,self.btnS.clock11,self.btnS.clock12,self.btnS.clock13,self.btnS.clock14,self.btnS.clock15,self.btnS.clock16],[self.btnS.clock17,self.btnS.clock18,self.btnS.clock19,self.btnS.clock20,self.btnS.clock21,self.btnS.clock22,self.btnS.clock23],[self.btn.getBack]],"resize_keyboard":True})
        #2 times
        self.yNDash = json.dumps({"keyboard":[[self.btn.yesDash,self.btn.noDash]],"resize_keyboard":True}) 
        #2 times
        self.reportKeys = json.dumps ({"keyboard": [[self.btn.reportWeakWords,self.btn.reportWordsPartions], [self.btn.getBack]], "resize_keyboard": True})
        #2 times
        self.lanKeys = json.dumps({"keyboard":[[self.btnS.keyNMsgDe],[self.btnS.keyNMsgEn],[self.btnS.keyNMsgPer],[self.btn.getBack]],"resize_keyboard":True}) 
        #2 times
        self.yNKeys = json.dumps({"keyboard":[[self.btn.no, self.btn.yesDelete]],"resize_keyboard":True})
          #1 time
        # self.numWordsNew = json.dumps({"keyboard":[[self.btnS.threeNew,self.btnS.twoNew,self.btnS.oneNew],[self.btn.getBack]],"resize_keyboard":True})

        

        
        
        ################################ inlineKeys #############can be user for all languages ###########################
        # self.wayMenuAddChange = json.dumps({"keyboard":[[self.btn.changeWay],[self.btn.addWay]],"resize_keyboard":True})
    # def wayKeys(self,way):

    #     add = {'text': self.btn.addWay, 'callback_data':self.btn.addWay}
    #     change = {'text': self.btn.changeWay, 'callback_data':self.btn.changeWay}
    #     subtract = {'text': self.btn.subtractWay, 'callback_data':self.btn.subtractWay}
    #     getBack = {'text': self.btn.getBack,'callback_data':MNVPer().secondMenu}
    #     if isinstance(way,list): 
    #         length = len(way)
    #     else:
    #         length = 1
    #     # print(way,length)
    #     keysArray = ""
    #     if length == 4:
    #         keysArray = [subtract]
    #     elif length <4 and 1<length:
    #         keysArray = [subtract,change,add]
    #     elif length ==1:
    #         keysArray = [add,change]
    #     output = json.dumps({'inline_keyboard': [keysArray,[getBack]],"resize_keyboard":True})
    #     return output

    # def addWayKeys(self,way):
    #     print(f"way = {way}")
    #     addPer =  {'text': self.btnS.addPersian, 'callback_data':self.btnS.addPersian}
    #     addEn = {'text': self.btnS.addEnglish, 'callback_data':self.btnS.addEnglish}
    #     addSyn = {'text': self.btnS.addSynonym, 'callback_data':self.btnS.addSynonym}
    #     addDe = {'text': self.btnS.addDeutsch, 'callback_data':self.btnS.addDeutsch}
    #     getBack = {'text': self.btn.getBack,'callback_data':self.mnv.endEditWay}




    #     allWaysWithAdd = [{self.btnS.persianTextEn:addPer},{self.btnS.deutschText:addDe},{self.btnS.englishText:addEn},{self.btnS.synonymText:addSyn}]
    #     allWays = [self.btnS.persianTextEn,self.btnS.deutschText,self.btnS.englishText,self.btnS.synonymText]
    #     keys = []
    #     remainWays = []
    #     print(f"allWays = {allWays}")
    #     if isinstance(way,list):
    #         for z in allWays:
    #             if z not in way:
    #                 remainWays.append(z)
    #         # remainWays = [x for x in way if x not in allWays]
    #     else:
            
    #         for x in allWays:
    #             print(x)
    #             if way !=x:
    #                 remainWays.append(x)
    #         # remainWays = way if way not in allWays
    #     print(f'remainWays = {remainWays}')
    #     for z in allWaysWithAdd:
    #         for x,y in z.items():
    #             if x in remainWays:
    #                 keys.append(y)
    #     print(keys)
    #     if len(keys)<3:
    #         output = json.dumps({'inline_keyboard': [keys,[getBack]],"resize_keyboard":True})
    #     elif len(keys) == 3:
    #         output = json.dumps({'inline_keyboard': [[keys[0],keys[1]],[keys[2]],[getBack]],"resize_keyboard":True})
    #     elif len(keys) == 4:
    #         output = json.dumps({'inline_keyboard': [[keys[0],keys[1]],[keys[2],keys[3]],[getBack]],"resize_keyboard":True})
    #     # json.dumps({'inline_keyboard': [elements,beforeNnext,[getBack]],"resize_keyboard":True})
    #     return output

    # def subtractWayKeys(self,way):
    #     addPer =  {'text': self.btnS.subtractPersian, 'callback_data':self.btnS.subtractPersian}
    #     addEn = {'text': self.btnS.subtractEnglish, 'callback_data':self.btnS.subtractEnglish}
    #     addSyn = {'text': self.btnS.subtractSynonym, 'callback_data':self.btnS.subtractSynonym}
    #     addDe = {'text': self.btnS.subtractDeutsch, 'callback_data':self.btnS.subtractDeutsch}
    #     getBack = {'text': self.btn.getBack,'callback_data':MNVPer().endEditWay}
    #     allWaysWithAdd = [{self.btnS.persianTextEn:addPer},{self.btnS.deutschText:addDe},{self.btnS.englishText:addEn},{self.btnS.synonymText:addSyn}]
    #     keys = []
    #     for z in allWaysWithAdd:
    #         for x,y in z.items():
    #             if x in way:
    #                 keys.append(y)
    #     if len(keys)<3:
    #         output = json.dumps({'inline_keyboard': [keys,[getBack]],"resize_keyboard":True})
    #     elif len(keys) == 3:
    #         output = json.dumps({'inline_keyboard': [[keys[0],keys[1]],[keys[2]],[getBack]],"resize_keyboard":True})
    #     elif len(keys) == 4:
    #         output = json.dumps({'inline_keyboard': [[keys[0],keys[1]],[keys[2],keys[3]],[getBack]],"resize_keyboard":True})
    #     print(f'output = {output}')
    #     return output


        

    # def reviewAnswer(self,reviewsKeysCB,ways,counter,length,data,wordType):
        # print(f" data = {data}\n ways = {ways}")
        # keys = ways
        # if isinstance (keys,str):
        #     keys = [ways]
        # keys.append(wordType)
        # elements = []
        # keys.remove(data)
        # de = {'text': self.btnS.deutschText, 'callback_data':reviewsKeysCB[0]}
        # en = {'text': self.btnS.englishText, 'callback_data':reviewsKeysCB[1]}
        # syn = {'text': self.btnS.synonymText, 'callback_data':reviewsKeysCB[2]}
        # per = {'text': self.btnS.persianText,'callback_data':reviewsKeysCB[3]}
        # word = {'text': self.btn.word , 'callback_data':reviewsKeysCB[4]}
        # identifyArray = [{self.btnS.persianTextEn:per},{self.btnS.deutschText:de},{self.btnS.synonymText:syn},{self.btnS.englishText:en},{reviewsKeysCB[4]:word}]
        # for z in identifyArray:
        #     for x,y in z.items():
        #         if x in keys:
        #             elements.append(y)
        # print(f"elements = {elements}")
        # print(f"typeRev = {wordType}")
        # beforeNnext = self.beforeNextKeys(counter,length,wordType)
        # getBack = {'text': self.btn.getBack,'callback_data':MNVPer().endReview}
        # if beforeNnext is False :
        #     output = json.dumps({'inline_keyboard': [elements,[getBack]],"resize_keyboard":True})
        # else:
        #     output = json.dumps({'inline_keyboard': [elements,beforeNnext,[getBack]],"resize_keyboard":True})
        # print(output)
        # return output

            
    # def beforeNextKeys(self,counter,length,typeRev):
    #     print(f"typeRev = {typeRev}")
    #     beforeChapNS = {'text': self.btn.beforeWordChapNS, 'callback_data':self.btn.beforeWordChapNS}
    #     nextChapNS = {'text': self.btn.nextWordChapNS,'callback_data':self.btn.nextWordChapNS}        

    #     beforeLeitBP = {'text': self.btn.beforeWordLeitBP, 'callback_data':self.btn.beforeWordLeitBP}
    #     nextLeitBP = {'text': self.btn.nextWordLeitBP,'callback_data':self.btn.nextWordLeitBP}

    #     beforeWW = {'text': self.btn.beforeWordWW, 'callback_data':self.btn.beforeWordWW}
    #     nextWW = {'text': self.btn.nextWordWW,'callback_data':self.btn.nextWordWW}
        
    #     # wordBCs = [{self.btnS.wordChapNSCB:self.btn.chapterNSection},{self.btnS.wordLeitBPCB:self.btn.leitnerBoxParts},{self.btnS.wordWWCB:self.btn.weakWords},{self.btn.nextWordChapNS:self.btn.chapterNSection},{self.btn.beforeWordChapNS:self.btn.chapterNSection},{self.btn.nextWordLeitBP:self.btn.leitnerBoxParts},{self.btn.beforeWordLeitBP:self.btn.leitnerBoxParts},{self.btn.nextWordWW:self.btn.weakWords},{self.btn.beforeWordWW:self.btn.weakWords}]

    #     counterIf = counter +1

    #     output = ""
    #     if counterIf == length and counterIf == 1:
    #         return False

    #     elif typeRev == self.btn.chapterNSection or typeRev == self.btnS.wordChapNSCB:
    #         if  counterIf == length:
    #             output = [beforeChapNS]
    #             # return [beforeChapNS]
    #         elif counterIf !=length and counterIf == 1:
    #             # return [nextChapNS]
    #             output = [nextChapNS]
    #         elif counterIf !=length and counterIf !=1:
    #             output = [beforeChapNS,nextChapNS]
    #             # return [beforeChapNS,nextChapNS]

    #     elif typeRev == self.btn.leitnerBoxParts or typeRev == self.btnS.wordLeitBPCB:
    #         if counterIf == length:
    #             # return [beforeLeitBP]
    #             output = [beforeLeitBP]
    #         elif counterIf !=length and counterIf == 1:
    #             output = [nextLeitBP]
    #             # return [nextLeitBP]
    #         elif counterIf !=length and counterIf !=1:
    #             output = [beforeLeitBP,nextLeitBP]
    #             # return [beforeLeitBP,nextLeitBP]
        
    #     elif typeRev == self.btn.weakWords or typeRev == self.btnS.wordWWCB:
    #         if counterIf == length:
    #             output = [beforeWW]
    #             # return [beforeWW]
    #         elif counterIf !=length and counterIf == 1:
    #             output = [nextWW]
    #             # return [nextWW]
    #         elif counterIf !=length and counterIf !=1:
    #             # return [beforeWW,nextWW]
    #             output = [beforeWW,nextWW]
    #     # outputLast = [output,[getBack]]
    #     # output.append(getBack)
    #     print(f'output beforeNextKeys = {output}')
    #     return output

    # def reviewMoreThanOne(self,counter,waysRevTypeCB,ways,length,msg):
    #     elements = []
    #     print(f'msg = {msg}')
    #     # print(f"chNSWCB = {waysRevTypeCB}")
    #     # print(f"chNSWCB[0] = {chNSWCB[0]}")
    #     # print(f"chNSWCB[1] = {chNSWCB[1]}")
    #     # print(f"chNSWCB[2] = {chNSWCB[2]}")
    #     # print(f"chNSWCB[3] = {chNSWCB[3]}")
    #     de = {'text': self.btnS.deutschText, 'callback_data':waysRevTypeCB[0]}
    #     en = {'text': self.btnS.englishText, 'callback_data':waysRevTypeCB[1]}
    #     syn = {'text': self.btnS.synonymText, 'callback_data':waysRevTypeCB[2]}
    #     per = {'text': self.btnS.persianText,'callback_data':waysRevTypeCB[3]}

    #     # nextArray = [{self.btn.chapterNSection:self.btn.nextWordChapNS},{self.btn.leitnerBoxParts:self.btn.nextWordLeitBP},{self.btn.weakWords:self.btn.nextWordWW}]
    #     # wordBCs = [{self.btnS.wordChapNSCB:self.btn.chapterNSection},{self.btnS.wordLeitBPCB:self.btn.leitnerBoxParts},{self.btnS.wordWWCB:self.btn.weakWords},{self.btn.nextWordChapNS:self.btn.chapterNSection},{self.btn.beforeWordChapNS:self.btn.chapterNSection},{self.btn.nextWordLeitBP:self.btn.leitnerBoxParts},{self.btn.beforeWordLeitBP:self.btn.leitnerBoxParts},{self.btn.nextWordWW:self.btn.weakWords},{self.btn.beforeWordWW:self.btn.weakWords}]
    #     wordBCs = [{self.btn.nextWordChapNS:self.btn.chapterNSection},{self.btn.beforeWordChapNS:self.btn.chapterNSection},{self.btn.nextWordLeitBP:self.btn.leitnerBoxParts},{self.btn.beforeWordLeitBP:self.btn.leitnerBoxParts},{self.btn.nextWordWW:self.btn.weakWords},{self.btn.beforeWordWW:self.btn.weakWords}]

    #     typeRev = ''
    #     for z in wordBCs:
    #         for x,y in z.items():
    #             if msg == x:
    #                 typeRev = y
            
    #     if typeRev == '':
    #         typeRev = msg
    #     print(f"typeRev = {typeRev}")
    #     nextBeforeKeys = self.beforeNextKeys(counter,length,typeRev)
    #     getBack = {'text': self.btn.getBack,'callback_data':MNVPer().endReview}





    #      ######
    #     identifyArray = [{self.btnS.persianTextEn:per},{self.btnS.deutschText:de},{self.btnS.synonymText:syn},{self.btnS.englishText:en}]
    #     for z in identifyArray:
    #         for x,y in z.items():
    #             if x in ways:
    #                 elements.append(y)
    #     print(f"elements = {elements}")
    #     # output = json.dumps({'inline_keyboard': [elements,[next]],"resize_keyboard":True})
    #     # output = json.dumps({'inline_keyboard': [elements],"resize_keyboard":True})
    #     output = json.dumps({'inline_keyboard': [elements,nextBeforeKeys,[getBack]],"resize_keyboard":True})
    #     print(output)

    #     return output


