from flask import Flask
from flask_restful import Resource, Api
import csv
from collections import deque

app = Flask(__name__)
api = Api(app)


sensor_filename = '/var/log/sensors2csv/sensors2csv.csv.log'


class AllSensors(Resource):

    def get_last_row(self, csv_filename):
        with open(csv_filename, 'r') as f:
            # Deque with a max length of one to store the last element
            return deque(csv.reader(f), 1)[0]

    def get(self):

        return self.get_last_row(sensor_filename)


api.add_resource(AllSensors, '/sensors')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
