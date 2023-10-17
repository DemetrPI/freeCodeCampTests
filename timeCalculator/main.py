from time_calculator import add_time
from pytest import main


print(add_time("11:06 PM", "2:02"))


# Run unit tests automatically
main(['-vv'])