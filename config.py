#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @trojanzhex


import os

class Config(object):

    # Get a bot token from botfather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7279728762:AAGOel3zhLLYa5x0v9EOFHmzjvDQ9dmgfV4")


    # Get from my.telegram.org (or @UseTGXBot)
    APP_ID = int(os.environ.get("APP_ID", "22606849"))
    API_HASH = os.environ.get("API_HASH", "ef85493cd32eadcb5309b5957d8d1b86")


    # Array to store users who are authorized to use the bot
    AUTH_USERS = set(int(x) for x in os.environ.get("AUTH_USERS", "6440021089").split())
    
