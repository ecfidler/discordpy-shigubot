import discord

from util_macros import WHID, YONI, RULES, MILD, SPICY, YPANTRY, FPANTRY, TPANTRY, MAJOR, CHEF

# Server Checks

def is_whid(payload):
    return payload.member.guild.id == WHID

def is_yoni(member):
    return member.guild.id == YONI

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