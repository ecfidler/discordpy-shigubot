#from discord.ext import commands
import discord

#from macros import WHID, YONI, RULES, MILD, SPICY, YPANTRY, FPANTRY, TPANTRY, MAJOR, CHEF


# Temp Macros

WHID = 173840048343482368 # what have i done
YONI = 592214628550049794 # yoni's sauce emporium

RULES = 592216496659496990 # rules channel in sauce emporium
MILD = 592222434396995604 # chef's choice mild in sauce emporium
SPICY = 592225505592344577 # chef's choice spicy in sauce emporium
YPANTRY = 688202956599853199 # yoni's pantry in sauce emporium
FPANTRY = 688213248163709112 # fops' pantry in sauce emporium
TPANTRY = 771774117422301215 # tbone's pantry in sauce emporium

MAJOR = 374095810868019200
CHEF = 676571207323090944

# Server Checks

def is_whid(payload):
    return payload.member.guild.id == WHID

def is_yoni(payload):
    return payload.member.guild.id == YONI

# Channel Checks

def is_rules(channel):
    return channel.id == RULES

def is_mild(channel):
    return channel.id == MILD

def is_spicy(channel):
    return channel.id == SPICY

def is_yPantry(channel):
    return channel.id == YPANTRY

def is_fPantry(channel):
    return channel.id == FPANTRY

def is_tPantry(channel):
    return channel.id == TPANTRY

# Role Checks

def is_major(member):
    return any([role.id == MAJOR for role in member.roles])

def is_chef(member):
    return any([role.id == CHEF for role in member.roles])