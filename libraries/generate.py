from random import randint

# Get the first number and keep asking until they provide a valid integer
while True:
    try:
        x = int(input("Choose the first number: "))
        break
    except ValueError:
        print("Invalid integer")

# ask for the second number, two diff loops prevent looping back to loop 1
while True:
    try:
        y = int(input("Choose the second number: "))
        if y < x:
            print("Second number must be greater than the first number")
            continue
        # Continue restarts the loop from that point on
        # Break exits the loop no matter whats under it
        # Pass lets it go further on
        break
    except ValueError:
        print("Invalid integer")

randomNumber = randint(x, y)

print(f"Your number is {randomNumber}")