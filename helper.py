from datetime import datetime
import time

from fuzzywuzzy import fuzz
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager

from mapping import format_station_name, format_bus_stop_name, get_bus_direction


def calculate_fare_and_summarise_trips(trips, transaction_date):
  # open LTA's fare calculator page
  driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
  driver.get("https://www.lta.gov.sg/content/ltagov/en/map/fare-calculator.html")
  time.sleep(1)

  # set fare type
  fare_type = Select(driver.find_element(By.ID, "fareType"))
  fare_type.select_by_visible_text('Adult')

  # process 1st trip
  first_trip = trips[0]
  card_pane = driver.find_element(By.CSS_SELECTOR, "div.card.tab-pane")
  card_pane.click()
  fill_up_trip(card_pane, first_trip)

  # process the remaining trips
  remaining_trip = trips[1:]
  for i in range(len(remaining_trip)):
    element = driver.find_element(By.ID, "addTrip")
    element.click()
    time.sleep(1)

    card_panes = driver.find_elements(By.CSS_SELECTOR, "div.card.tab-pane")
    next_pane = card_panes[i+1]
    next_pane.click()
    next_trip = remaining_trip[i]
    fill_up_trip(next_pane, next_trip)

  # calculate
  driver.find_element(By.ID, "calTrip").click()
  fare_text = ""
  while fare_text == "":
    fare_text = driver.find_element(By.CSS_SELECTOR, "h4.fare").text
  fare_in_cents = int(float(fare_text[1:]) * 100)

  # get table
  table = driver.find_element(By.CSS_SELECTOR, "table.results-container-table")
  table_body = table.find_element(By.CSS_SELECTOR, "tbody")
  rows = table_body.find_elements(By.CSS_SELECTOR, "tr")
  summarised_trips = []
  for row in rows:
    cols = row.find_elements(By.CSS_SELECTOR, "td")
    summarised_trips.append({
      "Trip No": cols[0].text,
      "Service": cols[1].text,
      "Board": cols[2].text,
      "Alight": cols[3].text,
      "Distance": cols[4].text,
      "Fare": cols[5].text,
    })
  
  # get distance
  distance_text = ""
  while distance_text == "":
    distance_text = driver.find_element(By.CSS_SELECTOR, "span.distance").text
  distance = float(distance_text.split(" ")[0])

  # use old fare structure if before 23 Dec 2023
  if datetime.strptime(transaction_date, "%Y-%m-%dT%H:%M:%S") < datetime(2023, 12, 23):
    if distance <= 4.2:
      fare_in_cents -= 10
    else:
      fare_in_cents -= 11

  # return summary
  summary = {
    "Transaction Date": transaction_date,
    "Total Distance": distance_text,
    "Total Fare (After Adjustment)": fare_in_cents,
    "Trips": summarised_trips
  }
  
  return fare_in_cents, summary


def fill_up_trip(card_pane, trip):
  if trip["BusServiceNo"] is None:
    # check if trip is a train service
    fr = format_station_name(trip["EntryLocationName"])
    to = format_station_name(trip["ExitLocationName"])
    mrt_fill(card_pane, fr, to)
  else:
    no = trip["BusServiceNo"]
    dir = get_bus_direction(trip)
    fr = format_bus_stop_name(trip["OriBoardingBusStopCode"] + " - " + trip["EntryLocationName"])
    to = format_bus_stop_name(trip["OriAlightingBusStopCode"] + " - " + trip["ExitLocationName"])
    bus_fill(card_pane, no, dir, fr, to)


def bus_fill(card_pane, no, dir, fr, to):
  # click on bus icon
  bus_btn = card_pane.find_element(By.CSS_SELECTOR, "button.busBtn")
  bus_btn.click()

  bus_seg = card_pane.find_element(By.CSS_SELECTOR, "div.busSegment")

  # fill up required data
  bus_no = Select(bus_seg.find_element(By.CSS_SELECTOR, "select.busSelect"))
  bus_no.select_by_visible_text(no)

  bus_dir = Select(bus_seg.find_element(By.CSS_SELECTOR, "select.busDir"))
  bus_dir.select_by_value(dir)

  bus_fr = Select(bus_seg.find_element(By.CSS_SELECTOR, "select.busFrom"))
  select_bus_stop(bus_fr, fr)

  bus_to = Select(bus_seg.find_element(By.CSS_SELECTOR, "select.to"))
  select_bus_stop(bus_to, to)


def select_bus_stop(select_ele, text):
  try:
    select_ele.select_by_visible_text(text)
  except:
    print(f"cannot find {text} in options")

    # use fuzzywuzzy to find the best options if not found
    best_text = None
    best_ratio = 0
    for option in select_ele.options:
      curr_text = option.text
      curr_ratio = fuzz.ratio(curr_text.lower(), text.lower())  # case insensitive
      if curr_ratio > best_ratio:
        best_text = curr_text
        best_ratio = curr_ratio

    print(f"selecting {best_text} instead")
    select_ele.select_by_visible_text(best_text)


def mrt_fill(card_pane, fr, to):
  # click on mrt icon
  mrt_btn = card_pane.find_element(By.CSS_SELECTOR, "button.mrtBtn")
  mrt_btn.click()

  mrt_seg = card_pane.find_element(By.CSS_SELECTOR, "div.mrtSegment")

  # fill up required data
  mrt_fr = Select(mrt_seg.find_element(By.CSS_SELECTOR, "select.trainFrom"))
  mrt_fr.select_by_visible_text(fr)

  mrt_to = Select(mrt_seg.find_element(By.CSS_SELECTOR, "select.to"))
  mrt_to.select_by_visible_text(to)
