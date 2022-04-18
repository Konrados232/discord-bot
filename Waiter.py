import time
from datetime import datetime

class Waiter:

    def elden_ring_time(self):
        time_now = datetime.now()
        elden_ring_premiere = datetime(2022, 2, 25, 0, 0, 0)

        time_between = elden_ring_premiere - time_now

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