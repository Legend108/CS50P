import re

valid_months = [
    "january",
    "february",
    "march",
    "april",
    "may",
    "june",
    "july",
    "august",
    "september",
    "october",
    "november",
    "december"
]

def slf(match: str):
    check = re.match(r"^(?P<m>[0-9]{1,2})/(?P<d>[0-9]{1,2})/(?P<y>[0-9]{4})$", match)
    if check:
        if int(check.group("d")) <= 31: # type: ignore
            if int(check.group("m")) <= 12: # type: ignore
                return f"{check.group("y")}-{check.group("m")}-{check.group("d")}"
            return False
        return False
    else:
        return False

def written(match: str):
    check = re.match(r"^(?P<m>[a-zA-Z]+) (?P<d>[0-9]{1,2}), (?P<y>[0-9]{4})$", match)
    if check:
        if check.group("m").lower() in valid_months: # type: ignore
            m_n = valid_months.index(check.group("m").lower())
            if int(check.group("d")) <= 31: # type: ignore
                return f"{check.group("y")}-{m_n+1}-{check.group("d")}"
            return False
        else:
            return False
    else:
        return False

def main():
    while True:
        date = input("Enter a date: ")
        if dt := slf(date):
            print(dt)
            break
        if ds := written(date):
            print(ds)
            break
        continue

if __name__ == "__main__":
    main()