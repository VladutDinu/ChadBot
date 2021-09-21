import discord
from discord.ext import commands
import music
import rps
import predictor
import os
import tensorflow as tf
import help
token = ''
with open('config.env', 'r') as conf:
    token = conf.readline().split('=')[1]
client=commands.Bot(command_prefix="$", intents=discord.Intents.all())


cogs=[music, rps, predictor, help]

for i in range(len(cogs)):
    cogs[i].setup(client)

client.run(token)