from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from webdriver_manager.chrome import ChromeDriverManager


# script to get a list of MRT/LRT names as shown in LTA Fare Calculator
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.lta.gov.sg/content/ltagov/en/map/fare-calculator.html")

card_pane = driver.find_element(By.CSS_SELECTOR, "div.card.tab-pane")
card_pane.click()

mrt_btn = card_pane.find_element(By.CSS_SELECTOR, "button.mrtBtn")
mrt_btn.click()

mrt_seg = card_pane.find_element(By.CSS_SELECTOR, "div.mrtSegment")
mrt_select = Select(mrt_seg.find_element(By.CSS_SELECTOR, "select.trainFrom"))
options = [x.text for x in mrt_select.options]

res = {}
for option in options:
  if option == "Select MRT/LRT Station":
    continue

  parsed = option.split("(")
  key = parsed[0][:-1]
  value = parsed[1][:-1]
  res[key] = value

print(res)
