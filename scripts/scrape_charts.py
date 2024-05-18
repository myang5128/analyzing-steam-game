# import packages --------------------------------------------------------------

import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup
import time

# load data so that we can get link information --------------------------------

games = pd.read_csv("data/games.csv")

# use map() to loop over links -------------------------------------------------

domain = "https://steamcharts.com/"

# remove chart from end of link

game_links = games["links"].apply(lambda link: "/".join(link.split("/")[:-2]))

# add correct suffix

game_pages = [domain + path for path in game_links]

# map our function to each game

scraped_db = map(scrape_chart, game_pages)

# turn into list and concatenate

scraped_db = pd.concat(list(scraped_db))

# merge old and new data on games

games1 = games.merge(scraped_db, on = "name")

# write out to file ------------------------------------------------------------

games1.to_csv("data/games2.csv", index = False)
