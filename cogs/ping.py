import discord
from discord.ext import commands

class Ping(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.slash_command()
    async def ching(self, ctx):
        await ctx.tree.sync()

        bot_latency = round(self.client.latency * 1000)

        embed_message = discord.Embed(
            title = f"chong : {bot_latency} ms"
        )

        embed_message.set_author(
            name = f'Requested by {ctx.author.name}',
            icon_url = ctx.author.avatar
        )

        await ctx.send(embed = embed_message)

    @commands.command()
    async def embed_test(self, ctx):

        embed_message = discord.Embed(
            title = "Tile of Embed",
            description = "Description Test",
            color = discord.Color.gold()      # ctx.author.color
        )

        embed_message.set_author(name = f'Requested by {ctx.author.name}', icon_url = ctx.author.avatar)
        embed_message.set_thumbnail(url = ctx.guild.icon)
        embed_message.set_image(url = ctx.guild.icon)
        embed_message.add_field(name = "field name", value = "field value", inline = False)
        embed_message.set_footer(text = "This is a footer", icon_url = ctx.author.avatar)

        await ctx.send(embed = embed_message)

async def setup(client):
    await client.add_cog(Ping(client))