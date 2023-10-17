from pytest import main
from arithmetic_arranger import arithmetic_arranger


print(arithmetic_arranger(['32 - 698', '1 - 3801', '45 + 43', '123 + 49', '988 + 40'], True))


# Run unit tests automatically
main(['-vv'])
