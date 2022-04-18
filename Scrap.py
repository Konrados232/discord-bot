# obsolete code, needs refactoring

import re

from lxml import html
import requests

"""
class Scrap:
    def __init__(self):
        self.subject_dict = {}
        self.subjects_info = []

    def find_number_omega(self, page):
        text = page.text

        found_string = text.split("Liczba osób w grupie")[1]
        found_string_number = found_string.split("Limit miejsc")[0]
        xd = found_string.split("Limit miejsc")[1]
        found_string_limit = xd.split("Zaliczenie:")[0]

        found_number = re.findall(r'[\d.]+', found_string_number)
        found_limit = re.findall(r'[\d.]+', found_string_limit)

        string_date = text.split("każd")[1]
        found_string_date = string_date.split("<br>")[0]

        string_name = text.split(
            "<a href='https://www.usosweb.uj.edu.pl/kontroler.php?_action=katalog2/przedmioty/index' onclick='return Common.confirmWarnings();'>")[
            1]
        found_string_name = string_name.split("Plan zajęć w 21/22L")[0]
        temp = found_string_name.split("<span lang='pl'>")[1]
        temp2 = temp.split("</span>")[0]

        temp2 = temp2.replace("Java", "Jawa")

        if self.subject_dict.get(temp2) is None:
            self.subject_dict[temp2] = (int(found_number[1]), int(found_limit[1]))
        else:
            sub_tuple = self.subject_dict[temp2]
            number = sub_tuple[0] + int(found_number[1])
            limit = sub_tuple[1] + int(found_limit[1])
            self.subject_dict[temp2] = (number, limit)

        new_info = temp2 + " (" + found_string_date[1:] + " ) " + found_number[1] + "/" + found_limit[1]
        self.subjects_info.append(new_info)
        print(temp2 + " (" + found_string_date[1:] + " ) " + found_number[1] + "/" + found_limit[1])

    def calculate_percentage(self):
        for i in self.subject_dict:
            subject_tuple = self.subject_dict.get(i)
            current_number = subject_tuple[0]
            subject_limit = subject_tuple[1]
            percentage = current_number / subject_limit

            new_percentage = i + " " + str(current_number) + "/" + str(subject_limit) + " " + str(
                round(percentage * 100, 2)) + "%"
            self.subjects_info.append(new_percentage)

            print(i + " " + str(current_number) + "/" + str(subject_limit) + " " + str(
                round(percentage * 100, 2)) + "%")

    def get_long_string(self):
        # WWW
        page0 = requests.get(
            'https://www.usosweb.uj.edu.pl/kontroler.php?_action=katalog2/przedmioty/pokazZajecia&zaj_cyk_id=497218&gr_nr=1')

        #

        print()
        print("Procentowe zapełnienie: ")

        self.subjects_info.append('\n')
        self.subjects_info.append("Procentowe zapełnienie: ")

        self.calculate_percentage()

        print(self.convert_table_to_string(self.subjects_info))


    def convert_table_to_string(self, table):
        long_string = ""
        for i in table:
            long_string += i
            long_string += '\n'

        return long_string

    def do_command(self):
        self.get_long_string()
        return self.convert_table_to_string(table=self.subjects_info)
"""