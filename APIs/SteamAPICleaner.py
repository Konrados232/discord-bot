

class SteamAPIHandlerCleaner:
    def __init__(self):
        pass


    def _extract_data(self, data, appid):
        return data[appid]["data"]


    def _get_name(self, game_data):
        return game_data["name"]


    def _get_short_description(self, game_data):
        return game_data["short_description"]
    
    
    def _get_detailed_description(self, game_data):
        return game_data["detailed_description"]

    
    def _get_header_img_url(self, game_data):
        return game_data["header_image"]


    def _get_platforms(self, game_data):
        platforms = []
        if game_data["platforms"]["windows"]:
            platforms.append("Windows")
        if game_data["platforms"]["mac"]:
            platforms.append("Mac")
        if game_data["platforms"]["linux"]:
            platforms.append("Linux")
        
        return platforms


    def _get_achievements(self, game_data):
        if "achievements" not in game_data:
            return int(0)
        else:
            return int(game_data["achievements"]["total"])


    def _get_release_date(self, game_data):
        return game_data["release_date"]["date"]

    
    def _get_categories(self, game_data):
        cat_list = [x["description"] for x in game_data["categories"]]
        return cat_list
    

    def _get_genres(self, game_data):
        genre_list = [x["description"] for x in game_data["genres"]]
        return genre_list


    def _get_developer(self, game_data):
        return game_data["developers"][0]
    

    def _get_publisher(self, game_data):
        return game_data["publishers"][0]



    def clean_data(self, data, appid):
        new_dict = { }
        game_data = self._extract_data(data, str(appid))

        new_dict["name"]  = self._get_name(game_data)
        new_dict["desc"] = self._get_short_description(game_data)
        new_dict["header_url"] = self._get_header_img_url(game_data)
        new_dict["platforms"] = self._get_platforms(game_data)
        new_dict["developer"] = self._get_developer(game_data)
        new_dict["publisher"] = self._get_publisher(game_data)
        new_dict["achievements"] = self._get_achievements(game_data)
        new_dict["release_date"] = self._get_release_date(game_data)
        new_dict["categories"] = self._get_categories(game_data)
        new_dict["genres"] = self._get_genres(game_data)

        return new_dict
