def main():
    student = get_student()
    print(f"Name is {student[0]} and house {student[1]}", student[2])

def get_student():
    name = input("What's your name: ")
    house = input("What's your house: ")
    tuple1 = ("harry", "hermione")

    return (name, house, tuple1) # this is a tuple, its a non changeable/immutable Type of List.
                        # works like a list too accessing using positions and idnexes


if __name__ == "__main__":
    main()