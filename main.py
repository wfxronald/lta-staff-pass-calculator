import json

from helper import calculate_fare


with open('data.json') as f:
  dataset = json.load(f)
histories = dataset['Histories']

total_fare = 0
for history in histories:
  trips = history['Trips']
  fare = calculate_fare(trips)
  total_fare += fare

print(total_fare)
