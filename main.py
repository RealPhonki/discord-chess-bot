import discord
from discord.ext import commands, tasks
from itertools import cycle
import logging
import platform
import os
import asyncio

TOKEN = "MTE0MzcwOTU3NDY4ODQxOTk0MA.GqZCjC.mWGAQNzGVPVO9zeifQ-nVyNmHZf_3LRk10ZJ30"
client = commands.Bot(command_prefix="/", intents=discord.Intents.all())

class LoggingFormatter(logging.Formatter):
    # Colors
    black = "\x1b[30m"
    red = "\x1b[31m"
    green = "\x1b[32m"
    yellow = "\x1b[33m"
    blue = "\x1b[34m"
    gray = "\x1b[38m"
    # Styles
    reset = "\x1b[0m"
    bold = "\x1b[1m"

    COLORS = {
        logging.DEBUG: gray + bold,
        logging.INFO: blue + bold,
        logging.WARNING: yellow + bold,
        logging.ERROR: red,
        logging.CRITICAL: red + bold,
    }

    def format(self, record):
        log_color = self.COLORS[record.levelno]
        format = "(black){asctime}(reset) (levelcolor){levelname:<8}(reset) (green){name}(reset) {message}"
        format = format.replace("(black)", self.black + self.bold)
        format = format.replace("(reset)", self.reset)
        format = format.replace("(levelcolor)", log_color)
        format = format.replace("(green)", self.green + self.bold)
        formatter = logging.Formatter(format, "%Y-%m-%d %H:%M:%S", style="{")
        return formatter.format(record)

logger = logging.getLogger("discord_bot")
logger.setLevel(logging.INFO)

# Console handler
console_handler = logging.StreamHandler()
console_handler.setFormatter(LoggingFormatter())

# File handler
file_handler = logging.FileHandler(filename="discord.log", encoding="utf-8", mode="w")
file_handler_formatter = logging.Formatter(
    "[{asctime}] [{levelname:<8}] {name}: {message}", "%Y-%m-%d %H:%M:%S", style="{"
)
file_handler.setFormatter(file_handler_formatter)

# Add the handlers
logger.addHandler(console_handler)
logger.addHandler(file_handler)
client.logger = logger

@tasks.loop(seconds=5)
async def change_status():
    bot_status = cycle(["Bullet Chess", "with you", "Classic Chess", "Cricket", "Duck Chess", "Atomic Chess", "Fog of war Chess"])
    await client.change_presence(activity=discord.Game(next(bot_status)))

@client.event
async def on_ready():
    client.logger.info(f"Logged in as {client.user.name}")
    client.logger.info(f"discord.py API version: {discord.__version__}")
    client.logger.info(f"Python version: {platform.python_version()}")
    client.logger.info(f"Running on: {platform.system()} {platform.release()} ({os.name})")
    client.logger.info("-------------------")
    change_status.start()

async def load():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            extension = filename[:-3]
            try:
                await client.load_extension(f"cogs.{extension}")
                client.logger.info(f"Loaded extension '{extension}'")
            except Exception as e:
                exception = f"{type(e).__name__}: {e}"
                client.logger.error(f"Failed to load extension {extension}\n{exception}")

async def main():
    async with client:
        await load()
        await client.start(TOKEN)

asyncio.run(main())