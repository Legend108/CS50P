from PIL import Image
import sys
import os

 # Only one argument needed
if len(sys.argv) > 2 or len(sys.argv) == 1:
    print("Wrong number of arguments, provide only one image for thumbnail")
    sys.exit()

if not os.path.isfile(sys.argv[1]):
    print("File does not exist")
    sys.exit()

# From the documentation

file_provided = sys.argv[1]
stan_size = 200, 200

with Image.open(file_provided) as img:
    img.thumbnail(stan_size)
    img.save("thumbnail_" + file_provided)