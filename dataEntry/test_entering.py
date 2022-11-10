import pytest
import pymongo
import string
from bson.objectid import ObjectId
import bson



# from xlrd import open_workbook as OW

class Db:
    def __init__(self):
        self.connection = pymongo.MongoClient("localhost",27017)
        self.database= self.connection["woerterbuch"]
        self.userCollection = self.database["user"]
        self.wordCollection = self.database["word"]
        self.meaningCollection = self.database["meaning"]
        self.bookCollection = self.database["book"]
        self.sectionCollection =  self.database["section"]
        self.settingCollection = self.database["setting"]
        self.backupCollection = self.database["backup"]
        self.testMeaningCollection  = self.database["testMeaning"]

class Search:
    def __init__(self):
        self.obj_Db = Db()
        self.test = "hi"
        
    def simpleSearch(self,word,deutsch=None):
        output = False

        # wordOutput = {"wordId":None,"word":None,"wordType":None,"article":None,"wordVoiceName":None,"wordTelAdd":None}
        # meaningNbookOutput = {"meaningId":None,"meaningNumDaf":None,"deutschMeaning":None,"deuName":None,"deuTelegramLink":None,"englishMeaning":None,"engName":None,"engTelegramLink":None,"synonymMeaning":None,"synName":None,"synTelegramLink":None,"persianMeaning":None,"perName":None,"perTelegramLink":None,"bookId":None,"bookName":None,"chapter":None,"content":None,"page":None,"lesson":None,"publisher":None}

        # wordNumRow
        verification = False
        for col in self.obj_Db.wordCollection.find({"word":word},{"_id"}):
            for keys in col.keys():
                verification = True
        if verification is True:
            output = []
            bookNum = 0
            # bookNumRow,meaningNumRow,wordNumRow
            
            if deutsch == None:
                meaningCondition= {"wordDetails.word":word}
            else :
                meaningCondition= {"wordDetails.word":word,"deutsch":deutsch}
            wordOutputMongo = {"_id":1,"word":1,"wordType":1,"article":1,"voice":1}
            for col in self.obj_Db.wordCollection.find({"word":word},wordOutputMongo):
                wordDic = {}
                oneWord = []
                for field,val in col.items():
                    if field == "_id":
                        wordDic["wordId"]=val
                    elif field == "word":
                        wordDic["word"]=val
                    elif field == "wordType":
                        wordDic["wordType"]=val
                    elif field == "article":
                        wordDic["article"]=val
                    elif field == "voice":
                        wordDic["wordVoiceName"]=val["name"]
                        wordDic["wordtelegramLink"]=val["telegramLink"]
                # oneWord.append(wordDic)
                
                output.append(wordDic)








            meaningOutputMongo = {"_id":1,"deutsch":1,"english":1,"synonym":1,"persian":1,"meaningNumDaf":1,"synVoice":1,"engVoice":1,"perVoice":1,"deuVoice":1}
            
            for x in range(len(output)):
                i=0
                for col in self.obj_Db.meaningCollection.find(meaningCondition,meaningOutputMongo):
                    meaningOutput = {}
                    i=i+1
                    #FIXME meaning10
                    for field,val in col.items():
                        if field == "_id":
                            meaningOutput["meaningId"]=val
                        elif field == "deutsch":
                            meaningOutput["deutschMeaning"]=val
                        elif field =="english":
                            meaningOutput["englishMeaning"]=val
                        elif field =="synonym":
                            meaningOutput["synonymMeaning"]=val
                        elif field =="persian":
                            meaningOutput["persianMeaning"]=val
                        elif field =="meaningNumDaf":
                            meaningOutput["meaningNumDaf"]=val
                        elif field =="synVoice":                    
                            meaningOutput["synName"]=val["synName"]
                            meaningOutput["synTelegramLink"]=val["synTelegramLink"]
                        elif field =="engVoice":
                            meaningOutput["engName"]=val["engName"]
                            meaningOutput["engTelegramLink"]=val["engTelegramLink"]
                        elif field =="perVoice":
                            meaningOutput["perName"]=val["perName"]
                            meaningOutput["perTelegramLink"]=val["perTelegramLink"]
                        elif field =="deuVoice":
                            meaningOutput["deuName"]=val["deuName"]
                            meaningOutput["deuTelegramLink"]=val["deuTelegramLink"]
                    # print(f"meaning{i}")
                        # temp[f"meaning{i}"]=meaningOutput
                        
                    output[x][f"meaning{i}"]= meaningOutput

                for x in range(len(output)): 
                    for field,val in output[x].items():
                        for i in range(10):
                            if field==f"meaning{i}":
                                tempMeaning = val
                                bookCondition = {"word":word,"meaningId":val["meaningId"]} 
                                bookOutputMongo = {"_id":1,"bookName":1,"chapter":1,"content":1,"page":1,"lesson":1,"publisher":1}
                                k = 0
                                for col in self.obj_Db.bookCollection.find(bookCondition,bookOutputMongo):
                                    bookOutput = {}
                                    k=k+1
                                    for fieldBook , valBook in col.items():
                                        if fieldBook == "_id":
                                            bookOutput["bookId"]=valBook
                                        elif fieldBook == "bookName":
                                            bookOutput["bookName"]=valBook
                                        elif fieldBook == "chapter":
                                            bookOutput["chapter"]=valBook
                                        elif fieldBook == "bookName":
                                            bookOutput["bookName"]=valBook
                                        elif fieldBook == "content":
                                            bookOutput["content"]=valBook
                                        elif fieldBook == "page":
                                            bookOutput["page"]=valBook
                                        elif fieldBook == "lesson":
                                            bookOutput["lesson"]=valBook
                                        elif fieldBook == "publisher":
                                            bookOutput["publisher"]=valBook
                                    
                                    tempMeaning[f"book{k}"]= bookOutput  
                                
                                output[x][f"meaning{i}"]=tempMeaning


        return output

    def getWordValues(self,wordId,word=None):
        output = {}
        if isinstance(wordId,str):
            temp = ObjectId(wordId)
            wordId = temp
        
        if word !=None:
            condition = {"_id":wordId,"word":word}
        else:
            condition = {"_id":wordId}
        outputMongo = {"_id":1,"word":1,"wordType":1,"article":1,"voice":1,"meaningId":1}
        wordVerification = False
        for col in self.obj_Db.wordCollection.find(condition,outputMongo):
                for field,val in col.items():
                    wordVerification = True
                    if field == "_id":
                        output["wordId"]=val
                    elif field == "word":
                        output["word"]=val
                    elif field == "wordType":
                        output["wordType"]=val
                    elif field == "article":
                        output["article"]=val
                    elif field == "voice":
                        output["wordVoiceName"]=val["name"]
                        output["wordtelegramLink"]=val["telegramLink"]
        if wordVerification is False:
            output = False
        return output
    def getMeaningValues(self,meaningId,deutsch=None):
        output = {}
        condition = None
        if isinstance(meaningId,str):
            condition = {"_id":ObjectId(meaningId)}
        else:
            condition = {"_id":meaningId}
        outputMon = {"_id":1,"deutsch":1,"english":1,"synonym":1,"persian":1,"meaningNumDaf":1,"synVoice":1,"engVoice":1,"perVoice":1,"deuVoice":1,"wordDetails":1}
        for col in self.obj_Db.meaningCollection.find(condition,outputMon):
            for field,val in col.items():
                if field == "_id":
                    output["meaningId"] = val
                elif field == "deutsch":
                    output["deutsch"] = val
                elif field == "english":
                    output["english"] = val
                elif field == "synonym":
                    output["synonym"] = val
                elif field == "persian":
                    output["persian"] = val
                elif field == "meaningNumDaf":
                    output["meaningNumDaf"] = val
                elif field == "synVoice":
                    output["synName"]=val["synName"]
                    output["synTelegramLink"]=val["synTelegramLink"]
                elif field == "engVoice":
                    output["engName"]=val["engName"]
                    output["engTelegramLink"]=val["engTelegramLink"]
                elif field == "perVoice":
                    output["perName"] = val["perName"]
                    output["perTelegramLink"] = val["perTelegramLink"]
                elif field == "deuVoice":
                    output["deuName"]=val["deuName"]
                    output["deuTelegramLink"]=val["deuTelegramLink"]
                elif field == "wordDetails":
                    output["wordId"]=val["wordId"]
                    output["word"]=val["word"]
                    output["wordType"]=val["wordType"]
                    output["article"]=val["article"]
        return output            
    def getBookValues(self,bookId,bookName=None):
        output={}
        condition = None
        if isinstance(bookId,str):
            temp =ObjectId(bookId)
            bookId=temp

        if bookName!=None:
            condition = {"_id":bookId,"bookName":bookName}
        else:
            condition = {"_id":bookId}

        outputMon = {"_id":1,"bookName":1,"chapter":1,"content":1,"page":1,"lesson":1,"publisher":1,"word":1,"meaningId":1}

        for col in self.obj_Db.bookCollection.find(condition,outputMon):
            for field,val in col.items():
                if field == "_id":
                    output["bookId"] = val
                elif field == "bookName":
                    output["bookName"] = val
                elif field == "chapter":
                    output["chapter"] = val                      
                elif field == "content":
                    output["content"] = val
                elif field == "page":
                    output["page"] = val
                elif field == "lesson":
                    output["lesson"] = val
                elif field == "publisher":
                    output["publisher"] = val
                elif field == "word":
                    output["word"] = val
                elif field == "meaningId":
                    output["meaningId"] = val   
        return output 

    def getSearchContain(self,word):
        output=False
        words=[]
        condition={"word":{"$regex":word}}
        outputMongo = {"_id":0,"word":1}
        for col in self.obj_Db.wordCollection.find(condition,outputMongo):
            for keys in col.keys():
                words.append(col[keys])
        if len(words)!=0:
            output = words
        return output

    def getAllwords(self):
        output = False
        words = []
        for col in self.obj_Db.wordCollection.find({},{"_id":0,"word":1}):
            for keys in col.keys():
                words.append(col[keys])
        if len(words)!=0:
            output = words.copy()
        return output

    # def getIndexWord(self,wordsList,word):
    #     output=False
    #     for x in wordsList.items():



class Editing:
    def __init__(self):
        self.obj_Db = Db()


    def editWord(self,wordId,word=None,wordType=None,article=None,voiceName=None,telegramLink=None):
        print(f"wordId = {wordId}")
        output = False
        meaningId = None
        condition = None
        if isinstance(wordId,str):
            condition = {"_id":ObjectId(wordId)}
        else:
            condition = {"_id":wordId}
        
        if wordType!=None:
            valUpdate={"wordType":wordType}
        if article!=None:
            valUpdate={"article":article}
        if voiceName!=None:
            valUpdate={"voice.name":voiceName}
        if telegramLink!=None:
            valUpdate={"voice.telegramLink":telegramLink}
        verification = False
        for col in self.obj_Db.wordCollection.find(condition,{"_id":0,"meaningId":1}):
            for keys in col.keys():
                verification = True
                meaningId = col[keys]
        if verification is True:
            if word!=None:
                valUpdate={"word":word}
                self.obj_Db.wordCollection.update_many(condition,{"$set":valUpdate})
                output = True
                # valUpdateMeaning={"word":word}
                # self.obj_Db.wordCollection.update_many({"wordDetails.word":word},{"$set":valUpdateMeaning})
            if wordType!=None:
                valUpdate={"wordType":wordType}
                self.obj_Db.wordCollection.update_many(condition,{"$set":valUpdate})
                output = True
            if article!=None:
                valUpdate={"article":article}
                self.obj_Db.wordCollection.update_many(condition,{"$set":valUpdate})
                output = True
            if voiceName!=None:
                valUpdate={"voice.name":voiceName}
                self.obj_Db.wordCollection.update_many(condition,{"$set":valUpdate})
                output = True
            if telegramLink!=None:
                valUpdate={"voice.telegramLink":telegramLink}
                self.obj_Db.wordCollection.update_many(condition,{"$set":valUpdate})
                output = True
            if isinstance(meaningId,list):
                for x in meaningId:
                    mId = None
                    if isinstance(x,str):
                        condition = {"_id":ObjectId(x)}
                        mId = ObjectId(x)

                    else:
                        condition = {"_id":x}
                        mId = x
                    # for col in self.obj_Db.meaningCollection.find(condition)
                    if word!=None:
                        # valUpdateMeaning={"word":word}
                        self.obj_Db.meaningCollection.update_many(condition,{"$set":{"wordDetails.word":word}})
                        self.obj_Db.bookCollection.update_many({"meaningId":mId},{"$set":{"word":word}})
                    if wordType!=None:
                        self.obj_Db.meaningCollection.update_many(condition,{"$set":{"wordDetails.wordType":wordType}})
                    if article!=None:
                        self.obj_Db.meaningCollection.update_many(condition,{"$set":{"wordDetails.article":article}})
            else:
                    mId = None
                    if isinstance(x,str):
                        condition = {"_id":ObjectId(x)}
                        mId = ObjectId(x)

                    else:
                        condition = {"_id":x}
                        mId = x
                    # for col in self.obj_Db.meaningCollection.find(condition)
                    if word!=None:
                        # valUpdateMeaning={"word":word}
                        self.obj_Db.meaningCollection.update_many(condition,{"$set":{"wordDetails.word":word}})
                        self.obj_Db.bookCollection.update_many({"meaningId":mId},{"$set":{"word":word}})
                    if wordType!=None:
                        self.obj_Db.meaningCollection.update_many(condition,{"$set":{"wordDetails.wordType":wordType}})
                    if article!=None:
                        self.obj_Db.meaningCollection.update_many(condition,{"$set":{"wordDetails.article":article}})


            
        return output

    def editMeaning(self,meaningId,deutsch=None,english=None,synonym=None,persian=None,meaningNumDaf=None,synName=None,synTelegramLink=None,engName=None,engTelegramLink=None,perName=None,perTelegramLink=None,deuName=None,deuTelegramLink=None):
        output = False
        # print(f"perName = {perName}")
        condition = None
        if (meaningId,str):
            condition = {"_id":ObjectId(meaningId)}
        else:
            condition = {"_id":meaningId}
        if deutsch !=None:
            self.obj_Db.meaningCollection.update_many(condition,{"$set":{"deutsch":deutsch}})
            output=True
        if english!=None:
            self.obj_Db.meaningCollection.update_many(condition,{"$set":{"english":english}})    
            output=True
        if synonym !=None:
            self.obj_Db.meaningCollection.update_many(condition,{"$set":{"synonym":synonym}})  
            output = True
        if persian !=None:
            self.obj_Db.meaningCollection.update_many(condition,{"$set":{"persian":persian}})    
            output = True
        if meaningNumDaf !=None:
            self.obj_Db.meaningCollection.update_many(condition,{"$set":{"meaningNumDaf":meaningNumDaf}})    
            output = True
        if synName !=None:
            self.obj_Db.meaningCollection.update_many(condition,{"$set":{"synVoice.synName":synName}})    
            output = True
        if synTelegramLink !=None:
            self.obj_Db.meaningCollection.update_many(condition,{"$set":{"synVoice.synTelegramLink":synTelegramLink}})    
            output = True
        if engName !=None:
            self.obj_Db.meaningCollection.update_many(condition,{"$set":{"engVoice.engName":engName}})    
            output = True
        if engTelegramLink !=None:
            self.obj_Db.meaningCollection.update_many(condition,{"$set":{"engVoice.engTelegramLink":engTelegramLink}})    
            output = True
        if perName !=None:
            self.obj_Db.meaningCollection.update_many(condition,{"$set":{"perVoice.perName":perName}})    
            output = True
        if perTelegramLink !=None:
            self.obj_Db.meaningCollection.update_many(condition,{"$set":{"perVoice.perTelegramLink":perTelegramLink}})    
            output = True
        if deuName !=None:
            self.obj_Db.meaningCollection.update_many(condition,{"$set":{"deuVoice.deuName":deuName}})    
            output = True
        if deuTelegramLink !=None:
            self.obj_Db.meaningCollection.update_many(condition,{"$set":{"deuVoice.deuTelegramLink":deuTelegramLink}})    
            output = True
        return output


    def editBook(self,bookId,bookName=None,chapter=None,content=None,page=None,lesson=None,publisher=None):
        condition=None
        if isinstance(bookId,str):
            condition={"_id":ObjectId(bookId)}
        else:
            condition={"_id":bookId}
        if bookName!=None:
            valUpdate = {"bookName":bookName}
            self.obj_Db.bookCollection.update_many(condition,{"$set":valUpdate})
        if chapter!=None:
            valUpdate = {"chapter":chapter}
            self.obj_Db.bookCollection.update_many(condition,{"$set":valUpdate})
        if content!=None:
            valUpdate = {"content":content}
            self.obj_Db.bookCollection.update_many(condition,{"$set":valUpdate})
        if page!=None:
            valUpdate = {"page":page}
            self.obj_Db.bookCollection.update_many(condition,{"$set":valUpdate})
        if lesson!=None:
            valUpdate = {"lesson":lesson}
            self.obj_Db.bookCollection.update_many(condition,{"$set":valUpdate})
        if publisher!=None:
            valUpdate = {"publisher":publisher}
            self.obj_Db.bookCollection.update_many(condition,{"$set":valUpdate})









class Deleting:
    def __init__(self):
        self.obj_Db = Db()
    def deleteWord(self,wordId):
        output = False
        if isinstance(wordId,str):
            condition = {"_id":ObjectId(wordId)}
        else:
            condition = {"_id":wordId}
        self.obj_Db.wordCollection.delete_one(condition)
        verification = False
        for col in self.obj_Db.wordCollection.find(condition,{"word":1}):
            for keys in col.keys():
                verification = True
        if verification is True:
            output = True
        return output
    def deleteMeaning(self,meaningId,deutsch=None):
        output = True
        if isinstance(meaningId,str):
            temp = ObjectId(meaningId)
            meaningId = temp
        if deutsch !=None:
            condition = {"_id":meaningId,"deutsch":deutsch}
        else:
            condition = {"_id":meaningId}
        self.obj_Db.meaningCollection.delete_one(condition)
        for col in self.obj_Db.meaningCollection.find(condition,{"_id":1}):
            for keys in col.keys():
                output = False
        return output


    def deleteBook(self,bookId,meaningId=None):
        output = True
        if isinstance(bookId,str):
            temp = ObjectId(bookId)
            bookId = temp
        if meaningId !=None:
            condition = {"_id":bookId,"meaningId":meaningId}
        else:
            condition = {"_id":bookId}
        self.obj_Db.bookCollection.delete_one(condition)
        for col in self.obj_Db.bookCollection.find(condition,{"_id":1}):
            for keys in col.keys():
                output = False
        return output

        

class Entering:
    def __init__(self):
        self.obj_Db=Db()
    def checkRepeatedWord(self,word):
        #if there is a word like that returning True
        # and if there is not like this word returning False
        output = False
        repeatedWordList = []
        for col in self.obj_Db.wordCollection.find({"word":word},{"_id":0,"word":1}):
            for keys in col.keys():
                repeatedWordList.append(col[keys])
        if len(repeatedWordList) !=0:
            output=True
        return output



    def enterNewWord(self,word,wordType=None,article=None,voiceName=None,telegramLink=None,meaningId=None):
        output = False
        insVal = {"word":word,"wordType":wordType,"article":article,"voice":{"name":voiceName,"telegramLink":telegramLink},"meaningId":meaningId}

        self.obj_Db.wordCollection.insert_one(insVal)
        for col in self.obj_Db.wordCollection.find(insVal,{"_id":1}):
            for keys in col.keys():
                output = col[keys]
        return output

    def enterNewChildMeaning(self,wordId,deutsch,word, wordType=None,article=None,meaningNumDaf=None,deuName=None,deuTelegramLink=None,english=None,engName=None,engTelegramLink=None,synonym=None,synName=None,synTelegramLink=None,persian=None,perName=None,perTelegramLink=None):
        output = False
        verificationMeaningId = False
        verificationWord = False
        insertVal = {"deutsch":deutsch,"english":english,"synonym":synonym,"persian":persian,"meaningNumDaf":meaningNumDaf,"english":english,"synVoice":{"synName":synName,"synTelegramLink":synTelegramLink},"engVoice":{"engName":engName,"engTelegramLink":engTelegramLink},"perVoice":{"perName":perName,"perTelegramLink":perTelegramLink},"deuVoice":{"deuName":deuName,"deuTelegramLink":deuTelegramLink},"wordDetails":{"wordId":wordId,"word":word,"wordType":wordType,"article":article}}
        self.obj_Db.meaningCollection.insert_one(insertVal)
        outputMongo = {"_id":1}
        meaningId = None
        # cond ={"deutsch":deutsch,"wordDetails":{"wordId":wordId,"word":word,"wordType":wordType,"article":article}}
        for col in self.obj_Db.meaningCollection.find(insertVal,outputMongo):
            for keys in col.keys():
                meaningId = col[keys]
                verificationMeaningId=True
        # print(f"meaningId = {meaningId}\nverificationMeaningId = {verificationMeaningId}")
        meaningIdWordColcMongo=None
        for col in self.obj_Db.wordCollection.find({"_id":wordId},{"meaningId":1,"_id":0}):
            for keys in col.keys():
                meaningIdWordColcMongo=col[keys]
                verificationWord=True
        if isinstance(meaningIdWordColcMongo,str):
            temp = [meaningIdWordColcMongo]
            temp.append(ObjectId(meaningId))
            meaningIdWordColcMongo=temp
        # print(f"meaningIdWordColcMongo = {meaningIdWordColcMongo}")
        self.obj_Db.wordCollection.update_many({"_id":wordId},{"$set":{"meaningId":meaningIdWordColcMongo}})
        if verificationWord is True and verificationMeaningId is True:
            output = {"wordId":wordId,"meaningId":meaningId}
        return output

    def enterNewBook(self,meaningId,bookName,chapter=None,content=None,page=None,lesson=None,publisher=None,word=None):
        if isinstance(meaningId,str):
           temp = ObjectId(meaningId)
           meaningId = temp
        output = False
        insVal = {"bookName":bookName,"chapter":chapter,"content":content,"page":page,"lesson":lesson,"publisher":publisher,"word":word,"meaningId":meaningId}
        self.obj_Db.bookCollection.insert_one(insVal)
        for col in self.obj_Db.bookCollection.find(insVal,{"_id":1}):
            for keys in col.keys():
                output = col[keys]
        return output

    def enterNewMeaning(self,deutsch,word,wordType=None,article=None,meaningNumDaf=None,deuName=None,deuTelegramLink=None,english=None,engName=None,engTelegramLink=None,synonym=None,synName=None,synTelegramLink=None,persian=None,perName=None,perTelegramLink=None):
        output = False
        verificationMeaningId = False
        insertVal = {"deutsch":deutsch,"english":english,"synonym":synonym,"persian":persian,"meaningNumDaf":meaningNumDaf,"english":english,"synVoice":{"synName":synName,"synTelegramLink":synTelegramLink},"engVoice":{"engName":engName,"engTelegramLink":engTelegramLink},"perVoice":{"perName":perName,"perTelegramLink":perTelegramLink},"deuVoice":{"deuName":deuName,"deuTelegramLink":deuTelegramLink},"wordDetails":{"wordId":None,"word":word,"wordType":wordType,"article":article}}
        self.obj_Db.meaningCollection.insert_one(insertVal)
        outputMongo = {"_id":1}
        meaningId = None
        for col in self.obj_Db.meaningCollection.find(insertVal,outputMongo):
            for keys in col.keys():
                meaningId = col[keys]
                verificationMeaningId=True

        if verificationMeaningId is True:
            output = meaningId
        return output

    def enterAll(self,word,deutsch,bookName,wordType=None,article=None,voiceName=None,telegramLink=None,english=None,synonym=None,persian=None,meaningNumDaf=None,synName=None,synTelegramLink=None,perName=None,perTelegramLink=None,deuName=None,deuTelegramLink=None,engName=None,engTelegramLink=None,chapter=None,content=None,page=None,lesson=None,publisher=None):

        outputMeaningId = self.enterNewMeaning(deutsch,word,wordType=wordType,article=article,meaningNumDaf=meaningNumDaf,deuName=deuName,deuTelegramLink=deuTelegramLink,english=english,engName=engName,engTelegramLink=engTelegramLink,synonym=synonym,synName=synName,synTelegramLink=synTelegramLink,persian=persian,perName=perName,perTelegramLink=perTelegramLink)

        outputWordId = self.enterNewWord(word,wordType=wordType,article=article,voiceName=voiceName,telegramLink=telegramLink,meaningId=outputMeaningId)

        self.obj_Db.meaningCollection.update_many({"_id":outputMeaningId},{"$set":{"wordDetails.wordId":outputWordId}})

        outputBookId = self.enterNewBook(outputMeaningId,bookName,chapter=chapter,content=content,page=page,lesson=lesson,publisher=publisher,word=word)
        output = [outputWordId,outputMeaningId,outputBookId]
        return output
        


@pytest.fixture
def deleting():
    deleting=Deleting()
    return deleting       


@pytest.fixture
def search():
    search = Search()
    return search

@pytest.fixture
def editing():
    editing = Editing()
    return editing

@pytest.fixture
def db():
    db = Db()
    return db
@pytest.fixture
def entering():
    entering=Entering()
    return entering

class Testdb:
    def test_WordInMeaningNWordComparison(self,db):
        listMeaning = []
        listWord = []
        for colM in db.wordCollection.find({},{"word":1,"_id":0}):
            for keys in colM.keys():
                listWord.append(colM[keys])
        for colW in db.meaningCollection.find({},{"word":1,"_id":0}):
            for keys in colW.keys():
                listMeaning.append(colW[keys])
        if len(listMeaning) != len(listWord):
            difference = set(listWord)-set(listMeaning)
            # print(f"{difference = }")
        assert len(listMeaning) == len(listWord)        

class TestSearch:
    @pytest.mark.parametrize("word,deutsch",[
        ("sich freuen [vr]","freu·en; freute, hat gefreut; [Vr] 1 sich (über etwas (Akk)) freuen wegen etwas ein Gefühl der Freude empfinden <sich sehr, ehrlich, riesig freuen>: sich über ein Geschenk, einen Anruf freuen; Ich habe mich sehr darüber gefreut, dass wir uns endlich kennen gelernt haben; Ich freue mich, Sie wieder zu sehen"),
        ("die Entschuldigung;-,en",None),
        (None,"Na·me der; -ns, -n; 1 das Wort (oder die Wörter), unter dem man eine Person oder Sache kennt und durch das man sie identifizieren kann <jemandem / etwas einen Namen geben; einen Namen für jemanden / etwas suchen, finden, aussuchen; jemandes Namen tragen; sich einen anderen Namen beilegen, zulegen; seinen Namen nennen, sagen, angeben, verschweigen>: Jeder nennt sie Nini, aber ihr wirklicher Name ist Martina; Sein Name ist Meier  || K-: Namen(s)änderung, Namen(s)verzeichnis, Namen(s)wechsel  || -K: Familienname, Firmenname, Flussname, Frauenname, Hundename, Jungenname, Künstlername, Ländername, Mädchenname, Männername, Ortsname, Städtename, Stoffname, Tiername, Vorname"),
        (None,None),
        ("someWord",None),
        (None,"someDeutsch"),
        ("someWord","someDeutsch")


    ])
    def test_simpleSearch(self,word,deutsch,db,search):
        # output = [{"wordId":wordId,"word":word,"wordType":wordType,"article":article,"wordVoiceName":wordVoiceName,"wordTelAdd":wordTelAdd,
        # meaning1:{
            # "meaningId":meaningId,"deutschMeaning":deutschMeaning,"deutschFileName":deutschFileName,"deutschTelAdd":deutschTelAdd,"englishMeaning":englishMeaning,"englishTelAdd":englishTelAdd,"synonymMeaning":synonymMeaning,"synonymFileName":synonymFileName,"synonymTelAdd":synonymTelAdd,"persianMeaning":persianMeaning,"persianFileName":persianFileName,"persianTelAdd":persianTelAdd,book1:{
            # "bookId":bookId,"bookName":bookName,"chapter":chapter,"content":content,"page":page,"lesson":lesson,"publisher":publisher
            # }

        output = search.simpleSearch(word,deutsch)
        if output is not False:
            strWords = ["wordId","word","wordType","article","wordVoiceName","wordtelegramLink","wordNumRow","meaning1","meaning2","meaning3","meaning4","meaning5","meaning6","meaning7","meaning8","meaning9","meaning10"]
            
            strMeaning=["meaningId","deutschMeaning","deuName","deuTelegramLink","englishMeaning","engName","engTelegramLink","synonymMeaning","synName","synTelegramLink","persianMeaning","meaningNumDaf","perName","perTelegramLink","meaningNumRow","book1","book2","book3","book4","book5","book6","book7","book8","book9","book10"]
            strBook=["bookId","bookName","chapter","content","page","lesson","publisher","bookNumRow"]
            objectIdFields = ["wordId","meaningId","bookId"]
            # bookNumRow,meaningNumRow,wordNumRow
            assert isinstance(output,list)
            assert len(output)>0
            wordNum = 0
            meaningNum = 0
            bookNum = 0
            for x in output:
                assert isinstance(x,dict) 
                for field,val in x.items():

                    assert field in strWords
                    if field in objectIdFields:
                        assert isinstance(val,bson.objectid.ObjectId)
                    for i in range(1,10):
                        if field == f"meaning{i}":

                            for fieldMeaning,valmeaning in val.items():
                                # print(f"fieldMeaning = {fieldMeaning}")
                                assert fieldMeaning in strMeaning 
                                if fieldMeaning in objectIdFields:
                                    assert isinstance(valmeaning,bson.objectid.ObjectId) 
                                for j in range(1,10):
                                    if fieldMeaning == f"book{j}":
                                        for fieldBook,valBook in valmeaning.items():

                                            assert fieldBook in strBook 
                                            if fieldBook in objectIdFields:
                                                assert isinstance(valBook,bson.objectid.ObjectId) 
    @pytest.mark.parametrize("oneWordValues,wordVal",[
        ("word1",None),
        ("word2",False),
        ("word3",None),
        ("word4",False),
        ("word5",None)
    ])
    def test_getWordValues(self,db,entering,deleting,search,oneWordValues,wordValues,wordVal):
        ##process to make a word and get word Id
        wordTest,wordTypeTest,articleTest,voiceNameTest,telegramLinkTest,meaningIdTest=wordValues[oneWordValues] 
        if wordVal ==None:
            word=wordVal
        elif wordVal is False:
            word = wordTest
        wordId = entering.enterNewWord(wordTest,wordTypeTest,articleTest,voiceNameTest,telegramLinkTest,meaningIdTest)
        ## deleting.deleteWord(wordId)
        ##

        output = False
        if word !=None:
            output = search.getWordValues(wordId,word)
            condition = {"_id":wordId,"word":word}
        else:
            output = search.getWordValues(wordId)
            condition = {"_id":wordId}
        if len(output) !=0:
            assert isinstance (output,dict)
            assert wordId == output["wordId"]
            if word!=None:
                assert word == output["word"]
            fieldList = ["wordId","word","wordType","article","wordVoiceName","wordtelegramLink"]
            for field,val in output.items():
                assert field in fieldList
            outputMongo = {"_id":1,"word":1,"wordType":1,"article":1,"voice":1,"meaningId":1}
            wordVerification = False
      
            for col in db.wordCollection.find(condition,outputMongo):
                    for field,val in col.items():
                        wordVerification = True
                        if field == "_id":
                            assert output["wordId"]==val
                        elif field == "word":
                            assert output["word"]==val
                        elif field == "wordType":
                            assert output["wordType"]==val
                        elif field == "article":
                            assert output["article"]==val
                        elif field == "voice":
                            assert output["wordVoiceName"]==val["name"]
                            assert output["wordtelegramLink"]==val["telegramLink"]
            assert wordVerification is True
            ## delete test word
            deleting.deleteWord(wordId)
            # print(wordId)
            verification = False
            for col in db.wordCollection.find({"_id":wordId},{"_id":1}):
                for keys in col.keys():
                    verification = True
            assert verification is False    
    @pytest.mark.parametrize("oneWordValues,oneMeaningVlue",[
        ("word1","meaning1"),
        ("word2","meaning2"),
        ("word3","meaning3"),
        ("word4","meaning4"),
        ("word5","meaning5")
    ])
    def test_getMeaningValues(self,db,entering,deleting,search,meaningValues,oneMeaningVlue,wordValues,oneWordValues):
        wordTest,wordTypeTest,articleTest,voiceNameTest,telegramLinkTest,meaningIdTest=wordValues[oneWordValues] 

        wordId = entering.enterNewWord(wordTest,wordTypeTest,articleTest,voiceNameTest,telegramLinkTest,meaningIdTest)

        deutschTest,englishTest,synonymTest,persianTest,meaningNumDafTest,synNameTest,synTelegramLinkTest,perNameTest,perTelegramLinkTest,deuNameTest,deuTelegramLinkTest,engNameTest,engTelegramLinkTest,_=meaningValues[oneMeaningVlue]

        ouputNewChildMeaning=entering.enterNewChildMeaning(wordId,deutschTest,wordTest, wordTypeTest,articleTest,meaningNumDafTest,deuNameTest,deuTelegramLinkTest,englishTest,engNameTest,engTelegramLinkTest,synonymTest,synNameTest,synTelegramLinkTest,persianTest,perNameTest,perTelegramLinkTest)

        meaningId = ouputNewChildMeaning["meaningId"]

        output = search.getMeaningValues(meaningId) 
        if output is not False:
            meaningIdMon,deutschMon,wordIdMon,wordMon, wordTypeMon,articleMon,meaningNumDafMon,deuNameMon,deuTelegramLinkMon,englishMon,engNameMon,engTelegramLinkMon,synonymMon,synNameMon,synTelegramLinkMon,persianMon,perNameMon,perTelegramLinkMon = None,None, None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None
            condition = None
            if isinstance(meaningId,str):
                condition = {"_id":ObjectId(meaningId)}
            else:
                condition = {"_id":meaningId}
            outputMon = {"_id":1,"deutsch":1,"english":1,"synonym":1,"persian":1,"meaningNumDaf":1,"synVoice":1,"engVoice":1,"perVoice":1,"deuVoice":1,"wordDetails":1}
            for col in db.meaningCollection.find(condition,outputMon):
                for field,val in col.items():
                    if field == "_id":
                        meaningIdMon = val
                    elif field == "deutsch":
                        deutschMon = val
                    elif field == "english":
                        englishMon = val
                    elif field == "synonym":
                        synonymMon = val
                    elif field == "persian":
                        persianMon = val
                    elif field == "meaningNumDaf":
                        meaningNumDafMon = val
                    elif field == "synVoice":
                        synNameMon=val["synName"]
                        synTelegramLinkMon=val["synTelegramLink"]
                    elif field == "engVoice":
                        engNameMon=val["engName"]
                        engTelegramLinkMon=val["engTelegramLink"]
                    elif field == "perVoice":
                        perNameMon = val["perName"]
                        perTelegramLinkMon = val["perTelegramLink"]
                    elif field == "deuVoice":
                        deuNameMon=val["deuName"]
                        deuTelegramLinkMon=val["deuTelegramLink"]
                    elif field == "wordDetails":
                        wordIdMon=val["wordId"]
                        wordMon=val["word"]
                        wordTypeMon=val["wordType"]
                        articleMon=val["article"]
            assert  meaningIdMon == meaningId
            assert output ["meaningId"]== meaningIdMon    
            assert output ["deutsch"]== deutschMon
            assert output ["english"]== englishMon
            assert output ["synonym"]== synonymMon
            assert output ["persian"]== persianMon
            assert output ["meaningNumDaf"]== meaningNumDafMon
            assert output ["synName"]== synNameMon
            assert output ["synTelegramLink"]== synTelegramLinkMon
            assert output ["engName"]== engNameMon
            assert output ["engTelegramLink"]== engTelegramLinkMon
            assert output ["perName"]== perNameMon
            assert output ["perTelegramLink"]== perTelegramLinkMon
            assert output ["deuName"]== deuNameMon
            assert output ["deuTelegramLink"]== deuTelegramLinkMon

            assert output ["wordId"]== wordIdMon
            assert output ["word"]== wordMon
            assert output ["wordType"]== wordTypeMon
            assert output ["article"]== articleMon
            
            ### deleting word and meaning test
            ##delete word test
            outputWordDel = deleting.deleteWord(wordId)
            if outputWordDel is True:
                if isinstance(wordId,str):
                    condition = {"_id":ObjectId(wordId)}
                else:
                    condition = {"_id":wordId}
                verification = False
                for col in db.wordCollection.find(condition,{"word":1}):
                    for keys in col.keys():
                        verification = True
                assert verification is False
            ## delete meaning test
            outputMeaningDel = deleting.deleteMeaning(meaningId)
            if outputMeaningDel is True:
                if isinstance(wordId,str):
                    condition = {"_id":ObjectId(meaningId)}
                else:
                    condition = {"_id":meaningId}
                verification = False
                for col in db.meaningCollection.find(condition,{"deutsch":1}):
                    for keys in col.keys():
                        verification = True
                assert verification is False
    @pytest.mark.parametrize("oneWordValues,oneMeaningVlue,oneBookValues",[
        ("word1","meaning1","book1"),
        ("word2","meaning2","book2"),
        ("word3","meaning3","book3"),
        ("word4","meaning4","book4"),
        ("word5","meaning5","book5")
    ])
    def test_getBookValues(self,db,entering,deleting,search,meaningValues,oneMeaningVlue,wordValues,oneWordValues,oneBookValues,bookValues):
        ### make test values
        wordTest,wordTypeTest,articleTest,voiceNameTest,telegramLinkTest,meaningIdTest=wordValues[oneWordValues] 

        wordId = entering.enterNewWord(wordTest,wordTypeTest,articleTest,voiceNameTest,telegramLinkTest,meaningIdTest)

        deutschTest,englishTest,synonymTest,persianTest,meaningNumDafTest,synNameTest,synTelegramLinkTest,perNameTest,perTelegramLinkTest,deuNameTest,deuTelegramLinkTest,engNameTest,engTelegramLinkTest,_=meaningValues[oneMeaningVlue]

        outputEnterNewChildMeaning = entering.enterNewChildMeaning(wordId,deutschTest,wordTest, wordTypeTest,articleTest,meaningNumDafTest,deuNameTest,deuTelegramLinkTest,englishTest,engNameTest,engTelegramLinkTest,synonymTest,synNameTest,synTelegramLinkTest,persianTest,perNameTest,perTelegramLinkTest)
        bookNameTest,chapterTest,contentTest,pageTest,lessonTest,publisherTest,_,_=bookValues[oneBookValues]
        # outputEnterNewChildMeaning = {"wordId":wordId,"meaningId":meaningId}
        meaningId = outputEnterNewChildMeaning["meaningId"]
        bookId = entering.enterNewBook(meaningId,bookNameTest,chapterTest,contentTest,pageTest,lessonTest,publisherTest,wordTest)
        ##### 
        output= search.getBookValues(bookId)


        if len(output)!=0:
            bookIdMon,bookNameMon,chapterMon,contentMon,pageMon,lessonMon,publisherMon,wordMon,meaningIdMon=None,None,None,None,None,None,None,None,None
            condition = None
            if isinstance(bookId,str):
                condition = {"_id":ObjectId(bookId)}
            else:
                condition = {"_id":bookId}
            outputMon = {"_id":1,"bookName":1,"chapter":1,"content":1,"page":1,"lesson":1,"publisher":1,"word":1,"meaningId":1}

            for col in db.bookCollection.find(condition,outputMon):
                for field,val in col.items():
                    if field == "_id":
                        bookIdMon = val
                    elif field == "bookName":
                        bookNameMon = val
                    elif field == "chapter":
                        chapterMon = val                      
                    elif field == "content":
                        contentMon = val
                    elif field == "page":
                        pageMon = val
                    elif field == "lesson":
                        lessonMon = val
                    elif field == "publisher":
                        publisherMon = val
                    elif field == "word":
                        wordMon = val
                    elif field == "meaningId":
                        meaningIdMon = val    

            assert bookIdMon == bookId
            assert output["bookId"] == bookIdMon
            assert output["bookName"] == bookNameMon
            assert output["chapter"] == chapterMon
            assert output["content"] == contentMon
            print(f"output = {output}")
            assert output["page"] == pageMon
            assert output["lesson"] == lessonMon
            assert output["publisher"] == publisherMon
            assert output["word"] == wordMon
            assert output["meaningId"] == meaningIdMon
            ### deleting word and meaning test
            ##delete word test
            outputWordDel = deleting.deleteWord(wordId)
            if outputWordDel is True:
                if isinstance(wordId,str):
                    condition = {"_id":ObjectId(wordId)}
                else:
                    condition = {"_id":wordId}
                verification = False
                for col in db.wordCollection.find(condition,{"word":1}):
                    for keys in col.keys():
                        verification = True
                assert verification is False
            ## delete meaning test
            outputMeaningDel = deleting.deleteMeaning(meaningId)
            if outputMeaningDel is True:
                if isinstance(wordId,str):
                    condition = {"_id":ObjectId(meaningId)}
                else:
                    condition = {"_id":meaningId}
                verification = False
                for col in db.meaningCollection.find(condition,{"deutsch":1}):
                    for keys in col.keys():
                        verification = True
                assert verification is False
            # ## delete book test
            outputBookId = bookId
            outputBookDel = deleting.deleteBook(outputBookId)
            if outputBookDel is True:
                if isinstance(outputBookId,str):
                    condition = {"_id":ObjectId(outputBookId)}
                else:
                    condition = {"_id":outputBookId}
                verification = False
                for col in db.bookCollection.find(condition,{"_id":1}):
                    for keys in col.keys():
                        verification = True
                assert verification is False

    # @pytest.mark.parametrize("alphabet",[
    #     ("a"),
    #     ("f"),
    #     ("e"),
    #     ("sich")
    # ])
    # def test_containedWordOrAlphabet(self,db,alphabet):
    #     words = []
    #     # condition = {"word":f"/{alphabet}/"}
    #     condition = {"word":{'$regex':alphabet}}
    #     outputMongo={"_id":0,"word":1}
    #     for col in db.wordCollection.find(condition,outputMongo):
    #         for keys in col.keys():
    #             words.append(col[keys])
    #     print(f"words = {words}")

    @pytest.mark.parametrize("word",[
        ("a"),
        ("b"),
        ("fr"),
        ("di"),
        ("de")
    ])
    def test_getSearchContain(self,db,search,word):
        output=search.getSearchContain(word)
        print(output)
        if output is not False:
            assert (output,list)
            assert len(output)>0

    def test_getAllWords(self,db,search):
        output=search.getAllwords()
        if output is not False:
            assert isinstance(output,list)
            for x in output:
                assert isinstance(x,str)

    # @pytest.mark.parametrize("wordsList,word",[
    #     (["yek","do","se","chahar"],"yek"),
    #     (["yek","do","se","chahar"],"do"),
    #     (["yek","do","se","chahar"],"se"),
    #     (["yek","do","se","chahar"],"panj")
    # ])
    # def test_getIndexWord(self,db,search,wordsList,word):
    #     output=search.getIndexWord(wordsList,word)
    #     if output is not False:
    #         assert isinstance(output,int)
    #         assert word in wordsList

class TestEditing:


    @pytest.mark.parametrize("oneWordValues,word,wordType,article,voiceName,telegramLink,meaningId,oneMeaningVlue,oneBookValues",[
        ("word1","w1","wt1","a1","vn1","tl1",["mn1"],"meaning1","book1"),
        ("word2","w2","wt2","a2","vn2","tl2",["mn2"],"meaning2","book2"),
        ("word3","w3","wt3","a3","vn3","tl3",["mn3"],"meaning3","book4"),
        ("word4","w4","wt4","a4","vn4","tl4",["mn4"],"meaning4","book4"),
        ("word5","w5","wt5","a5","vn5","tl5",["mn5"],"meaning5","book5")
    ])
    def test_editWord(self,db,editing,entering,deleting,wordValues,oneWordValues,word,wordType,article,voiceName,telegramLink,meaningId,oneMeaningVlue,meaningValues,oneBookValues,bookValues):
        ## create test values
        wordTest,wordTypeTest,articleTest,voiceNameTest,telegramLinkTest,meaningIdTest=wordValues[oneWordValues] 

        wordId = entering.enterNewWord(wordTest,wordTypeTest,articleTest,voiceNameTest,telegramLinkTest,meaningIdTest)

        deutschTest,englishTest,synonymTest,persianTest,meaningNumDafTest,synNameTest,synTelegramLinkTest,perNameTest,perTelegramLinkTest,deuNameTest,deuTelegramLinkTest,engNameTest,engTelegramLinkTest,_=meaningValues[oneMeaningVlue]

        outputEnterNewChildMeaning = entering.enterNewChildMeaning(wordId,deutschTest,wordTest, wordTypeTest,articleTest,meaningNumDafTest,deuNameTest,deuTelegramLinkTest,englishTest,engNameTest,engTelegramLinkTest,synonymTest,synNameTest,synTelegramLinkTest,persianTest,perNameTest,perTelegramLinkTest)
        bookNameTest,chapterTest,contentTest,pageTest,lessonTest,publisherTest,_,_=bookValues[oneBookValues]
        meaningId = outputEnterNewChildMeaning["meaningId"]
        if isinstance(wordId,str):
            cond={"_id":ObjectId(wordId)}
        else:
            cond={"_id":wordId}
        db.wordCollection.update_many(cond,{"$set":{"meaningId":[meaningId]}})
        outputId = entering.enterNewBook(meaningId,bookNameTest,chapterTest,contentTest,pageTest,lessonTest,publisherTest,wordTest)
        #####




        output= editing.editWord(wordId,word,wordType,article,voiceName,telegramLink)
        # print(f"output = {output}")
        if output is True:
            if isinstance(wordId,str):
                condition = {"_id":ObjectId(wordId)}
            else:
                condition = {"_id":wordId}
            outputMongo = {"word":1,"article":1,"wordType":1,"voice":1,"meaningId":1}
            wordMongo,wordTypeMongo,articleMongo,voiceNameMongo,telegramLinkMongo,meaningIdMongo = None,None,None,None,None,None
            for col in db.wordCollection.find(condition,outputMongo):
                for field,val in col.items():
                    if field =="word":
                        wordMongo = val
                    elif field == "article":
                        articleMongo = val
                    elif field == "wordType":
                        wordTypeMongo = val
                    elif field == "voice":
                        voiceNameMongo = val["name"]
                        telegramLinkMongo = val["telegramLink"]
                    elif field == "meaningId":
                        meaningIdMongo = val

            # print(f"telegramLink ={telegramLink}\ntelegramLinkMongo = {telegramLinkMongo}")
            if voiceName != None:
                assert voiceName == voiceNameMongo
            if telegramLink != None:
                assert telegramLink == telegramLinkMongo
                # print(f"telegramLink ={telegramLink}\ntelegramLinkMongo = {telegramLinkMongo}")
            
            if isinstance(meaningIdMongo,list):
                for x in meaningIdMongo:
                    condition=None
                    mId = None
                    if isinstance(x,str):
                        condition = {"_id":ObjectId(x)}
                        mId = ObjectId(x)
                    else:
                        condition = {"_id":x}
                        mId = x
                    outputMonMean = {"_id":1,"wordDetails":1}
                    wordMean,wordTypeMean,articleMean=None,None,None
                    for col in db.meaningCollection.find(condition,outputMonMean):
                        for field,val in col.items():
                            # print("hi from in list")
                            if field == "wordDetails":
                                wordMean=val["word"]
                                wordTypeMean=val["wordType"]
                                articleMean=val["article"]
                    # print(f"wordMean = {wordMean}\nwordTypeMean={wordTypeMean}\narticleMean={articleMean}")
                    wordBook=None
                    outputMonBook = {"word":1,"_id":0}
                    for col in db.bookCollection.find({"meaningId":mId},outputMonBook):
                        for keys in col.keys():
                            wordBook = col[keys]

                    if word !=None:
                        assert word == wordMongo
                        assert word == wordMean
                        assert word == wordBook
                    if wordType !=None:
                        assert wordType == wordTypeMongo
                        assert wordType == wordTypeMean
                    if article != None:
                        assert article == articleMongo
                        assert article == articleMean
            else:
                    if isinstance(meaningIdMongo,str):
                        condition = {"_id":ObjectId(meaningIdMongo)}
                    else:
                        condition = {"_id":meaningIdMongo}
                    outputMonMean = {"_id":1,"wordDetails":1}
                    wordMean,wordTypeMean,articleMean=None,None,None
                    for col in db.meaningCollection.find(condition,outputMonMean):
                        for field,val in col.items():
                            if field == "wordDetails":
                                # print("hi from in str")
                                wordMean=val["word"]
                                wordTypeMean=val["wordType"]
                                articleMean=val["article"]
                    # print(f"wordMean = {wordMean}\nwordTypeMean={wordTypeMean}\narticleMean={articleMean}")
                    wordBook=None
                    outputMonBook = {"word":1,"_id":0}
                    for col in db.bookCollection.find(condition,outputMonBook):
                        for keys in col.keys():
                            wordBook = col[keys]

                    if word !=None:
                        assert word == wordMongo
                        assert word == wordMean
                        assert word == wordBook
                    if wordType !=None:
                        assert wordType == wordTypeMongo
                        assert wordType == wordTypeMean
                    if article != None:
                        assert article == articleMongo
                        assert article == articleMean


            ## delete test word
            # deleting.deleteWord(wordId)
            # # print(wordId)
            # verification = False
            # for col in db.wordCollection.find({"_id":wordId},{"_id":1}):
            #     for keys in col.keys():
            #         verification = True
            # assert verification is False    

            ### deleting word and meaning test
            ##delete word test
            outputWordDel = deleting.deleteWord(wordId)
            if outputWordDel is True:
                if isinstance(wordId,str):
                    condition = {"_id":ObjectId(wordId)}
                else:
                    condition = {"_id":wordId}
                verification = False
                for col in db.wordCollection.find(condition,{"word":1}):
                    for keys in col.keys():
                        verification = True
                assert verification is False
            ## delete meaning test
            if isinstance(meaningIdMongo,list):

                for x in meaningIdMongo:
                    mId=None
                    condition = None
                    outputMeaningDel = deleting.deleteMeaning(x)
                    if outputMeaningDel is True:
                        if isinstance(x,str):
                            condition = {"_id":ObjectId(x)}
                            mId = ObjectId(x)
                        else:
                            condition = {"_id":x}
                            mId = ObjectId(x)
                        verification = False
                        for col in db.meaningCollection.find(condition,{"deutsch":1}):
                            for keys in col.keys():
                                verification = True
                        assert verification is False
                    ### delete book part list
                    db.bookCollection.delete_one({"meaningId":mId})
                    verification = False
                    for col in db.bookCollection.find({"meaningId":mId},{"meaningId":1}):
                        for keys in col.keys():
                            verification = True
                    assert verification is False
            else:
                    mId=None
                    condition = None
                    outputMeaningDel = deleting.deleteMeaning(meaningIdMongo)
                    if outputMeaningDel is True:
                        if isinstance(meaningIdMongo,str):
                            condition = {"_id":ObjectId(meaningIdMongo)}
                            mId = ObjectId(meaningId)
                        else:
                            condition = {"_id":meaningIdMongo}
                            mId = meaningIdMongo
                        verification = False
                        for col in db.meaningCollection.find(condition,{"deutsch":1}):
                            for keys in col.keys():
                                verification = True
                        assert verification is False
                    ### delete book part str
                    db.bookCollection.delete_one({"meaningId":mId})
                    verification = False
                    for col in db.bookCollection.find({"meaningId":mId},{"meaningId":1}):
                        for keys in col.keys():
                            verification = True
                    assert verification is False
        







    @pytest.mark.parametrize("oneMeaningVlue,oneWordValues,editedValues",[
        ("meaning1","word1",{"deutsch":"deutschEdit1","english":"englishEdit1","synonym":"synonymEdit1","persian":None,"meaningNumDaf":"meaningNumDafEdit1","synName":"synNameEdit1","synTelegramLink":"synTelegramLinkEdit1","engName":"engNameEdit1","engTelegramLink":None,"perName":"perNameEdit1","perTelegramLink":"perTelegramLinkEdit1","deuName":"deuNameEdit1","deuTelegramLink":"deuTelegramLinkEdit1"}),
        ("meaning2","word2",{"deutsch":"deutschEdit2","english":"englishEdit2","synonym":"synonymEdit2","persian":"persianEdit1","meaningNumDaf":"meaningNumDafEdit2","synName":"synNameEdit2","synTelegramLink":"synTelegramLinkEdit2","engName":"engNameEdit2","engTelegramLink":None,"perName":None,"perTelegramLink":"perTelegramLinkEdit2","deuName":"deuNameEdit2","deuTelegramLink":"deuTelegramLinkEdit2"}),
        ("meaning3","word3",{"deutsch":"deutschEdit3","english":"englishEdit3","synonym":"synonymEdit3","persian":"persianEdit1","meaningNumDaf":"meaningNumDafEdit3","synName":"synNameEdit3","synTelegramLink":None,"engName":"engNameEdit3","engTelegramLink":"engTelegramLinkEdit3","perName":"perNameEdit3","perTelegramLink":"perTelegramLinkEdit3","deuName":None,"deuTelegramLink":"deuTelegramLinkEdit3"}),
        ("meaning4","word4",{"deutsch":"deutschEdit4","english":"englishEdit4","synonym":"synonymEdit4","persian":None,"meaningNumDaf":"meaningNumDafEdit4","synName":"synNameEdit4","synTelegramLink":"synTelegramLinkEdit4","engName":"engNameEdit4","engTelegramLink":None,"perName":"perNameEdit4","perTelegramLink":"perTelegramLinkEdit4","deuName":"deuNameEdit4","deuTelegramLink":"deuTelegramLinkEdit4"}),
        ("meaning5","word5",{"deutsch":"deutschEdit5","english":"englishEdit5","synonym":"synonymEdit5","persian":"persianEdit1","meaningNumDaf":"meaningNumDafEdit5","synName":"synNameEdit5","synTelegramLink":None,"engName":"engNameEdit5","engTelegramLink":"engTelegramLinkEdit5","perName":"perNameEdit5","perTelegramLink":None,"deuName":"deuNameEdit5","deuTelegramLink":"deuTelegramLinkEdit5"})
    ]) 

    def test_editMeaning(self,db,editing,entering,deleting,oneMeaningVlue,meaningValues,oneWordValues,wordValues,editedValues):
        wordTest,wordTypeTest,articleTest,voiceNameTest,telegramLinkTest,meaningIdTest=wordValues[oneWordValues] 

        wordId = entering.enterNewWord(wordTest,wordTypeTest,articleTest,voiceNameTest,telegramLinkTest,meaningIdTest)

        deutschTest,englishTest,synonymTest,persianTest,meaningNumDafTest,synNameTest,synTelegramLinkTest,perNameTest,perTelegramLinkTest,deuNameTest,deuTelegramLinkTest,engNameTest,engTelegramLinkTest,_=meaningValues[oneMeaningVlue]

        ouputNewChildMeaning=entering.enterNewChildMeaning(wordId,deutschTest,wordTest, wordTypeTest,articleTest,meaningNumDafTest,deuNameTest,deuTelegramLinkTest,englishTest,engNameTest,engTelegramLinkTest,synonymTest,synNameTest,synTelegramLinkTest,persianTest,perNameTest,perTelegramLinkTest)

        meaningId = ouputNewChildMeaning["meaningId"]
        output = editing.editMeaning(meaningId,deutsch=editedValues["deutsch"],english=editedValues["english"],synonym=editedValues["synonym"],persian=editedValues["persian"],meaningNumDaf=editedValues["meaningNumDaf"],synName=editedValues["synName"],synTelegramLink=editedValues["synTelegramLink"],engName=editedValues["engName"],engTelegramLink=editedValues["engTelegramLink"],perName=editedValues["perName"],perTelegramLink=editedValues["perTelegramLink"],deuName=editedValues["deuName"],deuTelegramLink=editedValues["deuTelegramLink"])
        if output is not False:
            condition={"_id":meaningId}
            outputMongo={"_id":1,"deutsch":1,"english":1,"synonym":1,"persian":1,"meaningNumDaf":1,"synVoice":1,"engVoice":1,"perVoice":1,"deuVoice":1}
            meaningIdMon,deutschMon,englishMon,synonymMon,persianMon,meaningNumDafMon,synNameMon,synTelegramLinkMon,engNameMon,engTelegramLinkMon,perNameMon,perTelegramLinkMon,deuNameMon,deuTelegramLinkMon = None,None,None,None,None,None,None,None,None,None,None,None,None,None
            for col in db.meaningCollection.find(condition,outputMongo):
                for keys,val in col.items():
                        if keys == "_id":
                            meaningIdMon=val
                        elif keys == "deutsch":
                            deutschMon = val
                        elif keys == "english":
                            englishMon = val
                        elif keys == "synonym":
                            synonymMon = val
                        elif keys == "persian":
                            persianMon = val
                        elif keys == "meaningNumDaf":
                            meaningNumDafMon = val
                        elif keys == "synVoice":
                            synNameMon=val["synName"]
                            synTelegramLinkMon=val["synTelegramLink"]
                        elif keys == "engVoice":
                            engNameMon=val["engName"]
                            engTelegramLinkMon=val["engTelegramLink"]
                        elif keys == "perVoice":
                            perNameMon=val["perName"]
                            perTelegramLinkMon=val["perTelegramLink"]
                        elif keys == "deuVoice":
                            deuNameMon=val["deuName"]
                            deuTelegramLinkMon=val["deuTelegramLink"]


            assert meaningId == meaningIdMon
            if editedValues["deutsch"] !=None:
                # print(f"editedValues[deutsch] ={editedValues['deutsch']}\n deutschMon={deutschMon}")
                assert editedValues["deutsch"] == deutschMon
            if editedValues["english"] !=None:
                assert editedValues["english"] == englishMon
            if editedValues["synonym"] !=None: 
                assert editedValues["synonym"]== synonymMon
            if editedValues["persian"] !=None:
                assert editedValues["persian"] == persianMon
            if editedValues["meaningNumDaf"] !=None:
                assert editedValues["meaningNumDaf"] == meaningNumDafMon
            if editedValues["synName"] !=None:
                assert editedValues["synName"] == synNameMon
            if editedValues["synTelegramLink"] !=None:
                assert editedValues["synTelegramLink"] == synTelegramLinkMon
            if editedValues["engName"] !=None:
                assert editedValues["engName"] == engNameMon
            if editedValues["engTelegramLink"] !=None:
                print(f"editedValues[engTelegramLink] ={editedValues['engTelegramLink']}\n engTelegramLinkMon={engTelegramLinkMon}")
                assert editedValues["engTelegramLink"] == engTelegramLinkMon
            if editedValues["perName"] !=None:
                assert editedValues["perName"] == perNameMon
            if editedValues["perTelegramLink"] !=None:
                assert editedValues["perTelegramLink"] == perTelegramLinkMon
            if editedValues["deuName"] !=None:
                assert editedValues["deuName"] == deuNameMon
            if editedValues["deuTelegramLink"] !=None:
                assert editedValues["deuTelegramLink"] == deuTelegramLinkMon

            ### deleting word and meaning test
            ##delete word test
            outputWordDel = deleting.deleteWord(wordId)
            if outputWordDel is True:
                if isinstance(wordId,str):
                    condition = {"_id":ObjectId(wordId)}
                else:
                    condition = {"_id":wordId}
                verification = False
                for col in db.wordCollection.find(condition,{"word":1}):
                    for keys in col.keys():
                        verification = True
                assert verification is False
            ## delete meaning test
            outputMeaningDel = deleting.deleteMeaning(meaningId)
            if outputMeaningDel is True:
                if isinstance(wordId,str):
                    condition = {"_id":ObjectId(meaningId)}
                else:
                    condition = {"_id":meaningId}
                verification = False
                for col in db.meaningCollection.find(condition,{"deutsch":1}):
                    for keys in col.keys():
                        verification = True
                assert verification is False




    @pytest.mark.parametrize("oneMeaningVlue,oneWordValues,oneBookValues,editValues",[
        ("meaning1","word1","book1",{"bookName":"bookNameEdited1","chapter":"chapterEdited1","content":"contentEdited1","page":"pageEdited1","lesson":"lessonEdited1","publisher":"publisherEdited1","word":"wordEdited1","meaningId":"meaningIdEdited1"}),
        
        ("meaning2","word2","book2",{"bookName":"bookNameEdited2","chapter":"chapterEdited2","content":"contentEdited2","page":"pageEdited2","lesson":"lessonEdited2","publisher":"publisherEdited2","word":"wordEdited2","meaningId":"meaningIdEdited2"}),
        
        ("meaning3","word3","book3",{"bookName":"bookNameEdited3","chapter":"chapterEdited3","content":"contentEdited3","page":"pageEdited3","lesson":"lessonEdited1","publisher":"publisherEdited3","word":"wordEdited3","meaningId":"meaningIdEdited3"}),
        
        ("meaning4","word4","book4",{"bookName":"bookNameEdited4","chapter":"chapterEdited4","content":"contentEdited4","page":"pageEdited4","lesson":"lessonEdited4","publisher":"publisherEdited4","word":"wordEdited4","meaningId":"meaningIdEdited4"}),
        
        ("meaning5","word5","book5",{"bookName":"bookNameEdited5","chapter":"chapterEdited5","content":"contentEdited5","page":"pageEdited5","lesson":"lessonEdited5","publisher":"publisherEdited5","word":"wordEdited5","meaningId":"meaningIdEdited5"})
    ])
    def test_editBook(self,db,editing,deleting,entering,meaningValues,oneMeaningVlue,wordValues,oneWordValues,bookValues,oneBookValues,editValues):
        ## inster test values
        wordTest,wordTypeTest,articleTest,voiceNameTest,telegramLinkTest,meaningIdTest=wordValues[oneWordValues] 

        wordId = entering.enterNewWord(wordTest,wordTypeTest,articleTest,voiceNameTest,telegramLinkTest,meaningIdTest)

        deutschTest,englishTest,synonymTest,persianTest,meaningNumDafTest,synNameTest,synTelegramLinkTest,perNameTest,perTelegramLinkTest,deuNameTest,deuTelegramLinkTest,engNameTest,engTelegramLinkTest,_=meaningValues[oneMeaningVlue]

        outputEnterNewChildMeaning = entering.enterNewChildMeaning(wordId,deutschTest,wordTest, wordTypeTest,articleTest,meaningNumDafTest,deuNameTest,deuTelegramLinkTest,englishTest,engNameTest,engTelegramLinkTest,synonymTest,synNameTest,synTelegramLinkTest,persianTest,perNameTest,perTelegramLinkTest)
        bookNameTest,chapterTest,contentTest,pageTest,lessonTest,publisherTest,_,_=bookValues[oneBookValues]

        meaningId = outputEnterNewChildMeaning["meaningId"]

        outputBookId = entering.enterNewBook(meaningId,bookNameTest,chapterTest,contentTest,pageTest,lessonTest,publisherTest,wordTest)
        
        
        ##
        output = editing.editBook(outputBookId,bookName = editValues["bookName"],chapter = editValues["chapter"],content=editValues["content"],page=editValues["page"],lesson=editValues["lesson"],publisher=editValues["publisher"])
        
        # "bookName":"bookNameEdited1","chapter":"chapterEdited2","content":"contentEdited1","page":"pageEdited1","lesson":"lessonEdited1","publisher":"publisherEdited1","word":"wordEdited1"
        if output is not False:
            bookIdMon,bookNameMon,chapterMon,contentMon,pageMon,lessonMon,publisherMon,wordMon=None,None,None,None,None,None,None,None
            if isinstance(outputBookId,str):
                condition= {"_id":ObjectId(outputBookId)}
            else:
                condition= {"_id":outputBookId}
            outputMon = {"_id":1,"bookName":1,"chapter":1,"content":1,"page":1,"lesson":1,"publisher":1,"word":1}
            for col in db.bookCollection.find(condition,outputMon):
                for field,val in col.items():
                    if field == "_id":
                        bookIdMon = val
                    elif field == "bookName":
                        bookNameMon =val
                    elif field == "chapter":
                        chapterMon = val
                    elif field == "content":
                        contentMon = val
                    elif field == "page":
                        pageMon = val
                    elif field == "lesson":
                        lessonMon = val
                    elif field == "publisher":
                        publisherMon = val
                    elif field == "word":
                        wordMon = val
            if editValues["bookName"]!=None:
               assert  editValues["bookName"] == bookNameMon
            if editValues["chapter"]!=None:
               assert editValues["chapter"] == chapterMon
            if editValues["content"]!=None:
               assert editValues["content"] == contentMon                
            if editValues["page"]!=None:
               assert editValues["page"] == pageMon
            if editValues["lesson"]!=None:
               assert editValues["lesson"] == lessonMon
            if editValues["publisher"]!=None:
               assert editValues["publisher"] == publisherMon
            if editValues["chapter"]!=None:
               assert editValues["chapter"] == chapterMon

            ### deleting word and meaning test
            ##delete word test
            outputWordDel = deleting.deleteWord(wordId)
            if outputWordDel is True:
                if isinstance(wordId,str):
                    condition = {"_id":ObjectId(wordId)}
                else:
                    condition = {"_id":wordId}
                verification = False
                for col in db.wordCollection.find(condition,{"word":1}):
                    for keys in col.keys():
                        verification = True
                assert verification is False
            ## delete meaning test
            outputMeaningDel = deleting.deleteMeaning(meaningId)
            if outputMeaningDel is True:
                if isinstance(wordId,str):
                    condition = {"_id":ObjectId(meaningId)}
                else:
                    condition = {"_id":meaningId}
                verification = False
                for col in db.meaningCollection.find(condition,{"deutsch":1}):
                    for keys in col.keys():
                        verification = True
                assert verification is False
            # ## delete book test
            outputBookDel = deleting.deleteBook(outputBookId)
            if outputBookDel is True:
                if isinstance(outputBookId,str):
                    condition = {"_id":ObjectId(outputBookId)}
                else:
                    condition = {"_id":outputBookId}
                verification = False
                for col in db.bookCollection.find(condition,{"_id":1}):
                    for keys in col.keys():
                        verification = True
                assert verification is False


class TestDeleting:
    @pytest.mark.parametrize("oneWordValues",[
        ("word1"),
        ("word2"),
        ("word3"),
        ("word4"),
        ("word5")
    ])
    def test_deleteWord(self,db,entering,deleting,wordValues,oneWordValues):
        wordTest,wordTypeTest,articleTest,voiceNameTest,telegramLinkTest,meaningIdTest=wordValues[oneWordValues] 
        # wordId=valtest.insertTestWord(wordTest,wordTypeTest,articleTest,voiceNameTest,telegramLinkTest,meaningIdTest)

        wordId = entering.enterNewWord(wordTest,wordTypeTest,articleTest,voiceNameTest,telegramLinkTest,meaningIdTest)
        ## deleting.deleteWord(wordId)


        output = deleting.deleteWord(wordId)
        if output is True:
            if isinstance(wordId,str):
                condition = {"_id":ObjectId(wordId)}
            else:
                condition = {"_id":wordId}
            verification = False
            for col in db.wordCollection.find(condition,{"word":1}):
                for keys in col.keys():
                    verification = True
            assert verification is False
    @pytest.mark.parametrize("oneMeaningVlue,oneWordValues",[
        ("meaning1","word1"),
        ("meaning2","word2"),
        ("meaning3","word3"),
        ("meaning4","word4"),
        ("meaning5","word5")
    ]) 
    def test_deleteMeaning(self,db,entering,deleting,oneMeaningVlue,meaningValues,oneWordValues,wordValues):
        ##process of make word and meaning
        wordTest,wordTypeTest,articleTest,voiceNameTest,telegramLinkTest,meaningIdTest=wordValues[oneWordValues] 
        # wordId=valtest.insertTestWord(wordTest,wordTypeTest,articleTest,voiceNameTest,telegramLinkTest,meaningIdTest)

        wordId = entering.enterNewWord(wordTest,wordTypeTest,articleTest,voiceNameTest,telegramLinkTest,meaningIdTest)
        ## deleting.deleteWord(wordId)

        deutsch,english,synonym,persian,meaningNumDaf,synName,synTelegramLink,perName,perTelegramLink,deuName,deuTelegramLink,engName,engTelegramLink,_=meaningValues[oneMeaningVlue]

        outputMeaning = entering.enterNewChildMeaning(wordId,deutsch,wordTest, wordTypeTest,articleTest,meaningNumDaf,deuName,deuTelegramLink,english,engName,engTelegramLink,synonym,synName,synTelegramLink,persian,perName,perTelegramLink)
        meaningId=outputMeaning["meaningId"]
        wordIdOutput = outputMeaning["wordId"]
        #####

        if deutsch == None:
            output = deleting.deleteMeaning(meaningId,deutsch)
        else:
            output = deleting.deleteMeaning(meaningId)
        if output is True:
            if isinstance(wordId,str):
                condition = {"_id":ObjectId(meaningId)}
            else:
                condition = {"_id":meaningId}
            verification = False
            for col in db.meaningCollection.find(condition,{"_id":1}):
                for keys in col.keys():
                    verification = True
            assert verification is False

            ### delete test word    
            outputDel = deleting.deleteWord(wordId)
            if outputDel is True:
                if isinstance(wordId,str):
                    condition = {"_id":ObjectId(wordId)}
                else:
                    condition = {"_id":wordId}
                verification = False
                for col in db.wordCollection.find(condition,{"word":1}):
                    for keys in col.keys():
                        verification = True
                assert verification is False


    @pytest.mark.parametrize("oneMeaningVlue,oneWordValues,oneBookValues",[
        ("meaning1","word1","book1"),
        ("meaning2","word2","book2"),
        ("meaning3","word3","book3"),
        ("meaning4","word4","book4"),
        ("meaning5","word5","book5")
    ])
      
    def test_deleteBook(self,db,deleting,entering,meaningValues,oneMeaningVlue,oneWordValues,wordValues,oneBookValues,bookValues):
        wordTest,wordTypeTest,articleTest,voiceNameTest,telegramLinkTest,meaningIdTest=wordValues[oneWordValues] 

        wordId = entering.enterNewWord(wordTest,wordTypeTest,articleTest,voiceNameTest,telegramLinkTest,meaningIdTest)

        deutschTest,englishTest,synonymTest,persianTest,meaningNumDafTest,synNameTest,synTelegramLinkTest,perNameTest,perTelegramLinkTest,deuNameTest,deuTelegramLinkTest,engNameTest,engTelegramLinkTest,_=meaningValues[oneMeaningVlue]

        outputEnterNewChildMeaning = entering.enterNewChildMeaning(wordId,deutschTest,wordTest, wordTypeTest,articleTest,meaningNumDafTest,deuNameTest,deuTelegramLinkTest,englishTest,engNameTest,engTelegramLinkTest,synonymTest,synNameTest,synTelegramLinkTest,persianTest,perNameTest,perTelegramLinkTest)
        bookNameTest,chapterTest,contentTest,pageTest,lessonTest,publisherTest,_,_=bookValues[oneBookValues]
        # outputEnterNewChildMeaning = {"wordId":wordId,"meaningId":meaningId}
        meaningId = outputEnterNewChildMeaning["meaningId"]

        outputId = entering.enterNewBook(meaningId,bookNameTest,chapterTest,contentTest,pageTest,lessonTest,publisherTest,wordTest)
        bookId = outputId
       
        output = deleting.deleteBook(bookId)
        if output is not False:
            verification = False
            if isinstance(bookId,str):
                condition = {"_id":ObjectId(bookId)}
            else:
                condition = {"_id":bookId}
            for col in db.bookCollection.find(condition,{"_id":1}):
                for keys in col.keys():
                    verification=True
            assert verification == False
            ### deleting word and meaning test
            ##delete word test
            outputWordDel = deleting.deleteWord(wordId)
            if outputWordDel is True:
                if isinstance(wordId,str):
                    condition = {"_id":ObjectId(wordId)}
                else:
                    condition = {"_id":wordId}
                verification = False
                for col in db.wordCollection.find(condition,{"word":1}):
                    for keys in col.keys():
                        verification = True
                assert verification is False
            ## delete meaning test
            outputMeaningDel = deleting.deleteMeaning(meaningId)
            if outputMeaningDel is True:
                if isinstance(wordId,str):
                    condition = {"_id":ObjectId(meaningId)}
                else:
                    condition = {"_id":meaningId}
                verification = False
                for col in db.meaningCollection.find(condition,{"deutsch":1}):
                    for keys in col.keys():
                        verification = True
                assert verification is False



class TestEntering:
    @pytest.mark.parametrize("oneWordValues",[
        ("word1"),
        ("word2"),
        ("word3"),
        ("word4"),
        ("word5")
    ])
    def test_enterNewWord(self,entering,deleting,db,oneWordValues,wordValues):
        
        wordTest,wordTypeTest,articleTest,voiceNameTest,telegramLinkTest,meaningIdTest=wordValues[oneWordValues]

        output = entering.enterNewWord(wordTest,wordTypeTest,articleTest,voiceNameTest,telegramLinkTest,meaningIdTest)
        if output is not False:
            condition = {"word":wordTest,"wordType":wordTypeTest,"article":articleTest,"voice":{"name":voiceNameTest,"telegramLink":telegramLinkTest},"meaningId":meaningIdTest}
            outputMongo = {"_id":1}
            wordId = None
            for col in db.wordCollection.find(condition,outputMongo):
                for keys in col.keys():
                    wordId = col[keys]
            assert output == wordId
            
            ### delete word test
            outputDel = deleting.deleteWord(wordId)
            if outputDel is True:
                if isinstance(wordId,str):
                    condition = {"_id":ObjectId(wordId)}
                else:
                    condition = {"_id":wordId}
                verification = False
                for col in db.wordCollection.find(condition,{"word":1}):
                    for keys in col.keys():
                        verification = True
                assert verification is False

    @pytest.mark.parametrize("oneMeaningVlue,oneWordValues",[
        ("meaning1","word1"),
        ("meaning2","word2"),
        ("meaning3","word3"),
        ("meaning4","word4"),
        ("meaning5","word5")
    ])
    def test_enterNewChildMeaning(self,db,deleting,entering,meaningValues,oneMeaningVlue,oneWordValues,wordValues):
        ## make word process 
        wordTest,wordTypeTest,articleTest,voiceNameTest,telegramLinkTest,meaningIdTest=wordValues[oneWordValues] 
        # wordId=valtest.insertTestWord(wordTest,wordTypeTest,articleTest,voiceNameTest,telegramLinkTest,meaningIdTest)
        wordId = entering.enterNewWord(wordTest,wordTypeTest,articleTest,voiceNameTest,telegramLinkTest,meaningIdTest)
        ## deleting.deleteWord(wordId)

        deutsch,english,synonym,persian,meaningNumDaf,synName,synTelegramLink,perName,perTelegramLink,deuName,deuTelegramLink,engName,engTelegramLink,_=meaningValues[oneMeaningVlue]



        # wordId,deutsch,word, wordType=None,article=None,meaningNumDaf=None,deuName=None,deuTelegramLink=None,english=None,engName=None,engTelegramLink=None,synonym=None,synName=None,synTelegramLink=None,persian=None,perName=None,perTelegramLink=None

        ### output = {"wordId":wordId,"meaningId":meaningId}
        # word = word
        output = entering.enterNewChildMeaning(wordId,deutsch,wordTest, wordTypeTest,articleTest,meaningNumDaf,deuName,deuTelegramLink,english,engName,engTelegramLink,synonym,synName,synTelegramLink,persian,perName,perTelegramLink)
        db.wordCollection.update_many({"_id":output["wordId"]},{"$set":{"meaningId":[output["meaningId"]]}})
        print(f"output = {output}")
        if output is not False:
            assert isinstance(output,dict)
            meaningVerification = False
            wordVerification = False
            for col in db.wordCollection.find({"_id":output["wordId"],"meaningId":{"$in":[output["meaningId"]]}},{"_id":1}):
                for keys in col.keys():
                    wordVerification = True
            assert wordVerification is True
            meaningId,deutschMongo,meaningNumDafMongo,deuNameMongo,deuTelegramLinkMongo,englishMongo,engNameMongo,engTelegramLinkMongo,synonymMongo,synNameMongo,synTelegramLinkMongo,persianMongo,perNameMongo,perTelegramLinkMongo,wordIdMongo,wordMongo,wordTypeMongo,articleMongo=None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None
            outputMeaning = {"_id":1,"deutsch":1,"english":1,"synonym":1,"synonym":1,"persian":1,"meaningNumDaf":1,"synVoice":1,"engVoice":1,"perVoice":1,"deuVoice":1,"wordDetails":1}
            for col in db.meaningCollection.find({"_id":output["meaningId"]},outputMeaning):
                for field,val in col.items():
                    meaningVerification=True
                    if field == "_id":
                        meaningId = val 
                    elif field == "deutsch":
                        deutschMongo = val
                    elif field == "english":
                        englishMongo = val
                    elif field == "synonym":
                        synonymMongo = val
                    elif field == "persian":
                        persianMongo = val
                    elif field == "meaningNumDaf":
                        meaningNumDafMongo = val
                    elif field == "synVoice":
                        synNameMongo = val["synName"]
                        synTelegramLinkMongo = val["synTelegramLink"]
                    elif field == "engVoice":
                        engNameMongo = val["engName"]
                        engTelegramLinkMongo = val["engTelegramLink"]
                    elif field == "perVoice":
                        perNameMongo = val["perName"]
                        perTelegramLinkMongo = val["perTelegramLink"]
                    elif field == "deuVoice":
                        deuNameMongo = val["deuName"]
                        deuTelegramLinkMongo = val["deuTelegramLink"]
                    elif field == "wordDetails":
                        wordIdMongo = val["wordId"]
                        wordMongo = val["word"]
                        wordTypeMongo = val["wordType"]
                        articleMongo = val["article"]

            assert meaningVerification is True
            assert wordIdMongo != None 
            assert isinstance(wordIdMongo,ObjectId)
            assert wordId == wordIdMongo

            assert deutschMongo
            assert isinstance(deutschMongo,str)
            assert deutsch == deutschMongo

            assert wordMongo!=None
            assert isinstance(wordMongo,str)
            assert wordTest == wordMongo

            assert meaningId == output["meaningId"]

            if wordTypeTest !=None:
                assert wordTypeTest == wordTypeMongo
            if articleTest !=None:
                assert articleTest == articleMongo               
            if meaningNumDaf !=None:
                assert meaningNumDaf == meaningNumDafMongo
            if deuName !=None:
                assert deuName == deuNameMongo
            if deuTelegramLink !=None:
                assert deuTelegramLink == deuTelegramLinkMongo
            if english !=None:
                assert english == englishMongo
            if engTelegramLink !=None:
                assert engTelegramLink == engTelegramLinkMongo
            if synonym !=None:
                assert synonym == synonymMongo
            if synName !=None:
                assert synName == synNameMongo
            if synTelegramLink !=None:
                assert synTelegramLink == synTelegramLinkMongo  
            if perName !=None:
                assert perName == perNameMongo  
            if persian !=None:
                assert persian ==  persianMongo 
            if perTelegramLink !=None:
                assert perTelegramLink ==  perTelegramLinkMongo 
            ### deleting word and meaning test
            ##delete word test
            outputWordDel = deleting.deleteWord(wordId)
            if outputWordDel is True:
                if isinstance(wordId,str):
                    condition = {"_id":ObjectId(wordId)}
                else:
                    condition = {"_id":wordId}
                verification = False
                for col in db.wordCollection.find(condition,{"word":1}):
                    for keys in col.keys():
                        verification = True
                assert verification is False
            ## delete meaning test
            outputMeaningDel = deleting.deleteMeaning(meaningId)
            if outputMeaningDel is True:
                if isinstance(wordId,str):
                    condition = {"_id":ObjectId(meaningId)}
                else:
                    condition = {"_id":meaningId}
                verification = False
                for col in db.meaningCollection.find(condition,{"deutsch":1}):
                    for keys in col.keys():
                        verification = True
                assert verification is False

    @pytest.mark.parametrize("oneMeaningVlue,oneWordValues,oneBookValues",[
        ("meaning1","word1","book1"),
        ("meaning2","word2","book2"),
        ("meaning3","word3","book3"),
        ("meaning4","word4","book4"),
        ("meaning5","word5","book5")
    ])
    def test_enterNewBook(self,db,deleting,entering,meaningValues,oneMeaningVlue,oneWordValues,wordValues,oneBookValues,bookValues):
        wordTest,wordTypeTest,articleTest,voiceNameTest,telegramLinkTest,meaningIdTest=wordValues[oneWordValues] 

        wordId = entering.enterNewWord(wordTest,wordTypeTest,articleTest,voiceNameTest,telegramLinkTest,meaningIdTest)

        deutschTest,englishTest,synonymTest,persianTest,meaningNumDafTest,synNameTest,synTelegramLinkTest,perNameTest,perTelegramLinkTest,deuNameTest,deuTelegramLinkTest,engNameTest,engTelegramLinkTest,_=meaningValues[oneMeaningVlue]

        outputEnterNewChildMeaning = entering.enterNewChildMeaning(wordId,deutschTest,wordTest, wordTypeTest,articleTest,meaningNumDafTest,deuNameTest,deuTelegramLinkTest,englishTest,engNameTest,engTelegramLinkTest,synonymTest,synNameTest,synTelegramLinkTest,persianTest,perNameTest,perTelegramLinkTest)
        bookNameTest,chapterTest,contentTest,pageTest,lessonTest,publisherTest,_,_=bookValues[oneBookValues]
        # outputEnterNewChildMeaning = {"wordId":wordId,"meaningId":meaningId}
        meaningId = outputEnterNewChildMeaning["meaningId"]

        output = entering.enterNewBook(meaningId,bookNameTest,chapterTest,contentTest,pageTest,lessonTest,publisherTest,wordTest)
        if output is not False:
            bookId = None
            if isinstance(output,str):
                bookId = ObjectId(output)
            else:
                bookId=output
            bookNameMon,chapterMon,contentMon,pageMon,lessonMon,publisherMon,wordMon,meaningIdMon = None,None,None,None,None,None,None,None
            outputMon = {"bookName":1,"chapter":1,"content":1,"page":1,"lesson":1,"publisher":1,"word":1,"meaningId":1}    

            condition = {"_id":bookId}
            for col in db.bookCollection.find(condition,outputMon):
                for field,val in col.items():
                    if field == "bookName":
                        bookNameMon = val
                    elif field == "chapter":
                        chapterMon = val
                    elif field == "content":
                        contentMon = val                        
                    elif field == "page":
                        pageMon = val            
                    elif field == "lesson":
                        lessonMon = val
                    elif field == "publisher":
                        publisherMon = val
                    elif field == "word":
                        wordMon = val
                    elif field == "meaningId":
                        meaningIdMon = val
            # meaningId,bookNameTest,chapterTest,contentTest,lessonTest,publisherTest,wordTest
            # bookNameMon,chapterMon,contentMon,pageMon,lessonMon,publisherMon,wordMon,meaningIdMon
            assert bookNameTest == bookNameMon 
            if chapterTest!=None:
                assert chapterTest == chapterMon
            if contentTest!=None:
                assert contentTest == contentMon
            if lessonTest!=None:
                assert lessonTest == lessonMon
            if publisherTest!=None:
                assert publisherTest == publisherMon
            if wordTest!=None:
                assert wordTest == wordMon

            ### deleting word and meaning test
            ##delete word test
            outputWordDel = deleting.deleteWord(wordId)
            if outputWordDel is True:
                if isinstance(wordId,str):
                    condition = {"_id":ObjectId(wordId)}
                else:
                    condition = {"_id":wordId}
                verification = False
                for col in db.wordCollection.find(condition,{"word":1}):
                    for keys in col.keys():
                        verification = True
                assert verification is False
            ## delete meaning test
            outputMeaningDel = deleting.deleteMeaning(meaningId)
            if outputMeaningDel is True:
                if isinstance(meaningId,str):
                    condition = {"_id":ObjectId(meaningId)}
                else:
                    condition = {"_id":meaningId}
                verification = False
                for col in db.meaningCollection.find(condition,{"deutsch":1}):
                    for keys in col.keys():
                        verification = True
                assert verification is False
            # ## delete book test
            outputBookDel = deleting.deleteBook(bookId)
            if outputBookDel is True:
                if isinstance(bookId,str):
                    condition = {"_id":ObjectId(bookId)}
                else:
                    condition = {"_id":bookId}
                verification = False
                for col in db.bookCollection.find(condition,{"_id":1}):
                    for keys in col.keys():
                        verification = True
                assert verification is False
    @pytest.mark.parametrize("oneMeaningVlue,oneWordValues,oneBookValues",[
        ("meaning1","word1","book1"),
        ("meaning2","word2","book2"),
        ("meaning3","word3","book3"),
        ("meaning4","word4","book4"),
        ("meaning5","word5","book5")
    ])
    def test_enterAll(self,db,entering,deleting,meaningValues,oneMeaningVlue,oneWordValues,wordValues,oneBookValues,bookValues):
        wordTest,wordTypeTest,articleTest,voiceNameTest,telegramLinkTest,meaningIdTest=wordValues[oneWordValues] 

        deutschTest,englishTest,synonymTest,persianTest,meaningNumDafTest,synNameTest,synTelegramLinkTest,perNameTest,perTelegramLinkTest,deuNameTest,deuTelegramLinkTest,engNameTest,engTelegramLinkTest,_=meaningValues[oneMeaningVlue]

        bookNameTest,chapterTest,contentTest,pageTest,lessonTest,publisherTest,_,_=bookValues[oneBookValues]


        # (self,word,deutsch,bookName,wordType=None,article=None,voiceName=None,telegramLink=None,english=None,synonym=None,persian=None,meaningNumDaf=None,synName=None,synTelegramLink=None,perName=None,perTelegramLink=None,deuName=None,deuTelegramLink=None,engName=None,engTelegramLink=None,chapter=None,content=None,page=None,lesson=None,publisher=None):

        output = entering.enterAll(wordTest,deutschTest,bookNameTest,wordTypeTest,articleTest,voiceNameTest,telegramLinkTest,englishTest,synonymTest,persianTest,meaningNumDafTest,synNameTest,synTelegramLinkTest,perNameTest,perTelegramLinkTest,deuNameTest,deuTelegramLinkTest,engNameTest,engTelegramLinkTest,chapterTest,contentTest,pageTest,lessonTest,publisherTest)
        # print(f"output = {output}")
        if output is not False:
            assert (output,list)
            for x in output:
                assert isinstance(x,bson.objectid.ObjectId)

            wordIdMongo,wordMongo,wordTypeMongo,articleMongo,voiceNameMongo,telegramLinkMongo,meaningIdWordMongo=None,None,None,None,None,None,None
            conditionWord= {"_id":output[0]}
            outputWord={"_id":1,"word":1,"wordType":1,"article":1,"voice":1,"meaningId":1}
            verficationWord = False
            for col in db.wordCollection.find(conditionWord,outputWord):
                verficationWord = True
                for field,val in col.items():
                    if field == "word":
                        wordMongo=val
                    elif field == "wordType":
                        wordTypeMongo=val
                    elif field == "article":
                        articleMongo=val
                    elif field == "voice":
                        voiceNameMongo = val["name"]
                        telegramLinkMongo = val["telegramLink"]
                    elif field == "meaningId":
                        meaningIdWordMongo = val
                    elif field == "_id":
                        wordIdMongo = val
            assert verficationWord is True
            assert output[0]== wordIdMongo
            assert output [1]==meaningIdWordMongo
            assert wordMongo == wordTest
            
            if wordTypeTest != None:
               assert wordTypeTest == wordTypeMongo
            if  articleTest != None:
               assert articleTest == articleMongo
            if voiceNameTest != None:
               assert voiceNameTest == voiceNameMongo
            if telegramLinkTest != None:
               assert telegramLinkTest == telegramLinkMongo    

            # meaning test
            meaningIdMongo,deutschMongo,englishMongo,synonymMongo,persianMongo,meaningNumDafMongo,synNameMongo,synTelegramLinkMongo,engNameMongo,engTelegramLinkMongo,perNameMongo,perTelegramLinkMongo,deuNameMongo,deuTelegramLinkMongo,wordIdMeaningMongo,wordMeaningMongo,wordTypeMeaningMongo,articleMeaningMongo=None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None
            conditionMeaning= {"_id":output[1]}
            outputMeaning={"_id":1,"deutsch":1,"english":1,"synonym":1,"persian":1,"meaningNumDaf":1,"synVoice":1,"engVoice":1,"perVoice":1,"deuVoice":1,"wordDetails":1}
            verficationMeaning = False
            for col in db.meaningCollection.find(conditionMeaning,outputMeaning):
                verficationMeaning = True
                for field,val in col.items():
                    if field == "_id":
                       meaningIdMongo=val 
                    if field == "deutsch":
                        deutschMongo=val
                    elif field == "english":
                        englishMongo=val
                    elif field == "synonym":
                        synonymMongo=val
                    elif field == "persian":
                         persianMongo=val   
                    elif field == "meaningNumDaf":
                        meaningNumDafMongo=val
                    elif field == "synVoice":
                        synNameMongo = val["synName"]
                        synTelegramLinkMongo = val["synTelegramLink"]
                    elif field == "engVoice":
                        engNameMongo = val["engName"]
                        engTelegramLinkMongo = val["engTelegramLink"]
                    elif field == "perVoice":
                        perNameMongo = val["perName"]
                        perTelegramLinkMongo = val["perTelegramLink"]
                    elif field == "deuVoice":
                        deuNameMongo = val["deuName"]
                        deuTelegramLinkMongo = val["deuTelegramLink"]
                    elif field == "wordDetails":
                        wordIdMeaningMongo = val["wordId"]
                        wordMeaningMongo = val["word"]
                        wordTypeMeaningMongo = val["wordType"]
                        articleMeaningMongo = val["article"]




            assert verficationMeaning is True
            assert output[0]== wordIdMeaningMongo
            assert output [1]==meaningIdMongo
            assert deutschMongo == deutschTest
            assert wordMeaningMongo == wordMongo

            # deutschTest,englishTest,synonymTest,persianTest,meaningNumDafTest,synNameTest,synTelegramLinkTest,perNameTest,perTelegramLinkTest,deuNameTest,deuTelegramLinkTest,engNameTest,engTelegramLinkTest

            # meaningIdMongo,deutschMongo,englishMongo,synonymMongo,persianMongo,meaningNumDafMongo,synNameMongo,synTelegramLinkMongo,engNameMongo,engTelegramLinkMongo,perNameMongo,perTelegramLinkMongo,deuNameMongo,deuTelegramLinkMongo,wordIdMeaningMongo,wordMeaningMongo,wordTypeMeaningMongo,articleMeaningMongo=None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None

            if englishTest != None:
               assert englishTest == englishMongo
            if  synonymTest != None:
               assert synonymTest == synonymMongo
            if persianTest != None:
               assert persianTest == persianMongo
            if meaningNumDafTest != None:
               assert meaningNumDafTest == meaningNumDafMongo    

            if synNameTest != None:
               assert synNameTest == synNameMongo
            if  synTelegramLinkTest != None:
               assert synTelegramLinkTest == synTelegramLinkMongo
            if perNameTest != None:
               assert perNameTest == perNameMongo
            if perTelegramLinkTest != None:
               assert perTelegramLinkTest == perTelegramLinkMongo    
            if deuNameTest != None:
               assert deuNameTest == deuNameMongo
            if  deuTelegramLinkTest != None:
               assert deuTelegramLinkTest == deuTelegramLinkMongo
            if engNameTest != None:
               assert engNameTest == engNameMongo
            if engTelegramLinkTest != None:
               assert engTelegramLinkTest == engTelegramLinkMongo    
            if wordTypeTest != None:
                assert wordTypeTest == wordTypeMeaningMongo
            if articleTest != None:
                assert articleTest == articleMeaningMongo

            ## book test
            bookIdMongo,bookNameMongo,chapterMongo,contentMongo,pageMongo,lessonMongo,publisherMongo,wordBookMongo,meaningIdBookMongo=None,None,None,None,None,None,None,None,None
            conditionBook= {"_id":output[2]}
            outputBook={"_id":1,"bookName":1,"chapter":1,"content":1,"page":1,"lesson":1,"publisher":1,"word":1,"meaningId":1}
            verificationBook = False
            for col in db.bookCollection.find(conditionBook,outputBook):
                verificationBook = True
                for field,val in col.items():
                    
                    if field == "bookName":
                        bookNameMongo=val
                    elif field == "chapter":
                        chapterMongo =val
                    elif field == "content":
                        contentMongo =val
                    elif field == "page":
                         pageMongo = val
                    elif field == "lesson":
                         lessonMongo = val
                    elif field == "publisher":
                         publisherMongo = val
                    elif field == "word":
                         wordBookMongo = val
                    elif field == "meaningId":
                         meaningIdBookMongo = val
                    elif field == "_id":
                        bookIdMongo = val

            assert verificationBook is True
            assert output[2]== bookIdMongo
            assert output [1]==meaningIdBookMongo
            assert bookNameTest == bookNameMongo
            assert wordTest ==  wordBookMongo

            if bookNameTest != None:
               assert bookNameTest == bookNameMongo
            if  chapterTest != None:
               assert chapterTest == chapterMongo
            if contentTest != None:
               assert contentTest == contentMongo
            if pageTest != None:
               assert pageTest == pageMongo   
            if lessonTest != None:
               assert lessonTest == lessonMongo
            if publisherTest != None:
               assert publisherTest == publisherMongo   

            ### deleting word and meaning test
            ##delete word test
            outputWordDel = deleting.deleteWord(output[0])
            if outputWordDel is True:
                if isinstance(output[0],str):
                    condition = {"_id":ObjectId(output[0])}
                else:
                    condition = {"_id":output[0]}
                verification = False
                for col in db.wordCollection.find(condition,{"word":1}):
                    for keys in col.keys():
                        verification = True
                assert verification is False
            ## delete meaning test
            outputMeaningDel = deleting.deleteMeaning(output[1])
            if outputMeaningDel is True:
                if isinstance(output[1],str):
                    condition = {"_id":ObjectId(output[1])}
                else:
                    condition = {"_id":output[1]}
                verification = False
                for col in db.meaningCollection.find(condition,{"deutsch":1}):
                    for keys in col.keys():
                        verification = True
                assert verification is False
            # ## delete book test
            outputBookDel = deleting.deleteBook(output[2])
            if outputBookDel is True:
                if isinstance(output[2],str):
                    condition = {"_id":ObjectId(output[2])}
                else:
                    condition = {"_id":output[2]}
                verification = False
                for col in db.bookCollection.find(condition,{"_id":1}):
                    for keys in col.keys():
                        verification = True
                assert verification is False
    @pytest.mark.parametrize("word",[
        ("sich freuen [vr]"),
        ("die Entschuldigung;-,en"),
        ("der Herr;-(e)n, -en"),
        ("ggg")
    ])
    def test_checkRepeatedWord(self,db,entering,word):
        output = entering.checkRepeatedWord(word)
        assert isinstance(output,bool)
        if output is False:
            lenghtRepeatedWord = []
            for col in db.wordCollection.find({"word":word},{"_id":0,"word":1}):
                for keys in col.keys():
                    lenghtRepeatedWord.append(col[keys])  
            assert  len(lenghtRepeatedWord)==0


    @pytest.mark.parametrize("oneMeaningVlue",[
        ("meaning1"),
        ("meaning2"),
        ("meaning3"),
        ("meaning4"),
        ("meaning5")
    ])
    def test_enterNewMeaning(self,db,entering,deleting,meaningValues,oneMeaningVlue):
        pass
        # (self,deutsch,word,wordId=None, wordType=None,article=None,meaningNumDaf=None,deuName=None,deuTelegramLink=None,english=None,engName=None,engTelegramLink=None,synonym=None,synName=None,synTelegramLink=None,persian=None,perName=None,perTelegramLink=None)
        deutschTest,englishTest,synonymTest,persianTest,meaningNumDafTest,synNameTest,synTelegramLinkTest,perNameTest,perTelegramLinkTest,deuNameTest,deuTelegramLinkTest,engNameTest,engTelegramLinkTest,wordDetails=meaningValues[oneMeaningVlue]
        wordTest = wordDetails["word"]
        wordTypeTest= wordDetails["wordType"]
        articleTest= wordDetails["article"]
        outputMeaningId = entering.enterNewMeaning(deutschTest,wordTest,wordType=wordTypeTest,article=articleTest,meaningNumDaf=meaningNumDafTest,deuName=deuNameTest,deuTelegramLink=deuTelegramLinkTest,english=englishTest,engName=engNameTest,engTelegramLink=engTelegramLinkTest,synonym=synonymTest,synName=synNameTest,synTelegramLink=synTelegramLinkTest,persian=persianTest,perName=perNameTest,perTelegramLink=perTelegramLinkTest)

        if outputMeaningId is not False:
            condition = {"_id":outputMeaningId}
            outputMongo = {"_id":1,"deutsch":1,"english":1,"synonym":1,"synonym":1,"persian":1,"meaningNumDaf":1,"synVoice":1,"engVoice":1,"perVoice":1,"deuVoice":1,"wordDetails":1}

            meaningIdMongo,wordIdMongo,deutschMongo,meaningNumDafMongo,deuNameMongo,deuTelegramLinkMongo,englishMongo,engNameMongo,engTelegramLinkMongo,synonymMongo,synNameMongo,synTelegramLinkMongo,persianMongo,perNameMongo,perTelegramLinkMongo,wordIdMongo,wordMongo,wordTypeMongo,articleMongo=None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None
            # outputMeaning = {"_id":1,"deutsch":1,"english":1,"synonym":1,"synonym":1,"persian":1,"meaningNumDaf":1,"synVoice":1,"engVoice":1,"perVoice":1,"deuVoice":1,"wordDetails":1}
            for col in db.meaningCollection.find(condition,outputMongo):
                for field,val in col.items():
                    meaningVerification=True
                    if field == "_id":
                        meaningIdMongo = val 
                    elif field == "deutsch":
                        deutschMongo = val
                    elif field == "english":
                        englishMongo = val
                    elif field == "synonym":
                        synonymMongo = val
                    elif field == "persian":
                        persianMongo = val
                    elif field == "meaningNumDaf":
                        meaningNumDafMongo = val
                    elif field == "synVoice":
                        synNameMongo = val["synName"]
                        synTelegramLinkMongo = val["synTelegramLink"]
                    elif field == "engVoice":
                        engNameMongo = val["engName"]
                        engTelegramLinkMongo = val["engTelegramLink"]
                    elif field == "perVoice":
                        perNameMongo = val["perName"]
                        perTelegramLinkMongo = val["perTelegramLink"]
                    elif field == "deuVoice":
                        deuNameMongo = val["deuName"]
                        deuTelegramLinkMongo = val["deuTelegramLink"]
                    elif field == "wordDetails":
                        wordIdMongo = val["wordId"]
                        wordMongo = val["word"]
                        wordTypeMongo = val["wordType"]
                        articleMongo = val["article"]

            assert meaningVerification is True
            assert outputMeaningId != None 
            assert isinstance(outputMeaningId,ObjectId)
            assert outputMeaningId == meaningIdMongo
            assert deutschMongo != None
            assert wordMongo!=None
            assert wordIdMongo == None
            assert deutschTest == deutschMongo
            assert isinstance(wordMongo,str)
            assert wordTest == wordMongo
            if wordTypeTest !=None:
                assert wordTypeTest == wordTypeMongo
            if articleTest !=None:
                assert articleTest == articleMongo               
            if meaningNumDafTest !=None:
                assert meaningNumDafTest == meaningNumDafMongo
            if deuNameTest !=None:
                assert deuNameTest == deuNameMongo
            if deuTelegramLinkTest !=None:
                assert deuTelegramLinkTest == deuTelegramLinkMongo
            if englishTest !=None:
                assert englishTest == englishMongo
            if engTelegramLinkTest !=None:
                assert engTelegramLinkTest == engTelegramLinkMongo
            if synonymTest !=None:
                assert synonymTest == synonymMongo
            if synNameTest !=None:
                assert synNameTest == synNameMongo
            if synTelegramLinkTest !=None:
                assert synTelegramLinkTest == synTelegramLinkMongo  
            if perNameTest !=None:
                assert perNameTest == perNameMongo  
            if persianTest !=None:
                assert persianTest ==  persianMongo 
            if perTelegramLinkTest !=None:
                assert perTelegramLinkTest ==  perTelegramLinkMongo

            ## delete meaning test
            outputMeaningDel = deleting.deleteMeaning(outputMeaningId)
            if outputMeaningDel is True:
                if isinstance(outputMeaningId,str):
                    condition = {"_id":ObjectId(outputMeaningId)}
                else:
                    condition = {"_id":outputMeaningId}
                verification = False
                for col in db.meaningCollection.find(condition,{"deutsch":1}):
                    for keys in col.keys():
                        verification = True
                assert verification is False

