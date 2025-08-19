import socket

s = socket.socket()
s.bind(("127.0.0.1", 6000))
s.listen()

print("Ожидание подключения...")
conn, addr = s.accept()
print("Connected:", addr)

while True:
    data = conn.recv(1024)
    if not data:
        break  # клиент отключился
    message = data.decode()

    if message.strip() == "exit":
        print("Клиент вышел")
        break

    print("Клиент:", message)
    conn.sendall(("Эхо: " + message).encode())

conn.close()
s.close()
