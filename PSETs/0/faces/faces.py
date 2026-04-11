def main():
    emoticon = input()
    print(convert(emoticon))

def convert(e: str):
    if not e:
        print("Provide an argument")
    else:
        s = e.replace(":)", "🙂").replace(":(", "🙁")
        return s

if __name__ =="__main__":
    main()
