balance = 0

def add(n: int):
    global balance # Balance is not available inside the function so we use global to declare it as usable
    balance += n

add(50)

print(balance)