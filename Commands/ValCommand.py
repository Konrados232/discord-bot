from discord.ext import commands
from Shared.GameScraper import GameScraper


class ValCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.valheim = GameScraper()


    @commands.group()
    async def val(self, ctx):
        if ctx.invoked_subcommand is None:
            await ctx.send("Unknown command.")


    @val.command()
    async def craft(self, ctx, *message_content: str):
        print(message_content)
        big_message = self.valheim.get_item_info(list(message_content))
        await ctx.channel.send(f"Here's you recipe {ctx.author.mention} ```{big_message}```")
