# a = {"outer":{"name":1,"telegramLink":3}}
# # print(a["outer"])
# b = []
# # print(b)
# # print(len(b))
# # print(b[0])
# a = {"x":{"b":21,"h":32}}
# print(a["x"])
# print(a["x"]["b"])

# # a,b,c,d = 0,2,4,5

# z = [1,1,2,2,3]
# # print(f"{list(set(z)) = }")

# h = [i for i in z if i]
# y= [1,3,2]
# if z == y :
#     # print("equal")
# g = {"h":1,"salam":44}
# # f = {"jjj":11}
# f = {"salam":33}
# # out = g+f
# g.update(f)
# # g.add(f)
# # print(f"{g = }")

# dd = [1,2,3,4,5]
# gg= list(set(dd))
# # print(f"{gg = }")
# cc = [1]
# intercetion = set(dd)&set(cc)
# # print(f"{intercetion = }")

# hh = {"wordDetails":{"someF":"someVal"}}
# p = {"word":"hello"}
# cc = {"wordType":"Verb"}
# g={}
# g.update(cc)
# g.update(p)
# print(f"{g = }")
# hh.update(g)
# print(f"dictionary {hh = }")
# hh.pop("wordType")
# print(f"dictionary {hh = }")
# hh["wordDetails"]["word"]=1
# print(f"dictionary {hh = }")

# l = [1,2,3,4,5,1,2,3,4,5]
# h = list(set(l))
# print(f"h = {h}")
# i = "aaa"
# b = "bbb"
# c = i +b
# print(f"c = {c}")
from statistics import mode


d = "5f30077014082a0f00465048"
c= "5f30077014082a0f004650485dc5c380ec972f0ee087361d"
# 5dc5c380ec972f0ee087361d
xx = "5f30077014082a0f004650485dc5c380ec972f0ee087361d5da7467a6c8002022619ea05"

# g = xx.split(24)
#saparate ids func
print(xx[22:24])
x = 24
out = [xx[i: i + x] for i in range(0, len(xx), x)]
print(f"out = {out}")
['5f30077014082a0f00465048', '5dc5c380ec972f0ee087361d', '5da7467a6c8002022619ea05']
# "5da7467a6c8002022619ea05"
# arr = [xx]
# h = []
# for i in arr:
#     if len(i)/24 !=1  and len(i)>24 :
#         temp = ""
#         for j in range(len(i)):
            
#             if j%24==0 and j !=0:
#                 h.append(temp)
#                 temp=""
#             temp = temp+i[j]
# print(f"h = {h}")
# h = ['5f30077014082a0f00465048', '5dc5c380ec972f0ee087361d']
# h = ['5f30077014082a0f004650485', 'dc5c380ec972f0ee087361d5']
# h = ['5f30077014082a0f004650485', 'dc5c380ec972f0ee087361d5']
# g = xx.split(24)
# print(g)

# "deutsch","english","synonym","persian","meaningNumDaf","synVoice","synName","synName","engVoice","engName","engTelegramLink","perVoice","perName","perTelegramLink","deuVoice","deuName","deuTelegramLink","wordDetails","wordId","word","wordType","article"