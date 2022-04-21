import discord
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


client = discord.Client()
data_read = read_release_date_data_json()
valheim = GameScraper()
waiter = Waiter(data_read)



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

        #TO-DO refactor
        if message.content.startswith("!release add"):
            contents = message.content.split()
            date = next(x for x in contents if "." in x)
            date_index = contents.index(date)
            title = " ".join(contents[2:date_index])
            developer = " ".join(contents[date_index+1:])

            message_to_send = waiter.add_date(title, date, developer)
            await message.channel.send(message_to_send)
        if message.content.startswith("!release delete"):
            contents = message.content.split()
            date = next(x for x in contents if "." in x)
            date_index = contents.index(date)
            title = " ".join(contents[2:date_index])
            developer = " ".join(contents[date_index+1:])

            message_to_send = waiter.delete_date(title, date, developer)
            await message.channel.send(message_to_send)
    else:

        if "bocie" in message.content and "konradobocie" not in message.content:
            name = strip_name(message.author)
            message_to_send = get_stripped_message(message.content)
            await message.channel.send(message_to_send + name)
            
        if "ඞ" in message.content:
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


client.run(secret_key)
