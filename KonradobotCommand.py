from discord.ext import commands


class KonradobotCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.group()
    async def konradobot(self, ctx):
        if ctx.invoked_subcommand is None:
            await ctx.send("A witam")


    @konradobot.command()
    async def przedmioty(self, ctx):
        # currently obsolete, prints default message instead
        #x = Scrap()
        #big_message = x.do_command()
        #await message.channel.send(f"Spis przedmiotów {message.author.mention} ```{big_message}```")
        await ctx.channel.send("Obecnie niedostępne.")
