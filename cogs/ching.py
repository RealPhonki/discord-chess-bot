import discord
from discord.ext import commands

class Ping(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("ching.py status | ready")
    
    @commands.command()
    async def ping(self, ctx):
        bot_latency = round(self.client.latency * 1000)
        await ctx.send(f"pong : {bot_latency} ms")

    @commands.command()
    async def embed_test(self, ctx):
        embed_message = discord.Embed(
            title = "Tile of Embed",
            description = "Description Test",
            color = discord.Color.random()      # ctx.author.color
        )

async def setup(client):
    await client.add_cog(Ping(client))