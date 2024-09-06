#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for shixi_time

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
        responseDICT = json.load(open(os.path.join(os.path.dirname(os.path.dirname(__file__)), "reply/reply_shixi_time.json"), encoding="utf-8"))
    except Exception as e:
        print("[ERROR] responseDICT => {}".format(str(e)))

parent_pth = os.path.split(path)[0]

with open(f'{parent_pth}/account.info') as f:
    account = json.load(f)

articut = Articut(username=account['username'], apikey=account['api_key'], version='v271')

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG:
        print("[shixi_time] {} ===> {}".format(inputSTR, utterance))

def getResponse(utterance, args):
    resultSTR = ""
    if utterance in responseDICT:
        if len(responseDICT[utterance]):
            resultSTR = sample(responseDICT[utterance], 1)[0].format(*args)

    return resultSTR

def getResult(inputSTR, utterance, args, resultDICT, refDICT, pattern=""):
    debugInfo(inputSTR, utterance)

    posSTR = "".join(articut.parse(inputSTR, userDefinedDictFILE=userDefinedDICT)['result_pos'])
    if '實習時間' not in resultDICT:
        resultDICT['實習時間'] = []

    if utterance == "實習期間需要工作多久":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
            if resultDICT["response"]:
                resultDICT["source"] = "reply"
        else:
            resultDICT['實習時間'].append("實習時間")

    if utterance == "實習的時長":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
            if resultDICT["response"]:
                resultDICT["source"] = "reply"
        else:
            resultDICT['實習時間'].append("實習時間")

    if utterance == "實習的時間":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
            if resultDICT["response"]:
                resultDICT["source"] = "reply"
        else:
            resultDICT['實習時間'].append("實習時間")

    if utterance == "實習的時間安排是怎麼樣的":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
            if resultDICT["response"]:
                resultDICT["source"] = "reply"
        else:
            resultDICT['實習時間'].append("實習時間")

    if utterance == "實習的時間怎麼說":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
            if resultDICT["response"]:
                resultDICT["source"] = "reply"
        else:
            resultDICT['實習時間'].append("實習時間")

    if utterance == "實習的時間是怎麼安排的":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
            if resultDICT["response"]:
                resultDICT["source"] = "reply"
        else:
            resultDICT['實習時間'].append("實習時間")

    if utterance == "實習的時間是被規定好的嗎":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
            if resultDICT["response"]:
                resultDICT["source"] = "reply"
        else:
            resultDICT['實習時間'].append("實習時間")

    if utterance == "實習的時間有被規定嗎":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
            if resultDICT["response"]:
                resultDICT["source"] = "reply"
        else:
            resultDICT['實習時間'].append("實習時間")

    if utterance == "實習要多久":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
            if resultDICT["response"]:
                resultDICT["source"] = "reply"
        else:
            resultDICT['實習時間'].append("實習時間")

    if utterance == "實習通常在什麼時候":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
            if resultDICT["response"]:
                resultDICT["source"] = "reply"
        else:
            resultDICT['實習時間'].append("實習時間")

    if utterance == "有規定實習時間嗎":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
            if resultDICT["response"]:
                resultDICT["source"] = "reply"
        else:
            resultDICT['實習時間'].append("實習時間")

    if utterance == "甚麼時間可以去實習":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
            if resultDICT["response"]:
                resultDICT["source"] = "reply"
        else:
            resultDICT['實習時間'].append("實習時間")

    if utterance == "要實習多久":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
            if resultDICT["response"]:
                resultDICT["source"] = "reply"
        else:
            resultDICT['實習時間'].append("實習時間")

    return resultDICT