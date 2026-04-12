inp = input("Type.... ").strip()
out = ""
for let in inp:
    if let.lower() not in ["a", "e", "i", "o", "u"]:
        out += let
print(out)