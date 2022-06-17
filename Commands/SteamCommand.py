from discord.ext import commands

from APIs.SteamAPICleaner import SteamAPIHandlerCleaner
from APIs.SteamAPIEmbed import SteamAPIEmbed
from APIs.SteamAPIHandler import SteamAPIHandler
from APIs.SteamListConverter import SteamListConverter


class SteamCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.steam_handler = SteamAPIHandler()
        self.steam_cleaner = SteamAPIHandlerCleaner()
        self.steam_embed = SteamAPIEmbed()
        self.steam_converter = SteamListConverter()


    def _convert_name_to_appid(self, game_name):
        all_games_list = self.steam_converter.get_data()
        if game_name in all_games_list:
            return all_games_list[game_name]
        else:
            return None


    @commands.group()
    async def steam(self, ctx):
        if ctx.invoked_subcommand is None:
            await ctx.send("Unknown command.")


    @steam.command()
    async def info(self, ctx, *message_content: str):
        merged_content = "".join(message_content).lower()
        appid = self._convert_name_to_appid(merged_content)

        if appid is None:
            await ctx.channel.send("Couldn't find the game!")
        else:
            game_data = self.steam_handler.fetch_data(appid)
            cleaned_data = self.steam_cleaner.clean_data(game_data, appid)
            embed_to_send = self.steam_embed.get_embed(cleaned_data)
            await ctx.channel.send(embed=embed_to_send)

        