import csv
from datetime import datetime

dayCounter = [0] * 7
hourCounter = [0] * 24
names = []

filenames = ['smartwaiver-5dea5d6b4b24a.csv', 'smartwaiver-5dea5d7bbbd78.csv',
             'smartwaiver-5dea5d7cc249d.csv', 'smartwaiver-5dea5d738dfeb.csv',
             'smartwaiver-5dea5d77821ec.csv']


def readFile(file):
    reader = csv.reader(file, skipinitialspace=True)
    next(reader)  # skip header
    for row in reader:
        datetime_object = datetime.strptime(row[3], '%Y-%m-%d %H:%M')
        dayCounter[datetime_object.weekday()] += 1
        hourCounter[datetime_object.hour] += 1
        if [row[0], row[1]] not in names:
            names.append([row[0], row[1]])


for filename in filenames:
    with open(filename, 'r') as file:
        readFile(file)

print("number of visits by day:")
print(dayCounter)
print("number of visits by hour:")
print(hourCounter)
print("list of names that visited:")
print(names)
print(len(names))
