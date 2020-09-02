from discord.ext import commands
import discord
import asyncio
import os

# Allows the audio to loop
class LoopingSource(discord.AudioSource):
    def __init__(self, source_factory):
        self.factory = source_factory
        self.source = source_factory()

    def read(self):
        ret = self.source.read()
        if not ret:
            self.source.cleanup()
            self.source = self.factory()
            ret = self.source.read()
        return ret

def setup(bot):
    bot.add_cog(Storm(bot))

class Storm(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        self.audio_path = os.path.join(bot.source_path,'sounds','storm.wav')

        self.audio = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio(self.audio_path))

        self.vol = .5

    def makeSource(self):
        audio_source = self.audio
        audio_source.volume = self.vol

        return audio_source

    async def startAudio(self, vc):
        audioLoop = LoopingSource(self.makeSource)
        vc.play(audioLoop)

    @commands.command(help="plays a looping soundscape of a thunderstorm", brief="starts a storm")
    async def toggledownfall(self, ctx):

        vc = ctx.guild.voice_client

        if not vc or vc not in self.bot.voice_clients:
            target = await ctx.author.voice.channel.connect()
            await self.startAudio(target)
            await ctx.message.add_reaction("🌩")

        elif vc.channel != ctx.author.voice.channel:
            await vc.disconnect()
            target = await ctx.author.voice.channel.connect()
            await self.startAudio(target)
            await ctx.message.add_reaction("🌩")

        else:
            await vc.disconnect()
            await ctx.message.add_reaction("☀")
        
    '''
    @commands.command(aliases=["vol"], help="changes the volume of the rain, default 50/100",brief="volume of rain")
    async def volume(self, ctx, *, value: int):
        if value > 100 or value < 0:
            await ctx.message.add_reaction("❌")
        else:
            vol = value * 0.01
            self.audio_source.source.volume = vol
            await ctx.message.add_reaction("✔")
    '''