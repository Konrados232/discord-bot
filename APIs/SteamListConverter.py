import requests
import json


class SteamListConverter:
    def __init__(self):
        self.all_list_url = r"https://api.steampowered.com/ISteamApps/GetAppList/v2/"
        self.all_games_file = r"datafiles/allgames.json"


    def _fetch_data(self):
        data = requests.get(self.all_list_url)
        return json.loads(data.text)


    def _convert_data(self, data):
        base_dict = {}
        app_list = data["applist"]["apps"]

        for app in app_list:
            base_dict[app["name"].lower()] = app["appid"]
        
        return base_dict


    def _save_to_file(self, converted_data, file_name):
        with open(file_name, "w") as f:
            json.dump(converted_data, f)


    def update_data(self):
        """Updates the local data of all Steam games. Use only when necessary."""
        apps_data = self._fetch_data()
        converted_data = self._convert_data(apps_data)
        self._save_to_file(converted_data, self.all_games_file)


    def get_data(self):
        with open(self.all_games_file, "r") as f:
            data = json.load(f)
        return data

