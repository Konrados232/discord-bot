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
        author = f"{message.author.name}"
        content = f"{message.content}"
        date = message.created_at
        self.deleted_messages[channel_id] = (author, content, date, avatar)

    def get_snipe_embed(self, channel_id):
        if self.deleted_messages[channel_id] == None:
            return "There is nothing to snipe."

        title = f"{self.deleted_messages[channel_id][0]}:"
        color = 0x00ff00

        embed = discord.Embed(title=title, color=color)
        embed.add_field(name="", value=f"{self.deleted_messages[channel_id][1]}", inline=False)
        embed.set_footer(text=f"{self.deleted_messages[channel_id][2]}")
        embed.set_thumbnail(url=self.deleted_messages[channel_id][3])

        return embed
    