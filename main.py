import json

from helper import calculate_fare_and_summarise_trips


with open('data.json') as f:
  dataset = json.load(f)
histories = dataset['Histories']

total_fare = 0
summarised_histories = []
for history in histories:
  trips = history['Trips']
  transaction_date = history['EntryTransactionDate']
  fare, summary = calculate_fare_and_summarise_trips(trips, transaction_date)
  total_fare += fare
  summarised_histories.append(summary)

to_write = {
  "Total Fare": total_fare,
  "Histories": summarised_histories
}
with open("out.json", "w") as outfile:
    outfile.write(json.dumps(to_write, indent=4))
