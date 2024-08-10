import os

import discord
from discord.ext import commands 
from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

intents = discord.Intents.all()

client = commands.Bot(command_prefix='!',intents=intents)

@client.event
async def on_ready():
    print("The bot is ready for use")
    print("------------------------")


@client.command()
async def hello(ctx):
    await ctx.send("Hello i am utube bot")


client.run(os.environ.get("DISCORD_API_SECRET"))
