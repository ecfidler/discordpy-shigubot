from discord.ext import commands
import discord
import asyncio

status = discord.Activity(name="the rain", type=discord.ActivityType.listening)

def setup(bot):
    bot.add_cog(Startup(bot))

class Startup(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f" {self.bot.user}, ready to sortie")
        await self.bot.change_presence(activity=status)