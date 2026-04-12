from pyfiglet import Figlet
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("--font", "-f", help="Select a font")
parsed = parser.parse_args()

inp = input("Input: ")

if parsed.font or parsed.f:
    try:
        if parsed.font:
            f = Figlet(font=parsed.font)
        else:
            f = Figlet(font=parsed.f)
        print(f.renderText(inp))
    except:
        print("Invalid font")
else:
    print(Figlet().renderText(inp))