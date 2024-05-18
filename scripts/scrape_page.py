# import packages --------------------------------------------------------------

import pandas as pd
import numpy as np
import requests
from bs4 import BeautifulSoup
import time

# https://store.steampowered.com/
# generate empty df
empty_df = pd.DataFrame({
        "name": [],
        "genres": np.nan,
        "developer": np.nan,
        "publisher": np.nan,
        "release": np.nan,
        "platforms": np.nan,
        "tags": np.nan,
        "SP/Coop/MP": np.nan,
        "base price": np.nan,
        "negative reviews": np.nan,
        "positive reviews": np.nan,
        "total reviews": np.nan
        
    })
    
# function: scrape_page --------------------------------------------------------


def scrape_page(url):
    
    time.sleep(5)

    # read page
    page = requests.get(url).content
    soup = BeautifulSoup(page, "html5lib")

    # scrape name
    name = soup.select("#appHubAppName")
    name = [name.text for name in name]
    if len(name) == 0:
        return empty_df

    # scrape tags
    tags = soup.select(".app_tag")
    tags = [tag.text for tag in tags]
    tags = ''.join(tags)
    tags = tags.replace("\t", "")
    tags = tags.replace("\n", ",")
    tags = [tags[1:-1]]

    # scrape publisher
    publisher = soup.select("#game_highlights .dev_row+ .dev_row a")
    publisher = [publisher.text for publisher in publisher]
    publisher = [",".join(publisher)]

    # scrape developer
    developer = soup.select("#developers_list a")
    developer = [developer.text for developer in developer]
    developer = [",".join(developer)]

    # scrape genre
    genres = soup.select("#genresAndManufacturer span a")
    genres = [genre.text for genre in genres]
    genres = [','.join(genres)]

    # scrape release date
    release = soup.select(".date")
    release = [release.text for release in release]
    if len(release) == 0:
        return empty_df

    # scrape SP/Coop/MP
    internet = soup.select("a.game_area_details_specs_ctn")
    internet = [internet.text for internet in internet]
    internet = ",".join(internet)
    internet = internet.split(",")
    internet_list = ["Single-player", "Online PvP", "Online Co-op",
                     "LAN Co-op", "Shared/Split Screen Co-op", "Shared/Split Screen PvP"]
    internets = []
    for word in internet:
        if word in internet_list:
            internets.append(word)
    internets = [",".join(internets)]

    # scrape platforms
    platforms = soup.select(".sysreq_tab")
    platforms = [platforms.text for platforms in platforms]
    if len(platforms) == 0:
        platforms = "Windows"
    else:
        platforms = "".join(platforms)
        platforms = platforms.replace("\t", "")
        platforms = platforms.replace("\n", ",")
        platforms = platforms.replace(" + ", ",")
        platforms = [platforms[1:-1]]
        
    # scrape price
    cost = soup.select(".discount_pct")
    if len(cost) == 0:
        cost = soup.select(".game_purchase_price")
    else:
        cost = soup.select(".game_purchase_discount_countdown+ .game_purchase_action .discount_original_price")
    cost = [cost.text for cost in cost]
    if len(cost) == 0:
        return empty_df
    else:
        cost = cost[0]
        cost = "".join(cost)
        cost = cost.replace("\t", "")
        cost = cost.replace("\n", "")
        cost = cost.replace("$", "")
    
    # scrape negative reviews
    review_neg = soup.select("#review_type_negative+ label")
    review_neg = [review_neg.text for review_neg in review_neg]
    review_neg = "".join(review_neg)
    review_neg = review_neg.replace("Negative\xa0(", "")
    review_neg = review_neg.replace(")", "")
    review_neg = review_neg.replace(",", "")
    
    # scrape positive reviews
    review_pos = soup.select("#review_type_positive+ label")
    review_pos = [review_pos.text for review_pos in review_pos]
    review_pos = "".join(review_pos)
    review_pos = review_pos.replace("Positive\xa0(", "")
    review_pos = review_pos.replace(")", "")
    review_pos = review_pos.replace(",", "")
    
    # add up reviews
    review_sum = str(int(review_neg) + int(review_pos))
    
    # generate df for games
    game = pd.DataFrame({
        "name": name,
        "genres": genres,
        "developer": developer,
        "publisher": publisher,
        "release": release,
        "platforms": platforms,
        "tags": tags,
        "SP/Coop/MP": internets,
        "base price": cost,
        "negative reviews": review_neg,
        "positive reviews": review_pos,
        "total reviews": review_sum
        
    })

    return game


# tests
#test = scrape_page("https://store.steampowered.com//app/2427560")	
#scrape_page("https://store.steampowered.com//app/730/charts/")
#scrape_page("https://store.steampowered.com//app/1509960/charts/")
