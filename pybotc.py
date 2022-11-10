# 
import requests
import configparser as cfg
import json
import sys
sys.path.append( "../")

class Bot:
       
        def __init__(self,config):
                self.config = config
                self.token = self.read_token_from_config_file()
                self.base = "https://api.telegram.org/bot{}/".format(self.token)


        def get_updates(self,offset=None):
                # url = self.base + "getUpdates?timeout=0.1&"
                url = self.base + "getUpdates?timeout=5"
                # print(f"url = {url}")
                if offset:
                        url = url + "&offset={}".format(offset + 1)
                        # print("url = {}".format(url))
                try:
                        r = requests.get(url)
                        out = json.loads(r.content)
                        # print(f"out = {out}") 
                        return out
                except:
                        print("we've company on internat connection") 


        def getChatMember(self,chat_id,user_id):
                url = self.base + f"getChatMember?chat_id={chat_id}&user_id={user_id}"
                print(f"url = {url}")
                if chat_id and user_id:
                        r = requests.get(url)
                        output = json.loads(r.content)
                        print(f'output = {output}')
                        try:
                           out = output['result']['status']
                           if out == 'member' or out == 'administrator' or out == 'creator':
                                outputBoolean = True
                           else:
                                outputBoolean = False
                        except:
                           out = json.loads(r.content)
                           outputBoolean = False
                return outputBoolean,out


        def sendDocument(self,chat_id,openedfile,caption,disable_notification=True): 
                # multipart/from-data
                url = self.base + f"sendDocument?chat_id={chat_id}&caption={caption}&disable_notification={disable_notification}"
                # openedfile must be like this --> openedfile ={'document': open("copy.txt", "rb")}
                if  chat_id is not None and openedfile is not None and caption is not None :
                        requests.get(url,files=openedfile)

        def sendVideo(self,chat_id,video,caption):
                url = self.base + f"sendVideo?chat_id={chat_id}&video={video}&caption={caption}" 
                if  chat_id is not None and video is not None and caption is not None :
                        requests.get(url)   
        
        def sendMessage(self,chat_id,msg,parse_mode,customKey): 
                parse_mode = "HTML"
                url = self.base + "sendMessage?chat_id={}&text={}&parse_mode={}&reply_markup={}".format(chat_id,msg,parse_mode,customKey) 
                print("url = {}".format(url))
                if msg is not None:
                        requests.get(url)

        def editMessage(self,chat_id,msg_id,msg,parse_mode,customKey):
                url = self.base + f"editMessageText?chat_id={chat_id}&message_id={msg_id}&text={msg}&reply_markup={customKey}&parse_mode={parse_mode}"
                if  chat_id is not None  :
                        print(url)
                        requests.get(url)


        def forwardMessage(self,chat_id,from_chat_id,message_id,disable_notification=True): 
                
                url = self.base + f"forwardMessage?chat_id={chat_id}&from_chat_id={from_chat_id}&message_id={message_id}&disable_notification={disable_notification}" 
                # print("url = {}".format(url))
                if  chat_id is not None and from_chat_id is not None and message_id is not None :
                        requests.get(url)


        def read_token_from_config_file(self):
                parser = cfg.ConfigParser()
                parser.read(self.config)
                # print(parser.read(self.config))
                return parser.get('creds', 'token')
class Type:
        def __init__(self,config):
                self.config = config
           

        def typSystem(self):
                parser = cfg.ConfigParser()
                parser.read(self.config)
                # print(parser.read(self.config))
                return parser.get('differency', 'kind')


class mail:
        def __init__(self,config):
                self.config = config

        def email(self):
                parser = cfg.ConfigParser()
                parser.read(self.config)
                # print(parser.read(self.config))
                m=parser.get('mail', 'ail')  
                p=parser.get('mail', 'pa')
                return m,p      
# v = Bot("config.cfg").read_token_from_config_file("config.cfg")
# bot = Bot("config.cfg")

# # print(f"v = {v}")
# # openedfile ={'document': open("copy.txt", "rb")}
# # f = r"D:\project\WoerterbuchProject\mainV2\dailyReport\dR_73543260.mp4"
# f = "D:\\project\\WoerterbuchProject\\mainV2\\dailyReport\\dR_73543260.mp4"
# # f = r"D:\\project\\WoerterbuchProject\\mainV2\\dailyReport\\kk.txt"
# # f = r"D:\project\WoerterbuchProject\mainV2\dailyReport\kk.txt"
# # video =open(f, "rb")
# openedfile ={'document': open(f, "rb")}
# caption = "test"
# chat_id = 73543260
# # # bot.sendDocument(chat_id,openedfile,fehrestAghazinMsg,disable_notification=True)
# # bot.sendVideo(chat_id,video,caption)
# bot.sendDocument(chat_id,openedfile,caption,disable_notification=True)
# print("send")