# import packages --------------------------------------------------------------

import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup
import time

# load data so that we can get link information --------------------------------

games = pd.read_csv("data/games_base.csv")
second_games = pd.read_csv("data/games2.csv")

# use map() to loop over links -------------------------------------------------

domain = "https://store.steampowered.com/"

# remove chart from end of link

game_links = games["links"].apply(lambda link: "/".join(link.split("/")[:-2]))

# add correct suffix

game_pages = [domain + path for path in game_links]

# test section 

game_pages_test = game_pages[:20]
scraped_db = map(scrape_page, game_pages_test)
scraped_db = pd.concat(list(scraped_db))
scraped_db.to_csv("data/games_sectiontest.csv", index=False)
print("Section test done!")

# section 1, 0-1000

game_pages_1 = game_pages[:1000]
scraped_db = map(scrape_page, game_pages_1)
scraped_db = pd.concat(list(scraped_db))
scraped_db.to_csv("data/games_section1.csv", index=False)
print("Section 1 done!")

# section 2, 1000-2000

game_pages_2 = game_pages[1000:2000]
scraped_db = map(scrape_page, game_pages_2)
scraped_db = pd.concat(list(scraped_db))
scraped_db.to_csv("data/games_section2.csv", index=False)
print("Section 2 done!")

# section 3, 2000-3000

game_pages_3 = game_pages[2000:3000]
scraped_db = map(scrape_page, game_pages_3)
scraped_db = pd.concat(list(scraped_db))
scraped_db.to_csv("data/games_section3.csv", index=False)
print("Section 3 done!")

# section 4, 3000-4000

game_pages_4 = game_pages[3000:4000]
scraped_db = map(scrape_page, game_pages_4)
scraped_db = pd.concat(list(scraped_db))
scraped_db.to_csv("data/games_section4.csv", index=False)
print("Section 4 done!")

# section 5, 4000-5000

game_pages_5 = game_pages[4000:5000]
scraped_db = map(scrape_page, game_pages_5)
scraped_db = pd.concat(list(scraped_db))
scraped_db.to_csv("data/games_section5.csv", index=False)
print("Section 5 done!")

# section 6, 5000-6000
game_pages_6 = game_pages[5000:6000]
scraped_db = map(scrape_page, game_pages_6)
scraped_db = pd.concat(list(scraped_db))
scraped_db.to_csv("data/games_section6.csv", index=False)
print("Section 6 done!")

# section end, 6000 - end
game_pages_end = game_pages[6000:]
scraped_db = map(scrape_page, game_pages_end)
scraped_db = pd.concat(list(scraped_db))
scraped_db.to_csv("data/games_sectionend.csv", index=False)
print("Section end done!")

print("Begin merging!")
# grabs checkpoint data
sec1 = pd.read_csv("data/games_section1.csv")
sec2 = pd.read_csv("data/games_section2.csv")
sec3 = pd.read_csv("data/games_section3.csv")
sec4 = pd.read_csv("data/games_section4.csv")
sec5 = pd.read_csv("data/games_section5.csv")
sec6 = pd.read_csv("data/games_section6.csv")
secend = pd.read_csv("data/games_sectionend.csv")

# add all data to list
csv_list = []
csv_list.append(sec1)
csv_list.append(sec2)
csv_list.append(sec3)
csv_list.append(sec4)
csv_list.append(sec5)
csv_list.append(sec6)
csv_list.append(secend)
games_final = pd.concat(csv_list)

# merge game data with existing df
games_final = games_final.merge(second_games, on="name", how = "left")
games_final = games_final.fillna(0)

# drop bad columns
games_final = games_final.drop(columns=['last_word', 'links', 'Unnamed: 0'])
print("Merged fullsec w/ other csv!")

# write out to file ------------------------------------------------------------

games_final.to_csv("data/games_full.csv", index=False)


