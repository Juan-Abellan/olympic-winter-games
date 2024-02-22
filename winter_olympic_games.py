# pylint: disable=missing-docstring

import csv

COUNTRIES_FILEPATH = "data/dictionary.csv"
MEDALS_FILEPATH = "data/winter.csv"


def most_decorated_athlete_ever():
    """Returns who won the most winter olympic games medals (gold/silver/bronze) ever"""
    athletes = {}
    with open(MEDALS_FILEPATH, mode='r') as csv_file:
        csv_reader_medals = csv.DictReader(csv_file)
        # print(f'''
        # {csv_reader_medals = }
        # {type(csv_reader_medals) = }
        # ''')
        for row in csv_reader_medals:
            # print(f'''
            # {row = }
            # {row['Athlete'] = }''')
            if row['Athlete'] not in athletes:
                athletes[row['Athlete']] = 1
            else:
                athletes[row['Athlete']] += 1
    # print(f'''
    # {athletes = }
    # {type(athletes) = }
    # {len(athletes) = }
    # ''')
    sorted_athletes_dict = sorted(athletes.items(), key=lambda x: x[1], reverse=True)
    return dict(sorted_athletes_dict[:1:])


def country_with_most_gold_medals(min_year, max_year):
    """Returns which country won the most gold medals between `min_year` and `max_year`"""
    pass  # YOUR CODE HERE

def top_three_women_in_five_thousand_meters():
    """Returns the three women with the most 5000 meters medals(gold/silver/bronze)"""
    pass  # YOUR CODE HERE
