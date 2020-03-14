''' source code https://github.com/DaRealFreak/saucenao

- Each "result" contains a dictionary.
- Each dictionary has 2 inner dictionaries, the header, and the data
- The header contains the similarity
- data contains 'title', 'content', and 'ext_urls'
- Content is a list of info about the image
- ext_urls is a list of urls
'''

import logging
from saucenao import SauceNao
#from shigubot import getText
import discord
import os

source_path = os.path.dirname(os.path.abspath(__file__))

def getText(file):
    with open(file, "r") as f:
        lines = f.read()
        return lines.strip()

key = getText(os.path.join(source_path,'keychain','saucekey.txt'))

saucenao = SauceNao(directory='directory', databases=999, minimum_similarity=65, combine_api_types=False, api_key=key,
                    exclude_categories='', move_to_categories=False,  use_author_as_category=False,
                    output_type=SauceNao.API_HTML_TYPE, start_file='', log_level=logging.ERROR,
                    title_minimum_similarity=90)

def makeSauceEmbed():

    results = saucenao.check_file(file_name=os.path.join(source_path,'images','sauce.jpg'))

    #results = saucenao.check_file(file_name="J:\\Github\\discordpy-shigubot\\images\\sauce.jpg") # os.path.join(source_path,'images','sauce.jpg')

    sauceEmbed = discord.Embed(title="Source[s] found:", color=0xea9cff)
    sauceEmbed.set_author(name="sauceNAO", url="https://saucenao.com/index.php", icon_url="attachment://icon.png")
    sauceEmbed.set_thumbnail(url="attachment://sauce.jpg")

    if results == []:
        sauceEmbed.add_field(name="No results :(", value="It may be an error with the bot, try checking the website", inline=False)
        return sauceEmbed

    for x in results:

        # for debugging
        #print(x['data']['content'])
        #print(x['data']['ext_urls'])
        
        for c in x['data']['content']:
            if c == '':
                continue
            c = c.split(":",1)
            name = c[0] + ":"
            sauceEmbed.add_field(name=name, value=c[1], inline=True)

        links = ""
        for a in x['data']['ext_urls']:
            if a == '':
                continue
            b = a.strip('https://')
            b = b.split("/")
            b = b[0]

            links += "["+b+"]"+"("+a+") \n"
        
        if links != "":
            sauceEmbed.add_field(name="Links:", value=links, inline=False)
    
    sauceEmbed.set_footer(text="Message @fops#1969 if you have any questions")

    return sauceEmbed
