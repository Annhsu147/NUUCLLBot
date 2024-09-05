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

#from <your_loki_main_program> import execLoki

logging.basicConfig(level=logging.DEBUG)

def getLokiResult(inputSTR, filterLIST=[]):
    splitLIST = ["！", "，", "。", "？", "!", ",", "\n", "；", "\u3000", ";"] #
    # 設定參考資料
    refDICT = { # value 必須為 list
        #"key": []
    }
    resultDICT = execLoki(inputSTR, filterLIST=filterLIST, splitLIST=splitLIST, refDICT=refDICT)
    logging.debug("Loki Result => {}".format(resultDICT))
    return resultDICT

class BotClient(discord.Client):

    def resetMSCwith(self, messageAuthorID):
        '''
        清空與 messageAuthorID 之間的對話記錄
        '''
        templateDICT = {    "id": messageAuthorID,
                             "updatetime" : datetime.now(),
                             "latestQuest": "",
                             "false_count" : 0
        }
        return templateDICT

    async def on_ready(self):
        # ################### Multi-Session Conversation :設定多輪對話資訊 ###################
        self.templateDICT = {"updatetime" : None,
                             "latestQuest": "",
                             "Response":[]
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
            elif msgSTR.lower() in ["哈囉","嗨","嗨嗨","安安","泥豪","泥嚎","你好","您好","hi","hello"]:
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
                    replySTR = msgSTR.title()+" @{}！這裡是聯合大學華語文學系的資訊小角落，本bot是這裡的負責人！有關系上的問題都可以詢問我喔( ੭˙ᗜ˙)੭\n想要開啟您的聯大華文探索之旅？立即於輸入框中@本bot並打聲招呼吧⸜( ᐛ )⸝".format(message.author.id)
                        
            elif message.author.id not in self.mscDICT:
                replySTR = '(o_O)嗯?你是誰?要先跟本bot打招呼，本bot才能為你解答喔~\n（哼哼打招呼才有禮貌，不禮貌的孩子本bot才不理你<(`^´)>'

# ##########非初次對話：這裡用 Loki 計算語意
            else: #檢查用戶是否結束對話
                if msgSTR.lower() in 'bye,bye bye,byebye,good bye,goodbye,拜拜,拜咿,掰掰,再見,下次見'.split(','):
                    # 刪除之前的對話，並給予結束的回覆。
                    self.mscDICT[message.author.id] = self.resetMSCwith(message.author.id)
                    replySTR = '掰掰@{} ～ 我們下次見啦！\n如果覺得本bot有回答到你心坎裡，請給本bot一個五星好評呦ദ്ദി ˃ ᵕ ˂ )'


                else: #開始處理正式對話
                    #從這裡開始接上 NLU 模型
                    resultDICT = getLokiResult(msgSTR)
                    if self.mscDICT[message.author.id]['Response']:
                        ansLIST = self.mscDICT[message.author.id]["Response"]
                        replySTR = ""
                    
                    logging.debug("######\nLoki 處理結果如下：")
                    logging.debug(resultDICT)
            await message.reply(replySTR)


if __name__ == "__main__":
    with open("account.info", encoding="utf-8") as f: #讀取account.info
        accountDICT = json.loads(f.read())
    client = BotClient(intents=discord.Intents.default())
    client.run(accountDICT["discord_token"])
