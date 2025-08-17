import sys

for login in sys.argv[1:]:
    login.strip()
    if len(login) < 5:
        sys.stderr.write(f"'{login}' Слишком короткий\n")
    else:
        sys.stdout.write(f"'{login}' Валидный\n")
