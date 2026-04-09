# Generate average/mean using statistics

from statistics import mean
# Get the first number
while True:
    try:
        x = float(input("Choose your first number: "))
        break
    except ValueError:
        print("Choose a valid number")

while True:
    try:
        y = float(input("Choose the second number: "))
        break
    except ValueError:
        print("Choose a valid number")

print(mean([x,y]))