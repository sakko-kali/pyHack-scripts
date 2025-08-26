import csv
import os

fieldnames=["name", "screen", "CPU", "antutu", "signal", "battery", "price","rating"]

with open("iqoo.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    if os.stat("iqoo.csv").st_size == 0:
        writer.writeheader()

    while True:
        row = {}
        print("Введите данные:")

        for field in fieldnames:
            row[field] = input(f"{field}: ").strip()

        print([row[f] for f in fieldnames])

        writer.writerow(row)


