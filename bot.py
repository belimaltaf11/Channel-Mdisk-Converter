from pyrogram import Client
from aiohttp import web
from route import web_server
import datetime
from config import *
from database import db
from helpers import temp
from utils import broadcast_admins 

import logging
import logging.config 

# Get logging configurations
logging.config.fileConfig('logging.conf')
logging.getLogger().setLevel(logging.INFO) 

class Bot(Client): 

    def __init__(self):
        super().__init__(
            name="converter",
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=BOT_TOKEN,
            workers=200,
            plugins={"root": "plugins"},
            sleep_threshold=15,
        )

    async def start(self):  
        temp.START_TIME = datetime.datetime.now()
        await super().start()
        me = await self.get_me()
        self.username = '@' + me.username
        temp.BOT_USERNAME = me.username
        temp.FIRST_NAME = me.first_name 

   app = web.AppRunner(await web_server())
        await app.setup()
        bind_address = "0.0.0.0"       
        await web.TCPSite(app, bind_address, PORT).start()     
        

        if not await db.get_bot_stats():
            await db.create_stats()
            
        await broadcast_admins(self, '** Bot started successfully **')
        logging.info('Bot started')


    async def stop(self, *args):
        await broadcast_admins(self, '** Bot Stopped Bye **')
        await super().stop()
        logging.info('Bot Stopped Bye')
