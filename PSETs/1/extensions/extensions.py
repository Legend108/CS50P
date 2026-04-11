import re

file = input("File name: ").strip().lower()

application_check = re.search(r"^.*\.(pdf|zip)$", file)
img_check= re.search(r"^.*\.(png|gif)$", file)
jpeg_check = re.search(r"^.*\.(jpg|jpeg)$", file)
txt_check = re.search(r"^.*\.txt$", file)

if application_check: print(f"application/{application_check[1]}")
if img_check: print(f"image/{img_check[1]}")
if jpeg_check: print(f"image/jpeg")
if txt_check: print(f"text/plain")
if not any([application_check, img_check, jpeg_check, txt_check]): print("application/octet-stream")
# any() returns True if at least one element in the list is "truthy" (not None/False)
# Here, it checks if any of our regex matches were successful