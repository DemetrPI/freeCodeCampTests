import pytest
from time_calculator import add_time

# # Test cases without weekDay
test_cases_without_weekDay = [
    pytest.param("3:30 PM", "2:12", "5:42 PM", id="test_same_period"),
    pytest.param("11:55 AM", "3:12", "3:07 PM", id="test_different_period"),
    pytest.param("9:15 PM", "5:30", "2:45 AM (next day)", id="test_next_day"),
    pytest.param("11:40 AM", "0:25", "12:05 PM", id="test_period_change_at_twelve"),
    pytest.param("2:59 AM", "24:00", "2:59 AM (next day)", id="test_twenty_four"),
    pytest.param("11:59 PM", "24:05", "12:04 AM (2 days later)", id="test_two_days_later"),
    pytest.param("8:16 PM", "466:02", "6:18 AM (20 days later)", id="test_high_duration"),
    pytest.param("5:01 AM", "0:00", "5:01 AM", id="test_no_change")]

# Test cases with weekDay
test_cases_with_weekDay = [    
    pytest.param("3:30 PM", "2:12", "Monday", "5:42 PM, Monday", id="test_same_period_with_day"),
    pytest.param("2:59 AM", "24:00", "saturDay", "2:59 AM, Sunday (next day)", id="test_twenty_four_with_day"),
    pytest.param("11:59 PM", "24:05", "Wednesday", "12:04 AM, Friday (2 days later)", id="test_two_days_later_with_day"),
    pytest.param("8:16 PM", "466:02", "tuesday", "6:18 AM, Monday (20 days later)", id="test_high_duration_with_day"),
]

@pytest.mark.parametrize("start, duration, weekDay, expected", test_cases_with_weekDay)
def test_add_time(start, duration, weekDay, expected):
    actual = add_time(start, duration, weekDay)
    assert actual == expected

@pytest.mark.parametrize("start, duration, expected", test_cases_without_weekDay)
def test_add_time_(start, duration, expected):
    actual = add_time(start, duration)
    assert actual == expected
    
