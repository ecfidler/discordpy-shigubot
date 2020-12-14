from discord.ext import commands
import discord
import asyncio
import random
import os

from .util_checks import is_yoni, is_chef
from .util_macros import RULES, VALET, MILD, SPICY, YPANTRY, FPANTRY, TPANTRY, KITCHEN, BLUE, RED, PURPLE, PATRON, NSFW, SPEAK, SPEAKALT

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
        
        member = payload.member

        if not (is_yoni(member)):
            return

        channel = await self.bot.get_channel(payload.channel_id)
        message = await channel.fetch_message(payload.message_id)

        if (channel == RULES and (payload.emoji.name == SPEAK or payload.emoji.name == SPEAKALT)):
            await member.add_roles(member.guild.get_role(NSFW))
            return

        # Chef only Commands

        if not is_chef(member):
            return

        # Push Images to Pantries

        if payload.emoji.name == BLUE:
            await self.push_image(message,MILD)
            return

        if payload.emoji.name == RED:
            await self.push_image(message,SPICY)
            return

        if payload.emoji.name == PURPLE:
            dest = pantries.get(member.id,KITCHEN) # returns the id of #kitchen if used by non pantried chef
            await self.push_image(message,dest,False)
            return

    @commands.Cog.listener()
    async def on_member_join(self, member):

        if not is_yoni(member):
            return
        
        owner = "<@{fops}>".format(fops=self.bot.owner_id)

        out = "Ohayo {user}!\nWelcome to Yoni's Sauce Emporium! Please take a second to read the {rules} channel before getting lost in the sauce. If you have any questions, feel free to ask {fops}.".format(user=member.mention, rules=self.bot.get_channel(RULES).mention, fops=owner)
        
        await self.bot.get_channel(VALET).send(out)
        await member.add_roles(member.guild.get_role(PATRON))