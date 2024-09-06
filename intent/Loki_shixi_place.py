#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for shixi_place

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
        responseDICT = json.load(open(os.path.join(os.path.dirname(os.path.dirname(__file__)), "reply/reply_shixi_place.json"), encoding="utf-8"))
    except Exception as e:
        print("[ERROR] responseDICT => {}".format(str(e)))

parent_pth = os.path.split(path)[0]

with open(f'{parent_pth}/account.info') as f:
    account = json.load(f)

articut = Articut(username=account['username'], apikey=account['api_key'], version='v271')

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG:
        print("[shixi_place] {} ===> {}".format(inputSTR, utterance))

def getResponse(utterance, args):
    resultSTR = ""
    if utterance in responseDICT:
        if len(responseDICT[utterance]):
            resultSTR = sample(responseDICT[utterance], 1)[0].format(*args)

    return resultSTR

def getResult(inputSTR, utterance, args, resultDICT, refDICT, pattern=""):
    debugInfo(inputSTR, utterance)

    posSTR = "".join(articut.parse(inputSTR, userDefinedDictFILE=userDefinedDICT)['result_pos'])
    if '實習地點' not in resultDICT:
        resultDICT['實習地點'] = []

    if utterance == "可以去哪些海外的實習":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
            if resultDICT["response"]:
                resultDICT["source"] = "reply"
        else:
            resultDICT['實習地點'].append("海外實習地點")

    if utterance == "可以去哪裡實習":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
            if resultDICT["response"]:
                resultDICT["source"] = "reply"
        else:
            resultDICT['實習地點'].append("實習地點")

    if utterance == "可以去甚麼地方實習":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
            if resultDICT["response"]:
                resultDICT["source"] = "reply"
        else:
            resultDICT['實習地點'].append("實習地點")

    if utterance == "可以有哪幾個海外的實習":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
            if resultDICT["response"]:
                resultDICT["source"] = "reply"
        else:
            resultDICT['實習地點'].append("海外實習地點")

    if utterance == "國內的實習的地點":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
            if resultDICT["response"]:
                resultDICT["source"] = "reply"
        else:
            resultDICT['實習地點'].append("國內實習地點")

    if utterance == "實習的地點":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
            if resultDICT["response"]:
                resultDICT["source"] = "reply"
        else:
            resultDICT['實習地點'].append("實習地點")

    if utterance == "實習的地點有哪些":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
            if resultDICT["response"]:
                resultDICT["source"] = "reply"
        else:
            resultDICT['實習地點'].append("實習地點")

    if utterance == "有哪些實習的地點":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
            if resultDICT["response"]:
                resultDICT["source"] = "reply"
        else:
            resultDICT['實習地點'].append("實習地點")

    if utterance == "有多少個海外的實習":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
            if resultDICT["response"]:
                resultDICT["source"] = "reply"
        else:
            resultDICT['實習地點'].append("海外實習地點")

    if utterance == "海外的實習可以去哪些國家":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
            if resultDICT["response"]:
                resultDICT["source"] = "reply"
        else:
            resultDICT['實習地點'].append("海外實習地點")

    if utterance == "海外的實習可以去哪幾個國家":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
            if resultDICT["response"]:
                resultDICT["source"] = "reply"
        else:
            resultDICT['實習地點'].append("海外實習地點")

    if utterance == "海外的實習的國家有哪些":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
            if resultDICT["response"]:
                resultDICT["source"] = "reply"
        else:
            resultDICT['實習地點'].append("海外實習地點")

    if utterance == "海外的實習的國家有哪幾個":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
            if resultDICT["response"]:
                resultDICT["source"] = "reply"
        else:
            resultDICT['實習地點'].append("海外實習地點")

    if utterance == "海外的實習的地點":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
            if resultDICT["response"]:
                resultDICT["source"] = "reply"
        else:
            resultDICT['實習地點'].append("海外實習地點")

    return resultDICT