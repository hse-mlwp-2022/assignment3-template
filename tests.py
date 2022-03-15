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
 