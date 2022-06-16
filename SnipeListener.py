from discord.ext import commands


class SnipeListener(commands.Cog):
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

    
    def get_snipe_data(self, channel_id):
        return self.deleted_messages[channel_id]
