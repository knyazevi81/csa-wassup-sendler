from aiogram import Bot
from aiogram.dispatcher import Dispatcher
import os
from dotenv import load_dotenv
import config
from db.models import User, db
from aiogram.contrib.fsm_storage.memory import MemoryStorage

def database_export():
    db.connect()
    db.create_tables([User])
    db.close()

load_dotenv()

bot = Bot(config.TELEGRAM_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())