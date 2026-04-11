def main() -> None:
    yell("Hello", "World", "Again", reverse=False)

def yell(*args, reverse: bool=False) -> None:
    # for arg in args:
    #    list.append(arg.upper())
    # list: list = map(str.upper, args)
    list = [word.upper() for word in args]
    if not reverse:
        print(*list)
    else:
        list.reverse()
        print(*list)

if __name__ == "__main__":
    main()