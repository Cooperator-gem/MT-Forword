I#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Dark Angel

import os
import logging

class Config:
    
    API_ID = int(os.environ.get("API_ID", 2819362))
    API_HASH = os.environ.get("API_HASH", "578ce3d09fadd539544a327c45b55ee4")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "5612759440:AAGsHWbTEv2uffQcwkaAFoTdf-FDeHXR5Aw") 
    BOT_SESSION = os.environ.get("BOT_SESSION", "bot") 
    CAPTION = os.environ.get("CAPTION", "")
    FROM_CHANNEL = os.environ.get("FROM_CHANNEL", "@moneiac_course")
    FILTER_TYPE = os.environ.get("FILTER_TYPE", "")
    OWNER_ID = os.environ.get("OWNER_ID", "1211202733")
    LIMIT = int(os.environ.get("LIMIT", "25000"))
    SKIP_NO = int(os.environ.get("SKIP_NO", "0"))
    SESSION = os.environ.get("SESSION", "BQCfla0mR5gMIYbIrRR9Of6BaiAs2bROZPhw-oPiGtpFWc2ew-qwJnhlLzAKj75jf9AXkUklCkDQwRh-eMgAvFpOwVY47OqLiBO5mrOx-lgIr-2AFfcOu65VYTeAUa4YAGLOn320Y6dpaSQ4KADxqqGiqqwl2oTnsS28LQ8Tse0akZ57wkekm97vW93IJO6JFU28hrr7DQgG65MepL2Qv3wtfOq6-J3WPGsief8wusklWhRg7Lf7xkoqfG5ucYtTz2wXIZ9V0mOwfNYTbo-Ps58LjCv8yo7l65-i5vZqGKEVGjjMBjgEUx2e17oJ_NorLbUyVQB-Yj2ZEzklQLqZ4NcZSDF8rQA")
    TO_CHANNEL = int(os.environ.get("TO_CHANNEL", -1001601169374))
def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
