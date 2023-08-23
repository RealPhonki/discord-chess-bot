import discord
import nextcord
import chess
from discord.ext import commands

class ChessHandler():
    def __init__(self, fen):
        self.board = chess.Board()

        if fen != None: self.board.set_board_fen(fen)

class Ping(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.slash_command()
    async def start_match(self, ctx):
        # create board

        # send embed with move choices

        # when a move is selected by a player

        pass

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