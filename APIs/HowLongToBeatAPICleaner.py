

class HowLongToBeatAPICleaner:
    def __init__(self, base_dict):
        self.base_dict = base_dict
    
    def _get_name(self, data):
        return data.game_name


    def _get_image_url(self, data):
        return data.game_image_url


    def _get_gameplay_main(self, data):
        return data.gameplay_main


    def _get_gameplay_main_extra(self, data):
        return data.gameplay_main_extra


    def _get_gameplay_completionist(self, data):
        return data.gameplay_completionist


    def clean_data(self, data):
        new_dict = dict(self.base_dict)

        new_dict["name"] = self._get_name(data) 
        new_dict["image_url"] = self._get_image_url(data)
        new_dict["gameplay_main"] = self._get_gameplay_main(data)
        new_dict["gameplay_main_extra"] = self._get_gameplay_main_extra(data)
        new_dict["gameplay_completionist"] = self._get_gameplay_completionist(data)

        return new_dict

