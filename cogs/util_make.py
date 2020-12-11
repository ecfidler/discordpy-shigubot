import discord

video_types = ['.mov','.mp4','.mkv']

# Returns a lowlight pin (not starboard clone)
def transcribe(message,pinner):
    content = message.content

    userColor = message.author.top_role.colour.value

    takenMessage=discord.Embed(title="Message Content", description=content, color=userColor)

    for attachment in message.attachments:
        takenMessage.set_image(url=attachment.url)

    userName = message.author.display_name
    pfp = message.author.avatar_url
    channel = message.channel.name
    created = message.created_at # returns datetime.datetime
    jumpLink = message.jump_url
    realDate = str(created.month) + "/" + str(created.day) + "/" + str(created.year)
    footer = str(str(channel) + " | " + str(realDate) + " | pinned by " + str(pinner))

    jumpValue = "[Jump!](" + jumpLink + ")"
    takenMessage.add_field(name="Original Message",value=jumpValue)
    takenMessage.set_author(name=userName,icon_url=pfp)
    takenMessage.set_footer(text=footer)
    return takenMessage