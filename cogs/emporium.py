from discord.ext import commands
import discord
import asyncio
import random
import os

from .util_checks import is_yoni, is_chef
from .util_macros import RULES, MILD, SPICY, YPANTRY, FPANTRY, TPANTRY, KITCHEN, BLUE, RED, PURPLE

sauce_messages = ["earned 3 michelin stars!","was some good shit.","brought tears to the chefs' eyes.","caught the attention of a chef!","deserved special recgnition!"]

pantries = {
    196742230659170304 : YPANTRY, # yoni
    173839815400357888 : FPANTRY, # fops
    316272031022841856 : TPANTRY # tbone
}

def setup(bot):
    bot.add_cog(Emporium(bot))

class Emporium(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.image_path = os.path.join(self.bot.source_path,'images','chefchoice.jpg')

    async def push_image(self,message,destination,text=True):
        async with message.channel.typing():
            if text:
                out = "{user}\'s post in {channel} {special_message}".format(user=message.author.mention, channel=message.channel.mention, special_message=random.choice(sauce_messages))
            else:
                out = ""
            
            await message.attachments[-1].save(self.image_path)
            image = discord.File(self.image_path)

            await self.bot.get_channel(destination).send(out, file=image)

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):

        if not (is_yoni(payload) and is_chef(payload.member)):
            return

        message = await self.bot.get_channel(payload.channel_id).fetch_message(payload.message_id)

        if payload.emoji.name == BLUE:
            await self.push_image(message,MILD)

        if payload.emoji.name == RED:
            await self.push_image(message,SPICY)

        if payload.emoji.name == PURPLE:
            dest = pantries.get(payload.member.id,KITCHEN) # returns the id of #kitchen if used by non pantried chef
            await self.push_image(message,dest,False)

        