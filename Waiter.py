import time
from datetime import datetime
import json

class Waiter:
    def __init__(self, json_file):
        self.json_file = json_file
        self.release_dates = json_file['dates']


    def add_date(self, name, date, developer):
        if not self.validate_date(date):
            print("Wrong date format.")
            return "Źle podana data!"

        if self.name_exists(name):
            print("Game already exists.")
            return "Już taka gra jest!"

        print("hello")
        new_date = {
        "name": name,
        "release_date": date,
        "developer": developer
        }

        self.release_dates.append(new_date)
        self.write_to_json()
        print("Game added.") 
        return "Gra dodana!"
                

    def delete_date(self, name, date, developer):
        if not self.name_exists(name):
            print("Game doesn't exist.")
            return "Nie da się usunąć czegoś, co nie istnieje... Chyba"
        
        temp_date = {
            "name": name,
            "release_date": date,
            "developer": developer
        }

        self.release_dates.remove(temp_date)
        self.write_to_json()
        print("Game deleted.")
        return "Istnienie tej gry przestało funkcjonować"
    
    def write_to_json(self):
        self.json_file['dates'] = self.release_dates
        print(self.json_file)
        with open('datafiles/release_dates.json', 'w') as f:
            json.dump(self.json_file, f)
            

    def validate_date(self, date):
        try:
            return bool(datetime.strptime(date, "%d.%m.%Y"))
        except ValueError:
            return False

    def name_exists(self, name):
        return any(d['name'] == name for d in self.release_dates)
   

    def split_seconds_to_tuple(self, time_in_seconds):
        days = divmod(time_in_seconds, 86400)
        hours = divmod(days[1], 3600)
        minutes = divmod(hours[1], 60)
        seconds = divmod(minutes[1], 1)
        
        return (int(days[0]), int(hours[0]), int(minutes[0]), int(seconds[0]))


    def release_date_time(self, name):
        if not self.name_exists(name):
            return "Jakiej gry? O_o"

        release_date_dict = next((item for item in self.release_dates if item["name"] == name), False)

        time_now = datetime.now()
        game_release_date = datetime.strptime(release_date_dict["release_date"], "%d.%m.%Y")

        time_between = game_release_date - time_now
        time_in_seconds = time_between.total_seconds()

        if time_in_seconds < 0:
            return "Już jest, czas na gamin!" 

        days, hours, minutes, seconds = self.split_seconds_to_tuple(time_in_seconds)

        return_message = f"{seconds} sekund"

        if minutes != 0:
            return_message = f"{minutes} minut i " + return_message

        if hours != 0:
            return_message = f"{hours} godzin, " + return_message

        if days != 0:
            return_message = f"{days} dni, " + return_message
        
        if days == 1:
            return_message = f"{days} dzień, " + return_message

        return return_message

    def get_release_dates(self):
        return self.release_dates