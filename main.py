import discord
from discord.ext import commands
import random
import threading
import time
import json
import traceback
from datetime import datetime
#from Scrap import Scrap
from GameScraper import GameScraper
from Waiter import Waiter

#TO-DO -> 
# move useful methods to other file/class
# reorganize commands

# refreshed, currently unused
"""
def every(delay, task):
  next_time = time.time() + delay
  while True:
    time.sleep(max(0, next_time - time.time()))
    try:
      task()
    except Exception:
      traceback.print_exc()
      # in production code you might want to have this instead of course:
      # logger.exception("Problem while executing repetitive task.")
    # skip tasks if we are behind schedule:
    next_time += (time.time() - next_time) // delay * delay + delay

def refresh_message():
  print("refresh", time.time())

   #threading.Thread(target=lambda: every(500, refresh_message)).start()
"""


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


def randomize():
    return random.randrange(0, 100)


def super_randomize():
    return random.randrange(0, 5000)


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
valheim = GameScraper()
waiter = Waiter(data_read)



@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")
    
@bot.event
async def on_message(message):
    await bot.process_commands(message)
    
    if message.author == bot.user:
        return

    if super_randomize() == 42:
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



@bot.command()
async def hello(ctx):
    await ctx.send(f"Hello {ctx.author.mention}!")

@bot.command(name="random")
async def generate_random_number(ctx):
    await ctx.channel.send(str(randomize()) + "!")


@bot.group()
async def konradobot(ctx):
    if ctx.invoked_subcommand is None:
        await ctx.send("A witam")

@konradobot.command()
async def przedmioty(ctx):
    # currently obsolete, prints default message instead
    #x = Scrap()
    #big_message = x.do_command()
    #await message.channel.send(f"Spis przedmiotów {message.author.mention} ```{big_message}```")
    await ctx.channel.send("Obecnie niedostępne.")

@bot.group()
async def konradobocie(ctx):
    if ctx.invoked_subcommand is None:
        await ctx.send("No hej?")

@konradobocie.command(name="czy")
async def whether(ctx, message_content):
    if "popiera" in message_content or "popierasz" in message_content:
        await ctx.channel.send("Nikogo nie popieram, bo jestem botem")
        return
    random_number = randomize()
    this_message = ""
    if random_number < 25:
        this_message = "Jak najbardziej"
    elif 25 <= random_number < 50:
        this_message = "No w sumie czemu nie"
    elif 50 <= random_number < 75:
        this_message = "Kurde no ciężko stwierdzić"
    else:
        this_message = "Tylko nie to"
    await ctx.channel.send(this_message)
    

@bot.group()
async def val(ctx):
    if ctx.invoked_subcommand is None:
        await ctx.send("Unknown command.")

@val.command()
async def craft(ctx, *message_content: str):
    print(message_content)
    big_message = valheim.get_item_info(list(message_content))
    await ctx.channel.send(f"Here's you recipe {ctx.author.mention} ```{big_message}```")

@bot.group()
async def release(ctx):
    if ctx.invoked_subcommand is None:
        await ctx.send("Unknown command.")


#TO-DO refactor
@release.command()
async def add(ctx, *message_content: str):
    date = next(x for x in message_content if "." in x)
    date_index = message_content.index(date)
    title = " ".join(message_content[2:date_index])
    developer = " ".join(message_content[date_index+1:])

    message_to_send = waiter.add_date(title, date, developer)
    await ctx.channel.send(message_to_send)

@release.command()
async def delete(ctx, *message_content: str):
    date = next(x for x in message_content if "." in x)
    date_index = message_content.index(date)
    title = " ".join(message_content[2:date_index])
    developer = " ".join(message_content[date_index+1:])

    message_to_send = waiter.delete_date(title, date, developer)
    await ctx.channel.send(message_to_send)


with open("secretkey") as f:
    secret_key = f.readline()


bot.run(secret_key)
