try:
    while True:
        frac = input("Fraction: ")
        sp = frac.split("/")
        X = int(sp[0])
        Y = int(sp[1])
        if X/Y > 1:
            print("E")
            continue
        elif X/Y < 1:
            print(f"{round(X/Y*100)}%")
            break
        elif X/Y == 1:
            print("F")
            break
        else:
            print("E")

except ValueError:
    ...
except ZeroDivisionError:
    ...