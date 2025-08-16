

with open("logins.txt", "r", encoding="utf-8") as f_in, \
     open("short_logins.txt", "w", encoding="utf-8") as f_out:

    for line in f_in:
        login = line.strip()  # убрали \n
        if len(login) < 5:
            f_out.write(login + "\n")
            f_out.write(login + "\n")
