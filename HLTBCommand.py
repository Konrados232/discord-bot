from discord.ext import commands
from APIs.HowLongToBeatAPIHandler import HowLongToBeatAPIHandler
from APIs.HowLongToBeatAPICleaner import HowLongToBeatAPICleaner
from APIs.HowLongToBeatEmbed import HowLongToBeatEmbed


class HLTBCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        base_dict = {
            "name" : "",
            "image_url": "",
            "gameplay_main" : "",
            "gameplay_main_extra" : "",
            "gameplay_completionist" : ""
        }
        self.hltb_handler = HowLongToBeatAPIHandler()
        self.hltb_cleaner = HowLongToBeatAPICleaner(base_dict)
        self.hltb_embed = HowLongToBeatEmbed()


    @commands.command()
    async def hltb(self, ctx, *message_content: str):
        joined_message = " ".join(message_content)
        embed_to_send = ""
        fetched_data = self.hltb_handler.fetch_data(joined_message)
        if fetched_data is not None:
            cleaned_data = self.hltb_cleaner.clean_data(fetched_data)
            embed_to_send = self.hltb_embed.get_embed(cleaned_data)

        await ctx.channel.send(embed=embed_to_send)
