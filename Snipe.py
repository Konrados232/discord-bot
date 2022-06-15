import discord
from discord.ext import commands
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
       
        # message must be description in order not to have a gap
        embed = discord.Embed(color=color, description=self.deleted_messages[channel_id][1])
        embed.set_author(name=author_title, icon_url=self.deleted_messages[channel_id][3])
        embed.set_footer(text=time_deleted)
        #embed.set_thumbnail(url=self.deleted_messages[channel_id][3])

        return embed
    