# import stuff
import discord
from discord.ext import commands
import io

# this code runs from the directory that "main.py" is in
from logic.chess_handler import ChessHandler

# dropdown formatting
class DropdownMenu(discord.ui.Select):
    def __init__(self, cog, ctx: commands.Context, options: list) -> None:
        self.cog = cog
        self.ctx = ctx
        self.client = cog.client
        self.chess_handler = cog.chess_handler
        super().__init__(placeholder="Play a move", max_values=1, min_values=1, options=options)

    async def callback(self, interaction: discord.Interaction) -> None:
        await interaction.response.send_message(content=f'Played move: {self.values[0]}', ephemeral=True)
        self.chess_handler.board.push_san(self.values[0])

        discord_file = self.cog.board_image()
        embed = self.cog.board_embed(self.ctx)
        view = self.cog.legalmove_dropdown(self.ctx)

        await self.ctx.send(embed=embed, view=view, file=discord_file)

class ChessCommands(commands.Cog):
    def __init__(self, client: commands.Bot) -> None:
        self.client = client
        self.chess_handler = ChessHandler()

    def board_image(self) -> discord.File:
        """ Returns an image of the board """
        # gets raw png data from the chess_handler class
        image = self.chess_handler.get_board_png()

        # save the image to BytesIO stream
        image_stream = io.BytesIO()
        image.save(image_stream, format = "PNG")
        image_stream.seek(0) # move the stream cursor to the beginning

        # generate discord file instance for formatting
        return discord.File(image_stream, filename="board_img.png")

    def board_embed(self, ctx: commands.Context) -> discord.Embed:
        """ Creates the discord embed instance and returns it """
        # create embed
        embed = discord.Embed(
            title = "Chess game",
            color = discord.Color.gold()      # ctx.author.color
        )
        embed.set_image(url='attachment://board_img.png')
        embed.set_author(name = f'Requested by {ctx.author.name}', icon_url = ctx.author.avatar)
        return embed

    def legalmove_dropdown(self, ctx: commands.Context) -> discord.ui.View:
        """ Gets the dropdown view ui item"""
        legal_moves = self.chess_handler.legal_moves_str
        options = [discord.SelectOption(label = move) for move in legal_moves]
        dropdown = DropdownMenu(self, ctx, options)
        view = discord.ui.View()
        view.add_item(dropdown)
        return view

    @commands.command()
    async def display_board(self, ctx: commands.Context) -> None:
        await ctx.send(content="```Running command```")
        discord_file = self.board_image()
        await ctx.send("```Generated image file```")
        embed = self.board_embed(ctx)
        await ctx.send("```Created fancy embed```")
        view = self.legalmove_dropdown(ctx)
        await ctx.send("```Generated dropdown view```")

        try:
            await ctx.send(embed=embed, file=discord_file, view=view)
            await ctx.send("```Message sent successfully```")
        except:
            await ctx.send("```Failed to send message```")

# add cog extension to "client" (the bot)
# NOTE: THIS CODE RUNS FROM THE DIRECTORY THAT "main.py" IS IN
async def setup(client):
    await client.add_cog(ChessCommands(client))