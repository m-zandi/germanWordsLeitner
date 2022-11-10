from tkinter import *
from tkinter import ttk
from bson.objectid import ObjectId
root = Tk()

output = [{'wordId': ObjectId('5da748126c8002022619ea06'), 'word': 'sich freuen [vr]', 'wordType': 'Verb', 'article': '', 'wordVoiceName': 'sich freuen_Wort.mp3', 'wordtelegramLink': 'https://t.me/guew_resource/277', 'meaning1': {'meaningId': ObjectId('5dc5c380ec972f0ee087361d'), 'deutschMeaning': 'freu·en; freute, hat gefreut; [Vr] 1 sich (über etwas (Akk)) freuen wegen etwas ein Gefühl der Freude empfinden <sich sehr, ehrlich, riesig freuen>: sich über ein Geschenk, einen Anruf freuen; Ich habe mich sehr darüber gefreut, dass wir uns endlich kennen gelernt haben; Ich freue mich, Sie wieder zu sehen', 'englishMeaning': 'A refl. V. be pleased or glad (über + Akk. about); (froh sein) be happy;', 'synonymMeaning': 'sich erfreuen, Freude haben, fröhlich/glücklich sein, Gefallen finden/haben, genießen', 'persianMeaning': '1.sich ~ (über Akk.). خوشحال بودن (از);خوشحال شدن(از)', 'meaningNumDaf': '1', 'synName': 'sich freuen_Syn.mp3', 'synTelegramLink': 'https://t.me/guew_resource/288', 'engName': 'sich freuen_En.mp3', 'engTelegramLink': 'https://t.me/guew_resource/278', 'perName': 'sich freuen_1_Per.mp3', 'perTelegramLink': 'https://t.me/guew_resource/279', 'deuName': 'sich freuen_1_De.mp3', 'deuTelegramLink': 'https://t.me/guew_resource/289', 'book1': {'bookId': ObjectId('5da7467a6c8002022619ea05'), 'bookName': 'Großes Übungsbuch Wortschatz', 'chapter': '1 sich vorstellen', 'content': 'A-Kontakte, Informationen zur Person', 'page': '8&9', 'lesson': '', 'publisher': 'Hueber', 'bookNumRow': 3}, 'book2': {'bookId': ObjectId('5f2fb9f514082a0f00465047'), 'bookName': 'test', 'chapter': 'test', 'content': 'test', 'page': 'test', 'lesson': 'test', 'publisher': 'test'}, 'meaningNumRow': 2}, 'meaning2': {'meaningId': ObjectId('5f2fae6d14082a0f00465046'), 'deutschMeaning': 'test', 'englishMeaning': 'test', 'synonymMeaning': 'test', 'persianMeaning': 'test', 'meaningNumDaf': '1', 'synName': 'sich freuen_Syn.mp3', 'synTelegramLink': 'https://t.me/guew_resource/288', 'engName': 'sich freuen_En.mp3', 'engTelegramLink': 'https://t.me/guew_resource/278', 'perName': 'sich freuen_1_Per.mp3', 'perTelegramLink': 'https://t.me/guew_resource/279', 'deuName': 'sich freuen_1_De.mp3', 'deuTelegramLink': 'https://t.me/guew_resource/289', 'meaningNumRow': 4}, 'wordNumRow': 1}, {'wordId': ObjectId('5f30077014082a0f00465048'), 'word': 'sich freuen [vr]', 'wordType': 'test', 'article': 'test', 'wordVoiceName': 'sich freuen_Wort.mp3', 'wordtelegramLink': 'https://t.me/guew_resource/277', 'meaning1': {'meaningId': ObjectId('5dc5c380ec972f0ee087361d'), 'deutschMeaning': 'freu·en; freute, hat gefreut; [Vr] 1 sich (über etwas (Akk)) freuen wegen etwas ein Gefühl der Freude empfinden <sich sehr, ehrlich, riesig freuen>: sich über ein Geschenk, einen Anruf freuen; Ich habe mich sehr darüber gefreut, dass wir uns endlich kennen gelernt haben; Ich freue mich, Sie wieder zu sehen', 'englishMeaning': 'A refl. V. be pleased or glad (über + Akk. about); (froh sein) be happy;', 'synonymMeaning': 'sich erfreuen, Freude haben, fröhlich/glücklich sein, Gefallen finden/haben, genießen', 'persianMeaning': '1.sich ~ (über Akk.). خوشحال بودن (از);خوشحال شدن(از)', 'meaningNumDaf': '1', 'synName': 'sich freuen_Syn.mp3', 'synTelegramLink': 'https://t.me/guew_resource/288', 'engName': 'sich freuen_En.mp3', 'engTelegramLink': 'https://t.me/guew_resource/278', 'perName': 'sich freuen_1_Per.mp3', 'perTelegramLink': 'https://t.me/guew_resource/279', 'deuName': 'sich freuen_1_De.mp3', 'deuTelegramLink': 'https://t.me/guew_resource/289', 'book1': {'bookId': ObjectId('5da7467a6c8002022619ea05'), 'bookName': 'Großes Übungsbuch Wortschatz', 'chapter': '1 sich vorstellen', 'content': 'A-Kontakte, Informationen zur Person', 'page': '8&9', 'lesson': '', 'publisher': 'Hueber', 'bookNumRow': 7}, 'book2': {'bookId': ObjectId('5f2fb9f514082a0f00465047'), 
'bookName': 'test', 'chapter': 'test', 'content': 'test', 'page': 'test', 'lesson': 'test', 'publisher': 'test'}, 'meaningNumRow': 6}, 'meaning2': {'meaningId': ObjectId('5f2fae6d14082a0f00465046'), 'deutschMeaning': 'test', 'englishMeaning': 'test', 'synonymMeaning': 'test', 'persianMeaning': 'test', 'meaningNumDaf': '1', 'synName': 'sich freuen_Syn.mp3', 'synTelegramLink': 'https://t.me/guew_resource/288', 'engName': 'sich freuen_En.mp3', 'engTelegramLink': 'https://t.me/guew_resource/278', 'perName': 'sich freuen_1_Per.mp3', 'perTelegramLink': 'https://t.me/guew_resource/279', 'deuName': 'sich freuen_1_De.mp3', 'deuTelegramLink': 'https://t.me/guew_resource/289', 'meaningNumRow': 8}, 'wordNumRow': 5}]

treeview = ttk.Treeview(root)
treeview.pack()
# tree func for search
for x in range(len(output)):
    for field,val in output[x].items():
        if field == "wordId":
            treeview.insert("",str(x),str(val),text = output[x]["word"])
            # treeview.insert("",output[x]["wordId"],str(val),text = output[x]["word"])
        for i in range(1,10):
            if field == f"meaning{i}":
                for meaningField,meaningVal in val.items():
                    if meaningField == "meaningId":
                        print()
                        treeview.insert(str(output[x]["wordId"]),i,str(output[x]["wordId"])+str(meaningVal),text = output[x][field]["deutschMeaning"])
                    for j in range(1,10):
                        if meaningField == f"book{j}":
                            for bookField,bookVal in meaningVal.items():
                                if bookField == "bookId":
                                    print(str(output[x]["wordId"])+str(output[x][f"meaning{i}"]["meaningId"]))
                                    print(str(output[x]["wordId"])+str(output[x][f"meaning{i}"]["meaningId"])+str(bookVal))
                                    par=str(output[x]["wordId"])+str(output[x][f"meaning{i}"]["meaningId"])
                                    iddTree = str(output[x]["wordId"])+str(output[x][f"meaning{i}"]["meaningId"])+str(bookVal)
                                    treeview.insert(par,j,iddTree,text = meaningVal["publisher"])
# for select and go to next page 
treeview.config(selectmode="browse")
def callback(event):
    print(treeview.selection()[0])
treeview.bind('<<TreeviewSelect>>',callback)
# TreeviewSelect
# while(True):
#     v=treeview.selection()
#     print(v)

mainloop()






# treeview.insert("","0","word1",text = "word1")
# treeview.insert("word1","0","meaning1",text = "meaning1")
# treeview.insert("","1","word2",text = "word2")
# treeview.insert("word2","0","word2meaning1",text = "meaning1")
# treeview.insert("word2","1","word2meaning2",text = "meaning2meaning")
# treeview.insert("word2meaning2","0","book1",text = "book1")
# treeview.insert("word2meaning2","1","book2",text = "book2")
