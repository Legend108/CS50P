import random

lvls: list = [1,2,3]
lvl: int = 0
lvl1_u, lvl1_e = 1, 9
lvl2_u, lvl2_e = 10, 99
lvl3_u, lvl3_e = 100, 999
problems: list = list(range(10))

def main():
    Level = get_level()
    IntX, IntY = generate_integer(Level)
    index = 0
    score = 0
    for problem in problems:
        tries = 0 # tries reset with each problem, index doesn't and changes with each set/run
        solution = IntX[index] + IntY[index]
        print(f"Question {index+1}: {IntX[index]} + {IntY[index]}")
        index += 1
        while True:
            try:
                user = int(input("Solution: "))
                tries += 1
                if tries != 3:
                    if user == solution:
                        print("Correct!")
                        score += 1
                        break
                    else:
                        print("EEE")
                        continue
                else:
                    print("Solution is", solution)
                    break
            except ValueError:
                print("EEE")
                continue
    print(f"Your score is {score}")



def get_level() -> int:
    while True:
        try:
            set_lvl = int(input("Level: "))
            if set_lvl in lvls:
                break
            pass
        except ValueError:
            pass
    return set_lvl


def generate_integer(level):
    x = []
    y = []
    if level == 1:
        for _ in problems:
            x.append(random.randint(lvl1_u, lvl1_e))
            y.append(random.randint(lvl1_u, lvl1_e))
    elif level == 2:
        for _ in problems:
            x.append(random.randint(lvl2_u, lvl2_e))
            y.append(random.randint(lvl2_u, lvl2_e))
    else:
        for _ in problems:
            x.append(random.randint(lvl3_u, lvl3_e))
            y.append(random.randint(lvl3_u, lvl3_e))
    return x, y


if __name__ == "__main__":
    main()