import discord
from discord.ext import commands
from collections import namedtuple
from datetime import datetime

class Snipe(commands.Cog):
    def __init__(self, bot):
        self.deleted_messages = { }
        self.bot = bot

    @commands.Cog.listener()
    async def on_message_delete(self, message):
        channel_id = message.channel.id
        print(channel_id)
        avatar = message.author.avatar_url
        author = message.author.name
        content = message.content
        date = message.created_at
        self.deleted_messages[channel_id] = (author, content, date, avatar)

    def get_snipe_embed(self, channel_id):
        print(channel_id)
        if self.deleted_messages[channel_id] == None:
            return "There is nothing to snipe."

        author_title = f"{self.deleted_messages[channel_id][0]}:"
        time_deleted =  datetime.strftime(self.deleted_messages[channel_id][2], "%d.%m.%Y %H:%M:%S")
        color = 0x00ff00
       
        embed = discord.Embed(color=color)
        embed.set_author(name=author_title, icon_url=self.deleted_messages[channel_id][3])
        # this character makes name dissapear
        embed.add_field(name="\u200b", value=self.deleted_messages[channel_id][1], inline=False)
        embed.set_footer(text=time_deleted)
        #embed.set_thumbnail(url=self.deleted_messages[channel_id][3])

        return embed
    