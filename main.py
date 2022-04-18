import discord
import random
import threading
import time
import traceback
from datetime import datetime
#from Scrap import Scrap
from GameScraper import GameScraper
from Waiter import Waiter


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


client = discord.Client()
valheim = GameScraper()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
   


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if super_randomize() == 42:
        await message.channel.send(f'Randomowa wiadomość!')
    if message.content.startswith('!'):
        if message.content.startswith('!hello'):
            # name = strip_name(message.author)
            await message.channel.send(f'Hello {message.author.mention}!')

        if message.content.startswith('!random'):
            random_number = randomize()
            await message.channel.send(str(random_number) + "!")

        if message.content.startswith('!konradobot przedmioty'):
            # currently obsolete, prints default message instead
            #x = Scrap()
            #big_message = x.do_command()
            #await message.channel.send(f'Spis przedmiotów {message.author.mention} ```{big_message}```')
            await message.channel.send(f'Obecnie niedostępne')

        if message.content.startswith('!konradobocie czy'):
            if "popiera" in message.content.lower() or "popierasz" in message.content.lower():
                await message.channel.send(f"Nikogo nie popieram, bo jestem botem")
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
            await message.channel.send(f'{this_message}')

        if message.content.startswith('!val craft'):
            big_message = valheim.get_item_info(strip_message(message.content))
            await message.channel.send(f"Here's you recipe {message.author.mention} ```{big_message}```")
    else:

        if "bocie" in message.content and "konradobocie" not in message.content:
            name = strip_name(message.author)
            message_to_send = get_stripped_message(message.content)
            await message.channel.send(message_to_send + name)
        if "ඞ" in message.content:
            await message.channel.send(f'podejrzane')
        if "potek" in message.content.lower():
            name = strip_name(message.author)
            message_to_send = reminder()
            await message.channel.send(message_to_send + " " + name + "!")
        if "nie dam rady" in message.content.lower():
            name = strip_name(message.author)
            await message.channel.send("Dasz radę " + name + "!")

        if "elden ring" in message.content.lower() or "elden" in message.content.lower():
            if "kiedy" in message.content.lower() or "za ile" in message.content.lower():
                waiter = Waiter()
                message_to_send = waiter.elden_ring_time()
                await message.channel.send(f"{message_to_send} {message.author.mention}!")
            else:
                await message.channel.send(f"OOOOOOHHHHHH ELDEN RING!")

        if "konradobocie" in message.content.lower() and "co robiłeś, że cię nie było" in message.content.lower():
            await message.channel.send(f"Czytałem lore Dark Souls")




with open("secretkey") as f:
    secret_key = f.readline()


client.run(secret_key)
