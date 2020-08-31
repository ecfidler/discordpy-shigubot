from discord.ext import commands
import discord
import asyncio
from typing import Optional


def setup(bot):
    bot.add_cog(Admin(bot))

class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.is_owner()
    @commands.command()
    async def flip(self,ctx):
        await ctx.send("flop!")

    @commands.is_owner()
    @commands.command()
    async def echo(self, ctx, channel: Optional[discord.TextChannel], *, content: str):
        if channel:
            await channel.send(content)
        else:
            await ctx.send(content)

    @commands.is_owner()
    @commands.command()
    async def bye(self,ctx):
        await ctx.message.add_reaction("👋")
        await self.bot.close()
    