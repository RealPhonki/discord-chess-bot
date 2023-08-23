import discord
import chess
from discord.ext import commands

class ChessHandler():
    def __init__(self, fen):
        self.board = chess.Board()

        if fen != None: self.board.set_board_fen(fen)

class Select(discord.ui.Select):
    def __init__(self):
        options = [
            discord.SelectOption(lable="test option 1", description="test"),
            discord.SelectOption(lable="test option 2", description="test"),
            discord.SelectOption(lable="test option 3", description="test"),
            discord.SelectOption(lable="test option 4", description="test")
        ]
        super().__init__(placeholder="Select an option", max_values=1, min_values=1, options=options)

class SelectView(discord.ui.View):
    def __init__(self, *, timeout = 180):
        super().__init__(timeout=timeout)
        self.add_item(Select())

class Ping(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.slash_command()
    async def test_dropdown(self, ctx):
        await ctx.send("Test", view=Select())
        # create board

        # send embed with move choices

        # when a move is selected by a player


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