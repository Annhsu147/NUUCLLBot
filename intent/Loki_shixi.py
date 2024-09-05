#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for shixi

    Input:
        inputSTR      str,
        utterance     str,
        args          str[],
        resultDICT    dict,
        refDICT       dict,
        pattern       str

    Output:
        resultDICT    dict
"""
from ArticutAPI import Articut
from random import sample
import json
import os
import re

DEBUG = True
CHATBOT_MODE = False

path = os.path.dirname(__file__)
userDefinedDICT = f"{path}/USER_DEFINED.json"
# userDefinedDICT = {}
# try:
#     userDefinedDICT = json.load(open(os.path.join(os.path.dirname(__file__), "USER_DEFINED.json"), encoding="utf-8"))
# except Exception as e:
#     print("[ERROR] userDefinedDICT => {}".format(str(e)))

responseDICT = {}
if CHATBOT_MODE:
    try:
        responseDICT = json.load(open(os.path.join(os.path.dirname(os.path.dirname(__file__)), "reply/reply_shixi.json"), encoding="utf-8"))
    except Exception as e:
        print("[ERROR] responseDICT => {}".format(str(e)))

parent_pth = os.path.split(path)[0]

with open(f'{parent_pth}/account.info') as f:
    account = json.load(f)

articut = Articut(username=account['username'], apikey=account['api_key'], version='v271')

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG:
        print("[shixi] {} ===> {}".format(inputSTR, utterance))

def getResponse(utterance, args):
    resultSTR = ""
    if utterance in responseDICT:
        if len(responseDICT[utterance]):
            resultSTR = sample(responseDICT[utterance], 1)[0].format(*args)

    return resultSTR

def getResult(inputSTR, utterance, args, resultDICT, refDICT, pattern=""):
    debugInfo(inputSTR, utterance)

    posSTR = "".join(articut.parse(inputSTR, userDefinedDictFILE=userDefinedDICT)['result_pos'])
    if '實習' not in resultDICT:
        resultDICT['實習'] = []

    if utterance == "一定要到國外實習嗎":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
            if resultDICT["response"]:
                resultDICT["source"] = "reply"
        else:
            match = re.search(pattern, posSTR)
            if match:
                resultDICT['實習'].append("一定要國外實習嗎")

    if utterance == "一定要去實習嗎":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
            if resultDICT["response"]:
                resultDICT["source"] = "reply"
        else:
            match = re.search(pattern, posSTR)
            if match:
                resultDICT['實習'].append("一定要實習嗎")

    if utterance == "了解有關國內的實習":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
            if resultDICT["response"]:
                resultDICT["source"] = "reply"
        else:
            match = re.search(pattern, posSTR)
            if match:
                resultDICT['實習'].append("國內實習")

    if utterance == "了解有關國外的實習":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
            if resultDICT["response"]:
                resultDICT["source"] = "reply"
        else:
            match = re.search(pattern, posSTR)
            if match:
                resultDICT['實習'].append("海外實習")

    if utterance == "了解關於國內的實習":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
            if resultDICT["response"]:
                resultDICT["source"] = "reply"
        else:
            match = re.search(pattern, posSTR)
            if match:
                resultDICT['實習'].append("國內實習")

    if utterance == "了解關於國外的實習":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
            if resultDICT["response"]:
                resultDICT["source"] = "reply"
        else:
            match = re.search(pattern, posSTR)
            if match:
                resultDICT['實習'].append("海外實習")

    if utterance == "只想在國內實習":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
            if resultDICT["response"]:
                resultDICT["source"] = "reply"
        else:
            match = re.search(pattern, posSTR)
            if match:
                resultDICT['實習'].append("只想在國內實習")

    if utterance == "可以去國外實習嗎":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
            if resultDICT["response"]:
                resultDICT["source"] = "reply"
        else:
            match = re.search(pattern, posSTR)
            if match:
                resultDICT['實習'].append("可以去海外實習")

    if utterance == "國內的實習":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
            if resultDICT["response"]:
                resultDICT["source"] = "reply"
        else:
            match = re.search(pattern, posSTR)
            if match:
                resultDICT['實習'].append("國內實習")

    if utterance == "實習":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
            if resultDICT["response"]:
                resultDICT["source"] = "reply"
        else:
            match = re.search(pattern, posSTR)
            if match:
                resultDICT['實習'].append("實習")

    if utterance == "我對國內實習感興趣":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
            if resultDICT["response"]:
                resultDICT["source"] = "reply"
        else:
            match = re.search(pattern, posSTR)
            if match:
                resultDICT['實習'].append("國內實習")

    if utterance == "我對國外實習有興趣":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
            if resultDICT["response"]:
                resultDICT["source"] = "reply"
        else:
            match = re.search(pattern, posSTR)
            if match:
                resultDICT['實習'].append("海外實習")

    if utterance == "提供一些和國外的實習有關的詳細資訊":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
            if resultDICT["response"]:
                resultDICT["source"] = "reply"
        else:
            match = re.search(pattern, posSTR)
            if match:
                resultDICT['實習'].append("海外實習")

    if utterance == "提供一些有關國內的實習的詳細資訊":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
            if resultDICT["response"]:
                resultDICT["source"] = "reply"
        else:
            match = re.search(pattern, posSTR)
            if match:
                resultDICT['實習'].append("國內實習")

    if utterance == "提供一些有關國外的實習的詳細資訊":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
            if resultDICT["response"]:
                resultDICT["source"] = "reply"
        else:
            match = re.search(pattern, posSTR)
            if match:
                resultDICT['實習'].append("海外實習")

    if utterance == "提供一些跟國內的實習有關的詳細資訊":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
            if resultDICT["response"]:
                resultDICT["source"] = "reply"
        else:
            match = re.search(pattern, posSTR)
            if match:
                resultDICT['實習'].append("國內實習")

    if utterance == "提供一些跟國內的實習相關的詳細資訊":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
            if resultDICT["response"]:
                resultDICT["source"] = "reply"
        else:
            match = re.search(pattern, posSTR)
            if match:
                resultDICT['實習'].append("國內實習")

    if utterance == "提供一些跟國外的實習相關的詳細資訊":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
            if resultDICT["response"]:
                resultDICT["source"] = "reply"
        else:
            match = re.search(pattern, posSTR)
            if match:
                resultDICT['實習'].append("海外實習")

    if utterance == "提供一些關於國內的實習的詳細資訊":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
            if resultDICT["response"]:
                resultDICT["source"] = "reply"
        else:
            match = re.search(pattern, posSTR)
            if match:
                resultDICT['實習'].append("國內實習")

    if utterance == "提供一些關於國外的實習的詳細資訊":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
            if resultDICT["response"]:
                resultDICT["source"] = "reply"
        else:
            match = re.search(pattern, posSTR)
            if match:
                resultDICT['實習'].append("海外實習")

    if utterance == "海外的實習":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
            if resultDICT["response"]:
                resultDICT["source"] = "reply"
        else:
            match = re.search(pattern, posSTR)
            if match:
                resultDICT['實習'].append("海外實習")

    return resultDICT