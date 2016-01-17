import csv
from collections import deque


class Csv2Json():

    def __init__(self, csv_filename):
        self.csv_filename = csv_filename

    def get_last_row(self):
        with open(self.csv_filename, 'r') as f:
            # Deque with a max length of one to store the last element
            return deque(csv.reader(f), 1)[0]

    def convert_json(self):
        pass


sensor_filename = '/var/log/sensors2csv/sensors2csv.csv.log'

if __name__ == '__main__':
    c2j = Csv2Json(sensor_filename)
    print(c2j.get_last_row())
