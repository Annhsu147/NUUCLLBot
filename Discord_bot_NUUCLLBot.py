#!/user/bin/env python
# -*- coding: utf-8 -*-

import logging
import discord
import json, os
import re
import pandas as pd
from datetime import datetime
from pprint import pprint
from NUUCLLBot import runLoki, execLoki
logging.basicConfig(level=logging.DEBUG)

pth = os.path.dirname(__file__)

punctuationPat = re.compile("[,\.\?:;，。？、：；\n]+")

def getLokiResult(inputSTR):
    punctuationPat = re.compile("[,\.\?:;，。？、：；\n]+")
    inputLIST = punctuationPat.sub("\n", inputSTR).split("\n")
    filterLIST = []
    # 因為加了標點去做分割，標點後會割出一個
    if inputLIST[-1]:
        resultDICT = execLoki(inputLIST, filterLIST)
    else:
        resultDICT = execLoki(inputLIST[:-1], filterLIST)
    logging.debug("Loki Result => {}".format(resultDICT))
    return resultDICT

class BotClient(discord.Client):

    def resetMSCwith(self, messageAuthorID):
        '''
        清空與 messageAuthorID 之間的對話記錄
        '''
        templateDICT = {    "id":messageAuthorID,
                            "updatetime":datetime.now(),
                            "latestQuest":"",
                            "false_count":0,
                            "Response":"",
                            "畢業":[],
                            "介紹":[],
                            "實習地點":[],
                            "實習時間":[],
                            "實習":[]

        }
        return templateDICT

    async def on_ready(self):
        # ################### Multi-Session Conversation :設定多輪對話資訊 ###################
        self.templateDICT = {"updatetime" : None,
                             "latestQuest": "",
                             "Response":[],
                             "畢業":[],
                             "介紹":[],
                             "實習地點":[],
                             "實習時間":[],
                             "實習":[]
        }
        self.mscDICT = { #userid:templateDICT
        }
        # ####################################################################################
        print('Logged on as {} with id {}'.format(self.user, self.user.id))

    async def on_message(self, message):
        # Don't respond to bot itself. Or it would create a non-stop loop.
        # 如果訊息來自 bot 自己，就不要處理，直接回覆 None。不然會 Bot 會自問自答個不停。
        if message.author == self.user:
            return None

        logging.debug("收到來自 {} 的訊息".format(message.author))
        logging.debug("訊息內容是 {}。".format(message.content))
        if self.user.mentioned_in(message):
            replySTR = "我是預設的回應字串…你會看到我這串字，肯定是出了什麼錯！"
            logging.debug("本 bot 被叫到了！")
            msgSTR = message.content.replace("<@{}> ".format(self.user.id), "").strip()
            logging.debug("人類說：{}".format(msgSTR))
            if msgSTR == "ping":
                replySTR = "pong"
            elif msgSTR == "ping ping":
                replySTR = "pong pong"

# ##########初次對話：這裡是 keyword trigger 的。
            elif msgSTR.lower() in ["哈囉","嗨","嗨嗨","安安","你好","您好","hi","hello"]:
                #有講過話(判斷對話時間差)
                if message.author.id in self.mscDICT.keys():
                    timeDIFF = datetime.now() - self.mscDICT[message.author.id]["updatetime"]
                    #有講過話，但與上次差超過 5 分鐘(視為沒有講過話，刷新template)
                    if timeDIFF.total_seconds() >= 300:
                        self.mscDICT[message.author.id] = self.resetMSCwith(message.author.id)
                        replySTR = "唔...? 泥嚎鴨～你真眼熟，可是本bot是重度臉盲患者，請再跟我打一次招呼吧！"
                    #有講過話，而且還沒超過5分鐘就又跟我 hello (就繼續上次的對話)
                    else:
                        replySTR = self.mscDICT[message.author.id]["latestQuest"]
                #沒有講過話(給他一個新的template)
                else:
                    self.mscDICT[message.author.id] = self.resetMSCwith(message.author.id)
                    replySTR = msgSTR.title()+"！這裡是聯合大學華語文學系的資訊小角落，本bot是這裡的負責人！\n有關系上的問題都可以詢問我喔( ੭˙ᗜ˙)੭\n想要開啟您的聯大華文探索之旅？立即於輸入框中@本bot直抒疑惑吧⸜( ᐛ )⸝"
                        
            elif message.author.id not in self.mscDICT:
                replySTR = '(o_O)嗯?你是誰?要先跟本bot打招呼，本bot才能為你解答喔~'

# ##########非初次對話：這裡用 Loki 計算語意
            else: #檢查用戶是否結束對話
                if msgSTR.lower() in 'bye,bye bye,byebye,good bye,goodbye,拜拜,拜咿,掰掰,再見,下次見'.split(','):
                    # 刪除之前的對話，並給予結束的回覆。
                    self.mscDICT[message.author.id] = self.resetMSCwith(message.author.id)
                    replySTR = '掰掰～ 我們下次見啦！\n如果覺得本bot有回答到你心坎裡，請給本bot一個五星好評呦ദ്ദി ˃ ᵕ ˂ )'


                else: #開始處理正式對話
                    #從這裡開始接上 NLU 模型
                    curr_pth = os.path.dirname(__file__)
                    nuucllinfoDF = pd.read_csv(f"{curr_pth}/nuucllinfo.csv", sep="\t", index_col=0)

                    resultDICT = getLokiResult(msgSTR)

                    self.mscDICT[message.author.id]['畢業'].extend(resultDICT['畢業'])
                    self.mscDICT[message.author.id]['介紹'].extend(resultDICT['介紹'])
                    self.mscDICT[message.author.id]['實習地點'].extend(resultDICT['實習地點'])
                    self.mscDICT[message.author.id]['實習時間'].extend(resultDICT['實習時間'])
                    self.mscDICT[message.author.id]['實習'].extend(resultDICT['實習'])


                    # 檢查回覆是否存在，存在表示有回覆需要處理
                    if self.mscDICT[message.author.id]['Response']:
                        ansLIST = self.mscDICT[message.author.id]["Response"]
                        replySTR = ""

                    elif self.mscDICT[message.author.id]['畢業']:
                        nuucllInfoKey = self.mscDICT[message.author.id]['畢業'][0]  # 取出第一個對應的值
                        replySTR = nuucllinfoDF.at[nuucllInfoKey, 'description']

                    elif self.mscDICT[message.author.id]['介紹']:
                        nuucllInfoKey = self.mscDICT[message.author.id]['介紹'][0]  # 取出第一個對應的值
                        replySTR = nuucllinfoDF.at[nuucllInfoKey, 'description']

                    elif self.mscDICT[message.author.id]['實習地點']:
                        nuucllInfoKey = self.mscDICT[message.author.id]['實習地點'][0]  # 取出第一個對應的值
                        replySTR = nuucllinfoDF.at[nuucllInfoKey, 'description']

                    elif self.mscDICT[message.author.id]['實習時間']:
                        nuucllInfoKey = self.mscDICT[message.author.id]['實習時間'][0]  # 取出第一個對應的值
                        replySTR = nuucllinfoDF.at[nuucllInfoKey, 'description']

                    elif self.mscDICT[message.author.id]['實習']:
                        nuucllInfoKey = self.mscDICT[message.author.id]['實習'][0]  # 取出第一個對應的值
                        replySTR = nuucllinfoDF.at[nuucllInfoKey, 'description']
        
                    logging.debug("######\nLoki 處理結果如下：")
                    logging.debug(resultDICT)
            await message.reply(replySTR)


if __name__ == "__main__":
    with open("account.info", encoding="utf-8") as f: #讀取account.info
        accountDICT = json.loads(f.read())
    client = BotClient(intents=discord.Intents.default())
    client.run(accountDICT["discord_token"])
