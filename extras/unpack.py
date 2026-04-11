coins = [100, 50, 25]

print(*coins) # Unpacks the array as 100, 50, 25

def currency(dollars, cents):
    return f"{dollars}.{cents}"

coins2 = {"dollars": 150, "cents": 89}

print(currency(**coins2)) # unpack as dollars=150, cents=89