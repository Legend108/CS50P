bal = 0

# Can only check using mypy, python doesnt take it seriously
def add(n: int) -> None:
    global bal
    bal += n


add("cat")
print(bal)