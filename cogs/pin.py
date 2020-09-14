from discord.ext import commands
import discord
import asyncio
import os
from util.checks import is_whid, is_major
from util.macros import LOW, PIN
from util.make import transcribe

def setup(bot):
    bot.add_cog(Pin(bot))

class Pin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_raw_reaction_add(self,payload):

        emoji = payload.emoji.name

        # Verify the correct channal and Emoji
        if not (is_whid(payload) and emoji == PIN):
            return

        member = payload.member

        # Verify that the user has permissions to use command
        if not is_major(member):
            return

        message = await member.fetch_message(payload.message_id)

        pin_embed = transcribe(message,member.display_name)

        await self.bot.get_channel(LOW).send(embed=pin_embed)

        await message.channel.send("Pinned!")






        

        
        
