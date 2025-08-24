import socket

domain = "8.8.4.4"
ip = socket.gethostbyaddr(domain)
print(f"IP-адрес {domain}: {ip}")