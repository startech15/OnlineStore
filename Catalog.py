# каталог получается из csv-файла Pricelist

import csv

class Catalog:
    __dict = dict.fromkeys(['№', 'Название', 'Стоимость'])
    __list = list()

    def parse(self):
        with open('Pricelist.csv', 'r') as csv_file:
            reader = csv.reader(csv_file, delimiter=";")
            Catalog.__dict = {name[1]: name[2].split(" ", )[-1].rstrip() for (num, name) in enumerate(reader)}

        return(Catalog.__dict)

