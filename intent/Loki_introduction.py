#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for introduction

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
        responseDICT = json.load(open(os.path.join(os.path.dirname(os.path.dirname(__file__)), "reply/reply_introduction.json"), encoding="utf-8"))
    except Exception as e:
        print("[ERROR] responseDICT => {}".format(str(e)))

parent_pth = os.path.split(path)[0]

with open(f'{parent_pth}/account.info') as f:
    account = json.load(f)

articut = Articut(username=account['username'], apikey=account['api_key'], version='v271')

# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG:
        print("[introduction] {} ===> {}".format(inputSTR, utterance))

def getResponse(utterance, args):
    resultSTR = ""
    if utterance in responseDICT:
        if len(responseDICT[utterance]):
            resultSTR = sample(responseDICT[utterance], 1)[0].format(*args)

    return resultSTR

def getResult(inputSTR, utterance, args, resultDICT, refDICT, pattern=""):
    debugInfo(inputSTR, utterance)

    posSTR = "".join(articut.parse(inputSTR, userDefinedDictFILE=userDefinedDICT)['result_pos'])
    if '介紹' not in resultDICT:
        resultDICT['介紹'] = []

    if utterance == "什麼是華語文學":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
            if resultDICT["response"]:
                resultDICT["source"] = "reply"
        else:
            resultDICT['介紹'].append("華文")

    if utterance == "介紹你們華文系":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
            if resultDICT["response"]:
                resultDICT["source"] = "reply"
        else:
            resultDICT['介紹'].append("華文系")

    if utterance == "華文系的介紹":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
            if resultDICT["response"]:
                resultDICT["source"] = "reply"
        else:
            resultDICT['介紹'].append("華文系")

    if utterance == "華語文學是什麼":
        if CHATBOT_MODE:
            resultDICT["response"] = getResponse(utterance, args)
            if resultDICT["response"]:
                resultDICT["source"] = "reply"
        else:
            resultDICT['介紹'].append("華文")

    return resultDICT