from discord.ext import commands
from Waiter import Waiter


class ReleaseCommand(commands.Cog):
    def __init__(self, bot, waiter):
        self.bot = bot
        self.waiter = waiter


    @commands.group()
    async def release(self, ctx):
        if ctx.invoked_subcommand is None:
            await ctx.send("Unknown command.")


    #TO-DO refactor
    @release.command()
    async def add(self, ctx, *message_content: str):
        date = next(x for x in message_content if "." in x)
        date_index = message_content.index(date)
        title = " ".join(message_content[:date_index])
        developer = " ".join(message_content[date_index+1:])

        message_to_send = self.waiter.add_date(title, date, developer)
        await ctx.channel.send(message_to_send)


    @release.command()
    async def delete(self, ctx, *message_content: str):
        date = next(x for x in message_content if "." in x)
        date_index = message_content.index(date)
        title = " ".join(message_content[2:date_index])
        developer = " ".join(message_content[date_index+1:])

        message_to_send = self.waiter.delete_date(title, date, developer)
        await ctx.channel.send(message_to_send)
