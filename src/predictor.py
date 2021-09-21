import discord
from discord.ext import commands
import youtube_dl
import time
import random
import numpy as np
import tensorflow as tf
class predictor(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.window_size = 7
        self.model = tf.keras.models.load_model('../model_training/model/temp')

    @commands.command()
    async def predict(self, ctx, array):
        temp = [int(var) for var in array.split(',')]
        

        forecast=[]
        forecast.append(self.model.predict(np.array(temp).reshape(1,7)))

        results = np.array(forecast)[:, 0, 0]
        await ctx.send("THE TEMPERATURE FOR TOMMOROW WILL EXACTLY BE: "+str(results[0]))


def setup(client):
    client.add_cog(predictor(client))