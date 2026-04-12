import pyfiglet 
import sys
import random

figlet: object = pyfiglet.Figlet()
fonts: list = figlet.getFonts()
q: str = "Text: "

if len(sys.argv) == 3:
    if sys.argv[1] in ["-f", "--font"]:
        if sys.argv[2] in fonts:
            print(pyfiglet.figlet_format(input(q), font=sys.argv[2]))
        else:
            sys.exit("Invalid font")
    else:
        sys.exit("Invalid syntax")
elif len(sys.argv) == 1:
    print(pyfiglet.figlet_format(input(q), font=random.choice(fonts)))
else:
    sys.exit("Invalid number of arguments")