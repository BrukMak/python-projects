# Basic stuff in python, for refreshing my memory

#String formatting
print("String formatting")
name = "Bruk"
s = f"Hello, World! {name}"

t = "Hello, World! {}".format(name)

print(s, t)
print(s == t)


#Slicing
print("\nSlicing")

l = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(l[::2]) #l[start:stop:step] => ['a', 'c', 'e', 'g']
print(l[::-1]) #l[start:stop:step] => ['g', 'f', 'e', 'd', 'c', 'b', 'a']
print(l[2:5]) #l[start:stop:step] => ['c', 'd', 'e']
print(l[2:5:2]) #l[start:stop:step] => ['c', 'e']

#Reading CSV files
from datetime import datetime
print("\nReading CSV files")
import csv
from pprint import pprint

with open('Laureates.csv', 'r') as file:
    reader = csv.DictReader(file) 
    laureates = list(reader)

for laureate in laureates:
    if laureate['surname'] == "Einstein":
        pprint(laureate)
        year = datetime.strptime(laureate['died'], '%Y-%m-%d')
        born = datetime.strptime(laureate['born'], '%Y-%m-%d')
        age = int(laureate['year'] )- int(laureate['born'][:4])
        died = year.year - born.year
        print("\n He was {} years old when he won the prize. He died at the age of {}".format(age, died))
        break



#Converting CSV to JSON
import json
print("\nConverting CSV to JSON")
with open('Laureates.json', 'w') as json_file:
    json.dump(laureates, json_file, indent=2)

#Challenge, json for laureates whoes name starts with 'A'
print("\nChallenge, json for laureates whoes name starts with 'A'")

with open('Laureates.json', 'r') as json_file:
    laureates = json.load(json_file)

with open ('Laureates_A.json', 'w') as json_file:
    for laureate in laureates:
        if laureate['name'].upper().startswith('A'):
            json.dump(laureate, json_file, indent=2)

#Loading a JSON Data using HTTP request
print("\nLoading a JSON Data using HTTP request")

import requests
response = requests.get("https://api.worldbank.org/v2/countries/USA/indicators/SP.POP.TOTL?per_page=5000&format=json")
print(response.status_code)  # This should print 200 for success.

data_for_last_twenty_years = response.json()[1][:20]
for data in data_for_last_twenty_years:
    val = data['value'] // 10_000_000
    print(f"{data['date']}: {data['value']}", "=" * val)
    # print("=" * val)
