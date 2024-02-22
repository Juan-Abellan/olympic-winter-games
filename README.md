# 🏅 Olympic Winter Games

Now that you have understood the basics of loading data from a CSV, let’s work with a real dataset from Kaggle. Run the two lines below to download the datasets we need for this challenge:

- curl https://wagon-public-datasets.s3.amazonaws.com/01-Python/02-Data-Sourcing/olympics_dictionary.csv > data/dictionary.csv
- curl https://wagon-public-datasets.s3.amazonaws.com/01-Python/02-Data-Sourcing/olympics_winter.csv > data/winter.csv

Go ahead and open those two files in your text editor to try & understand what they contain. The goal of this challenge is to implement the method in winter_olympic_games.py:

- Who won the most winter Olympic games medals (gold/silver/bronze) ever? (Hint: there’s just one answer)
- From min_year to max_year, which country won the most gold medals?
- Find the three women with the most 5000 meters medals(gold/silver/bronze).

⚠️ For this challenge, you can’t use pandas yet 😉. Let’s see how far you can go with just Python & the csv module.

Here some Viz of the results using Tableau Public:
https://public.tableau.com/app/profile/joao.avela/viz/OlympicWinterGames_17084355196450/WinterGames
