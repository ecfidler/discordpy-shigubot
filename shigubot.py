'''
Written by Ethan Fidler, 2020

Next Goal: add in toggledownfall, new cog 'storm'

'''

# System Libraries

import asyncio
import os

# External Libraries

import discord
from discord.activity import Activity
from discord.enums import ActivityType
from discord.ext import commands

# Global Functions

def getText(file):
    with open(file, "r") as f:
        lines = f.read()
        return lines.strip()

# Variables

prefix = "$w "
source_path = os.path.dirname(os.path.abspath(__file__))
token = getText(os.path.join(source_path,'keychain','token.txt'))
owner = 173839815400357888 # @fops#1969

# Setup Client

bot = commands.Bot(prefix)

bot.source_path = source_path

bot.owner_id = owner

bot.load_extension('cogs.admin')
bot.load_extension('cogs.startup')
bot.load_extension('cogs.reddit')
bot.load_extension('cogs.storm')

# Run Client

bot.run(token)