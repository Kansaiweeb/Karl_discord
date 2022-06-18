from commands.commands import setup
from discord.ext import commands
from dotenv import load_dotenv
import os
import logging

load_dotenv()
TOKEN = os.environ['TOKEN']


logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

bot = commands.Bot(command_prefix=commands.when_mentioned_or("!"),
                   description='Relatively simple music bot example',)

setup(bot)
bot.run(TOKEN)
