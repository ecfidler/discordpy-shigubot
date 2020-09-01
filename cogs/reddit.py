#! usr/bin/env python3
import praw
import random 
import os
from typing import Optional

from discord.ext import commands
import discord

def setup(bot):
    bot.add_cog(Startup(bot))

class Startup(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.reddit = self.redditLogin()
        self.pastaList = self.getPasta()

    def redditLogin(self):
        with open(os.path.join(self.bot.source_path,'keychain','redditkey.txt')) as file:
            keys = file.read().split('\n')
        
        reddit = praw.Reddit(client_id=keys[0],client_secret=keys[1],user_agent=keys[2],username=keys[3],password=keys[4])
        print(f'Logged into reddit as: {reddit.user.me()}')

        return reddit

    def getPasta(self):
        pasta = self.reddit.subreddit('copypasta').hot(limit=100)
        pastaBuffer = [submission.selftext for submission in pasta]
        random.shuffle(pastaBuffer)
        return pastaBuffer

    @commands.command(help="gets a copypasta from r/copypasta",brief="copypasta")
    async def pasta(self, ctx, *tts):
        speak = "tts" in tts
        if not self.pastaList:
            self.pastaList = self.getPasta()
        await ctx.message.add_reaction("🍜")
        try:
            await ctx.send(self.pastaList.pop(),tts=speak)
        except discord.errors.HTTPException:
            await ctx.send("sorry, pasta too LONG to display :flushed:")


        