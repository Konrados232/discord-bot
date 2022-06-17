import discord

class SteamAPIEmbed:
    def __init__(self):
        pass


    def _beautify_list(self, game_list):
        return ", ".join(game_list)

    def get_embed(self, data):
        color = 0x8a0094

        embed = discord.Embed(color=color)
        embed.title=data["name"]
        embed.set_author(name="Steam Game Info:")
        embed.set_thumbnail(url=data["header_url"])
        embed.add_field(name="Description", value=data["desc"], inline=False)
        embed.add_field(name="Developers", value=data["developer"], inline=False)
        embed.add_field(name="Publishers", value=data["publisher"])
        embed.add_field(name="Categories", value=self._beautify_list(data["categories"]), inline=False)
        embed.add_field(name="Genres", value=self._beautify_list(data["genres"]), inline=False)
        embed.add_field(name="Release Date", value=data["release_date"], inline=False)
        embed.add_field(name="Number of achievements", value=data["achievements"], inline=False)
        embed.add_field(name="Platforms", value=self._beautify_list(data["platforms"]), inline=False)

        return embed

