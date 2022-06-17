import discord
from discord.ext import commands


class HelpCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    def _get_embed(self):
        color = 0x36ffa4

        embed = discord.Embed(color=color)
        embed.title="Available commands:"
        embed.set_thumbnail(url=self.bot.user.avatar_url)
        embed.add_field(name="!hello", value="Welcome!", inline=False)
        embed.add_field(name="!hltb [game name]", value="Check how long to beat a game!", inline=False)
        embed.add_field(name="!steam info [game name]", value="Check Steam game's information!", inline=False)
        embed.add_field(name="!random", value="Flip a 100-sided coin!", inline=False)
        embed.add_field(name="!release add [game name] [date] [publisher]", value="Add game to releases!", inline=False)
        embed.add_field(name="!release delete [game name] [date] [publisher]", value="Delete game from releases!", inline=False)
        embed.add_field(name="!snipe", value="Take a look at recently deleted message!", inline=False)
        embed.add_field(name="!konradobocie czy [something]", value="What does the bot about [something]?", inline=False)
        embed.add_field(name="!help", value="You are literally reading this.", inline=False)

        return embed


    @commands.command(name="gigahelp")
    async def help_com(self, ctx):
        embed_to_send = self._get_embed()
        await ctx.channel.send(embed=embed_to_send)
