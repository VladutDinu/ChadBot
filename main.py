import discord
from discord.ext import commands
import music

client=commands.Bot(command_prefix="$", intents=discord.Intents.all())

client.run("6cb9749248a6a303964e22212938fff138bf2f1e004f110d492db86d8880529f")

cogs=[music]

for i in range(len(cogs)):
    cogs[i].setup(client)

