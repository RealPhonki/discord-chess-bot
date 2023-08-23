import discord
from discord.ext import commands

class Moderation(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.command()
    @commands.has_permissions(manage_messages=True)
    async def clean(self, ctx, count: int):
        await ctx.channel.purge(limit=count)

async def setup(client):
    await client.add_cog(Moderation(client))