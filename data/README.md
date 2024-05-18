Data for Final Project: \[Steam Games\]
================

### Codebook


<div class="cell-output-display">

| Variables              | Description                                                   | Type       |
|:-----------------------|:--------------------------------------------------------------|:-----------|
| `name`                 | game name                                                     | character  |
| `genres`               | the primary genre/s of the game                               | character  |
| `developer`            | developer/s of the game                                       | character  |
| `publisher`            | publisher/s of the game                                       | character  |
| `release date`         | number of months since release until Feb 2024                 | integer    |
| `platforms`            | number of platforms supported by the game                     | integer    |
| `tags`                 | list of tags of the game (user provided)                      | character  |
| `sp/coop/mp`           | respectively player vs ai/players vs ai/player/s vs player/s  | character  |
| `base price`           | price of game(excluding extra content)                        | integer    |
| `negative reviews`     | number of negative reviews                                    | integer    |
| `positive reviews`     | number of positive reviews                                    | integer    |
| `total reviews`        | number of reviews                                             | integer    |
| `24-hr peak(dd/mm)`    | daily player count peak as of mm-dd-2024                      | integer    |
| `all time peak`        | all time player count peak                                    | integer    |
| `positive review rate` | a ratio of positive reviews to total reviews                  | double     |
| `peak ratio`           | a ratio of the 24-hr peak to all time peak                    | double     |
| `success`              | if a game is considered successful                            | character  |
| `log_negative_reviews` | log of negative reviews                                       | double     |
| `log_positive_reviews` | log of positive reviews                                       | double     |
| `log_total_reviews`    | log of total reviews                                          | double     |
| `log_peak`             | log of 2h-hr peak                                             | double     |
| `log_all_time_peak`    | log of all time peak                                          | double     |

 
</div>
