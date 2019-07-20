import discord

def transcribe(message,pinner):
    content = message.content

    userColor = message.author.top_role.colour.value

    takenMessage=discord.Embed(title=content, color=userColor)

    for attachment in message.attachments:
        #content += attachment.url
        takenMessage.set_image(url=attachment.url)
    userName = message.author.display_name
    pFP = message.author.avatar_url
    channel = message.channel.name
    created = message.created_at # returns datetime.datetime
    jumpLink = message.jump_url
    realDate = str(created.month) + "/" + str(created.day) + "/" + str(created.year)
    footer = str(str(channel) + " | " + str(realDate) + " | pinned by " + str(pinner))

    takenMessage.set_author(name=userName, url=jumpLink,icon_url=pFP)
    takenMessage.set_footer(text=footer)
    return takenMessage

