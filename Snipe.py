import discord
from discord.ext import commands
from collections import namedtuple

class Snipe(commands.Cog):
    def __init__(self, bot):
        self.deleted_messages = { }
        self.bot = bot

    @commands.Cog.listener()
    async def on_message_delete(self, message):
        channel_id = message.channel.id
        print(channel_id)
        author = f"{message.author.name}"
        content = f"{message.content}"
        self.deleted_messages[channel_id] = (author, content)

    def get_snipe_message(self, channel_id):
        if self.deleted_messages[channel_id] == None:
            return "There is nothing to snipe."

        return f"{self.deleted_messages[channel_id][0]} wysłał {self.deleted_messages[channel_id][1]}"
    