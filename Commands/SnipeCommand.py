import discord
from discord.ext import commands
from datetime import datetime


class SnipeCommand(commands.Cog):
    def __init__(self, bot, snipe_listener):
        self.bot = bot
        self.snipe_listener = snipe_listener


    def get_embed(self, channel_id):
        deleted_message = self.snipe_listener.get_snipe_data(channel_id)
        if deleted_message == None:
                return "There is nothing to snipe."

        author_title = f"{deleted_message[0]}:"
        time_deleted =  datetime.strftime(deleted_message[2], "%d.%m.%Y %H:%M:%S")
        color = 0x00ff00
    
        # message must be description in order not to have a gap
        embed = discord.Embed(color=color, description=deleted_message[1])
        embed.set_author(name=author_title, icon_url=deleted_message[3])
        embed.set_footer(text=time_deleted)
        #embed.set_thumbnail(url=deleted_message[3])

        return embed


    @commands.command()
    async def snipe(self, ctx):
        embed_to_send = self.get_embed(ctx.channel.id)
        await ctx.send(embed=embed_to_send)
