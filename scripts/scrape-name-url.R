# load packages ----------------------------------------------------------------

library(tidyverse)
library(rvest)
library(polite)

# start polite session ---------------------------------------------------------

# set url 
domain <- "https://steamdb.info/charts/"

# agree session modification with the host
session <- bow(domain)

# read the page
page <- scrape(session)

# extract hyperlinks
game_names <- page |> 
  html_elements(".text-left+ td a") |>
  html_text()

# extract hyperlinks
game_links <- page |> 
  html_elements(".text-left+ td a") |>
  html_attr(name = "href")

games <- tibble(
  name = game_names,
  links = game_links
)

# filter dataset ---------------------------------------------------------------
# creates a new column that is just the last word for the game's name
games <- games |>
  mutate(last_word = str_extract(name, "\\w+$"))

# grepl or comparison both works, but grepl allows for non case-sensitivity
# drop demo games
games <- games |>
  subset(!grepl("demo", last_word, ignore.case = TRUE))

# Beta Test
games <- games |>
  subset(!grepl("beta", last_word, ignore.case = TRUE))

# Playtest
games <- games |>
  subset(!grepl("playtest", last_word, ignore.case = TRUE))

# Server
games <- games |>
  subset(!grepl("server", last_word, ignore.case = TRUE))
games <- games |>
  subset(!grepl("server", name, ignore.case = TRUE))

# Alpha 
games <- games |>
  subset(!grepl("alpha", last_word, ignore.case = TRUE))

# Test
games <- games |>
  subset(!grepl("test", last_word, ignore.case = TRUE))

# dropping specific game
games <- games |>
  subset(last_word != "Linux")
games <- games |>
  subset(last_word != "Win32")
games <- games |>
  subset(!grepl("beta", name, ignore.case = TRUE))
games <- games |>
  subset(name != "New World Public Test Realm")

games <- games |>
  subset(, c(name, links))

# save as CSV
write.csv(games, file = "data/games_base.csv")