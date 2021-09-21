import discord
from discord.ext import commands
import youtube_dl
import time
import random

class helper(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def helpls(self, ctx):
        await ctx.send('$join \n $rps <rock/paper/scissors> \n $predictor 1,2,3,4,5,6,7 (7 temperature values for Ploiesti City, KM 0) \n $play url (to play music from yt)\n')


def setup(client):
    client.add_cog(helper(client))