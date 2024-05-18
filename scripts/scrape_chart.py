# import packages --------------------------------------------------------------

import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup
import time

# set up an empty df
empty_df = pd.DataFrame({
  "name": [],
  "peak(2/28)": np.nan,
  "all_time_peak": np.nan
    })

# https://steamcharts.com/

# function: scrape_database ---------------------------------------------------

def scrape_chart(url):

    time.sleep(5)

    # read page
    page = requests.get(url).content
    soup = BeautifulSoup(page, "html5lib")

    # extract name
    name = soup.select("h1#app-title")
    name = [n1.text for n1 in name]
    if len(name) == 0:
      return empty_df
    
    
    # extract daily peak
    day_peak = soup.select(".app-stat:nth-child(3) .num")
    day_peak = [day.text for day in day_peak]

    # extract all time peak
    peak = soup.select(".app-stat~ .app-stat+ .app-stat .num")
    peak = [pk.text for pk in peak]

    # create df for games
    game_db = pd.DataFrame({
        "name": name,
        "peak(2/28)": day_peak,
        "all_time_peak": peak
    })

    return game_db
