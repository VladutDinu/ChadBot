import discord
from discord.ext import commands
import music
import os
token = ''
with open('config.env', 'r') as conf:
    token = conf.readline().split('=')[1]
client=commands.Bot(command_prefix="$", intents=discord.Intents.all())



cogs=[music]

for i in range(len(cogs)):
    cogs[i].setup(client)

client.run(token)