# Discord Bot

Discord bot written in Python using discord.py library for most functionalities. It also uses BeautifulSoup for scraping important information from wikia websites and makes use of Steam and HowLongToBeat APIs to gather information about video games.

Most important functions:
* Quirky responses to the keywords written by the users in chat, e.g. responding with the same text before "bocie" keyword.
* Writing information about Steam video games such as release date, developers, short description.
* Informing about length of the games provided by HowLongToBeat website.
* Writing crafting recipes for survival game Valheim.
* Releases function - users can write their own events with date and be reminded about them using "kiedy" keyword.
* Snipe function - remembering last deleted message in the Discord channel.
* Writing status of groups in current university registration (currently unavailable).

Future features:
* Writing more helpful information about Valheim (such as structures).

# Available Commands
* !gigahelp - info about commands
* !hello - welcomes you
* !hltb [name] - check game's length
* !steam info [name] - check game's overall information
* !release add [name] [date] [info] - add event for tracking
* !release delete [name] [date] [info] - remove from tracking

#Gallery
![Discord Bot](https://user-images.githubusercontent.com/25458415/174493596-f65e04ca-434c-448e-a4f8-da757beb8c7f.png)


