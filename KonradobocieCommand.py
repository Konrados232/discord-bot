from discord.ext import commands
from Utils import Utils


class KonradobocieCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.group()
    async def konradobocie(self, ctx):
        if ctx.invoked_subcommand is None:
            await ctx.send("No hej?")


    @konradobocie.command(name="czy")
    async def whether(self, ctx, message_content):
        if "popiera" in message_content or "popierasz" in message_content:
            await ctx.channel.send("Nikogo nie popieram, bo jestem botem")
            return
        random_number = Utils.randomize()
        this_message = ""
        if random_number < 25:
            this_message = "Jak najbardziej"
        elif 25 <= random_number < 50:
            this_message = "No w sumie czemu nie"
        elif 50 <= random_number < 75:
            this_message = "Kurde no ciężko stwierdzić"
        else:
            this_message = "Tylko nie to"
        await ctx.channel.send(this_message)
