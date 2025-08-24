import socket
import os
import subprocess
from sys import stdin, stdout

############################################Получить ip по домену#########################################
# domain = "8.8.4.4"
# ip = socket.gethostbyaddr(domain)
# print(f"IP-адрес {domain}: {ip}")

############################################Пинг по домену#########################################

# hostname = "google.com"
# resp = os.system(f"ping -c 4 {hostname}")
# if resp == 0:
#     print(f"{hostname} доступен")
# else:
#     print(f"{hostname} недоступен")

############################################Пинг по домену через subprocess#########################################

# hostname = "google.com"
# comand = f"ping -c 4 {hostname}".split()
# proc = subprocess.run(comand,capture_output=True, text=True)
# for line in proc.stdout.splitlines():
#     if "time=" in line:
#         print(line)

# p1 = subprocess.Popen(["ps","aux"], stdout=subprocess.PIPE, text=True)
# p2 = subprocess.Popen(["grep","python"], stdin=p1.stdout, stdout=subprocess.PIPE, text=True)
# output, _ = p2.communicate()
# print(output)
