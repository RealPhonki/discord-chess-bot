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
        image = self.chess_handler.get_board_png()

        # save the image to BytesIO stream
        image_stream = io.BytesIO()
        image.save(image_stream, format = "PNG")
        image_stream.seek(0) # move the stream cursor to the beginning

        # generate image file
        discord_file = discord.File(image_stream, filename="board_img.png")

        # create embed
        embed_message = discord.Embed(
            title = "Chess game",
            color = discord.Color.gold()      # ctx.author.color
        )
        embed_message.set_image(url='attachment://board_img.png')
        embed_message.set_author(name = f'Requested by {ctx.author.name}', icon_url = ctx.author.avatar)
        
        await ctx.send(embed=embed_message, file=discord_file)

    @commands.command()
    async def test_dropdown(self, ctx):
        await ctx.send("Test", view=SelectView())

async def setup(client):
    await client.add_cog(ChessMatch(client))