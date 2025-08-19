import socket

s = socket.socket()
s.bind(("127.0.0.1", 6000))
s.listen(1)

print("Ожидание подключения...")
conn, addr = s.accept()
print("Connected:", addr)

while True:
    data = conn.recv(1024)
    if not data:
        break  # клиент отключился
    message = data.decode().strip()

    if message == "bye":
        print("Клиент вышел")
        break

    print(message,"\n Введите ответ")
    out_message = input() + "\n"
    conn.sendall((out_message).encode())

conn.close()
s.close()
