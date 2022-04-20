import time
from datetime import datetime


class Waiter:
    def __init__(self, release_dates):
        self.release_dates = release_dates

    def add_date(self, name, date, developer):
        if any(d['name'] == name for d in self.release_dates):
            print("Game already exists.")
            return

        new_date = {
        "name": name,
        "release_date": date,
        "developer": developer
        }

        self.release_dates.append(new_date)
        print("Game added.") 
                

    def delete_date(self, name, date, developer):
        if not any(d['name'] == name for d in self.release_dates):
            print("Game doesn't exist.")
            return
        
        temp_date = {
            "name": name,
            "release_date": date,
            "developer": developer
        }

        self.release_dates.remove(temp_date)
        print("Game deleted.")

    def release_date_time(self, name):
        time_now = datetime.now()
        game_release_date = datetime(2022, 2, 25, 0, 0, 0)

        time_between = game_release_date - time_now

        time_in_seconds = time_between.total_seconds()

        days = divmod(time_in_seconds, 86400)
        hours = divmod(days[1], 3600)
        minutes = divmod(hours[1], 60)
        seconds = divmod(minutes[1], 1)
        if time_in_seconds < 0:
            return_message = f"Już jest, czas na gamin"
        else:
            if int(days[0]) == 1:
                return_message = f"Elden Ring będzie za {int(days[0])} dzień, {int(hours[0])} godzin, {int(minutes[0])} minut i {int(seconds[0])} sekund"
            elif int(days[0]) == 0:
                return_message = f"Elden Ring będzie za {int(hours[0])} godzin, {int(minutes[0])} minut i {int(seconds[0])} sekund"
                if int(hours[0]) == 0:
                    return_message = f"Elden Ring będzie za {int(minutes[0])} minut i {int(seconds[0])} sekund"
                    if int(minutes[0]) == 0:
                        return_message = f"Elden Ring będzie za {int(seconds[0])} sekund"
            else:
                return_message = f"Elden Ring będzie za {int(days[0])} dni, {int(hours[0])} godzin, {int(minutes[0])} minut i {int(seconds[0])} sekund"

        return return_message