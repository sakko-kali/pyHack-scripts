import csv


with open("sockets.csv","r") as file:
    reader = csv.reader(file)

    with open("New_sockets.csv","w") as f:
        writer=csv.writer(f)
        for lines in reader:
            writer.writerow(lines)