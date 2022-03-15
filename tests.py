import pytest

from pandas_exercise import columns, carrier_names, freight_total, mail_total, passengers_total, top_10_by_passengers, top_route_origin_city, top_route_dest_city, top_route_passengers_count, top_3_carriers_df, international_travel_per_country

score = 0.0


def is_iterable(object):
    try:
        z = iter(object)
    except TypeError:
        return False
    return True


def test_task2():
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


def test_task3():
    global score
    assert isinstance(carrier_names, int) == True, "Variable 'carrier_names' should be integer"
    assert carrier_names == 318, "Task 3: number of distinct carriers is wrong!"
    score += 0.5


def test_task4():
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
        if is_iterable(top_10_by_passengers):
            print(True)
            # score += 1.5
        print(f"\nScore is {score}")
    request.addfinalizer(print_score)
