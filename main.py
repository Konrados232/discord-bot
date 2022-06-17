import discord
from discord.ext import commands
import json

from Commands.HLTBCommand import HLTBCommand
from Commands.HelloCommand import HelloCommand
from Commands.HelpCommand import HelpCommand
from Commands.KonradobocieCommand import KonradobocieCommand
from Commands.KonradobotCommand import KonradobotCommand
from Commands.RandomCommand import RandomCommand
from Commands.ReleaseCommand import ReleaseCommand
from Commands.SnipeCommand import SnipeCommand
from Commands.SteamCommand import SteamCommand
from Commands.ValCommand import ValCommand
from Listeners.SnipeListener import SnipeListener
from Shared.Waiter import Waiter
from Shared.Utils import Utils

# useful methods

def strip_name(name):
    name_string = str(name)
    return name_string.split("#")[0]

def get_stripped_message(message):
    message_string = str(message)
    x = message_string.split("bocie")
    print(x[0])
    print(x[1])
    return x[0]

def strip_message(message):
    message_string = str(message)
    item_name = message_string.split("craft")[1]
    return item_name.strip()

def reminder():
    return "Pamiętaj o potku"

def read_release_date_data_json():
    with open('datafiles/release_dates.json', 'r') as f:
        data = json.load(f)
    return data

def split_sentence_combination(sentence):
    every_word = sentence.split()
    every_word = [a for a in every_word]
    return every_word

def check_name_mention(reminder_list, sentence):
    print(reminder_list)
    print(sentence)
    for d in reminder_list:
        splitted_name = split_sentence_combination(d['name'])
        print(d)
        for part in splitted_name:
            print(part)
            if not part.isdigit() and part in sentence:
                return d['name']
    
    return None


#client = discord.Client()
intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

data_read = read_release_date_data_json()
waiter = Waiter(data_read)

# listeners

snipe_listener = SnipeListener(bot)
bot.add_cog(snipe_listener)


# commands
hello_command = HelloCommand(bot)
bot.add_cog(hello_command)

random_command = RandomCommand(bot)
bot.add_cog(random_command)

help_command = HelpCommand(bot)
bot.add_cog(help_command)

konradobot_command = KonradobotCommand(bot)
bot.add_cog(konradobot_command)

konradobocie_command = KonradobocieCommand(bot)
bot.add_cog(konradobocie_command)

val_command = ValCommand(bot)
bot.add_cog(val_command)

release_command = ReleaseCommand(bot, waiter)
bot.add_cog(release_command)

snipe_command = SnipeCommand(bot, snipe_listener)
bot.add_cog(snipe_command)

hltb_command = HLTBCommand(bot)
bot.add_cog(hltb_command)

steam_command = SteamCommand(bot)
bot.add_cog(steam_command)

@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")

    
@bot.event
async def on_message(message):
    await bot.process_commands(message)
    
    if message.author == bot.user:
        return
        
    if Utils.super_randomize() == 42:
       await message.channel.send("Randomowa wiadomość!")

    if "bocie" in message.content and "konradobocie" not in message.content:
        name = strip_name(message.author)
        message_to_send = get_stripped_message(message.content)
        await message.channel.send(message_to_send + name)
        
    if "ඞ" in message.content or "U+0D9E" in message.content or "u0D9E" in message.content:
        await message.channel.send("podejrzane")

    if "potek" in message.content.lower():
        name = strip_name(message.author)
        message_to_send = reminder()
        await message.channel.send(message_to_send + " " + name + "!")
        
    if "nie dam rady" in message.content.lower():
        name = strip_name(message.author)
        await message.channel.send("Dasz radę " + name + "!")

    if "kiedy" in message.content.lower() or "za ile" in message.content.lower():
        title = check_name_mention(waiter.get_release_dates(), message.content)
        print(title)
        if title is not None:
            message_to_send = waiter.release_date_time(name=title)
            await message.channel.send(f"{message_to_send} {message.author.mention}!")

    if "konradobocie" in message.content.lower() and "co robiłeś, że cię nie było" in message.content.lower():
        await message.channel.send(f"Czytałem lore Dark Souls")



with open("secretkey") as f:
    secret_key = f.readline()


bot.run(secret_key)
