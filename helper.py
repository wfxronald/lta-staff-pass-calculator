import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager

from mapping import format_station_name
    

def calculate_fare(trips):
  # open LTA's fare calculator page
  driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
  driver.get("https://www.lta.gov.sg/content/ltagov/en/map/fare-calculator.html")

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
  time.sleep(1)
  fare_in_cents = int(float(driver.find_element(By.CSS_SELECTOR, "h4.fare").text[1:]) * 100)
  return fare_in_cents


def fill_up_trip(card_pane, trip):
  if trip["BusServiceNo"] is None:
    # check if trip is a train service
    fr = format_station_name(trip["EntryLocationName"])
    to = format_station_name(trip["ExitLocationName"])
    mrt_fill(card_pane, fr, to)
  else:
    no = trip["BusServiceNo"]
    dir = str(int(trip["BusDirection"][-1]) - 1)  # 1-indexed in SimplyGo, 0 indexed in LTA calculator page
    fr = trip["OriBoardingBusStopCode"] + " - " + trip["EntryLocationName"]
    to = trip["OriAlightingBusStopCode"] + " - " + trip["ExitLocationName"]
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
  bus_fr.select_by_visible_text(fr)

  bus_to = Select(bus_seg.find_element(By.CSS_SELECTOR, "select.to"))
  bus_to.select_by_visible_text(to)


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
