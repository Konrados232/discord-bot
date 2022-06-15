import discord

class HowLongToBeatEmbed:
    def __init__(self):
        pass


    def get_embed(self, data):
        url = r"https://howlongtobeat.com"
        color = 0x1b2ba6
        image_url = f"{url}{data['image_url']}"

        embed = discord.Embed(color=color)
        embed.title=data["name"]
        embed.set_author(name="How Long To Beat?")
        embed.set_thumbnail(url=image_url)
        embed.add_field(name="Gameplay Main", value=data["gameplay_main"], inline=False)
        embed.add_field(name="Gameplay Main Extra", value=data["gameplay_main_extra"], inline=False)
        embed.add_field(name="Gameplay Completionist", value=data["gameplay_completionist"], inline=False)  

        return embed

