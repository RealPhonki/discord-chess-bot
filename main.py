import discord
from discord.ext import commands, tasks
from itertools import cycle
import os
import asyncio

TOKEN = "MTE0MzcwOTU3NDY4ODQxOTk0MA.GqZCjC.mWGAQNzGVPVO9zeifQ-nVyNmHZf_3LRk10ZJ30"
client = commands.Bot(command_prefix="/", intents=discord.Intents.all())

bot_status = cycle(["Bullet Chess", "with you", "Classic Chess", "Cricket", "Duck Chess", "Atomic Chess", "Fog of war Chess"])

@tasks.loop(seconds=5)
async def change_status():
    await client.change_presence(activity=discord.Game(next(bot_status)))

@client.event
async def on_ready():
    print(f"Logged in as {client.user}")
    change_status.start()

async def load():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            await client.load_extension(f"cogs.{filename[:-3]}")

async def main():
    async with client:
        await load()
        await client.start(TOKEN)

asyncio.run(main())