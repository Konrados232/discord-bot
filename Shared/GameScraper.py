import requests
from bs4 import BeautifulSoup, SoupStrainer


class GameScraper:
    def __init__(self):
        self.url_prefix = r"https://valheim.fandom.com"
        main_url = r"https://valheim.fandom.com/wiki/Items_List"
        content = requests.get(main_url)
        self.soup = BeautifulSoup(content.text, 'html.parser')
        self.item_list = self.soup.find_all('a', href=True)

    def find_element_from(self, element_name):
        for i in self.item_list:
            if element_name in i.text:
                return i

        return None

    def load_item_info(self, item):
        content = requests.get(self.url_prefix + item['href'])
        item_soup = BeautifulSoup(content.text, 'html.parser')

        # print(item_soup.prettify())

        materials = item_soup.find(text="Crafting Materials")
        materials_parent = materials.parent.parent

        return materials_parent.find_all("li")

    def parse_list(self, table):
        long_string = ""
        for i in table:
            long_string += i.text
            long_string += '\n'

        return long_string

    def get_item_info(self, item_name):
        found_item = self.find_element_from(item_name)
        if found_item is None:
            return "Invalid request!"

        materials_list = self.load_item_info(found_item)
        return self.parse_list(materials_list)

