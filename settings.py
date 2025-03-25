import chicken_dinner.pubgapi
from chicken_dinner.pubgapi import PUBGCore
from chicken_dinner.pubgapi import PUBG
from pubg_python import PUBG, Shard
import pubg_python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Enum, Table, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker
import discord
import os
from aiogram.client.default import DefaultBotProperties
from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode

api_key = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJqdGkiOiJiYjBmMjI5MC1kYThhLTAxM2QtYmUyOC00NjQ0ZDA0YjAzMzEiLCJpc3MiOiJnYW1lbG9ja2VyIiwiaWF0IjoxNzQxMDI2Mjk1LCJwdWIiOiJibHVlaG9sZSIsInRpdGxlIjoicHViZyIsImFwcCI6ImNsYW5fYm90In0.VP7mJuRRQEJd27HJrEdzEIq1VpCZ3DIOr7GrE0oyxy8"

tg_token = "7397648711:AAFRcN2Rq-2fjrwftgXTi0UDRNlP-ny54bI"

DISCORD_BOT_TOKEN = os.getenv("DISCORD_BOT_TOKEN")

GUILD_ID = 627073760016465930

# Подключение к MySQL
DATABASE_URL = "mysql+mysqlconnector://root:ZyvctrUHgmkPUvkMQFoIyUvsnBOCEbeo@crossover.proxy.rlwy.net:25395/railway"
engine = create_engine(DATABASE_URL)

Base = declarative_base()

telegram_bot = Bot(
    token=tg_token,
    default=DefaultBotProperties(parse_mode=ParseMode.HTML)
)

dp = Dispatcher()

intents = discord.Intents.default()
intents.voice_states = True
intents.guilds = True
intents.members = True
client = discord.Client(intents=intents)

# Создание сессии
Session = sessionmaker(bind=engine)
session = Session()

# API PUBG
api_1 = chicken_dinner.pubgapi.PUBG(api_key, "pc-eu")

api_2 = pubg_python.PUBG(api_key, Shard.STEAM)
