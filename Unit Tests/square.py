def main():
    x = int(input("What's x? "))
    square(x)

def square(n="Enter a number."):
    try:
        return int(n)*int(n)
    except ValueError:
        return "Enter a number."
    except TypeError:
        return n

if __name__ == "__main__":
    main()