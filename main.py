import json

from helper import calculate_fare


with open('data.json') as f:
  dataset = json.load(f)
histories = dataset['Histories']

total_fare = 0
for history in histories:
  trips = history['Trips']
  transaction_date = history['EntryTransactionDate']
  fare = calculate_fare(trips, transaction_date)
  total_fare += fare

print(total_fare)
