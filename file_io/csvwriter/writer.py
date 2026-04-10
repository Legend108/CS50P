import csv

gpu_name = input("GPU name: ")

while True:
    try:
        gpu_price = int(input("GPU price: "))
        break
    except ValueError:
        print("Provide a valid gpu price")

with open("gpu.csv", "a") as file:
    writer = csv.writer(file)
    writer.writerow([gpu_name, gpu_price])