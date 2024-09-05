#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for graduation

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
        responseDICT = json.load(open(os.path.join(os.path.dirname(os.path.dirname(__file__)), "reply/reply_graduation.json"), encoding="utf-8"))
    except Exception as e:
        print("[ERROR] responseDICT => {}".format(str(e)))

parent_pth = os.path.split(path)[0]

with open(f'{parent_pth}/account.info') as f:
    account = json.load(f)

articut = Articut(username=account['username'], apikey=account['api_key'], version='v271')

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG:
        print("[graduation] {} ===> {}".format(inputSTR, utterance))

def getResponse(utterance, args):
    resultSTR = ""
    if utterance in responseDICT:
        if len(responseDICT[utterance]):
            resultSTR = sample(responseDICT[utterance], 1)[0].format(*args)

    return resultSTR

def getResult(inputSTR, utterance, args, resultDICT, refDICT, pattern=""):
    debugInfo(inputSTR, utterance)

    posSTR = "".join(articut.parse(inputSTR, userDefinedDictFILE=userDefinedDICT)['result_pos'])
    if '畢業' not in resultDICT:
        resultDICT['畢業'] = []

    if utterance == "修完幾個學分就能畢業":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
            if resultDICT["response"]:
                resultDICT["source"] = "reply"
        else:
            match = re.search(pattern, posSTR)
            if match:
                resultDICT['畢業'].append("學分")

    if utterance == "修完幾個學分才可以畢業":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
            if resultDICT["response"]:
                resultDICT["source"] = "reply"
        else:
            match = re.search(pattern, posSTR)
            if match:
                resultDICT['畢業'].append("學分")

    if utterance == "修完幾個學分才能夠畢業":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
            if resultDICT["response"]:
                resultDICT["source"] = "reply"
        else:
            match = re.search(pattern, posSTR)
            if match:
                resultDICT['畢業'].append("學分")

    if utterance == "如何才可以畢業":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
            if resultDICT["response"]:
                resultDICT["source"] = "reply"
        else:
            match = re.search(pattern, posSTR)
            if match:
                resultDICT['畢業'].append("畢業要求")

    if utterance == "怎麼才能夠畢業":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
            if resultDICT["response"]:
                resultDICT["source"] = "reply"
        else:
            match = re.search(pattern, posSTR)
            if match:
                resultDICT['畢業'].append("畢業要求")

    if utterance == "想要畢業":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
            if resultDICT["response"]:
                resultDICT["source"] = "reply"
        else:
            match = re.search(pattern, posSTR)
            if match:
                resultDICT['畢業'].append("想要畢業")

    if utterance == "有多少個學分就能畢業":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
            if resultDICT["response"]:
                resultDICT["source"] = "reply"
        else:
            match = re.search(pattern, posSTR)
            if match:
                resultDICT['畢業'].append("學分")

    if utterance == "有幾個學分才能夠畢業":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
            if resultDICT["response"]:
                resultDICT["source"] = "reply"
        else:
            match = re.search(pattern, posSTR)
            if match:
                resultDICT['畢業'].append("學分")

    if utterance == "畢業所需的要求":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
            if resultDICT["response"]:
                resultDICT["source"] = "reply"
        else:
            match = re.search(pattern, posSTR)
            if match:
                resultDICT['畢業'].append("畢業要求")

    if utterance == "畢業有哪些條件":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
            if resultDICT["response"]:
                resultDICT["source"] = "reply"
        else:
            match = re.search(pattern, posSTR)
            if match:
                resultDICT['畢業'].append("畢業要求")

    if utterance == "畢業的條件":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
            if resultDICT["response"]:
                resultDICT["source"] = "reply"
        else:
            pattern = r"\b畢業的?(條件|門檻|規定|標準|要求|方法|方式)\b"
            if re.search(pattern, posSTR):
                resultDICT['畢業'].append("畢業要求")

    if utterance == "要多少個學分才可以畢業":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
            if resultDICT["response"]:
                resultDICT["source"] = "reply"
        else:
            match = re.search(pattern, posSTR)
            if match:
                resultDICT['畢業'].append("學分")

    return resultDICT
