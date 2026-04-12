import random

level = 0
while True:
    try:
        lvl = int(input("Level: "))
        if lvl >= 1:
            chosen = random.randint(1, lvl)
            while True:
                try:
                    guess = int(input("Guess: "))
                    if guess >= 1:
                        if guess > chosen:
                            print("Too high!")
                        elif guess == chosen:
                            print("Correct!")
                            break
                        else:
                            print("Too low!")
                    else: 
                        continue
                except ValueError:
                    continue
        else:
            continue
        break
    except ValueError:
        continue