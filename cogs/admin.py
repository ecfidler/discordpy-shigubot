from discord.ext import commands
import discord
import asyncio
from typing import Optional


def setup(bot):
    bot.add_cog(Admin(bot))

class Admin(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(help="a basic ping for testing if the bot is responsive", brief="ping!")
    async def flip(self, ctx):
        await ctx.send("flop!")

    @commands.is_owner()
    @commands.command(hidden=True)
    async def echo(self, ctx, channel: Optional[discord.TextChannel], *, content: str):
        if channel:
            await channel.send(content)
        else:
            await ctx.send(content)

    @commands.is_owner()
    @commands.command(hidden=True)
    async def bye(self, ctx):
        await ctx.message.add_reaction("👋")

        extensions = self.bot.extensions.copy()

        for ext in extensions:
            self.bot.unload_extension(ext)

        await self.bot.close()
    
    @commands.is_owner()
    @commands.command(hidden=True)
    async def reload(self, ctx, arg: str):
        if "all" in arg:
            for ext in self.bot.extensions:
                self.bot.reload_extension(ext)
            await ctx.send('Reloading ' + ', '.join([(str(x)) for x in self.bot.extensions]))
        else:
            self.bot.reload_extension(arg)
            await ctx.send('Reloading ' + arg)

    @commands.is_owner()
    @commands.command(hidden=True)
    async def retrofit(self, ctx):
        # add in subprocess that gits it up to date, then reloads all cogs 
        pass


