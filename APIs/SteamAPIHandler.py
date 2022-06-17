import json
import requests


class SteamAPIHandler:
    def __init__(self):
        self.base_ulr = r"https://store.steampowered.com/api/appdetails?appids="
        self.additional_flags = [r"l=en"]
        

    def _make_url_with_id(self, appid):
        flags_combined = "&".join(self.additional_flags)
        return f"{self.base_ulr}{appid}&{flags_combined}"
    

    def fetch_data(self, appid):
        f = requests.get(self._make_url_with_id(appid))
        return json.loads(f.text)
    