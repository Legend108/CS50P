import sys
import requests
import json

if(len(sys.argv) != 2):
    sys.exit("Atleast/atmost 2 arguments are needed")

request= requests.get("https://itunes.apple.com/search?entity=song&term=" + sys.argv[1])
objects = request.json()

for object in objects["results"]:
    print(object["trackName"])