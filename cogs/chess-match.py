import discord
from discord.ext import commands
import io

from logic.chess_handler import ChessHandler

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

class ChessMatch(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.chess_handler = ChessHandler()
    
    @commands.command()
    async def display_board(self, ctx):
        # get pillow image
        image = self.chess_handler.checker_board

        # save the image to BytesIO stream
        image_stream = io.BytesIO()
        image.save(image_stream, format = "PNG")
        image_stream.seek(0) # move the stream cursor to the beginning

        # generate discord file
        discord_file = discord.File(image_stream, filename="board_img.png")
        
        await ctx.send(file=discord_file)

    @commands.command()
    async def test_dropdown(self, ctx):
        await ctx.send("Test", view=SelectView())
        # create board

        # send embed with move choices

        # when a move is selected by a player

async def setup(client):
    await client.add_cog(ChessMatch(client))
