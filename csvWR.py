import csv

with open("sockets.csv",newline="") as f_in, \
     open("sock.csv","w",newline="") as f_out:
     reader = csv.DictReader(f_in)
     writer = csv.DictWriter(f_out, fieldnames=["id","username","password"])
     writer.writeheader()
     for row in reader:
         if len(row["password"]) < 5:
             writer.writerow(row)







