'''

 A bot made for discord.py 1.0.1 by Ethan Fidler

 Emojis
 tada :: 🎉

 Todo:
 - When It's done, Take all of the weather based functions and **offload them**

 Other Features:

 - code spelling out words (alpha, bravo, delta)
 - poi
 - tarot card readings
 - minesweeper
 
 '''

import discord
import asyncio
import random

from help import helpEmbed
from dice import dice
from cards import drawCard
from pasta import getPasta
from forecast import getWeather
from pin import transcribe
from saucefinder import makeSauceEmbed

#globals
client = discord.Client()
authorId = 173839815400357888 # fops#1969
currentWeather = '.\\sounds\\rain.wav'
currStatus = discord.Activity(name="the rain | !weather help", type=discord.ActivityType.listening)
source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio(currentWeather))
vol = 0.25
currentClient = 0
#attachment images

#functions & classes

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

def getText(file):
    with open(file, "r") as f:
        lines = f.read()
        return lines.strip()

# weather / audio functions start here

def updateSource():
    tSource = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio(currentWeather))
    tSource.volume = vol
    return tSource

def checkWHID(message):
    if message.channel.guild.id != 173840048343482368:
        return

async def setVol(num,message):
    global vol
    global source
    if num > 100 or num < 0:
        await message.add_reaction("❌")
    else: 
        vol = num * 0.01
        source.source.volume = vol
        await message.add_reaction("✔")

async def join(message):
    if message.author.voice is not None:
        await message.author.voice.channel.connect()

async def leave(message):
    await message.guild.voice_client.disconnect()

async def setWeather(weatherIn,message):
    global currentWeather
    global currentClient
    global source

    #currentClient = updateClient(message)

    if weatherIn == 'clear':
        currentWeather = 'clear'
        await leave(message)
    else:
        try:
            await join(message)
        except:
            pass
        currentWeather = ".\\sounds\\" + weatherIn
        if client.voice_clients[currentClient].is_playing():
            client.voice_clients[currentClient].stop()
        source = LoopingSource(updateSource)
        client.voice_clients[currentClient].play(source)
        source.source.volume = vol
        print('Playing', currentWeather, '| at volume:', source.source.volume, '| In:',client.voice_clients[currentClient].guild)

async def weather(message):

    if " help" in message.content.lower(): #help command, tells user the working commands
        help_files = [discord.File(".\\images\\icon.png", filename="icon.png"),discord.File(".\\images\\doodle.png", filename="doodle.png")]
        await message.author.send(files=help_files,embed=helpEmbed)
        await message.add_reaction("✉")

    elif " rain" in message.content.lower(): # set the weather to rain
        await message.add_reaction("🌧")
        await setWeather("rain.wav",message)

    elif " thunderstorm" in message.content.lower(): # set the weather to a thunderstorm
        await message.add_reaction("⛈")
        await setWeather("storm.wav",message)

    elif " thunder" in message.content.lower(): # set the weather to just thunder
        await message.add_reaction("🌩")
        await setWeather("thunderonly.wav",message)

    elif " fire" in message.content.lower():
        await message.add_reaction("🔥")
        await setWeather("bonfire.wav",message)
    
    elif " clear" in message.content.lower(): # clears the weather
        await message.add_reaction("☀")
        await setWeather("clear",message)

    else: # error
        await message.add_reaction("❔")

# weather functions end here

async def play(message):
    global currentClient
    #currentClient = updateClient(message)
    client.voice_clients[currentClient].play(discord.FFmpegPCMAudio('.\\sounds\\rain.wav'))

async def snap(message):
    members = message.author.voice.channel.members
    toSnap = random.sample(members, int(len(members)/2))
    for member in toSnap:
        await member.move_to(client.get_channel(343939767068655616))

@client.event
async def on_ready():
    print(f" {client.user}, ready to sortie")
    await client.change_presence(activity=currStatus)

@client.event
async def on_raw_reaction_add(payload):
    if payload.emoji.name == "📌":
        checkWHID(await client.get_channel(payload.channel_id).fetch_message(payload.message_id))
        async with client.get_channel(payload.channel_id).typing():
            for role in client.get_guild(payload.guild_id).get_member(payload.user_id).roles:
                if role.id == 374095810868019200:
                    msg = await client.get_channel(payload.channel_id).fetch_message(payload.message_id)
                    await client.get_channel(580587430776930314).send(embed=transcribe(msg,client.get_guild(payload.guild_id).get_member(payload.user_id).display_name))
                    await client.get_channel(payload.channel_id).send("Pinned!")

    if payload.emoji.name == "🍝":
        async with client.get_channel(payload.channel_id).typing():
            msg = await client.get_channel(payload.channel_id).fetch_message(payload.message_id)
            try:
                await msg.attachments[-1].save(".\\images\\sauce.jpg")
                sauce_files = [discord.File(".\\images\\icon.png", filename="icon.png"),discord.File(".\\images\\sauce.jpg",filename="sauce.jpg")]
                try:
                    await msg.channel.send(files=sauce_files,embed=makeSauceEmbed())
                except Exception as e:
                    await msg.channel.send("Error, go tell #fops1969")
                    print(e)
            except:
                await msg.channel.send("No image found in message")
            

@client.event 
async def on_message(message): # Basically my Main
    print(f"{message.channel.guild.name[:4]} {message.channel}: {message.author}: {message.content}")

    if message.mention_everyone:
        message.channel.send("<:notification:544011898941734922>")
        print("Everyone just got pinged")

    if message.author == client.user:
        return

    if "!join" in message.content.lower(): # bot joins voice channel
        await join(message)

    if "!leave" in message.content.lower(): #bot leaves voice channel
        await leave(message)
        
    if "!drip" in message.content.lower(): # simple ping
        await message.channel.send("drop!")

    if "!flip" in message.content.lower(): # simple ping alt
        await message.channel.send("flop!")

    if "!say" in message.content.lower():
        await play(message)

    if "!ss" in message.content.lower().strip():
        guildId = message.channel.guild.id
        try:
            vcId = message.author.voice.channel.id
            URLmessage = "https://discordapp.com/channels/" + str(guildId) + "/" + str(vcId)
            await message.channel.send(URLmessage)
        except Exception as e:
            await message.channel.send("You aren't in a Voice Channel")
            print(e)

    if "!volume" in message.content.lower():
        msg = int(message.content.strip("!volume").strip())
        await setVol(msg,message)

    if "!bye" in message.content.lower(): # makes bot go offline
        if message.author.id == authorId:
            await message.add_reaction("👋")
            await client.close()

    if "!r" in message.content.lower():
        await message.add_reaction("🎲")
        await message.channel.send(dice(message.content.strip("!r")))

    if "!domt" in message.content.lower():
        async with message.channel.typing(): #added this line
            await message.add_reaction("🃏")
            card_file = discord.File(".\\images\\avdol.jpg", filename="avdol.jpg")
            await message.channel.send(file=card_file,embed=drawCard())

    if "!pasta" in message.content.lower():
        async with message.channel.typing(): #added this line
            await message.add_reaction("🍜")
            if "tts" in message.content.lower():
                await message.channel.send(getPasta(),tts=True)
            else:
                await message.channel.send(getPasta())

    if "!forecast " in message.content.lower():
        async with message.channel.typing(): #added this line
            pruned = message.content.lower().split(" ",2)[1].strip()
            await message.add_reaction("🌀")
            icon_file = discord.File(".\\images\\icon.png", filename="icon.png")
            await message.channel.send(file=icon_file,embed=getWeather(pruned))

    if "!thanos" in message.content.lower():
        checkWHID(message)
        async with message.channel.typing():
            for role in message.author.roles:
                if role.id == 374095810868019200:
                    await snap(message)
                    #await message.add_reaction("<a:snap:583370125592494081>")
                    await message.channel.send("<a:snap:583370125592494081>")
        

    if "!weather" in message.content.lower(): # weather commands (plays into an internal function for simplicity)
        await weather(message)
    
    elif "!toggledownfall" in message.content.lower(): #toggles between 'clear' and 'rain'
        if currentWeather == 'clear':
            await setWeather('rain',message)
            await message.add_reaction("🌧")
        else:
            await setWeather('clear',message)
            await message.add_reaction("☀")

client.run(getText(".\\keychain\\token.txt"))