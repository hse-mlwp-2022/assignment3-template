import pytest

import traceback

# from pandas_exercise import columns, carrier_names, freight_total, mail_total, passengers_total, top_10_by_passengers, top_route_origin_city, top_route_dest_city, top_route_passengers_count, top_3_carriers_df, international_travel_per_country

import pandas as pd
from collections import Counter

score = 0.0


def is_iterable(object):
    try:
        z = iter(object)
    except TypeError:
        return False
    return True


def test_exercise2():
    from pandas_exercise import columns
    global score
    assert is_iterable(columns) == True, "Variable 'columns' should be iterable"
    assert list(columns) == ['passengers', 'freight', 'mail', 'distance', 'unique_carrier',
       'airline_id', 'unique_carrier_name', 'unique_carrier_entity', 'region',
       'carrier', 'carrier_name', 'carrier_group', 'carrier_group_new',
       'origin_airport_id', 'origin_airport_seq_id', 'origin_city_market_id',
       'origin', 'origin_city_name', 'origin_state_abr', 'origin_state_fips',
       'origin_state_nm', 'origin_country', 'origin_country_name',
       'origin_wac', 'dest_airport_id', 'dest_airport_seq_id',
       'dest_city_market_id', 'dest', 'dest_city_name', 'dest_state_abr',
       'dest_state_fips', 'dest_state_nm', 'dest_country', 'dest_country_name',
       'dest_wac', 'year', 'quarter', 'month', 'distance_group', 'class',
       'data_source'], "Task 2: list of columns is wrong!"
    score += 0.5


def test_exercise3():
    from pandas_exercise import carrier_names
    global score
    assert isinstance(carrier_names, int) == True, "Variable 'carrier_names' should be integer"
    assert carrier_names == 318, "Task 3: number of distinct carriers is wrong!"
    score += 0.5


def test_exercise4():
    from pandas_exercise import freight_total, mail_total, passengers_total
    global score
    # assert isinstance(carrier_names, int) == True, "Variable 'carrier_names' should be integer"
    assert freight_total == 903296879.0, "Task 4: freight total is wrong!"
    assert mail_total == 29838395.0, "Task 4: mail total is wrong!"
    assert passengers_total == 10685608.0, "Task 4: passengers total is wrong!"
    score += 1


@pytest.fixture(scope="session", autouse=True)
def cleanup(request):
    def print_score():
        global score
        try:
            from pandas_exercise import top_10_by_passengers, top_route_origin_city, top_route_dest_city, top_route_passengers_count, top_3_carriers_df, international_travel_per_country
            # exercise 5
            print("")
            if is_iterable(top_10_by_passengers):
                carriers = ['American Airlines Inc.', 'United Air Lines Inc.', 'Delta Air Lines Inc.', 'JetBlue Airways', 'British Airways Plc', 'Lufthansa German Airlines', 'Westjet', 'Air Canada', 'Southwest Airlines Co.', 'Virgin Atlantic Airways']
                if Counter(top_10_by_passengers) == Counter(carriers):
                    score += 1.5
                    print("Task 5 is correct!")
                else:
                    print("Task 5 is wrong!")
                    extra = [x for x in list(top_10_by_passengers) if x not in carriers]
                    missing = [x for x in carriers if x not in list(top_10_by_passengers)]
                    print(f"The following carriers are wrong: {extra if extra else None}")
                    print(f"The following carriers are missing: {missing if missing else None}")
            else:
                print("Solution for exercise 5 not found. Is 'top_10_by_passengers' an iterable?")
            # exercise 6
            if isinstance(top_route_origin_city, str) and isinstance(top_route_dest_city, str) and isinstance(top_route_passengers_count, (int, float)):
                cities = ['Chicago, IL', 'New York, NY']
                passengers_count = 4131579
                if top_route_origin_city in cities and top_route_dest_city in cities and top_route_origin_city != top_route_dest_city and top_route_passengers_count == passengers_count:
                    score += 1.5
                    print("Task 6 is correct!")
                else:
                    print("Task 6 is wrong!")
                    if top_route_origin_city not in cities or top_route_dest_city not in cities or top_route_origin_city == top_route_dest_city:
                        print("Wrong origin and/or destination")
                    if top_route_passengers_count != passengers_count:
                        print("Wrong value of 'top_route_passengers_count'")
            else:
                print("Solution for exercise 6 not found. Are 'top_route_origin_city' and 'top_route_dest_city' strings? Is 'top_route_passengers_count' a number?")
            # exercise 7:
            if isinstance(top_3_carriers_df, pd.DataFrame) or isinstance(top_3_carriers_df, pd.Series):
                correct_carrier_names = ['American Airlines Inc.', 'United Air Lines Inc.', 'Delta Air Lines Inc.']
                correct_percentage_of_passengers = [13, 23, 31]
                if len(top_3_carriers_df.shape) == 1: # assume a pd.Series
                    carrier_names = top_3_carriers_df.index
                    percentage_of_passengers = sorted(top_3_carriers_df.tolist())
                elif 1 in top_3_carriers_df.shape: # assume a single column pd.DataFrame
                    carrier_names = top_3_carriers_df.index
                    percentage_of_passengers = sorted(top_3_carriers_df.iloc[:,0].tolist())
                else: # assume a two column pd.DataFrame
                    carrier_names = top_3_carriers_df.iloc[:,0]
                    percentage_of_passengers = sorted(list(top_3_carriers_df[:,1]))
                if Counter(carrier_names) == Counter(correct_carrier_names) and abs(percentage_of_passengers[0] - correct_percentage_of_passengers[0]) < 0.5 and abs(percentage_of_passengers[1] - 23) < 0.5 and abs(percentage_of_passengers[2] - 31) < 0.5:
                    score += 2
                    print("Task 7 is correct!")
                else:
                    print("Task 7 is wrong!")
                    if Counter(carrier_names) != Counter(correct_carrier_names):
                        extra = list(Counter(carrier_names) - Counter(correct_carrier_names))
                        missing = list(Counter(correct_carrier_names) - Counter(carrier_names))
                        print(f"Wrong list of airline carriers. The following carriers are wrong: {extra}. Number of missing carriers: {len(missing)}")
                    if not all([abs(x[0]-x[1])<0.5 for x in zip(percentage_of_passengers, correct_percentage_of_passengers)]):
                        print(f"Some passenger percentage values are wrong: {percentage_of_passengers}")
            else:
                print("Solution for exercise 7 not found. Is 'top_3_carriers_df' a pandas.DataFrame or a pandas.Series object?")
            # exercise 8:
            if isinstance(international_travel_per_country, pd.DataFrame) or isinstance(international_travel_per_country, pd.Series):
                correct_countries = ['Canada', 'Mexico', 'United Kingdom', 'Germany', 'Japan']
                correct_international_travel = [4, 5, 9, 13, 13]
                if len(international_travel_per_country.shape) == 1: # assume a pd.Series
                    countries = international_travel_per_country.index
                    international_travel = sorted(international_travel_per_country.tolist())
                elif 1 in international_travel_per_country.shape: # assume a single column pd.DataFrame
                    countries = international_travel_per_country.index
                    international_travel = sorted(international_travel_per_country.iloc[:,0].tolist())
                else: # assume a two column pd.DataFrame
                    countries = international_travel_per_country.iloc[:,0]
                    international_travel = sorted(list(international_travel_per_country.iloc[:,1]))
                if Counter(countries) == Counter(correct_countries) and all([abs(x[0]-x[1]) < 0.5 for x in zip(correct_international_travel, international_travel)]):
                    score += 3
                    print("Task 8 is correct!")
                else:
                    print("Task 8 is wrong!")
                    if Counter(countries) != Counter(correct_countries):
                        extra = list(Counter(countries) - Counter(correct_countries))
                        missing = list(Counter(correct_countries) - Counter(countries))
                        print(f"The following countries are wrong: {extra}. Number of missing countries: {len(missing)}")
                    if not all([abs(x[0]-x[1])<0.5 for x in zip(international_travel, correct_international_travel)]):
                        print(f"Some international travel per country percentage values are wrong: {international_travel}")
            else:
                print("Solution for exercise 8 not found. Is 'international_travel_per_country' a pandas.DataFrame or a pandas.Series object?")
        except Exception as e:
            print(e)
            print(traceback.format_exc())
        print(f"\nScore is {score}")
    request.addfinalizer(print_score)
