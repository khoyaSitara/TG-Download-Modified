# This file is a part of TG-FileStreamBot
# Coding : Jyothis Jayanth [@EverythingSuckz]


import os
import os.path
from ..vars import Var
import logging
from pyrogram import Client
from os import getcwd

logger = logging.getLogger("bot")
        
StreamBot = Client(
    name="WebStreamer",
    api_id=Var.API_ID,
    api_hash=Var.API_HASH,
    workdir="WebStreamer",
    plugins={"root": "WebStreamer/bot/plugins"},
    bot_token=Var.BOT_TOKEN,
    sleep_threshold=Var.SLEEP_THRESHOLD,
    workers=Var.WORKERS,
)

multi_clients = {}
work_loads = {}
