# use sys
import sys
from statistics import mean

# Check for lengths and if appropriate go to the next line
# Multiple cases to handle different scenarios, can just use 1 too
# using len(argv) != 3:
if len(sys.argv) < 3:
    sys.exit("Too few arguments")
elif len(sys.argv) > 3:
    sys.exit("Too many arguments")

try:
    num1 = float(sys.argv[1])
    num2 = float(sys.argv[2])
    print(round(mean([num1, num2])))
except ValueError:
    print("Choose numbers")

# sys.argv[1:] (Start counting from the 2nd element in the list)
# sys.argv[1:-1] (Start counting from the 2nd element and terminate at the 2nd last element of the list)