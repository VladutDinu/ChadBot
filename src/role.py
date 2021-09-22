import discord
from discord.ext import commands
import youtube_dl
import time
import random

class role(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def pwease_uwu(self, ctx, user: discord.Member, channel_name: discord.channel.VoiceChannel):
        roles = []
        for x in user.roles:
            roles.append(str(x))

        if 'Nevaccinat' in roles:
            await user.move_to(channel_name)


def setup(client):
    client.add_cog(role(client))