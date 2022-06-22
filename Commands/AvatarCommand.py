import discord
from discord.ext import commands


class AvatarCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    async def avatar(self, ctx, *, member: discord.Member = None):
        if not member:
            user_avatar = "Specify right person!"
        user_avatar = member.avatar_url

        await ctx.send(user_avatar)
