import pytest
from test_entering import Db as db
from bson.objectid import ObjectId

@pytest.fixture(scope="module")
def word1():
    word = "test1"
    wordType = "wordType1"
    article = "article1"
    voiceName = "voiceName1"
    telegramLink = "telegramLink1"
    meaningId = ["meaningId1"]
    yield word,wordType,article,voiceName,telegramLink,meaningId  

@pytest.fixture(scope="module")
def word2():
    word = "test2"
    wordType = "wordType2"
    article = "article2"
    voiceName = "voiceName2"
    telegramLink = "telegramLink2"
    meaningId = ["meaningId2"]
    yield word,wordType,article,voiceName,telegramLink,meaningId  

@pytest.fixture(scope="module")
def word3():
    word = "test3"
    wordType = "wordType3"
    article = "article3"
    voiceName = "voiceName3"
    telegramLink = "telegramLink3"
    meaningId = ["meaningId3"]
    yield word,wordType,article,voiceName,telegramLink,meaningId  


@pytest.fixture(scope="module")
def word4():
    word = "test4"
    wordType = "wordType4"
    article = "article1"
    voiceName = "voiceName4"
    telegramLink = "telegramLink4"
    meaningId = ["meaningId4"]

    yield word,wordType,article,voiceName,telegramLink,meaningId  

@pytest.fixture(scope="module")
def word5():
    word = "test5"
    wordType = "wordType5"
    article = "article5"
    voiceName = "voiceName5"
    telegramLink = "telegramLink5"
    meaningId = ["meaningId5"]
    yield word,wordType,article,voiceName,telegramLink,meaningId  

@pytest.fixture(scope="module")
def wordValues(word1,word2,word3,word4,word5):
    yield {"word1":word1,"word2":word2,"word3":word3,"word4":word4,"word5":word5}

@pytest.fixture(scope="module")
def meaning1():
    deutsch="deutsch1"
    english="english1"
    synonym="synonym1"
    persian="persian1"
    meaningNumDaf=1
    synName="synName1"
    synTelegramLink = "synTelegramLink1"
    perName = "perName1"
    perTelegramLink= "perTelegramLink1"
    deuName="deuName1"
    deuTelegramLink = "deuTelegramLink1"
    engName = "engName1"
    engTelegramLink= "engTelegramLink1"
    wordDetails = {"wordId":ObjectId("5f37b413d3ddcf7a235c24a3"),"word":"word1","wordType":"wordType1","article":"article1"}
    yield deutsch,english,synonym,persian,meaningNumDaf,synName,synTelegramLink,perName,perTelegramLink,deuName,deuTelegramLink,engName,engTelegramLink,wordDetails

@pytest.fixture(scope="module")
def meaning2():
    deutsch="deutsch2"
    english="english2"
    synonym="synonym2"
    persian="persian2"
    meaningNumDaf=1
    synName="synName2"
    synTelegramLink = "synTelegramLink2"
    perName = "perName2"
    perTelegramLink= "perTelegramLink2"
    deuName="deuName2"
    deuTelegramLink = "deuTelegramLink2"
    engName = "engName2"
    engTelegramLink= "engTelegramLink2"
    wordDetails = {"wordId":ObjectId("5f37b3f4d3ddcf7a235c24a2"),"word":"word2","wordType":"wordType2","article":"article2"}
    yield deutsch,english,synonym,persian,meaningNumDaf,synName,synTelegramLink,perName,perTelegramLink,deuName,deuTelegramLink,engName,engTelegramLink,wordDetails

@pytest.fixture(scope="module")
def meaning3():
    deutsch="deutsch3"
    english="english3"
    synonym="synonym3"
    persian="persian3"
    meaningNumDaf=1
    synName="synName3"
    synTelegramLink = "synTelegramLink3"
    perName = "perName3"
    perTelegramLink= "perTelegramLink3"
    deuName="deuName3"
    deuTelegramLink = "deuTelegramLink3"
    engName = "engName3"
    engTelegramLink= "engTelegramLink3"
    wordDetails = {"wordId":ObjectId("5f37b3d8d3ddcf7a235c24a1"),"word":"word3","wordType":"wordType3","article":"article3"}
    yield deutsch,english,synonym,persian,meaningNumDaf,synName,synTelegramLink,perName,perTelegramLink,deuName,deuTelegramLink,engName,engTelegramLink,wordDetails

@pytest.fixture(scope="module")
def meaning4():
    deutsch="deutsch4"
    english="english4"
    synonym="synonym4"
    persian="persian4"
    meaningNumDaf=1
    synName="synName4"
    synTelegramLink = "synTelegramLink4"
    perName = "perName4"
    perTelegramLink= "perTelegramLink4"
    deuName="deuName4"
    deuTelegramLink = "deuTelegramLink4"
    engName = "engName4"
    engTelegramLink= "engTelegramLink4"
    wordDetails = {"wordId":ObjectId("5f37b37ad3ddcf7a235c24a0"),"word":"word4","wordType":"wordType4","article":"article4"}
    yield deutsch,english,synonym,persian,meaningNumDaf,synName,synTelegramLink,perName,perTelegramLink,deuName,deuTelegramLink,engName,engTelegramLink,wordDetails

@pytest.fixture(scope="module")
def meaning5():
    deutsch="deutsch5"
    english="english5"
    synonym="synonym5"
    persian="persian5"
    meaningNumDaf=1
    synName="synName5"
    synTelegramLink = "synTelegramLink5"
    perName = "perName5"
    perTelegramLink= "perTelegramLink5"
    deuName="deuName5"
    deuTelegramLink = "deuTelegramLink5"
    engName = "engName5"
    engTelegramLink= "engTelegramLink5"
    wordDetails = {"wordId":ObjectId("5f37b358d3ddcf7a235c249f"),"word":"word5","wordType":"wordType5","article":"article5"}
    yield deutsch,english,synonym,persian,meaningNumDaf,synName,synTelegramLink,perName,perTelegramLink,deuName,deuTelegramLink,engName,engTelegramLink,wordDetails

@pytest.fixture(scope="module")
def meaningValues(meaning1,meaning2,meaning3,meaning4,meaning5):
    yield {"meaning1":meaning1,"meaning2":meaning2,"meaning3":meaning3,"meaning4":meaning4,"meaning5":meaning5}

@pytest.fixture(scope="module")
def book1():
    bookName="bookName1"
    chapter="chapter1"
    content="content1"
    page="page1"
    lesson="lesson1"
    publisher="publisher1"
    word = "word1"
    meaningId = ObjectId("5f37b413d3ddcf7a235c24a3")
    yield bookName,chapter,content,page,lesson,publisher,word,meaningId

@pytest.fixture(scope="module")
def book2():
    bookName="bookName2"
    chapter="chapter2"
    content="content2"
    page="page2"
    lesson="lesson2"
    publisher="publisher2"
    word = "word2"
    meaningId = ObjectId("5f37b3f4d3ddcf7a235c24a2")
    yield bookName,chapter,content,page,lesson,publisher,word,meaningId


@pytest.fixture(scope="module")
def book3():
    bookName="bookName3"
    chapter="chapter3"
    content="content3"
    page="page3"
    lesson="lesson3"
    publisher="publisher3"
    word = "word3"
    meaningId = ObjectId("5f37b3d8d3ddcf7a235c24a1")
    yield bookName,chapter,content,page,lesson,publisher,word,meaningId

@pytest.fixture(scope="module")
def book4():
    bookName="bookName4"
    chapter="chapter4"
    content="content4"
    page="page4"
    lesson="lesson4"
    publisher="publisher4"
    word = "word4"
    meaningId = ObjectId("5f37b37ad3ddcf7a235c24a0")
    yield bookName,chapter,content,page,lesson,publisher,word,meaningId

@pytest.fixture(scope="module")
def book5():
    bookName="bookName5"
    chapter="chapter5"
    content="content5"
    page="page5"
    lesson="lesson5"
    publisher="publisher5"
    word = "word5"
    meaningId = ObjectId("5f37b358d3ddcf7a235c249f")
    yield bookName,chapter,content,page,lesson,publisher,word,meaningId

@pytest.fixture(scope="module")
def bookValues(book1,book2,book3,book4,book5):
    yield {"book1":book1,"book2":book2,"book3":book3,"book4":book4,"book5":book5}

