import discord
from discord.ext import commands
import youtube_dl
import time
import random

class rps(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.choices = ['rock', 'paper', 'scissors']
    
    @commands.command()
    async def rps(self, ctx, choice):
        if choice in self.choices:
            chance = random.randint(1,1000)
            if(chance == 1 or chance == 999):
                await ctx.send('I AGREE AS A CHAD TO NAME YOU THE MASTER OF ROCK, PAPER, SCISSORS')
            else:
                if choice in "rock":
                    await ctx.send('PAPER! IT IS OK LITTLE CHAD, MAYBE NEXT TIME, DO NOT LOSE YOURSELF, TRAIN HARDER!')
                if choice in "paper":
                    await ctx.send('SCISSORS! IT IS OK LITTLE CHAD, MAYBE NEXT TIME, DO NOT LOSE YOURSELF, TRAIN HARDER!')
                if choice in "scissors":
                    await ctx.send('ROCK! IT IS OK LITTLE CHAD, MAYBE NEXT TIME, DO NOT LOSE YOURSELF, TRAIN HARDER!')
        else:
            await ctx.send('A CHAD SHOULD HAVE KNOWN HOW TO WRITE IN A CORRECT WAY, PLEASE CHOSE FROM : rock, paper, scissors')

def setup(client):
    client.add_cog(rps(client))