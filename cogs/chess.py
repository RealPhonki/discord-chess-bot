import discord
import chess
from discord.ext import commands

class Select(discord.ui.Select):
    def __init__(self):
        options = [
            discord.SelectOption(label="test option 1", description="test"),
            discord.SelectOption(label="test option 2", description="test"),
            discord.SelectOption(label="test option 3", description="test"),
            discord.SelectOption(label="test option 4", description="test")
        ]
        super().__init__(placeholder="Select an option", max_values=1, min_values=1, options=options)

    async def callback(self, interaction: discord.Interaction):
        await interaction.response.send_message(content = f"Selected option {self.values}", ephemeral = True)

class SelectView(discord.ui.View):
    def __init__(self, *, timeout = 180):
        super().__init__(timeout=timeout)
        self.add_item(Select())

class Chess(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.command()
    async def start_match(self, ctx):
        board = chess.Board()

        await ctx.send(board)

    @commands.command()
    async def test_dropdown(self, ctx):
        await ctx.send("Test", view=SelectView())
        # create board

        # send embed with move choices

        # when a move is selected by a player

async def setup(client):
    await client.add_cog(Chess(client))