import socket, threading

def handle_recive(sock,addr):
    while True:
        data = sock.recv(1024)
        if not data:
            print(f"Client: {addr} Disconnected!")
            sock.close()
            break
        message = data.decode().strip()
        if message.lower() == "bye":
            sock.send(b"Bye! Have a good day\n")
            sock.close()
            break
        print(message)

def heandle_send(sock):
    while True:
        message = input() + "\n"
        sock.sendall(message.encode())

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(("192.168.1.8", 6000))
sock.listen(2)


print("Ожидание подключения...")
conn, addr = sock.accept()
print("Подключен:", addr)

threading.Thread(target=handle_recive, args=(conn, addr), daemon=True).start()
heandle_send(conn)

sock.close()



