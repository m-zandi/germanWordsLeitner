from tkinter import *
from tkinter import ttk
import tkinter
# from test_entering import Db
import pymongo
from bson.objectid import ObjectId
import bson
import test_entering as TE
import pytest
class Db:
    def __init__(self):
        self.connection = pymongo.MongoClient("localhost",27017)
        self.database= self.connection["woerterbuch"]
        self.test = self.database["test"]
class Feedback:
    def __init__(self,master):
        self.obj_db = Db()
        notebook = ttk.Notebook(master)
        notebook.pack()

        self.frame1=ttk.Frame(notebook)
        self.frame2=ttk.Frame(notebook)
        self.frame3=ttk.Frame(notebook)
        self.frame4=ttk.Frame(notebook)
        self.frame5 =ttk.Frame(notebook)
        # self.notebook =notebook
        self.master = master
        
        # self.editNdel()

        notebook.add(self.frame1,text="Entering")
        notebook.add(self.frame2,text="Search")
        notebook.add(self.frame3,text="Advance Search")
        notebook.add(self.frame4,text="Report")

        self.nb = notebook

        self.entering()
        
        self.advanceSearch()
        self.report()
        # self.w=None
        ## component 
        self.treeViewSearchSimple = ttk.Treeview(self.frame2)
        ##
        self.outputSimpleSearch =None
        self.iidList = None
        self.editNdelWindow,self.wordEntry,self.wordTypeEntry,self.articleEntry,self.voiceNameEntry,self.telegramAddressEntry=None,None,None,None,None,None
        self.msgWarnEditedWord=None
        ##
        self.deleteWindow=None
        ## new meaning
        self.wordIn,self.newMeaningChild ,self.deuMeaning,self.meaningNumDaf,self.deuFileName,self.deuTelAdd,self.engMeaning,self.engFileName,self.engTelAdd,self.synMeaning,self.synFileName,self.synTelAdd,self.perMeaning,self.perFileName,self.perTelAdd = None ,None,None,None,None,None,None,None,None,None,None,None,None,None,None
        ## delete word variable
        self.wordVal = None
        ## edit meaning
        self.wordIn,self.editMeaningTL ,self.deuMeaningEdit,self.meaningNumDafEdit,self.deuFileNameEdit,self.deuTelAddEdit,self.engMeaningEdit,self.engFileNameEdit,self.engTelAddEdit,self.synMeaningEdit,self.synFileNameEdit,self.synTelAddEdit,self.perMeaningEdit,self.perFileNameEdit,self.perTelAddEdit,self.warnSureEdition = None ,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None
        ### delete meaning
        self.warnSureDelete=None
        ### new book
        self.newBookTL,self.bookNameEntry,self.chapterEntry,self.contentEntry,self.pageEntry,self.lessonEntry,self.publisherEntry,self.wordEntry=None,None,None,None,None,None,None,None
        ### edit book
        self.warnSureEditionBook,self.editBookTL,self.bookNameEntryEdit,self.chapterEntryEdit,self.contentEntryEdit,self.pageEntryEdit,self.lessonEntryEdit,self.publisherEntryEdit=None,None,None,None,None,None,None,None
        ### entering
        self.enterWarnTL,self.wordEntering,self.wordTypeEntering,self.articleEntering,self.bookNameEntering,self.chapterEntering,self.contentEntering,self.publisherEntering,self.lessonEntering,self.voiceNameEntering,self.telegramAddressEntering,self.meaningDeutschEntering,self.fileNameDeutschEntering,self.telegramAddressDeutschEntering,self.meaningEnglishEntering,self.fileNameEnglishEntering,self.telegramAddressEnglishEntering,self.meaningSynonymEntering,self.fileNameSynonymEntering,self.telegramAddressSynonymEntering,self.meaningPersianEntering,self.fileNamePersianEntering,self.telegramAddressPersianEntering,self.meaningNumDafEntering,self.pageEntering=None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None
        self.entering()
        
         ##### search
        self.search()
        self.listboxSimple,self.scrolList,self.outputAllWords=None,None,None
         
        ##### 
        

    def entering(self):
        # global word_text,wordType_text,article_text,bookName_text,chapter_text,content_text,publisher_text,lesson_text,voiceName_text,telegramAddress_text,meaningDeutsch_text,fileNameDeutsch_text,telegramAddressDeutsch_text,meaningEnglish_text,fileNameEnglish_text,telegramAddressEnglish_text,meaningSynonym_text,fileNameSynonym_text,telegramAddressSynonym_text,meaningPersian_text,fileNamePersian_text,telegramAddressPersian_text

        # frame1 = self.frame1
        # style = ttk.Style("BW.TLabel",font=("Arial",15,"bold"))
        ttk.Label(self.frame1,text = "Word",width=30).grid(row=0,column=1,sticky="nw", padx = 10)

        self.wordEntering = ttk.Entry(self.frame1,width=30)
        # self.wordEntering.insert(0,"hi")

        self.wordEntering.grid(row=1,column=1, padx = 10)
        wordType_label = ttk.Label(self.frame1,text = "Word Type").grid(row=2,column=1,sticky="nw")
        self.wordTypeEntering = ttk.Entry(self.frame1,width=30)
        self.wordTypeEntering.grid(row=3,column=1)
        article_label = ttk.Label(self.frame1,text = "article").grid(row=4,column=1,sticky="nw", padx = 10)
        self.articleEntering = ttk.Entry(self.frame1,width=30)
        self.articleEntering.grid(row=5,column=1, padx = 10,sticky="nw")
        bookName_label = ttk.Label(self.frame1,text = "book name").grid(row=6,column=1,sticky="nw", padx = 10)
        self.bookNameEntering = ttk.Entry(self.frame1,width=30)
        self.bookNameEntering.grid(row=7,column=1, padx = 10)
        chapter_label = ttk.Label(self.frame1,text = "chapter").grid(row=8,column=1,sticky="nw", padx = 10)
        self.chapterEntering = ttk.Entry(self.frame1,width=30)
        self.chapterEntering.grid(row=9,column=1, padx = 10)
        content_label = ttk.Label(self.frame1,text = "content").grid(row=10,column=1,sticky="sw", padx = 10)
        self.contentEntering = ttk.Entry(self.frame1,width=30)
        self.contentEntering.grid(row=11,column=1, padx = 10)
        publisher_label = ttk.Label(self.frame1,text = "publisher").grid(row=12,column=1,sticky="nw", padx = 10)
        self.publisherEntering = ttk.Entry(self.frame1,width=30)
        self.publisherEntering.grid(row=13,column=1, padx = 10)
        lesson_label = ttk.Label(self.frame1,text = "lesson").grid(row=14,column=1,sticky="nw", padx = 10)
        self.lessonEntering = ttk.Entry(self.frame1,width=30)
        self.lessonEntering.grid(row=15,column=1, padx = 10)

        page_label = ttk.Label(self.frame1,text = "page").grid(row=16,column=1,sticky="nw", padx = 10)
        self.pageEntering = ttk.Entry(self.frame1,width=30)
        self.pageEntering.grid(row=17,column=1, padx = 10)


        voiceName_label = ttk.Label(self.frame1,text = "word voice name").grid(row=0,column=4,sticky="nw")
        self.voiceNameEntering = ttk.Entry(self.frame1,width=30)
        self.voiceNameEntering.grid(row=1,column=3, sticky="nw", padx = 10)

        telegramAddress_label = ttk.Label(self.frame1,text = "word telegram address").grid(row=0,column=3,sticky="nw")
        self.telegramAddressEntering = ttk.Entry(self.frame1,width=30)
        self.telegramAddressEntering.grid(row=1,column=4,sticky="nw")
        #deutsch
        deutsch_label = ttk.Label(self.frame1,text = "deutsch",font=("Arial",15,"bold")).grid(row=4,column=4)

        meaningDeutsch_label = ttk.Label(self.frame1,text = "meaning : ").grid(row=5,column=3,sticky="ne")
        self.meaningDeutschEntering =Text(self.frame1,width=30,height=5)
        self.meaningDeutschEntering.grid(row=5,column=4)
        ## test
        # ttk.Label(self.frame1,text = "*",font=("Arial",25,"bold"),foreground="red").grid(row=5,column=4, padx = 10,sticky="w")
        #
        meaningDeutsch_label = ttk.Label(self.frame1,text = "meaning num DAF : ").grid(row=6,column=3,sticky="ne")
        self.meaningNumDafEntering=ttk.Entry(self.frame1,width=30)
        self.meaningNumDafEntering.grid(row=6,column=4,sticky="nw")
        fileNameDeutsch_label = ttk.Label(self.frame1,text = "file Name : ").grid(row=7,column=3,sticky="ne")
        self.fileNameDeutschEntering =ttk.Entry(self.frame1,width=30)
        self.fileNameDeutschEntering.grid(row=7,column=4,sticky="nw")
        telegramAddressDeutsch_label = ttk.Label(self.frame1,text = "telegram address : ").grid(row=8,column=3,sticky="ne")
        self.telegramAddressDeutschEntering =ttk.Entry(self.frame1,width=30)
        self.telegramAddressDeutschEntering.grid(row=8,column=4,sticky="nw")



        #english
        english_label = ttk.Label(self.frame1,text = "english",font=("Arial",15,"bold")).grid(row=10,column=4)

        meaningEnglish_label = ttk.Label(self.frame1,text = "meaning : ").grid(row=11,column=3,sticky="ne")
        self.meaningEnglishEntering =Text(self.frame1,width=30,height=5)
        self.meaningEnglishEntering.grid(row=11,column=4)
        fileNameEnglish_label = ttk.Label(self.frame1,text = "file Name : ").grid(row=12,column=3,sticky="ne")
        self.fileNameEnglishEntering =ttk.Entry(self.frame1,width=30)
        self.fileNameEnglishEntering.grid(row=12,column=4,sticky="nw")
        telegramAddressEnglish_label = ttk.Label(self.frame1,text = "telegram address : ").grid(row=13,column=3,sticky="ne")
        self.telegramAddressEnglishEntering =ttk.Entry(self.frame1,width=30)
        self.telegramAddressEnglishEntering.grid(row=13,column=4,sticky="nw")

 





        #synonym
        synonym_label = ttk.Label(self.frame1,text = "synonym",font=("Arial",15,"bold")).grid(row=4,column=6,columnspan=3)

        meaningSynonym_label = ttk.Label(self.frame1,text = "meaning : ").grid(row=5,column=6,sticky="ne")
        self.meaningSynonymEntering =Text(self.frame1,width=30,height=5)
        self.meaningSynonymEntering.grid(row=5,column=7)
        fileNameSynonym_label = ttk.Label(self.frame1,text = "file Name : ").grid(row=6,column=6,sticky="ne")
        self.fileNameSynonymEntering =ttk.Entry(self.frame1,width=30)
        self.fileNameSynonymEntering.grid(row=6,column=7,sticky="nw")
        telegramAddressSynonym_label = ttk.Label(self.frame1,text = "telegram address : ").grid(row=7,column=6,sticky="ne")
        self.telegramAddressSynonymEntering =ttk.Entry(self.frame1,width=30)
        self.telegramAddressSynonymEntering.grid(row=7,column=7,sticky="nw")




        #persian
        persian_label = ttk.Label(self.frame1,text = "persian",font=("Arial",15,"bold")).grid(row=9,column=6,columnspan=3)

        meaningPersian_label = ttk.Label(self.frame1,text = "meaning : ").grid(row=10,column=6,sticky="ne")
        self.meaningPersianEntering =Text(self.frame1,width=30,height=5)
        self.meaningPersianEntering.grid(row=10,column=7)
        fileNamePersian_label = ttk.Label(self.frame1,text = "file Name : ").grid(row=11,column=6,sticky="ne")
        self.fileNamePersianEntering =ttk.Entry(self.frame1,width=30)
        self.fileNamePersianEntering.grid(row=11,column=7,sticky="nw")
        telegramAddressPersian_label = ttk.Label(self.frame1,text = "telegram address : ").grid(row=12,column=6,sticky="ne")
        self.telegramAddressPersianEntering =ttk.Entry(self.frame1,width=30)
        self.telegramAddressPersianEntering.grid(row=12,column=7,sticky="nw")

        #button enter
        btn_nter = ttk.Button(self.frame1,command=self.enter_newWordMeaningBook,text="Enter",width=20).grid(row=14,column=6,columnspan=2,rowspan=3,ipady=20)
        # space
        ttk.Label(self.frame1,text = "").grid(row=10,column=5,sticky="ne",padx=30)
        ttk.Label(self.frame1,text = "").grid(row=10,column=8,sticky="ne",padx=20)
        ttk.Label(self.frame1,text = "").grid(row=1,column=2, padx = 20,sticky="w")
        ttk.Label(self.frame1,text = "").grid(row=13,column=0,padx=10)
    def enter_newWordMeaningBook(self):
        # frame1=self.frame
        # wordId=TE.Entering().enterNewWord(word,wordType=None,article=None,voiceName=None,telegramLink=None,meaningId=None)
        # meaningId = TE.Entering().enterNewChildMeaning(wordId,deutsch,word, wordType=None,article=None,meaningNumDaf=None,deuName=None,deuTelegramLink=None,english=None,engName=None,engTelegramLink=None,synonym=None,synName=None,synTelegramLink=None,persian=None,perName=None,perTelegramLink=None)
        # bookId=Entering().enterNewBook(meaningId,bookName,chapter=None,content=None,page=None,lesson=None,publisher=None,word=None)

        # self.word_text,self.wordType_text,self.article_text,self.bookName_text,self.chapter_text,self.content_text,self.publisher_text,self.lesson_text,self.voiceName_text,self.telegramAddress_text,self.meaningDeutsch_text,self.fileNameDeutsch_text,self.telegramAddressDeutsch_text,self.meaningEnglish_text,self.fileNameEnglish_text,self.telegramAddressEnglish_text,self.meaningSynonym_text,self.fileNameSynonym_text,self.telegramAddressSynonym_text,self.meaningPersian_text,self.fileNamePersian_text,self.telegramAddressPersian_text=None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None,None
        

        if self.wordEntering.get()=="":
            ttk.Label(self.frame1,text = "*",font=("Arial",25,"bold"),foreground="red").grid(row=1,column=2)
        else:
            ttk.Label(self.frame1,text = "  ",font=("Arial",25,"bold"),foreground="red").grid(row=1,column=2, padx = 10)
        if len(self.meaningDeutschEntering.get("1.0","end"))<2:
            ttk.Label(self.frame1,text = "*",font=("Arial",25,"bold"),foreground="red").grid(row=5,column=5,sticky="w")
        else:
            ttk.Label(self.frame1,text = "  ",font=("Arial",25,"bold"),foreground="red").grid(row=5,column=5, padx = 10,sticky="w")
        if self.bookNameEntering.get()=="":
            ttk.Label(self.frame1,text = "*",font=("Arial",25,"bold"),foreground="red").grid(row=7,column=2,sticky="w")
        else:
            ttk.Label(self.frame1,text = "  ",font=("Arial",25,"bold"),foreground="red").grid(row=7,column=2, padx = 10,sticky="w")
        if self.wordEntering.get()!="" and len(self.meaningDeutschEntering.get("1.0","end"))>1 and self.bookNameEntering.get()!="":
            word = self.wordEntering.get()
            outputRepeatedWord = TE.Entering().checkRepeatedWord(word)
            if outputRepeatedWord is False:

                deutschMeaning = self.meaningDeutschEntering.get("1.0","end")

                self.enterWarnTL = Toplevel(self.master)
                
                labelWin = ttk.Label(self.enterWarnTL,text = "Enter Word, Meaning, Book",font=('Arial',15,"bold")).grid(row=1,column=2,columnspan=4,sticky="nsew")
                labelWin = ttk.Label(self.enterWarnTL,text = "❗❓",font=('Arial',80,"bold")).grid(row=2,column=3,rowspan=3,columnspan=2,sticky="nw")
                
                wordLabel = ttk.Label(self.enterWarnTL,text = f"Word :{self.wordEntering.get()}",font = ("Arial",10,"bold")).grid(row=1,column=1,sticky="nw",padx = 20)

                # print(f"output else ={output}")
                wordTypeLabel = ttk.Label(self.enterWarnTL,text = f"deutsch meaning : {deutschMeaning}",wraplength=200 ).grid(row=2,column=1,sticky="nw",padx = 20)
                

                ttk.Label(self.enterWarnTL,text = f"Book Name : {self.bookNameEntering.get()}" ,font = ("Arial",10,"bold")).grid(row=3,column=1,sticky="nw",padx = 20)


                msg = ttk.Label(self.enterWarnTL,text = "Are you sure to Enter this word, Meaning and book to database !?",font=('Arial',10,"bold"),wraplength=600).grid(row=6,column=1,columnspan=4,padx=20)
                # ,sticky="nw"
                btn_yesEnter = ttk.Button(self.enterWarnTL,command = self.doneMsgNewWordMeaningBook,text="Yes")
                btn_yesEnter.grid(row = 7,column=3,sticky="nw")

                btn_noEnter = ttk.Button(self.enterWarnTL,command = self.enterWarnTL.destroy,text="No")
                btn_noEnter.grid(row = 7,column=4,sticky="nw")
                ttk.Label(self.enterWarnTL,text = "").grid(row=7,column=0,columnspan=3,padx=40)
                ttk.Label(self.enterWarnTL,text = "").grid(row=7,column=5,pady=10,padx=10)
            else:
                self.search()
                self.wordSearch.insert(0,word)
                self.search_btn()
                # self.wordEntering.delete("0","end")
                # self.meaningDeutschEntering.delete(1.0,"end")
                # self.bookNameEntering.delete("0","end")
                # self.wordTypeEntering.delete("0","end")
                # self.articleEntering.delete("0","end")
                # self.voiceNameEntering.delete("0","end")
                # self.telegramAddressEntering.delete("0","end")
                # self.meaningEnglishEntering.delete(1.0,"end")
                # self.meaningSynonymEntering.delete(1.0,"end")
                # self.meaningPersianEntering.delete(1.0,"end")
                # self.meaningNumDafEntering.delete("0","end")
                # self.fileNameSynonymEntering.delete("0","end")
                # self.telegramAddressSynonymEntering.delete("0","end")
                # self.fileNamePersianEntering.delete("0","end")
                # self.telegramAddressPersianEntering.delete("0","end")
                # self.fileNameDeutschEntering.delete("0","end")
                # self.telegramAddressDeutschEntering.delete("0","end")
                # self.fileNameEnglishEntering.delete("0","end")
                # self.telegramAddressEnglishEntering.delete("0","end")
                # self.chapterEntering.delete("0","end")
                # self.contentEntering.delete("0","end")
                # self.pageEntering.delete("0","end")
                # self.lessonEntering.delete("0","end")
                # self.publisherEntering.delete("0","end")
                # select search tab
                self.nb.select(self.frame2)
                ## msg repeat
                msg=Toplevel(self.master)
                ttk.Label(msg,text = f"Word :{word}").grid(row=0,column=1,sticky="nw",padx = 20,rowspan=3,pady = 20)


                ttk.Label(msg,text = "Repeated Word!!!",font=('Arial',30,"bold")).grid(row=0,column=2,sticky="nswe",columnspan=2)
                labelWin = ttk.Label(msg,text = "!?",font=('Arial',60,"bold")).grid(row=1,column=2,rowspan=3,sticky="nw")

                msgDeleted = ttk.Label(msg,text = f"The word ( {word} ) was entered to DB Before !",font=('Arial',15,"bold")).grid(row=5,column=1,sticky="nswe",columnspan=2)

                btn_OkEntered = ttk.Button(msg,command = msg.destroy,text="Ok")
                btn_OkEntered.grid(row = 7,column=1,columnspan=2)



    def doneMsgNewWordMeaningBook(self):
        self.wordEntering,self.wordTypeEntering,self.articleEntering,self.bookNameEntering,self.chapterEntering,self.contentEntering,self.publisherEntering,self.lessonEntering,self.voiceNameEntering,self.telegramAddressEntering,self.meaningDeutschEntering,self.fileNameDeutschEntering,self.telegramAddressDeutschEntering,self.meaningEnglishEntering,self.fileNameEnglishEntering,self.telegramAddressEnglishEntering,self.meaningSynonymEntering,self.fileNameSynonymEntering,self.telegramAddressSynonymEntering,self.meaningPersianEntering,self.fileNamePersianEntering,self.telegramAddressPersianEntering
        word=self.wordEntering.get()
        deutsch=self.meaningDeutschEntering.get("1.0","end")
        bookName=self.bookNameEntering.get()
        wordType=self.wordTypeEntering.get()
        article=self.articleEntering.get()
        voiceName=self.voiceNameEntering.get()
        telegramLink=self.telegramAddressEntering.get()
        # meaningId=self.
        english=self.meaningEnglishEntering.get("1.0","end")
        synonym=self.meaningSynonymEntering.get("1.0","end")
        persian=self.meaningPersianEntering.get("1.0","end")
        meaningNumDaf=self.meaningNumDafEntering.get()
        synName=self.fileNameSynonymEntering.get()
        synTelegramLink=self.telegramAddressSynonymEntering.get()
        perName=self.fileNamePersianEntering.get()
        perTelegramLink=self.telegramAddressPersianEntering.get()
        deuName=self.fileNameDeutschEntering.get()
        deuTelegramLink=self.telegramAddressDeutschEntering.get()
        engName=self.fileNameEnglishEntering.get()
        engTelegramLink=self.telegramAddressEnglishEntering.get()
        chapter=self.chapterEntering.get()
        content=self.contentEntering.get()
        page=self.pageEntering.get()
        lesson=self.lessonEntering.get()
        publisher=self.publisherEntering.get()
        output = TE.Entering().enterAll(word,deutsch,bookName,wordType=wordType,article=article,voiceName=voiceName,telegramLink=telegramLink,english=english,synonym=synonym,persian=persian,meaningNumDaf=meaningNumDaf,synName=synName,synTelegramLink=synTelegramLink,perName=perName,perTelegramLink=None,deuName=None,deuTelegramLink=None,engName=None,engTelegramLink=None,chapter=chapter,content=content,page=page,publisher=publisher)
        self.search()
        self.wordSearch=None
        # wordSearch.insert(0,word)
        self.search_btn()

        ###
        self.wordEntering.delete("0","end")
        self.meaningDeutschEntering.delete(1.0,"end")
        self.bookNameEntering.delete("0","end")
        self.wordTypeEntering.delete("0","end")
        self.articleEntering.delete("0","end")
        self.voiceNameEntering.delete("0","end")
        self.telegramAddressEntering.delete("0","end")
        # meaningId=self.
        self.meaningEnglishEntering.delete(1.0,"end")
        self.meaningSynonymEntering.delete(1.0,"end")
        self.meaningPersianEntering.delete(1.0,"end")
        self.meaningNumDafEntering.delete("0","end")
        self.fileNameSynonymEntering.delete("0","end")
        self.telegramAddressSynonymEntering.delete("0","end")
        self.fileNamePersianEntering.delete("0","end")
        self.telegramAddressPersianEntering.delete("0","end")
        self.fileNameDeutschEntering.delete("0","end")
        self.telegramAddressDeutschEntering.delete("0","end")
        self.fileNameEnglishEntering.delete("0","end")
        self.telegramAddressEnglishEntering.delete("0","end")
        self.chapterEntering.delete("0","end")
        self.contentEntering.delete("0","end")
        self.pageEntering.delete("0","end")
        self.lessonEntering.delete("0","end")
        self.publisherEntering.delete("0","end")
        ###
        # select search tab
        self.nb.select(self.frame2)
        #
        msg=Toplevel(self.master)
        ttk.Label(msg,text = f"Word :{word}").grid(row=0,column=1,sticky="nw",padx = 20,rowspan=3,pady = 20)

        ttk.Label(msg,text = f"deutsch meaning :{deutsch}",wraplength=500).grid(row=1,column=1,sticky="nw",padx = 20,rowspan=3,pady = 20)

        ttk.Label(msg,text = f"book Name :{bookName}").grid(row=2,column=1,sticky="nw",padx = 20,rowspan=3,pady = 20)

        labelWin = ttk.Label(msg,text = "✅",font=('Arial',60,"bold")).grid(row=0,column=2,rowspan=3,sticky="nw")

        msgDeleted = ttk.Label(msg,text = f"The word ( {word} ) with it's meaning and book entered to DB !",font=('Arial',15,"bold")).grid(row=5,column=1,sticky="nswe",columnspan=2)

        btn_OkEntered = ttk.Button(msg,command = msg.destroy,text="Ok")
        btn_OkEntered.grid(row = 7,column=1,columnspan=2)
        self.enterWarnTL.destroy()
        # self.treeViewSearchSimple.destroy()
        # self.search_btn()


    def search(self):
        # frame2 = self.frame2
        # panedWindow = ttk.PanedWindow(frame2)
        
        # global wordSearch
        # ,deutschSearch
        # ,wordValue,wordTypeValue,articleValue,deutschMeaningValue,bookNameValue,publisherValue
        word_label = ttk.Label(self.frame2,text = "Word").grid(row=0,column=0,sticky="nw", padx = 10)
        # global wordName
        wordName = tkinter.StringVar()
        self.wordSearch =ttk.Entry(self.frame2,width=30,textvariable=wordName)
        self.wordSearch.grid(row=1,column=0, padx = 10,sticky="nw")
        self.wordSearch.focus_set()
        wordName.trace("w",lambda l,idx,mode:self.search_btn())

        # deutsch_label = ttk.Label(self.frame2,text = "deutsch").grid(row=0,column=2,padx = 20,sticky="nw")
        # deutschSearch =ttk.Entry(self.frame2,width=30)
        # deutschSearch.grid(row=1,column=2, padx = 20,sticky="nw")
        # btn_search = ttk.Button(self.frame2,command = self.search_btn,text="Search").grid(row = 1,column=4)
        # self.frame2.bind("<Enter>",btn_search)
        ## all words   
        ttk.Label(self.frame2,text="All Words").grid(row=4,column=0,sticky="nw")
        scrolListAllWords=tkinter.Scrollbar(self.frame2)
        scrolListAllWords.grid(row=5,column=1,sticky="nsew")
        listBoxAllWords = Listbox(self.frame2,yscrollcommand=scrolListAllWords.set,width=30)
        listBoxAllWords.grid(row=5,column=0,)
        scrolListAllWords.config(command=listBoxAllWords.yview)

        self.outputAllWords=TE.Search().getAllwords()
        if isinstance(self.outputAllWords,list):
            for item in self.outputAllWords:
                listBoxAllWords.insert(END,item)

            listBoxAllWords.bind("<<ListboxSelect>>",self.selectLIstboxItem)
        # ttk.Label(self.frame2,text=f"{outputAllWords.index("")}").grid(row=5,column=2,sticky="nw")     
        ttk.Label(self.frame2,text=f"1 - {len(self.outputAllWords)}",font=("Arial",12,"bold")).grid(row=6,column=0) 


        self.master.mainloop()

    def advanceSearch(self):
        frame3 = self.frame3
        word_label = ttk.Label(frame3,text = "Word").grid(row=0,column=0,sticky="nw", padx = 10)
        word_text =ttk.Entry(frame3,width=10).grid(row=1,column=0, padx = 10)
        wordType_label = ttk.Label(frame3,text = "Word Type").grid(row=2,column=0,sticky="nw", padx = 10)
        wordType_text =ttk.Entry(frame3,width=10).grid(row=3,column=0, padx = 10)
        article_label = ttk.Label(frame3,text = "article").grid(row=4,column=0,sticky="nw", padx = 10)
        article_text =ttk.Entry(frame3,width=10).grid(row=5,column=0, padx = 10)
        bookName_label = ttk.Label(frame3,text = "book name").grid(row=6,column=0,sticky="nw", padx = 10)
        bookName_text =ttk.Entry(frame3,width=10).grid(row=7,column=0, padx = 10)
        chapter_label = ttk.Label(frame3,text = "chapter").grid(row=8,column=0,sticky="nw", padx = 10)
        chapter_text =ttk.Entry(frame3,width=10).grid(row=9,column=0, padx = 10)
        content_label = ttk.Label(frame3,text = "content").grid(row=10,column=0,sticky="nw", padx = 10)
        content_text =ttk.Entry(frame3,width=10).grid(row=11,column=0, padx = 10)
        publisher_label = ttk.Label(frame3,text = "publisher").grid(row=12,column=0,sticky="nw", padx = 10)
        publisher_text =ttk.Entry(frame3,width=10).grid(row=13,column=0, padx = 10)
        lesson_label = ttk.Label(frame3,text = "lesson").grid(row=14,column=0,sticky="nw", padx = 10)
        lesson_text =ttk.Entry(frame3,width=10).grid(row=15,column=0, padx = 10)


        voiceName_label = ttk.Label(frame3,text = "voice name").grid(row=0,column=1,padx = 20,sticky="nw")
        voiceName_text =ttk.Entry(frame3,width=10).grid(row=1,column=1, padx = 20)

        telegramAddress_label = ttk.Label(frame3,text = "telegram address").grid(row=0,column=2,sticky="nw")
        telegramAddress_text =ttk.Entry(frame3,width=15).grid(row=1,column=2)
        #deutsch
        deutsch_label = ttk.Label(frame3,text = "deutsch").grid(row=4,column=1,columnspan=2)

        meaningDeutsch_label = ttk.Label(frame3,text = "meaning : ").grid(row=5,column=1,sticky="ne")
        meaningDeutsch_text =ttk.Entry(frame3,width=15).grid(row=5,column=2)
        fileNameDeutsch_label = ttk.Label(frame3,text = "file Name : ").grid(row=6,column=1,sticky="ne")
        fileNameDeutsch_text =ttk.Entry(frame3,width=15).grid(row=6,column=2)
        telegramAddressDeutsch_label = ttk.Label(frame3,text = "telegram address : ").grid(row=7,column=1,sticky="ne")
        telegramAddressDeutsch_text =ttk.Entry(frame3,width=15).grid(row=7,column=2)

        #english
        english_label = ttk.Label(frame3,text = "english").grid(row=9,column=1,columnspan=2)

        meaningEnglish_label = ttk.Label(frame3,text = "meaning : ").grid(row=10,column=1,sticky="ne")
        meaningEnglish_text =ttk.Entry(frame3,width=15).grid(row=10,column=2)
        fileNameEnglish_label = ttk.Label(frame3,text = "file Name : ").grid(row=11,column=1,sticky="ne")
        fileNameEnglish_text =ttk.Entry(frame3,width=15).grid(row=11,column=2)
        telegramAddressEnglish_label = ttk.Label(frame3,text = "telegram address : ").grid(row=12,column=1,sticky="ne")
        telegramAddressEnglish_text =ttk.Entry(frame3,width=15).grid(row=12,column=2)

        #button enter
        btn_search = ttk.Button(frame3,text="Search").grid(row=1,column=4)

        #synonym
        synonym_label = ttk.Label(frame3,text = "synonym").grid(row=4,column=4,columnspan=2)

        meaningSynonym_label = ttk.Label(frame3,text = "meaning : ").grid(row=5,column=3,sticky="ne")
        meaningSynonym_text =ttk.Entry(frame3,width=15).grid(row=5,column=4)
        fileNameSynonym_label = ttk.Label(frame3,text = "file Name : ").grid(row=6,column=3,sticky="ne")
        fileNameSynonym_text =ttk.Entry(frame3,width=15).grid(row=6,column=4)
        telegramAddressSynonym_label = ttk.Label(frame3,text = "telegram address : ").grid(row=7,column=3,sticky="ne")
        telegramAddressSynonym_text =ttk.Entry(frame3,width=15).grid(row=7,column=4)

        #persian
        persian_label = ttk.Label(frame3,text = "persian").grid(row=9,column=4,columnspan=3)

        meaningPersian_label = ttk.Label(frame3,text = "meaning : ").grid(row=10,column=3,sticky="ne")
        meaningPersian_text =ttk.Entry(frame3,width=15).grid(row=10,column=4)
        fileNamePersian_label = ttk.Label(frame3,text = "file Name : ").grid(row=11,column=3,sticky="ne")
        fileNamePersian_text =ttk.Entry(frame3,width=15).grid(row=11,column=4)
        telegramAddressPersian_label = ttk.Label(frame3,text = "telegram address : ").grid(row=12,column=3,sticky="ne")
        telegramAddressPersian_text =ttk.Entry(frame3,width=15).grid(row=12,column=4)
        return word_text,wordType_text,article_text,bookName_text,chapter_text,content_text,publisher_text,lesson_text,voiceName_text,telegramAddress_text,meaningDeutsch_text,fileNameDeutsch_text,telegramAddressDeutsch_text,meaningEnglish_text,fileNameEnglish_text,telegramAddressEnglish_text,meaningSynonym_text,fileNameSynonym_text,telegramAddressSynonym_text,meaningPersian_text,fileNamePersian_text,telegramAddressPersian_text 
    
    def selectLIstboxItem(self,event):
        w=event.widget
        idx=int(w.curselection()[0])
        value=w.get(idx)
        ttk.Label(self.frame2,text=f"{self.outputAllWords.index(value)+1} - {value}                                                        ",font=("Arial",15,"bold")).grid(row=5,column=2,sticky="nw") 
        self.findTreeWord(value)

    def search_btn(self):
        frame2 = self.frame2
        # self.treeViewSearchSimple
        ####
        self.scrolList=tkinter.Scrollbar(self.frame2)
        self.scrolList.grid(row=2,column=1,sticky="nsew")
        # 
        # global listboxSimple
        # self.listboxSimple 
        self.listboxSimple = Listbox(self.frame2,yscrollcommand=self.scrolList.set,width=30)
        self.listboxSimple.grid(row=2,column=0,)
        # search.getSearchContain(word)
        self.scrolList.config(command=self.listboxSimple.yview)
        wordsContain = TE.Search().getSearchContain(self.wordSearch.get())
        if isinstance(wordsContain,list):
            for item in wordsContain:
                self.listboxSimple.insert(END,item)

            self.listboxSimple.bind("<<ListboxSelect>>",self.selectLIstboxItem)
        ## all words   
        # ttk.Label(self.frame2,text="All Words").grid(row=4,column=0)
        # scrolListAllWords=tkinter.Scrollbar(self.frame2)
        # scrolListAllWords.grid(row=5,column=1,sticky="nsew")
        # listBoxAllWords = Listbox(self.frame2,yscrollcommand=scrolListAllWords.set,width=30)
        # listBoxAllWords.grid(row=5,column=0,)
        # scrolListAllWords.config(command=listBoxAllWords.yview)

        # outputAllWords=TE.Search().getAllwords()
        # if isinstance(outputAllWords,list):
        #     for item in outputAllWords:
        #         listBoxAllWords.insert(END,item)

        #     listBoxAllWords.bind("<<ListboxSelect>>",self.selectLIstboxItem)

    def findTreeWord(self,word):
        frame2=self.frame2
        self.treeViewSearchSimple = ttk.Treeview(frame2)
        self.treeViewSearchSimple.grid(row=2,column=2,columnspan = 3,sticky = "nsew",ipadx = 200)
        # , -ipady, -padx
        self.treeViewSearchSimple.config(selectmode="browse")
        vsb=ttk.Scrollbar(frame2,orient="vertical",command=self.treeViewSearchSimple.yview)
        vsb.grid(row=2,column = 5,sticky = "nsew")
        # vsb.place(height=50)
        # tkinter.VERTICAL
        # tkinter.HORIZONTAL
        hsb =ttk.Scrollbar(frame2,orient="horizontal",command=self.treeViewSearchSimple.xview)
        hsb.grid(row=3,column = 2,columnspan = 3,sticky = "nsew")
        # hsb.place(x=20,y=10,height=10)
        # self.treeViewSearchSimple.configure(xscrollcommand=hsb.set)
        self.treeViewSearchSimple.configure(yscrollcommand=vsb.set,xscrollcommand=hsb.set)
        hsb.config(command=self.treeViewSearchSimple.xview)
        vsb.config(command=self.treeViewSearchSimple.yview)
        output=TE.Search().simpleSearch(word)
        self.outputSimpleSearch = output

        # print(f"output = {output}")
        if isinstance(output,bool) is not True:
           for x in range(len(output)):
                for field,val in output[x].items():
                    if field == "wordId":
                        self.treeViewSearchSimple.insert("",str(x),str(val),text = output[x]["word"])
                        # treeview.insert("",output[x]["wordId"],str(val),text = output[x]["word"])
                    for i in range(1,10):
                        if field == f"meaning{i}":
                            for meaningField,meaningVal in val.items():
                                if meaningField == "meaningId":
                                    
                                    self.treeViewSearchSimple.insert(str(output[x]["wordId"]),i,str(output[x]["wordId"])+str(meaningVal),text = output[x][field]["deutschMeaning"])
                                for j in range(1,10):
                                    if meaningField == f"book{j}":
                                        for bookField,bookVal in meaningVal.items():
                                            if bookField == "bookId":
                                                # print(str(output[x]["wordId"])+str(output[x][f"meaning{i}"]["meaningId"]))
                                                # print(str(output[x]["wordId"])+str(output[x][f"meaning{i}"]["meaningId"])+str(bookVal))
                                                par=str(output[x]["wordId"])+str(output[x][f"meaning{i}"]["meaningId"])
                                                iddTree = str(output[x]["wordId"])+str(output[x][f"meaning{i}"]["meaningId"])+str(bookVal)
                                                self.treeViewSearchSimple.insert(par,j,iddTree,text = meaningVal["bookName"])     
        else:
            self.treeViewSearchSimple.insert("","0","nothingFound",text = "Do Not Have It!")

        self.treeViewSearchSimple.bind("<Button-3>", self.do_popup)  
    def do_popup(self,event): 
        # print(f"event ={event}")
        # print(f"type(event) = {type(event)}")

        iid = self.treeViewSearchSimple.identify_row(event.y)
        # print(f"iid = {iid}")
        iddSplited = self.spliterIid(iid)
        menu = self.menuItems(iddSplited)
        if iid:
            self.treeViewSearchSimple.selection_set(iid)
        try: 
            menu.tk_popup(event.x_root, event.y_root) 
        finally: 
            menu.grab_release() 
        return iid,menu


    def menuItems(self,iidList):
            m = Menu(self.treeViewSearchSimple, tearoff = 0) 
            # print(f"iid menuItems = {iid}")
            # output = self.spliterIid(iid)
            # print(f"output = {output}")
            # print(f"len(output) = {len(output)}")
            self.iidList = iidList
            if len(iidList)==1:
                m.add_command(label ="edit word✍",command = self.editWord) 
                m.add_command(label ="delete word❌",command = self.deleteWordMenu)
                m.add_separator() 
                m.add_command(label ="new meaning 🆕",command = self.newMeaning) 
            elif len(iidList)==2:
                m.add_command(label ="edit meaning✍",command=self.editMeaning) 
                m.add_command(label ="delete meaning❌",command= self.deleteMeaning)
                m.add_separator() 
                m.add_command(label ="new book 🆕",command=self.newBookForm) 
            elif len(iidList)==3:
                m.add_command(label ="edit book✍",command=self.editBookForm) 
                m.add_command(label ="delete book❌",command=self.deleteBook)
            return m

    def deleteBook(self):
        # self.deleteBookTL
            bookId=self.iidList[2]
            output = TE.Search().getBookValues(bookId)
            meaningId = self.iidList[1]
            outputMeanVals = TE.Search().getMeaningValues(meaningId)
            self.deleteBookTL = Toplevel(self.master)
            
            labelWin = ttk.Label(self.deleteBookTL,text = "Delete Book",font=('Arial',20,"bold")).grid(row=1,column=2,columnspan=4,sticky="nsew")
            labelWin = ttk.Label(self.deleteBookTL,text = "❗❓",font=('Arial',80,"bold")).grid(row=2,column=3,rowspan=3,columnspan=2,sticky="nw")
            
            wordLabel = ttk.Label(self.deleteBookTL,text = f"Word :{outputMeanVals['word']}",font = ("Arial",10,"bold")).grid(row=1,column=1,sticky="nw",padx = 20)

            # print(f"output else ={output}")
            wordTypeLabel = ttk.Label(self.deleteBookTL,text = f"deutsch meaning : {outputMeanVals['deutsch']}",wraplength=200 ).grid(row=2,column=1,sticky="nw",padx = 20)
            

            ttk.Label(self.deleteBookTL,text = f"Book Name : {output['bookName']}" ,font = ("Arial",10,"bold")).grid(row=3,column=1,sticky="nw",padx = 20)

            ttk.Label(self.deleteBookTL,text = f"publisher : {output['publisher']}" ,font = ("Arial",10,"bold")).grid(row=4,column=1,sticky="nw",padx = 20)

            msg = ttk.Label(self.deleteBookTL,text = f"Are you sure to delete this  book ({output['bookName']}) !?",font=('Arial',15,"bold")).grid(row=6,column=1,columnspan=4,padx=20)
            # ,sticky="nw"
            btn_yesEdit = ttk.Button(self.deleteBookTL,command = self.deleteBookMsgDone,text="Yes")
            btn_yesEdit.grid(row = 7,column=3,sticky="nw")

            btn_noEdit = ttk.Button(self.deleteBookTL,command = self.deleteBookTL.destroy,text="No")
            btn_noEdit.grid(row = 7,column=4,sticky="nw")
            ttk.Label(self.deleteBookTL,text = "").grid(row=7,column=0,columnspan=3,pady=1,padx=40)

    def deleteBookMsgDone(self):
        pass
        bookId=self.iidList[2]
        outputBookVals = TE.Search().getBookValues(bookId)
        meaningId = self.iidList[1]
        outputMeanVals = TE.Search().getMeaningValues(meaningId)
        TE.Deleting().deleteBook(bookId)
        msg = Toplevel(self.master)
        # wordId = self.iidList[0]

        
        # wordEntry,wordTypeEntry,articleEntry,voiceNameEntry,telegramAddressEntry
        ttk.Label(msg,text = f"Word :{outputBookVals['word']}").grid(row=0,column=1,sticky="nw",padx = 20,rowspan=3,pady = 20)

        ttk.Label(msg,text = f"book name :{outputBookVals['bookName']}").grid(row=1,column=1,sticky="nw",padx = 20,rowspan=3,pady = 20)

        ttk.Label(msg,text = f"publisher :{outputBookVals['publisher']}").grid(row=2,column=1,sticky="nw",padx = 20,rowspan=3,pady = 20)

        labelWin = ttk.Label(msg,text = "✅",font=('Arial',60,"bold")).grid(row=0,column=2,rowspan=3,sticky="nw")

        msgDeleted = ttk.Label(msg,text = f"The Book ( {outputBookVals['bookName']} ) is eidted !",font=('Arial',15,"bold")).grid(row=5,column=1,sticky="nswe",columnspan=2)

        btn_OkDelete = ttk.Button(msg,command = msg.destroy,text="Ok")
        btn_OkDelete.grid(row = 7,column=1,columnspan=2)
        self.deleteBookTL.destroy()
        # self.treeViewSearchSimple.destroy()
        self.search_btn()




    def editBookForm(self):

        meaningId = self.iidList[1]
        outputMeanVals = TE.Search().getMeaningValues(meaningId) 
        word = outputMeanVals["word"]
        self.wordVal = word
        
        deuMeaning = outputMeanVals["deutsch"]
        bookId=self.iidList[2]
        output = TE.Search().getBookValues(bookId)
        # self.editBookTL,self.bookNameEntryEdit,self.chapterEntryEdit,self.contentEntryEdit,self.pageEntryEdit,self.lessonEntryEdit,self.publisherEntryEdit=None,None,None,None,None,None,None
        # print(f"output = {output}")
        self.editBookTL= Toplevel(self.master)

        wordLabel = ttk.Label(self.editBookTL,text = f"word : {word}",font=("Arial",12,"bold")).grid(row=1,column=1)
        wordLabel = ttk.Label(self.editBookTL,text = f"deutsch meaning : {deuMeaning}",wraplength=200,font=("Arial",10,"")).grid(row=1,column=2)


        labelWin = ttk.Label(self.editBookTL,text = "Edit Book",font=('Arial',25,"bold")).grid(row=2,column=4,columnspan=1,rowspan=5)

        # fieldList "bookName","chapter","content","page","lesson","publisher","word","meaningId"
        bookNameLabel = ttk.Label(self.editBookTL,text = "Book Name",font=("Arial",9,"bold")).grid(row=3,column=1,sticky="ne",pady=5)
        self.bookNameEntryEdit =ttk.Entry(self.editBookTL,width=45)
        self.bookNameEntryEdit.insert(0,output["bookName"])
        self.bookNameEntryEdit.grid(row=3,column=2,sticky="nw",pady=5)


        chapterLabel = ttk.Label(self.editBookTL,text = "chapter",font=("Arial",9,"bold")).grid(row=5,column=1,sticky="ne",pady=5)
        self.chapterEntryEdit =ttk.Entry(self.editBookTL,width=45)
        self.chapterEntryEdit.insert(0,output["chapter"])
        self.chapterEntryEdit.grid(row=5,column=2,sticky="nw",pady=5)


        contentLabel = ttk.Label(self.editBookTL,text = "content",font=("Arial",9,"bold")).grid(row=7,column=1,sticky="ne",pady=5)
        self.contentEntryEdit =ttk.Entry(self.editBookTL,width=45)
        self.contentEntryEdit.insert(0,output["content"])
        self.contentEntryEdit.grid(row=7,column=2,sticky="nw",pady=5)

        pageLabel = ttk.Label(self.editBookTL,text = "page",font=("Arial",9,"bold")).grid(row=9,column=1,sticky="ne",pady=5)
        self.pageEntryEdit =ttk.Entry(self.editBookTL,width=45)
        self.pageEntryEdit.insert(0,output["page"])
        self.pageEntryEdit.grid(row=9,column=2,sticky="nw",pady=5)


        lessonLabel = ttk.Label(self.editBookTL,text = "lesson",font=("Arial",9,"bold")).grid(row=11,column=1,sticky="ne",pady=5)
        self.lessonEntryEdit =ttk.Entry(self.editBookTL,width=45)
        self.lessonEntryEdit.insert(0,output["lesson"])
        self.lessonEntryEdit.grid(row=11,column=2,sticky="nw",pady=5)

        publisherLabel = ttk.Label(self.editBookTL,text = "publisher",font=("Arial",9,"bold")).grid(row=13,column=1,sticky="ne",pady=5)
        self.publisherEntryEdit =ttk.Entry(self.editBookTL,width=45)
        self.publisherEntryEdit.insert(0,output["publisher"])
        self.publisherEntryEdit.grid(row=13,column=2,sticky="nw",pady=5)

        
        btn_save = ttk.Button(self.editBookTL,command = self.editBookMsg,text="Save")
        btn_save.grid(row = 15,column=3)
        # self.frame2.bind("<Enter>",btn_search)

        btn_cancel = ttk.Button(self.editBookTL,command = self.editBookTL.destroy,text="Cancel")
        btn_cancel.grid(row = 15,column=4)
        ## space 
        ttk.Label(self.editBookTL,text = "").grid(row=16,column=0,padx=5)
        ttk.Label(self.editBookTL,text = "").grid(row=16,column=5,padx=5,pady=1)
        ##

    def editBookMsg(self):
        bookId=self.iidList[2]
        output = TE.Search().getBookValues(bookId)
        meaningId = self.iidList[1]
        outputMeanVals = TE.Search().getMeaningValues(meaningId) 
        # fieldList "bookName","chapter","content","page","lesson","publisher","word","meaningId"
        # self.editBookTL,self.bookNameEntryEdit,self.chapterEntryEdit,self.contentEntryEdit,self.pageEntryEdit,self.lessonEntryEdit,self.publisherEntryEdit=None,None,None,None,None,None,None
        if (self.bookNameEntryEdit.get()==output["bookName"] and
            self.chapterEntryEdit.get()==output["chapter"] and
            self.contentEntryEdit.get()==output["content"] and
            self.pageEntryEdit.get()==output["page"] and
            self.lessonEntryEdit.get()==output["lesson"] and
            self.publisherEntryEdit.get()==output["publisher"] ):
            warnEqual = Toplevel(self.master)
            ttk.Label(warnEqual,text = "!!!",font=('Arial',80,"bold")).grid(row=0,column=0,columnspan=1,padx = 30)

            labelWin = ttk.Label(warnEqual,text = "You didn't do any edition!",font=('Arial',12,"bold"))
            labelWin.grid(row = 2,column=0,columnspan=1,padx = 30)

            btn_Ok = ttk.Button(warnEqual,command = warnEqual.destroy,text="Ok")
            btn_Ok.grid(row = 3,column=0,columnspan=1)
            ttk.Label(warnEqual,text = "").grid(row = 4,column=0,columnspan=1,pady = 1)

           
           
           
           
        #    ttk.Label(self.newBookTL,text = "*",font=("Arial",25,"bold"),foreground="red").grid(row=3,column=3,sticky="nw")
        else:
            # pass
            self.warnSureEditionBook = Toplevel(self.master)
            
            labelWin = ttk.Label(self.warnSureEditionBook,text = "❗❓",font=('Arial',80,"bold")).grid(row=1,column=3,rowspan=3,columnspan=2,sticky="nw")

            wordLabel = ttk.Label(self.warnSureEditionBook,text = f"Word :{outputMeanVals['word']}",font = ("Arial",10,"bold")).grid(row=1,column=1,sticky="nw",padx = 20)

            # print(f"output else ={output}")
            wordTypeLabel = ttk.Label(self.warnSureEditionBook,text = f"deutsch meaning : {outputMeanVals['deutsch']}",wraplength=200 ).grid(row=2,column=1,sticky="nw",padx = 20)
            

            ttk.Label(self.warnSureEditionBook,text = f"Book Name : {self.bookNameEntryEdit.get()}" ,font = ("Arial",10,"bold")).grid(row=3,column=1,sticky="nw",padx = 20)

            msg = ttk.Label(self.warnSureEditionBook,text = f"Are you sure to save this edition book !?",font=('Arial',15,"bold")).grid(row=5,column=1,columnspan=4,padx=20)
            # ,sticky="nw"
            btn_yesEdit = ttk.Button(self.warnSureEditionBook,command = self.saveBookEditDone,text="Yes")
            btn_yesEdit.grid(row = 6,column=3,sticky="nw")

            btn_noEdit = ttk.Button(self.warnSureEditionBook,command = self.warnSureEditionBook.destroy,text="No")
            btn_noEdit.grid(row = 6,column=4,sticky="nw")
            ttk.Label(self.warnSureEditionBook,text = "").grid(row=7,column=0,columnspan=3,pady=1,padx=40)

    def saveBookEditDone(self):
        bookId=self.iidList[2]
        # self.editBookTL,self.bookNameEntryEdit,self.chapterEntryEdit,self.contentEntryEdit,self.pageEntryEdit,self.lessonEntryEdit,self.publisherEntryEdit=None,None,None,None,None,None,None

        # fieldList "bookName","chapter","content","page","lesson","publisher","word","meaningId"
        TE.Editing().editBook(bookId,bookName=self.bookNameEntryEdit.get(),chapter=self.chapterEntryEdit.get(),content=self.contentEntryEdit.get(),page=self.pageEntryEdit.get(),lesson=self.lessonEntryEdit.get(),publisher=self.publisherEntryEdit.get())

        msg = Toplevel(self.master)
        wordId = self.iidList[0]

        
        # wordEntry,wordTypeEntry,articleEntry,voiceNameEntry,telegramAddressEntry
        ttk.Label(msg,text = f"Word :{self.wordVal}").grid(row=0,column=1,sticky="nw",padx = 20,rowspan=3,pady = 20)

        ttk.Label(msg,text = f"book name :{self.bookNameEntryEdit.get()}").grid(row=1,column=1,sticky="nw",padx = 20,rowspan=3,pady = 20)

        ttk.Label(msg,text = f"publisher :{self.publisherEntryEdit.get()}").grid(row=2,column=1,sticky="nw",padx = 20,rowspan=3,pady = 20)

        labelWin = ttk.Label(msg,text = "✅",font=('Arial',60,"bold")).grid(row=0,column=2,rowspan=3,sticky="nw")

        msgDeleted = ttk.Label(msg,text = f"The Book ( {self.bookNameEntryEdit.get()} ) is eidted !",font=('Arial',15,"bold")).grid(row=5,column=1,sticky="nswe",columnspan=2)

        btn_OkDelete = ttk.Button(msg,command = msg.destroy,text="Ok")
        btn_OkDelete.grid(row = 7,column=1,columnspan=2)
        self.editBookTL.destroy()
        self.warnSureEditionBook.destroy()



    def newBookForm(self):
        meaningId = self.iidList[1]
        # print(f"meaningId = {meaningId}")
        meaningId = self.iidList[1]
        outputMeanVals = TE.Search().getMeaningValues(meaningId) 
        word = outputMeanVals["word"]
        self.wordVal = word
        deuMeaning = outputMeanVals["deutsch"]
        # self.newBookTL,self.bookNameEntry,self.chapterEntry,self.contentEntry,self.pageEntry,self.lessonEntry,self.publisherEntry,self.wordEntry=None,None,None,None,None,None,None,None
        # fieldList = ["wordId","word","wordType","article","wordVoiceName","wordtelegramLink"]
        self.newBookTL= Toplevel(self.master)

        wordLabel = ttk.Label(self.newBookTL,text = f"word : {word}",font=("Arial",12,"bold")).grid(row=1,column=1)
        wordLabel = ttk.Label(self.newBookTL,text = f"deutsch meaning : {deuMeaning}",wraplength=200,font=("Arial",10,"")).grid(row=1,column=2)

        # self.wordEntry =ttk.Entry(self.newBookTL,width=30)
        # self.wordEntry.grid(row=2,column=0, padx = 20) 

        labelWin = ttk.Label(self.newBookTL,text = "New Book",font=('Arial',25,"bold")).grid(row=2,column=4,columnspan=1,rowspan=5)
        # wordEntry,wordTypeEntry,articleEntry,voiceNameEntry,telegramAddressEntry
        # wordLabel = ttk.Label(self.newBookTL,text = "Word").grid(row=1,column=0,sticky="nw", padx = 20)

        bookNameLabel = ttk.Label(self.newBookTL,text = "Book Name",font=("Arial",9,"bold")).grid(row=3,column=1,sticky="ne",pady=5)
        self.bookNameEntry =ttk.Entry(self.newBookTL,width=30)
        self.bookNameEntry.grid(row=3,column=2,sticky="nw",pady=5)


        chapterLabel = ttk.Label(self.newBookTL,text = "chapter",font=("Arial",9,"bold")).grid(row=5,column=1,sticky="ne",pady=5)
        self.chapterEntry =ttk.Entry(self.newBookTL,width=30)
        self.chapterEntry.grid(row=5,column=2,sticky="nw",pady=5)


        contentLabel = ttk.Label(self.newBookTL,text = "content",font=("Arial",9,"bold")).grid(row=7,column=1,sticky="ne",pady=5)
        self.contentEntry =ttk.Entry(self.newBookTL,width=30)
        self.contentEntry.grid(row=7,column=2,sticky="nw",pady=5)

        pageLabel = ttk.Label(self.newBookTL,text = "page",font=("Arial",9,"bold")).grid(row=9,column=1,sticky="ne",pady=5)
        self.pageEntry =ttk.Entry(self.newBookTL,width=30)
        self.pageEntry.grid(row=9,column=2,sticky="nw",pady=5)


        lessonLabel = ttk.Label(self.newBookTL,text = "lesson",font=("Arial",9,"bold")).grid(row=11,column=1,sticky="ne",pady=5)
        self.lessonEntry =ttk.Entry(self.newBookTL,width=30)
        self.lessonEntry.grid(row=11,column=2,sticky="nw",pady=5)

        publisherLabel = ttk.Label(self.newBookTL,text = "publisher",font=("Arial",9,"bold")).grid(row=13,column=1,sticky="ne",pady=5)
        self.publisherEntry =ttk.Entry(self.newBookTL,width=30)
        self.publisherEntry.grid(row=13,column=2,sticky="nw",pady=5)

        
        btn_save = ttk.Button(self.newBookTL,command = self.newBookMsg,text="Save")
        btn_save.grid(row = 15,column=3)
        # self.frame2.bind("<Enter>",btn_search)

        btn_cancel = ttk.Button(self.newBookTL,command = self.newBookTL.destroy,text="Cancel")
        btn_cancel.grid(row = 15,column=4)
        ## space 
        ttk.Label(self.newBookTL,text = "").grid(row=16,column=0,padx=5)
        ttk.Label(self.newBookTL,text = "").grid(row=16,column=5,padx=5,pady=1)
        ##

    def newBookMsg(self):
        if self.bookNameEntry.get()=="":
           ttk.Label(self.newBookTL,text = "*",font=("Arial",25,"bold"),foreground="red").grid(row=3,column=3,sticky="nw")
        else:
            # pass
            self.warnMsgNB = Toplevel(self.master)
            # self.bookNameEntry,self.chapterEntry,self.contentEntry,self.pageEntry,self.lessonEntry,self.publisherEntry,self.wordEntry
            labelWin = ttk.Label(self.warnMsgNB,text = "❗❓",font=('Arial',80,"bold")).grid(row=1,column=3,rowspan=6,columnspan=2,sticky="nw")
            ttk.Label(self.warnMsgNB,text = f"word :{self.wordVal}",font=('Arial',10,"bold")).grid(row=1,column=1,sticky="nw",padx = 20)

            ttk.Label(self.warnMsgNB,text = f"book name :{self.bookNameEntry.get()}").grid(row=2,column=1,sticky="nw",padx = 20)


            ttk.Label(self.warnMsgNB,text = f"chapter : {self.chapterEntry.get()}" ).grid(row=3,column=1,sticky="nw",padx = 20)
            
            ttk.Label(self.warnMsgNB,text = f"content :{self.contentEntry.get()}").grid(row=4,column=1,sticky="nw",padx = 20)


            ttk.Label(self.warnMsgNB,text = f"page : {self.pageEntry.get()}" ).grid(row=5,column=1,sticky="nw",padx = 20)

            ttk.Label(self.warnMsgNB,text = f"lesson :{self.lessonEntry.get()}").grid(row=6,column=1,sticky="nw",padx = 20)


            ttk.Label(self.warnMsgNB,text = f"publisher : {self.publisherEntry.get()}" ).grid(row=7,column=1,sticky="nw",padx = 20)


            ttk.Label(self.warnMsgNB,text = f"Are you sure to Enter this book ({self.bookNameEntry.get()}) to DB !?",font=('Arial',15,"bold")).grid(row=8,column=1,columnspan=4,padx=20)
            # ,sticky="nw"
            btn_yesEdit = ttk.Button(self.warnMsgNB,command = self.saveNewBook,text="Yes")
            btn_yesEdit.grid(row = 9,column=3,sticky="nw")

            btn_noEdit = ttk.Button(self.warnMsgNB,command = self.warnMsgNB.destroy,text="No")
            btn_noEdit.grid(row = 9,column=4,sticky="nw")
            ttk.Label(self.warnMsgNB,text = "").grid(row=10,column=0,columnspan=3,pady=1,padx=40)    

    def saveNewBook(self):
        # pass
        meaningId = self.iidList[1]
        output = TE.Entering().enterNewBook(meaningId,self.bookNameEntry.get(),chapter=self.chapterEntry.get(),content=self.contentEntry.get(),page=self.pageEntry.get(),lesson=self.lessonEntry.get(),publisher=self.publisherEntry.get(),word=self.wordVal)
        self.warnMsgNB.destroy()
        # self.treeViewSearchSimple.destroy()
        self.search_btn()
        msg = Toplevel(self.master)
        wordId = self.iidList[0]

        
        # wordEntry,wordTypeEntry,articleEntry,voiceNameEntry,telegramAddressEntry
        ttk.Label(msg,text = f"Word :{self.wordVal}").grid(row=0,column=1,sticky="nw",padx = 20,rowspan=3,pady = 20)

        ttk.Label(msg,text = f"book name :{self.bookNameEntry.get()}").grid(row=1,column=1,sticky="nw",padx = 20,rowspan=3,pady = 20)

        ttk.Label(msg,text = f"publisher :{self.publisherEntry.get()}").grid(row=2,column=1,sticky="nw",padx = 20,rowspan=3,pady = 20)

        labelWin = ttk.Label(msg,text = "✅",font=('Arial',60,"bold")).grid(row=0,column=2,rowspan=3,sticky="nw")

        msgDeleted = ttk.Label(msg,text = f"The Book ( {self.bookNameEntry.get()} ) is Entered to DB !",font=('Arial',15,"bold")).grid(row=5,column=1,sticky="nswe",columnspan=2)

        btn_OkDelete = ttk.Button(msg,command = msg.destroy,text="Ok")
        btn_OkDelete.grid(row = 7,column=1,columnspan=2)
        self.newBookTL.destroy()









    def deleteMeaning(self):
        meaningId = self.iidList[1]
        output = TE.Search().getMeaningValues(meaningId) 
        self.warnSureDelete = Toplevel(self.master)
        ttk.Label(self.warnSureDelete,text = "Delete Meaning",font=('Arial',20,"bold")).grid(row=1,column=3,columnspan=2,sticky="nw")
        labelWin = ttk.Label(self.warnSureDelete,text = "❗❓",font=('Arial',80,"bold")).grid(row=2,column=3,rowspan=3,columnspan=2,sticky="nw")

        wordLabel = ttk.Label(self.warnSureDelete,text = f"Word :{output['word']}").grid(row=1,column=1,sticky="nw",padx = 20)


        wordTypeLabel = ttk.Label(self.warnSureDelete,text = f"deutsch meaning : {output['deutsch']}",wraplength=200 ).grid(row=2,column=1,sticky="nw",padx = 20)
        

        msg = ttk.Label(self.warnSureDelete,text = f"Are you sure to delete this meaning !?",font=('Arial',15,"bold")).grid(row=5,column=1,columnspan=4,padx=20)
        # ,sticky="nw"
        btn_yesEdit = ttk.Button(self.warnSureDelete,command = self.deletedMsgMeaning,text="Yes")
        btn_yesEdit.grid(row = 6,column=3,sticky="nw")

        btn_noEdit = ttk.Button(self.warnSureDelete,command = self.warnSureDelete.destroy,text="No")
        btn_noEdit.grid(row = 6,column=4,sticky="nw")
        ttk.Label(self.warnSureDelete,text = "").grid(row=6,column=0,columnspan=3,pady=1,padx=40)
    
    def deletedMsgMeaning(self):
        meaningId = self.iidList[1]
        outputMVals = TE.Search().getMeaningValues(meaningId)
        word = outputMVals["word"]
        deuMeaning = outputMVals["deutsch"] 
        output =TE.Deleting().deleteMeaning(meaningId)
        if output is True:
            self.warnSureDelete.destroy()
            # self.treeViewSearchSimple.destroy()
            self.search_btn()
            doneMsg = Toplevel(self.master)
            
            labelWin = ttk.Label(doneMsg,text = "✅",font=('Arial',80,"bold")).grid(row=1,column=3,rowspan=3,columnspan=2,sticky="nw")

            wordLabel = ttk.Label(doneMsg,text = f"Word :{word}").grid(row=1,column=1,sticky="nw",padx = 20)


            wordTypeLabel = ttk.Label(doneMsg,text = f"deutsch meaning : {deuMeaning}",wraplength=200 ).grid(row=2,column=1,sticky="nw",padx = 20)
            

            msg = ttk.Label(doneMsg,text = f"The Meaning is deleted !",font=('Arial',15,"bold")).grid(row=4,column=1,columnspan=4,padx=20)
            # ,sticky="nw"
            btn_ok = ttk.Button(doneMsg,command = doneMsg.destroy,text="Ok")
            btn_ok.grid(row = 5,column=0,columnspan=3)

            ttk.Label(doneMsg,text = "").grid(row=6,column=0,columnspan=3,pady=1,padx=40)

    def editMeaning(self):
        meaningId = self.iidList[1]
        #  "deutsch","english","synonym","persian","meaningNumDaf","synVoice","synName","synName","engVoice","engName","engTelegramLink","perVoice","perName","perTelegramLink","deuVoice","deuName","deuTelegramLink","wordDetails","wordId","word","wordType","article"

        output = TE.Search().getMeaningValues(meaningId) 

        self.editMeaningTL=Toplevel(self.master)
        wordlab = ttk.Label(self.editMeaningTL,text=f"Word : {output['word']}",font=("Arial",10,"bold")).grid(row=0,column=0,padx=20,sticky="nw",columnspan=2)

        deutschLab = ttk.Label(self.editMeaningTL,text="deutsch",font=("Arial",15,"bold")).grid(row=1,column=0,padx=20,columnspan=2,pady=5)

        deuMeaningLab = ttk.Label(self.editMeaningTL,text="meaning").grid(row=2,column=0,padx=20,sticky="ne",pady=3)
        self.deuMeaningEdit = Text(self.editMeaningTL,width=30,height=5)
        self.deuMeaningEdit.insert(1.0,output["deutsch"])
        self.deuMeaningEdit.grid(row=2,column=1,sticky="nw",pady=3)

        meaningNumDafLab = ttk.Label(self.editMeaningTL,text="meaning Num Daf").grid(row=3,column=0,padx=20,sticky="ne",pady=3)
        self.meaningNumDafEdit = ttk.Entry(self.editMeaningTL,width=40)
        self.meaningNumDafEdit.insert(0,output["meaningNumDaf"])
        self.meaningNumDafEdit.grid(row=3,column=1,sticky="nw",pady=3)

        deuFileNameLab = ttk.Label(self.editMeaningTL,text="file name").grid(row=4,column=0,padx=20,sticky="ne",pady=3)
        self.deuFileNameEdit = ttk.Entry(self.editMeaningTL,width=40)
        self.deuFileNameEdit.insert(0,output["deuName"])
        self.deuFileNameEdit.grid(row=4,column=1,sticky="nw",pady=3)

        deuTelAddLab = ttk.Label(self.editMeaningTL,text="telegram address").grid(row=5,column=0,padx=20,sticky="ne",pady=3)
        self.deuTelAddEdit = ttk.Entry(self.editMeaningTL,width=40)
        self.deuTelAddEdit.insert(0,output["deuTelegramLink"])
        self.deuTelAddEdit.grid(row=5,column=1,sticky="nw",pady=3)

        #  "deutsch","english","synonym","persian","meaningNumDaf","synVoice","synName","synName","engVoice","engName","engTelegramLink","perVoice","perName","perTelegramLink","deuVoice","deuName","deuTelegramLink","wordDetails","wordId","word","wordType","article"

        ##

        # de = StringVar()
        ## english
        # self.engMeaning,self.engFileName,self.engTelAdd
        englishLab = ttk.Label(self.editMeaningTL,text="english",font=("Arial",15,"bold")).grid(row=7,column=0,columnspan=2,sticky="s",pady=5)
        engMeaningLab = ttk.Label(self.editMeaningTL,text="meaning").grid(row=8,column=0,padx=20,sticky="ne",pady=3)
        self.engMeaningEdit = Text(self.editMeaningTL,width=30,height=5)
        self.engMeaningEdit.insert(1.0,output["english"])

        # self.deuMeaningEdit = Text(self.editMeaningTL,width=30,height=5)
        # self.deuMeaningEdit.insert(1.0,output["deutsch"])


        self.engMeaningEdit.grid(row=8,column=1,sticky="nw",pady=3)

        engFileNameLab = ttk.Label(self.editMeaningTL,text="file name").grid(row=9,column=0,padx=20,sticky="ne",pady=3)
        self.engFileNameEdit = ttk.Entry(self.editMeaningTL,width=40)
        self.engFileNameEdit.insert(0,output["engName"])
        self.engFileNameEdit.grid(row=9,column=1,sticky="nw",pady=3)

        engTelAddLab = ttk.Label(self.editMeaningTL,text="telegram address").grid(row=10,column=0,padx=20,sticky="ne",pady=3)
        self.engTelAddEdit = ttk.Entry(self.editMeaningTL,width=40)
        self.engTelAddEdit.insert(0,output["engTelegramLink"])
        self.engTelAddEdit.grid(row=10,column=1,sticky="nw",pady=3)

        #  "deutsch","english","synonym","persian","meaningNumDaf","synTelegramLink","synName","engVoice","engName","engTelegramLink","perVoice","perName","perTelegramLink","deuVoice","deuName","deuTelegramLink","wordDetails","wordId","word","wordType","article"


        ## Synonym
        # self.synMeaning,self.synFileName,self.synTelAdd
        synonymLab = ttk.Label(self.editMeaningTL,text="synonym",font=("Arial",15,"bold")).grid(row=1,column=3,columnspan=2,sticky="s",pady=5)
        synMeaningLab = ttk.Label(self.editMeaningTL,text="meaning").grid(row=2,column=3,padx=20,sticky="ne",pady=3)
        self.synMeaningEdit = Text(self.editMeaningTL,width=30,height=5)
        self.synMeaningEdit.insert(1.0,output["synonym"])
        self.synMeaningEdit.grid(row=2,column=4,sticky="nw",pady=3)

        synFileNameLab = ttk.Label(self.editMeaningTL,text="file name").grid(row=3,column=3,padx=20,sticky="ne",pady=3)
        self.synFileNameEdit = ttk.Entry(self.editMeaningTL,width=40)
        self.synFileNameEdit.insert(0,output["synName"])
        self.synFileNameEdit.grid(row=3,column=4,sticky="nw",pady=3)

        synTelAddLab = ttk.Label(self.editMeaningTL,text="telegram address").grid(row=4,column=3,padx=20,sticky="ne",pady=3)
        self.synTelAddEdit = ttk.Entry(self.editMeaningTL,width=40)
        self.synTelAddEdit.insert(0,output["synTelegramLink"])
        self.synTelAddEdit.grid(row=4,column=4,sticky="nw",pady=3)

        #  "deutsch","english","synonym","persian","meaningNumDaf","synTelegramLink","synName","engVoice","engName","engTelegramLink","perVoice","perName","perTelegramLink","deuVoice","deuName","deuTelegramLink","wordDetails","wordId","word","wordType","article"


        ## Persian
        # self.perMeaning,self.perFileName,self.perTelAdd,
        perisanLab = ttk.Label(self.editMeaningTL,text="perisan",font=("Arial",15,"bold")).grid(row=7,column=3,columnspan=2,sticky="s",pady=5)
        perMeaningLab = ttk.Label(self.editMeaningTL,text="meaning").grid(row=8,column=3,padx=20,sticky="ne",pady=3)
        self.perMeaningEdit = Text(self.editMeaningTL,width=30,height=5)
        self.perMeaningEdit.insert(1.0,output["persian"])
        self.perMeaningEdit.grid(row=8,column=4,sticky="nw",pady=3)

        perFileNameLab = ttk.Label(self.editMeaningTL,text="file name").grid(row=9,column=3,padx=20,sticky="ne",pady=3)
        self.perFileNameEdit = ttk.Entry(self.editMeaningTL,width=40)
        self.perFileNameEdit.insert(0,output["perName"])
        self.perFileNameEdit.grid(row=9,column=4,sticky="nw",pady=3)

        perTelAddLab = ttk.Label(self.editMeaningTL,text="telegram address").grid(row=10,column=3,padx=20,sticky="ne",pady=3)
        self.perTelAddEdit = ttk.Entry(self.editMeaningTL,width=40)
        self.perTelAddEdit.insert(0,output["perTelegramLink"])
        self.perTelAddEdit.grid(row=10,column=4,sticky="nw",pady=3)
        # space
        ttk.Label(self.editMeaningTL,text="").grid(row=11,column=5,pady=5)  
        #buttons
        btn_save = ttk.Button(self.editMeaningTL,command = self.warnEditMeaning,text="Save")
        btn_save.grid(row = 12,column=4,sticky="ne")


        btn_cancel = ttk.Button(self.editMeaningTL,command = self.editMeaningTL.destroy,text="Cancel")
        btn_cancel.grid(row = 12,column=5,sticky="nw")
        ttk.Label(self.editMeaningTL,text="edit meaning",font=("Arial",30,'bold')).grid(row=0,column=4,columnspan=2)
        ttk.Label(self.editMeaningTL,text="").grid(row=13,column=4,pady=2,padx=40)
        ttk.Label(self.editMeaningTL,text="").grid(row=13,column=5,padx=40)    



    def warnEditMeaning(self):
        meaningId = self.iidList[1]
        output = TE.Search().getMeaningValues(meaningId)
        # self.wordIn,self.editMeaningTL ,self.deuMeaningEdit,self.meaningNumDafEdit,self.deuFileNameEdit,self.deuTelAddEdit,self.engMeaningEdit,self.engFileNameEdit,self.engTelAddEdit,self.synMeaningEdit,self.synFileNameEdit,self.synTelAddEdit,self.perMeaningEdit,self.perFileNameEdit,self.perTelAddEdit = None ,None,None,None,None,None,None,None,None,None,None,None,None,None,None

        #  "deutsch","english","synonym","persian","meaningNumDaf","synTelegramLink","synName","engName","engTelegramLink","perName","perTelegramLink","deuName","deuTelegramLink","wordDetails","wordId","word","wordType","article"
        
        # warnSure = Toplevel(self.master)
        # print(f"self.deuMeaningEdit.get() ={self.deuMeaningEdit.get('1.0','end')} \noutput[deutsch] ={output['deutsch']}\nself.engFileNameEdit.get() = {self.engFileNameEdit.get()}\noutput[engName]={output['engName']}")
        if  (self.deuMeaningEdit.get("1.0","end").replace("\n","") == output["deutsch"] and 
            self.engMeaningEdit.get("1.0","end").replace("\n","") == output["english"]  and 
            self.synMeaningEdit.get("1.0","end").replace("\n","") == output["synonym"]  and
            self.perMeaningEdit.get("1.0","end").replace("\n","") == output["persian"]  and

            self.meaningNumDafEdit.get() == output["meaningNumDaf"]  and

            self.deuFileNameEdit.get() == output["deuName"]  and
            self.deuTelAddEdit.get() == output["deuTelegramLink"]  and

            self.engFileNameEdit.get() == output["engName"]  and            
            self.engTelAddEdit.get() == output["engTelegramLink"]  and

            self.synFileNameEdit.get() == output["synName"]  and
            self.synTelAddEdit.get() == output["synTelegramLink"]  and 

            self.perFileNameEdit.get() == output["perName"]  and
            self.perTelAddEdit.get() == output["perTelegramLink"]  ):

            warnEqual = Toplevel(self.master)
            ttk.Label(warnEqual,text = "!!!",font=('Arial',80,"bold")).grid(row=0,column=0,columnspan=1,padx = 30)

            labelWin = ttk.Label(warnEqual,text = "You didn't do any edition!",font=('Arial',12,"bold"))
            labelWin.grid(row = 2,column=0,columnspan=1,padx = 30)

            btn_Ok = ttk.Button(warnEqual,command = warnEqual.destroy,text="Ok")
            btn_Ok.grid(row = 3,column=0,columnspan=1)
            ttk.Label(warnEqual,text = "").grid(row = 4,column=0,columnspan=1,pady = 1)
        else:
            self.warnSureEdition = Toplevel(self.master)
            
            labelWin = ttk.Label(self.warnSureEdition,text = "❗❓",font=('Arial',80,"bold")).grid(row=1,column=3,rowspan=3,columnspan=2,sticky="nw")

            wordLabel = ttk.Label(self.warnSureEdition,text = f"Word :{output['word']}").grid(row=1,column=1,sticky="nw",padx = 20)


            wordTypeLabel = ttk.Label(self.warnSureEdition,text = f"deutsch meaning : {output['deutsch']}",wraplength=200 ).grid(row=2,column=1,sticky="nw",padx = 20)
            

            msg = ttk.Label(self.warnSureEdition,text = f"Are you sure to save this edition meaning !?",font=('Arial',15,"bold")).grid(row=4,column=1,columnspan=4,padx=20)
            # ,sticky="nw"
            btn_yesEdit = ttk.Button(self.warnSureEdition,command = self.saveMeaningEdit,text="Yes")
            btn_yesEdit.grid(row = 5,column=3,sticky="nw")

            btn_noEdit = ttk.Button(self.warnSureEdition,command = self.warnSureEdition.destroy,text="No")
            btn_noEdit.grid(row = 5,column=4,sticky="nw")
            ttk.Label(self.warnSureEdition,text = "").grid(row=5,column=0,columnspan=3,pady=1,padx=40)

    def saveMeaningEdit(self):
        # ,meaningId,deutsch=None,english=None,synonym=None,persian=None,meaningNumDaf=None,synName=None,synTelegramLink=None,engName=None,engTelegramLink=None,perName=None,perTelegramLink=None,deuName=None,deuTelegramLink=None):
        # print(f"self.deuFileNameEdit.get() = {self.deuFileNameEdit.get()}")
        meaningId = self.iidList[1]
        outputMVals = TE.Search().getMeaningValues(meaningId)
        output = TE.Editing().editMeaning(meaningId,deutsch=self.deuMeaningEdit.get("1.0","end").replace("\n",""),english=self.engMeaningEdit.get("1.0","end").replace("\n",""),synonym=self.synMeaningEdit.get("1.0","end").replace("\n",""),persian=self.perMeaningEdit.get("1.0","end").replace("\n",""),meaningNumDaf=self.meaningNumDafEdit.get(),synName=self.synFileNameEdit.get(),synTelegramLink=self.synTelAddEdit.get(),engName=self.engFileNameEdit.get(),engTelegramLink=self.engTelAddEdit.get(),perName=self.perFileNameEdit.get(),perTelegramLink=self.perTelAddEdit.get(),deuName=self.deuFileNameEdit.get(),deuTelegramLink=self.deuTelAddEdit.get())
        if output is True:
            self.editMeaningTL.destroy()
            self.warnSureEdition.destroy()
            doneMsg = Toplevel(self.master)
            
            labelWin = ttk.Label(doneMsg,text = "✅",font=('Arial',80,"bold")).grid(row=1,column=3,rowspan=3,columnspan=2,sticky="nw")

            wordLabel = ttk.Label(doneMsg,text = f"Word :{outputMVals['word']}").grid(row=1,column=1,sticky="nw",padx = 20)


            wordTypeLabel = ttk.Label(doneMsg,text = f"deutsch meaning : {outputMVals['deutsch']}",wraplength=200 ).grid(row=2,column=1,sticky="nw",padx = 20)
            

            msg = ttk.Label(doneMsg,text = f"edition Meaning Entered To DB !?",font=('Arial',15,"bold")).grid(row=3,column=1,columnspan=4,padx=20)
            # ,sticky="nw"
            btn_ok = ttk.Button(doneMsg,command = doneMsg.destroy,text="Ok")
            btn_ok.grid(row = 4,column=0,columnspan=3)

            ttk.Label(doneMsg,text = "").grid(row=5,column=0,columnspan=3,pady=1,padx=40)

        




    def newMeaning(self):
        # self.newMeaningChild ,self.deuMeaning,self.meaningNumDaf,self.deuFileName,self.deuTelAdd,self.engMeaning,self.engFileName,self.engTelAdd,self.synMeaning,self.synFileName,self.synTelAdd,self.perMeaning,self.perFileName,self.perTelAdd


        wordId = self.iidList[0]
        # print(f"wordId = {wordId}")
        # print(f"TE.Search.test = {TE.Search().test}")
        output = TE.Search().getWordValues(wordId)  
        # self.newMeaningChild ,self.deuMeaning,self.meaningNumDaf,self.deuFileName,self.deuTelAdd,self.engMeaning,,,,
        self.wordIn = output['word']

        self.newMeaningChild=Toplevel(self.master)
        wordlab = ttk.Label(self.newMeaningChild,text=f"Word : {output['word']}",font=("Arial",10,"bold")).grid(row=0,column=0,padx=20,sticky="nw",columnspan=2)

        deutschLab = ttk.Label(self.newMeaningChild,text="deutsch",font=("Arial",15,"bold")).grid(row=1,column=0,padx=20,columnspan=2,pady=5)

        deuMeaningLab = ttk.Label(self.newMeaningChild,text="meaning").grid(row=2,column=0,padx=20,sticky="ne",pady=3)
        self.deuMeaning = Text(self.newMeaningChild,width=30,height=5)
        self.deuMeaning.grid(row=2,column=1,sticky="nw",pady=3)

        meaningNumDafLab = ttk.Label(self.newMeaningChild,text="meaning Num Daf").grid(row=3,column=0,padx=20,sticky="ne",pady=3)
        self.meaningNumDaf = ttk.Entry(self.newMeaningChild,width=40)
        self.meaningNumDaf.grid(row=3,column=1,sticky="nw",pady=3)

        deuFileNameLab = ttk.Label(self.newMeaningChild,text="file name").grid(row=4,column=0,padx=20,sticky="ne",pady=3)
        self.deuFileName = ttk.Entry(self.newMeaningChild,width=40)
        self.deuFileName.grid(row=4,column=1,sticky="nw",pady=3)

        deuTelAddLab = ttk.Label(self.newMeaningChild,text="telegram address").grid(row=5,column=0,padx=20,sticky="ne",pady=3)
        self.deuTelAdd = ttk.Entry(self.newMeaningChild,width=40)
        self.deuTelAdd.insert(0,"https://t.me/guew_resource/")
        self.deuTelAdd.grid(row=5,column=1,sticky="nw",pady=3)



        ##

        de = StringVar()
        ## english
        # self.engMeaning,self.engFileName,self.engTelAdd
        englishLab = ttk.Label(self.newMeaningChild,text="english",font=("Arial",15,"bold")).grid(row=7,column=0,columnspan=2,sticky="s",pady=5)
        engMeaningLab = ttk.Label(self.newMeaningChild,text="meaning").grid(row=8,column=0,padx=20,sticky="ne",pady=3)
        self.engMeaning = Text(self.newMeaningChild,width=30,height=5)
        self.engMeaning.grid(row=8,column=1,sticky="nw",pady=3)

        engFileNameLab = ttk.Label(self.newMeaningChild,text="file name").grid(row=9,column=0,padx=20,sticky="ne",pady=3)
        self.engFileName = ttk.Entry(self.newMeaningChild,width=40)
        self.engFileName.grid(row=9,column=1,sticky="nw",pady=3)

        engTelAddLab = ttk.Label(self.newMeaningChild,text="telegram address").grid(row=10,column=0,padx=20,sticky="ne",pady=3)
        self.engTelAdd = ttk.Entry(self.newMeaningChild,width=40)
        self.engTelAdd.insert(0,"https://t.me/guew_resource/")
        self.engTelAdd.grid(row=10,column=1,sticky="nw",pady=3)


        ## Synonym
        # self.synMeaning,self.synFileName,self.synTelAdd
        synonymLab = ttk.Label(self.newMeaningChild,text="synonym",font=("Arial",15,"bold")).grid(row=1,column=2,columnspan=2,sticky="s",pady=5)
        synMeaningLab = ttk.Label(self.newMeaningChild,text="meaning").grid(row=2,column=3,padx=20,sticky="ne",pady=3)
        self.synMeaning = Text(self.newMeaningChild,width=30,height=5)
        self.synMeaning.grid(row=2,column=4,sticky="nw",pady=3)

        synFileNameLab = ttk.Label(self.newMeaningChild,text="file name").grid(row=3,column=3,padx=20,sticky="ne",pady=3)
        self.synFileName = ttk.Entry(self.newMeaningChild,width=40)
        self.synFileName.grid(row=3,column=4,sticky="nw",pady=3)

        synTelAddLab = ttk.Label(self.newMeaningChild,text="telegram address").grid(row=4,column=3,padx=20,sticky="ne",pady=3)
        self.synTelAdd = ttk.Entry(self.newMeaningChild,width=40)
        self.synTelAdd.insert(0,"https://t.me/guew_resource/")
        self.synTelAdd.grid(row=4,column=4,sticky="nw",pady=3)

        ## Persian
        # self.perMeaning,self.perFileName,self.perTelAdd,
        perisanLab = ttk.Label(self.newMeaningChild,text="perisan",font=("Arial",15,"bold")).grid(row=7,column=2,columnspan=2,sticky="s",pady=5)
        perMeaningLab = ttk.Label(self.newMeaningChild,text="meaning").grid(row=8,column=3,padx=20,sticky="ne",pady=3)
        self.perMeaning = Text(self.newMeaningChild,width=30,height=5)
        self.perMeaning.grid(row=8,column=4,sticky="nw",pady=3)

        perFileNameLab = ttk.Label(self.newMeaningChild,text="file name").grid(row=9,column=3,padx=20,sticky="ne",pady=3)
        self.perFileName = ttk.Entry(self.newMeaningChild,width=40)
        self.perFileName.grid(row=9,column=4,sticky="nw",pady=3)

        perTelAddLab = ttk.Label(self.newMeaningChild,text="telegram address").grid(row=10,column=3,padx=20,sticky="ne",pady=3)
        self.perTelAdd = ttk.Entry(self.newMeaningChild,width=40)
        self.perTelAdd.insert(0,"https://t.me/guew_resource/")
        self.perTelAdd.grid(row=10,column=4,sticky="nw",pady=3)
        #buttons
        btn_save = ttk.Button(self.newMeaningChild,command = self.saveNewMeaning,text="Save")
        btn_save.grid(row = 11,column=4)


        btn_cancel = ttk.Button(self.newMeaningChild,command = self.newMeaningChild.destroy,text="Cancel")
        btn_cancel.grid(row = 11,column=5)
        ttk.Label(self.newMeaningChild,text="new meaning",font=("Arial",30,'bold')).grid(row=0,column=4,columnspan=2)
        ttk.Label(self.newMeaningChild,text="").grid(row=12,column=4,pady=10)

    def saveNewMeaning(self):

        wordId = self.iidList[0]
        output = TE.Search().getWordValues(wordId)  

        deutsch = self.deuMeaning.get("1.0","end").replace("\n","")
        word=output["word"]
        wordType=output["wordType"]
        article= output["article"]

        meaningNumDaf = self.meaningNumDaf.get()
        deuName = self.deuFileName.get()
        deuTelegramLink = self.deuTelAdd.get()

        english = self.engMeaning.get("1.0","end").replace("\n","")
        engName = self.engFileName.get()
        engTelegramLink = self.engTelAdd.get()

        synonym = self.synMeaning.get("1.0","end").replace("\n","")
        synName = self.synFileName.get()
        synTelegramLink = self.synTelAdd.get()

        persian = self.perMeaning.get("1.0","end").replace("\n","")
        perName = self.perFileName.get()
        perTelegramLink = self.perTelAdd.get()

        


        if deutsch=="" or deutsch==None or deutsch == " " or len(deutsch)==1:
           d = ttk.Label(self.newMeaningChild,text="*",font=("Arial",20,"bold"))
           d.grid(row=2,column=2,sticky="nw",pady=3)
           d.config(foreground="red")
        else:
            TE.Entering().enterNewChildMeaning(wordId,deutsch,word, wordType=wordType,article=article,meaningNumDaf=meaningNumDaf,deuName=deuName,deuTelegramLink=deuTelegramLink,english=english,engName=engName,engTelegramLink=engTelegramLink,synonym=synonym,synName=synName,synTelegramLink=synTelegramLink,persian=persian,perName=perName,perTelegramLink=perTelegramLink)
            msg=Toplevel(self.master)
            tik=ttk.Label(msg,text="✅",font=("Arial",40,"bold")).grid(row=1,column=2,padx=20,columnspan=2,rowspan=3)
            wordlb = ttk.Label(msg,text=f"Word : {word}").grid(row=1,column=1,padx=20)
            deuMeaning = ttk.Label(msg,text=f"deutsch Meaning : {deutsch}").grid(row=2,column=1,padx=20)
            msgEnterd = ttk.Label(msg,text=f"new Meaning Enterd to DB!",font=("Arial",15,"bold")).grid(row=3,column=1,padx=20)
            btn_ok = ttk.Button(msg,text="Ok",command=msg.destroy).grid(row=4,column=1,columnspan=2) 
            self.newMeaningChild.destroy()
            self.search_btn()


        
    def editWord(self):
        wordId = self.iidList[0]
        # print(f"wordId = {wordId}")
        # print(f"TE.Search.test = {TE.Search().test}")
        output = TE.Search().getWordValues(wordId)  

        # fieldList = ["wordId","word","wordType","article","wordVoiceName","wordtelegramLink"]
        self.editNdelWindow= Toplevel(self.master)
        labelWin = ttk.Label(self.editNdelWindow,text = "Edit Word",font=('Arial',25,"bold")).grid(row=0,column=3,columnspan=2,rowspan=3)
        # wordEntry,wordTypeEntry,articleEntry,voiceNameEntry,telegramAddressEntry
        wordLabel = ttk.Label(self.editNdelWindow,text = "Word").grid(row=1,column=0,sticky="nw", padx = 20)
        self.wordEntry =ttk.Entry(self.editNdelWindow,width=30)
        self.wordEntry.insert(0,output["word"])
        self.wordEntry.grid(row=2,column=0, padx = 20)

        wordTypeLabel = ttk.Label(self.editNdelWindow,text = "Word Type").grid(row=4,column=0,sticky="nw", padx = 20)
        self.wordTypeEntry =ttk.Entry(self.editNdelWindow,width=30)
        self.wordTypeEntry.insert(0,output["wordType"])
        self.wordTypeEntry.grid(row=5,column=0, padx = 20)

        articleLabel = ttk.Label(self.editNdelWindow,text = "article").grid(row=7,column=0,sticky="nw", padx = 20)
        self.articleEntry =ttk.Entry(self.editNdelWindow,width=10)
        self.articleEntry.insert(0,output["article"])
        self.articleEntry.grid(row=8,column=0,sticky="nw", padx = 20)


        voiceNameLabel = ttk.Label(self.editNdelWindow,text = "voice name").grid(row=10,column=0,sticky="nw", padx = 20)
        self.voiceNameEntry =ttk.Entry(self.editNdelWindow,width=30)
        self.voiceNameEntry.insert(0,output["wordVoiceName"])
        self.voiceNameEntry.grid(row=11,column=0, padx = 20)

        telegramAddressLabel = ttk.Label(self.editNdelWindow,text = "word telegram Link").grid(row=13,column=0,sticky="nw", padx = 20)
        self.telegramAddressEntry =ttk.Entry(self.editNdelWindow,width=30)
        self.telegramAddressEntry.insert(0,output["wordtelegramLink"])
        self.telegramAddressEntry.grid(row=14,column=0, padx = 20)
        
        btn_save = ttk.Button(self.editNdelWindow,command = self.warnEditedWord,text="Save")
        btn_save.grid(row = 15,column=3)
        # self.frame2.bind("<Enter>",btn_search)

        btn_cancel = ttk.Button(self.editNdelWindow,command = self.editNdelWindow.destroy,text="Cancel")
        btn_cancel.grid(row = 15,column=4)


    def deleteWordMenu(self):
        wordId = self.iidList[0]
        # self.deleteWindow,self.wordContent,self.wordTypeContent,self.articleContent,self.voiceNameContent,self.telegramAddressContent
        # fieldList = ["wordId","word","wordType","article","wordVoiceName","wordtelegramLink"]
        output = TE.Search().getWordValues(wordId) 
        self.deleteWindow= Toplevel(self.master)
        self.wordVal = output["word"]
        labelWin = ttk.Label(self.deleteWindow,text = "Delete Word",font=('Arial',20,"bold")).grid(row=0,column=3,rowspan=3,sticky="nw")
        # wordEntry,wordTypeEntry,articleEntry,voiceNameEntry,telegramAddressEntry
        wordLabel = ttk.Label(self.deleteWindow,text = "Word :").grid(row=0,column=1,sticky="nw",padx = 20)
        wordContent =ttk.Label(self.deleteWindow,width=30,text = output["word"]).grid(row=0,column=2,sticky="nw")

        wordTypeLabel = ttk.Label(self.deleteWindow,text = "Word Type :").grid(row=2,column=1,sticky="nw",padx = 20)
        wordTypeContent =ttk.Label(self.deleteWindow,text = output["wordType"]).grid(row=2,column=2,sticky="nw")

        articleLabel = ttk.Label(self.deleteWindow,text = "article :").grid(row=4,column=1,sticky="nw",padx = 20)
        # self.articleContent =ttk.Entry(self.deleteWindow,width=10)
        articleContent = ttk.Label(self.deleteWindow,text = output["article"]).grid(row=4,column=2,sticky="nw")


        voiceNameLabel = ttk.Label(self.deleteWindow,text = "voice name :").grid(row=6,column=1,sticky="nw",padx = 20)
        voiceNameContent =ttk.Label(self.deleteWindow,width=30,text = output["wordVoiceName"]).grid(row=6,column=2,sticky="nw")

        telegramAddressLabel = ttk.Label(self.deleteWindow,text = "telegram address :").grid(row=8,column=1,sticky="nw",padx = 20)
        telegramAddressContent =ttk.Label(self.deleteWindow,width=30,text = output["wordtelegramLink"]).grid(row=8,column=2,sticky="nw")

        msg = ttk.Label(self.deleteWindow,text = f"Are you sure to Delete This word ( {output['word']} ) !?",font=('Arial',15,"bold")).grid(row=11,column=1,columnspan=3,sticky="nw")

        btn_yesDelete = ttk.Button(self.deleteWindow,command = self.deleteWord,text="Yes")
        btn_yesDelete.grid(row = 13,column=1)
        # self.frame2.bind("<Enter>",btn_search)

        btn_noDelete = ttk.Button(self.deleteWindow,command = self.deleteWindow.destroy,text="No")
        btn_noDelete.grid(row = 13,column=2)

    def deletedWordMag(self):
        msg = Toplevel(self.master)
        wordId = self.iidList[0]

        
        # wordEntry,wordTypeEntry,articleEntry,voiceNameEntry,telegramAddressEntry
        wordLabel = ttk.Label(msg,text = f"Word :{self.wordVal}").grid(row=0,column=1,sticky="nw",padx = 20,rowspan=3,pady = 20)

        labelWin = ttk.Label(msg,text = "✅",font=('Arial',60,"bold")).grid(row=0,column=2,rowspan=3,sticky="nw")

        msgDeleted = ttk.Label(msg,text = f"The Word ( {self.wordVal} ) is Deleted !",font=('Arial',15,"bold")).grid(row=5,column=1,sticky="nswe",columnspan=2)

        btn_OkDelete = ttk.Button(msg,command = msg.destroy,text="Ok")
        btn_OkDelete.grid(row = 7,column=1,columnspan=2)
        # self.frame2.bind("<Enter>",btn_search)

        # btn_noDelete = ttk.Button(msg,command = msg.destroy,text="No")
        # btn_noDelete.grid(row = 13,column=2)

    def deleteWord(self):
        wordId = self.iidList[0]
        TE.Deleting().deleteWord(wordId)
        self.deleteWindow.destroy()
        self.deletedWordMag()
        # self.treeViewSearchSimple.destroy()
        self.search_btn()

    def warnEditedWord(self):
        wordId = self.iidList[0]
        word = self.wordEntry.get()
        wordType = self.wordTypeEntry.get()
        article = self.articleEntry.get()
        voiceName = self.voiceNameEntry.get()
        telegramAddress = self.telegramAddressEntry.get()
        self.msgWarnEditedWord = Toplevel(self.master)
        ttk.Label(self.msgWarnEditedWord,text="❗❓",font=("Arial",60,"bold")).grid(row =1,column =2,rowspan=6,padx=20)
        wordlab = ttk.Label(self.msgWarnEditedWord,text=f"word = {word}").grid(row = 1,column =1,sticky="nw",padx=20)
        wordTypelab = ttk.Label(self.msgWarnEditedWord,text=f"wordType = {wordType}").grid(row = 2,column =1,sticky="nw",padx=20)
        articlelab = ttk.Label(self.msgWarnEditedWord,text=f"article = {article}").grid(row = 3,column =1,sticky="nw",padx=20)
        voiceNamelab = ttk.Label(self.msgWarnEditedWord,text=f"voice name = {voiceName}").grid(row = 4,column =1,sticky="nw",padx=20)
        telegramAddresslab = ttk.Label(self.msgWarnEditedWord,text=f"telegram Address = {telegramAddress}").grid(row = 5,column =1,sticky="nw",padx=20)
        ttk.Label(self.msgWarnEditedWord,text="").grid(row = 6,column =1,sticky="nw",pady=5)

        msgWarn = ttk.Label(self.msgWarnEditedWord,text=f"Are you sure about  {word} edition to save?",font=("Arial",10,"bold")).grid(row = 7,column =1,sticky="nw",padx=20,pady=10,columnspan=2)

        btn_yes = ttk.Button(self.msgWarnEditedWord,command = self.saveEditedWord,text="Save")
        #,font=('Arial',10,"bold")
        btn_yes.grid(row = 8,column=1,sticky="ne",padx=5,pady=5)
        # self.frame2.bind("<Enter>",btn_search)

        btn_no = ttk.Button(self.msgWarnEditedWord,command = self.msgWarnEditedWord.destroy,text="Cancel")
        btn_no.grid(row = 8,column=2,sticky="nw",padx=5,pady=5)
        
        

    def saveEditedWord(self):
        self.msgWarnEditedWord.destroy()
        
        wordId = self.iidList[0]
        word = self.wordEntry.get()
        wordType = self.wordTypeEntry.get()
        article = self.articleEntry.get()
        voiceName = self.voiceNameEntry.get()
        telegramAddress = self.telegramAddressEntry.get()

        msg = Toplevel(self.master)
        wordlab = ttk.Label(msg,text=f"word = {word}").grid(row = 1,column =1)
        wordTypelab = ttk.Label(msg,text=f"wordType = {wordType}").grid(row = 2,column =1)
        articlelab = ttk.Label(msg,text=f"article = {article}").grid(row = 3,column =1)
        voiceNamelab = ttk.Label(msg,text=f"voice Name = {voiceName}").grid(row = 4,column =1)
        telegramAddresslab = ttk.Label(msg,text=f"telegram Address = {telegramAddress}").grid(row = 5,column =1)
        msgWarn = ttk.Label(msg,text=f"Edition saved !",font=("Arial",15,"bold")).grid(row = 6,column =1)

        btn_ok = ttk.Button(msg,command = msg.destroy,text="Ok")
        btn_ok.grid(row = 7,column=1)
        tik=ttk.Label(msg,text="✅",font=("Arial",60,"bold")).grid(row=1,column=2,padx=20,rowspan=3)


        output = TE.Editing().editWord(wordId,word,wordType,article,voiceName,telegramAddress)
        print(f"output = {output}")
        self.editNdelWindow.destroy()
        

    def spliterIid(self,iid):
        lengthSplit = 24
        output = [iid[i: i + lengthSplit] for i in range(0, len(iid), lengthSplit)]
        return output
    def enter_btn(self):
        # wordId=TE.Entering().enterNewWord(word,wordType=None,article=None,voiceName=None,telegramLink=None,meaningId=None)
        # meaningId = TE.Entering().enterNewChildMeaning(wordId,deutsch,word, wordType=None,article=None,meaningNumDaf=None,deuName=None,deuTelegramLink=None,english=None,engName=None,engTelegramLink=None,synonym=None,synName=None,synTelegramLink=None,persian=None,perName=None,perTelegramLink=None)
        # bookId=Entering().enterNewBook(meaningId,bookName,chapter=None,content=None,page=None,lesson=None,publisher=None,word=None)
        inVal = self.w.get()
        # print(f"inVal = {inVal}")
        condition = {"_id":ObjectId("5f2d10763bc8917574621eed")}
        valFind = None
        for col in self.obj_db.test.find(condition,{"size":1,"_id":0}):
            for keys in col.keys():
                valFind = col[keys]
        # print(f"valFind = {valFind}")
        updatedVal = {"size":inVal}
        # self.obj_Db.bookCollection.update_many(condition,{"$set":updateFilNVal})
        self.obj_db.test.update_many(condition,{"$set":updatedVal})




    def report(self):
        pass

def main():
    root = Tk()
    
    feedback = Feedback(root)
    # feedback.entering()
    # feedback.search()
    # feedback.advanceSearch()
    # feedback.report()

    root.mainloop()

if __name__ == "__main__":main()
@pytest.fixture
def feedback():
    # root = Tk().call('wm', 'attributes', '.', '-topmost', '1')
    root = Tk()
    feedback=Feedback(root)
    return feedback
class TestFeedback:
    pass
# d = "5f30077014082a0f00465048"
# c= "5f30077014082a0f004650485dc5c380ec972f0ee087361d"
# # 5dc5c380ec972f0ee087361d
# xx = "5f30077014082a0f004650485dc5c380ec972f0ee087361d5da7467a6c8002022619ea05"
    @pytest.mark.parametrize("iid",[
        ("5f30077014082a0f00465048"),
        ("5f30077014082a0f004650485dc5c380ec972f0ee087361d"),
        ("5f30077014082a0f004650485dc5c380ec972f0ee087361d5da7467a6c8002022619ea05")
    ])
    def test_spliterIid(self,feedback,iid):
        output = feedback.spliterIid(iid)
        assert isinstance(output,list)
        # print(f"iid = {iid}")
        if len(iid)==24:
            assert len(output)==1
            # print(f"iid 24 = {iid}")
        elif len (iid)>24 and len(iid)<49:
            assert len(output)==2
            # print(f"iid >24 nad iid<49 = {iid}")
        elif len(iid)>48:
            # print(f"iid >48 = {iid}")
            assert len(output)==3

    @pytest.mark.parametrize("iid",[
        ("5f30077014082a0f00465048"),
        ("5f30077014082a0f004650485dc5c380ec972f0ee087361d"),
        ("5f30077014082a0f004650485dc5c380ec972f0ee087361d5da7467a6c8002022619ea05")
    ])   
    def test_menuItems(self,feedback,iid):
        output = feedback.menuItems(iid)
        # print(output)
        assert isinstance(output,tkinter.Menu)
    # @pytest.mark.parametrize("event",[
    #     ({"event":{ "state":"Mod1","num":3 ,"x":80,"y":76}}),
    #     ({ "state":"Mod1", "num":3 ,"x":67 ,"y":39}),
    #     ({ "state":"Mod1", "num":3 ,"x":61 ,"y":55})
    # ])
    # def test_do_popup(self,feedback,event):
    #     event.x = 43
    #    print(event.x)
    #    iid,menu = feedback.do_popup(event)
    #    print(f"iid = {iid}")
    #    print(f"type(iid) = {type(iid)}") 
    #    print(f"type(menu) = {type(menu)}")


    @pytest.mark.parametrize("meaningId",[
        ("5dc5c380ec972f0ee087361d"),
        ("5dc5c4fdec972f0ee087361e"),
        ("5dc5c512ec972f0ee087361f"),
        ("5dc5c516ec972f0ee0873620"),
        ("5dc5c518ec972f0ee0873621")
    ])
    def test_warnEditMeaning(self,feedback,meaningId):

        #  "deutsch","english","synonym","persian","meaningNumDaf","synVoice","synName","synName","engVoice","engName","engTelegramLink","perVoice","perName","perTelegramLink","deuVoice","deuName","deuTelegramLink","wordDetails","wordId","word","wordType","article"

        output = TE.Search().getMeaningValues(meaningId) 
        

        feedback.editMeaningTL=Toplevel(feedback.master)
        wordlab = ttk.Label(feedback.editMeaningTL,text=f"Word : {output['word']}",font=("Arial",10,"bold")).grid(row=0,column=0,padx=20,sticky="nw",columnspan=2)

        deutschLab = ttk.Label(feedback.editMeaningTL,text="deutsch",font=("Arial",15,"bold")).grid(row=1,column=0,padx=20,columnspan=2,pady=5)

        deuMeaningLab = ttk.Label(feedback.editMeaningTL,text="meaning").grid(row=2,column=0,padx=20,sticky="ne",pady=3)
        feedback.deuMeaningEdit = Text(feedback.editMeaningTL,width=30,height=5)
        feedback.deuMeaningEdit.insert(1.0,output["deutsch"])
        feedback.deuMeaningEdit.grid(row=2,column=1,sticky="nw",pady=3)

        meaningNumDafLab = ttk.Label(feedback.editMeaningTL,text="meaning Num Daf").grid(row=3,column=0,padx=20,sticky="ne",pady=3)
        feedback.meaningNumDafEdit = ttk.Entry(feedback.editMeaningTL,width=40)
        feedback.meaningNumDafEdit.insert(0,output["meaningNumDaf"])
        feedback.meaningNumDafEdit.grid(row=3,column=1,sticky="nw",pady=3)

        deuFileNameLab = ttk.Label(feedback.editMeaningTL,text="file name").grid(row=4,column=0,padx=20,sticky="ne",pady=3)
        feedback.deuFileNameEdit = ttk.Entry(feedback.editMeaningTL,width=40)
        feedback.deuFileNameEdit.insert(0,output["deuName"])
        feedback.deuFileNameEdit.grid(row=4,column=1,sticky="nw",pady=3)

        deuTelAddLab = ttk.Label(feedback.editMeaningTL,text="telegram address").grid(row=5,column=0,padx=20,sticky="ne",pady=3)
        feedback.deuTelAddEdit = ttk.Entry(feedback.editMeaningTL,width=40)
        feedback.deuTelAddEdit.insert(0,output["deuTelegramLink"])
        feedback.deuTelAddEdit.grid(row=5,column=1,sticky="nw",pady=3)

        #  "deutsch","english","synonym","persian","meaningNumDaf","synVoice","synName","synName","engVoice","engName","engTelegramLink","perVoice","perName","perTelegramLink","deuVoice","deuName","deuTelegramLink","wordDetails","wordId","word","wordType","article"

        ##

        # de = StringVar()
        ## english
        # self.engMeaning,self.engFileName,self.engTelAdd
        englishLab = ttk.Label(feedback.editMeaningTL,text="english",font=("Arial",15,"bold")).grid(row=7,column=0,columnspan=2,sticky="s",pady=5)
        engMeaningLab = ttk.Label(feedback.editMeaningTL,text="meaning").grid(row=8,column=0,padx=20,sticky="ne",pady=3)
        feedback.engMeaningEdit = Text(feedback.editMeaningTL,width=30,height=5)
        feedback.engMeaningEdit.insert(1.0,output["english"])

        # self.deuMeaningEdit = Text(self.editMeaningTL,width=30,height=5)
        # self.deuMeaningEdit.insert(1.0,output["deutsch"])


        feedback.engMeaningEdit.grid(row=8,column=1,sticky="nw",pady=3)

        engFileNameLab = ttk.Label(feedback.editMeaningTL,text="file name").grid(row=9,column=0,padx=20,sticky="ne",pady=3)
        feedback.engFileNameEdit = ttk.Entry(feedback.editMeaningTL,width=40)
        feedback.engFileNameEdit.insert(0,output["engName"])
        feedback.engFileNameEdit.grid(row=9,column=1,sticky="nw",pady=3)

        engTelAddLab = ttk.Label(feedback.editMeaningTL,text="telegram address").grid(row=10,column=0,padx=20,sticky="ne",pady=3)
        feedback.engTelAddEdit = ttk.Entry(feedback.editMeaningTL,width=40)
        feedback.engTelAddEdit.insert(0,output["engTelegramLink"])
        feedback.engTelAddEdit.grid(row=10,column=1,sticky="nw",pady=3)

        #  "deutsch","english","synonym","persian","meaningNumDaf","synTelegramLink","synName","engVoice","engName","engTelegramLink","perVoice","perName","perTelegramLink","deuVoice","deuName","deuTelegramLink","wordDetails","wordId","word","wordType","article"


        ## Synonym
        # self.synMeaning,self.synFileName,self.synTelAdd
        synonymLab = ttk.Label(feedback.editMeaningTL,text="synonym",font=("Arial",15,"bold")).grid(row=1,column=2,columnspan=2,sticky="s",pady=5)
        synMeaningLab = ttk.Label(feedback.editMeaningTL,text="meaning").grid(row=2,column=3,padx=20,sticky="ne",pady=3)
        feedback.synMeaningEdit = Text(feedback.editMeaningTL,width=30,height=5)
        feedback.synMeaningEdit.insert(1.0,output["synonym"])
        feedback.synMeaningEdit.grid(row=2,column=4,sticky="nw",pady=3)

        synFileNameLab = ttk.Label(feedback.editMeaningTL,text="file name").grid(row=3,column=3,padx=20,sticky="ne",pady=3)
        feedback.synFileNameEdit = ttk.Entry(feedback.editMeaningTL,width=40)
        feedback.synFileNameEdit.insert(0,output["synName"])
        feedback.synFileNameEdit.grid(row=3,column=4,sticky="nw",pady=3)

        synTelAddLab = ttk.Label(feedback.editMeaningTL,text="telegram address").grid(row=4,column=3,padx=20,sticky="ne",pady=3)
        feedback.synTelAddEdit = ttk.Entry(feedback.editMeaningTL,width=40)
        feedback.synTelAddEdit.insert(0,output["synTelegramLink"])
        feedback.synTelAddEdit.grid(row=4,column=4,sticky="nw",pady=3)

        #  "deutsch","english","synonym","persian","meaningNumDaf","synTelegramLink","synName","engVoice","engName","engTelegramLink","perVoice","perName","perTelegramLink","deuVoice","deuName","deuTelegramLink","wordDetails","wordId","word","wordType","article"


        ## Persian
        # self.perMeaning,self.perFileName,self.perTelAdd,
        perisanLab = ttk.Label(feedback.editMeaningTL,text="perisan",font=("Arial",15,"bold")).grid(row=7,column=2,columnspan=2,sticky="s",pady=5)
        perMeaningLab = ttk.Label(feedback.editMeaningTL,text="meaning").grid(row=8,column=3,padx=20,sticky="ne",pady=3)
        feedback.perMeaningEdit = Text(feedback.editMeaningTL,width=30,height=5)
        feedback.perMeaningEdit.insert(1.0,output["persian"])
        feedback.perMeaningEdit.grid(row=8,column=4,sticky="nw",pady=3)

        perFileNameLab = ttk.Label(feedback.editMeaningTL,text="file name").grid(row=9,column=3,padx=20,sticky="ne",pady=3)
        feedback.perFileNameEdit = ttk.Entry(feedback.editMeaningTL,width=40)
        feedback.perFileNameEdit.insert(0,output["perName"])
        feedback.perFileNameEdit.grid(row=9,column=4,sticky="nw",pady=3)

        perTelAddLab = ttk.Label(feedback.editMeaningTL,text="telegram address").grid(row=10,column=3,padx=20,sticky="ne",pady=3)
        feedback.perTelAddEdit = ttk.Entry(feedback.editMeaningTL,width=40)
        feedback.perTelAddEdit.insert(0,output["perTelegramLink"])
        feedback.perTelAddEdit.grid(row=10,column=4,sticky="nw",pady=3)
        #buttons
        btn_save = ttk.Button(feedback.editMeaningTL,command = feedback.warnEditMeaning,text="Save")
        btn_save.grid(row = 11,column=4)


        btn_cancel = ttk.Button(feedback.editMeaningTL,command = feedback.editMeaningTL.destroy,text="Cancel")
        btn_cancel.grid(row = 11,column=5)
        ttk.Label(feedback.editMeaningTL,text="edit meaning",font=("Arial",30,'bold')).grid(row=0,column=4,columnspan=2)
        ttk.Label(feedback.editMeaningTL,text="").grid(row=12,column=4,pady=10)

        # self.wordIn,self.editMeaningTL ,self.deuMeaningEdit,self.meaningNumDafEdit,self.deuFileNameEdit,self.deuTelAddEdit,self.engMeaningEdit,self.engFileNameEdit,self.engTelAddEdit,self.synMeaningEdit,self.synFileNameEdit,self.synTelAddEdit,self.perMeaningEdit,self.perFileNameEdit,self.perTelAddEdit = None ,None,None,None,None,None,None,None,None,None,None,None,None,None,None

        #  "deutsch","english","synonym","persian","meaningNumDaf","synTelegramLink","synName","engName","engTelegramLink","perName","perTelegramLink","deuName","deuTelegramLink","wordDetails","wordId","word","wordType","article"
        
        # warnSure = Toplevel(self.master)
        # print(f"self.deuMeaningEdit.get() ={feedback.deuMeaningEdit.get('1.0','end')} \noutput[deutsch] ={output['deutsch']}\nself.engFileNameEdit.get() = {feedback.engFileNameEdit.get()}\noutput[engName]={output['engName']}")
        # print(f"output = {output}")
        valEd = feedback.deuMeaningEdit.get('1.0','end')
        valOut = output["deutsch"]
        print(f"feedback.deuMeaningEdit.get(1.0,end)={feedback.deuMeaningEdit.get('1.0','end')}\noutput[deutsch]={output['deutsch']}")
        diffEd = [ x for x in valEd  if x not in valOut]
        diffOut =[ x for x in valOut   if x not in valEd]
        # print(f"diffEd = {diffEd}")
        # print(f"diffOut = {diffOut}")
        assert feedback.deuMeaningEdit.get("1.0","end").replace("\n","")  == output["deutsch"]  
        assert feedback.engMeaningEdit.get("1.0","end").replace("\n","")  == output["english"]   
        assert feedback.synMeaningEdit.get("1.0","end").replace("\n","")  == output["synonym"]  
        assert feedback.perMeaningEdit.get("1.0","end").replace("\n","")  == output["persian"]  

        assert feedback.meaningNumDafEdit.get() == output["meaningNumDaf"]  

        assert feedback.deuFileNameEdit.get() == output["deuName"]  
        assert feedback.deuTelAddEdit.get() == output["deuTelegramLink"]  

        assert feedback.engFileNameEdit.get() == output["engName"]              
        assert feedback.engTelAddEdit.get() == output["engTelegramLink"]  

        assert feedback.synFileNameEdit.get() == output["synName"]  
        assert feedback.synTelAddEdit.get() == output["synTelegramLink"]  

        assert feedback.perFileNameEdit.get() == output["perName"]  
        assert feedback.perTelAddEdit.get() == output["perTelegramLink"]  




        # if  (self.deuMeaningEdit.get("1.0","end") == output["deutsch"] and 
        #     self.engMeaningEdit.get("1.0","end") == output["english"]  and 
        #     self.synMeaningEdit.get("1.0","end") == output["synonym"]  and
        #     self.perMeaningEdit.get("1.0","end") == output["persian"]  and

        #     self.meaningNumDafEdit.get() == output["meaningNumDaf"]  and

        #     self.deuFileNameEdit.get() == output["deuName"]  and
        #     self.deuTelAddEdit.get() == output["deuTelegramLink"]  and

        #     self.engFileNameEdit.get() == output["engName"]  and            
        #     self.engTelAddEdit.get() == output["engTelegramLink"]  and

        #     self.synFileNameEdit.get() == output["synName"]  and
        #     self.synTelAddEdit.get() == output["synTelegramLink"]  and 

        #     self.perFileNameEdit.get() == output["perName"]  and
        #     self.perTelAddEdit.get() == output["perTelegramLink"]  ):
        # if  (self.deuMeaningEdit.get("1.0","end") == output["deutsch"] and self.engMeaningEdit.get("1.0","end") == output["english"]  and self.synMeaningEdit.get("1.0","end") == output["synonym"]  and
        #     self.perMeaningEdit.get("1.0","end") == output["persian"]  and self.meaningNumDafEdit.get() == output["meaningNumDaf"]  and self.deuFileNameEdit.get() == output["deuName"]  and self.deuTelAddEdit.get() == output["deuTelegramLink"]  and self.engFileNameEdit.get() == output["engName"]  and self.engTelAddEdit.get() == output["engTelegramLink"]  and self.synFileNameEdit.get() == output["synName"]  and self.synTelAddEdit.get() == output["synTelegramLink"]  and  self.perFileNameEdit.get() == output["perName"]  and
        #     self.perTelAddEdit.get() == output["perTelegramLink"] ):


        #     # pass
        #     warnEqual = Toplevel(self.master)
        #     ttk.Label(warnEqual,text = "!?",font=('Arial',20,"bold")).grid(row=0,column=2,sticky="nw")

        #     labelWin = ttk.Label(warnEqual,text = "You didn't any edition!",font=('Arial',12,"bold"))
        #     labelWin.grid(row = 2,column=1)

        #     btn_Ok = ttk.Button(warnEqual,command = warnEqual.destroy,text="Ok")
        #     btn_Ok.grid(row = 3,column=1)