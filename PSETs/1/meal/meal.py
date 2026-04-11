import re

def main():
    time = input("What time is it? ")
    dec_t = convert(time)
    if 7 <= dec_t <= 8:
        print("breakfast time")
    if 12 <= dec_t <= 13:
        print("lunch time")
    if 18 <= dec_t <= 19:
        print("dinner time")


def convert(time):
    if times := re.match(r"^(?P<h>[0-9]{1,2}):(?P<m>[0-5]{1}[0-9]{1})$", time):
        hr = int(times.group("h"))
        min = int(times.group("m"))
        return round(hr + min/60, 2)
    else:
        raise ValueError("Invalid Time")


if __name__ == "__main__":
    main()