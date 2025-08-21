import socket
import threading
import sys
import csv

clients = []


def server_start():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(("0.0.0.0", 6000))
    sock.listen(5)

    print("Ждем подключений")
    threading.Thread(target=hendle_send, daemon=True).start()

    while True:
        conn, addr = sock.accept()
        print(f"Клиент: {addr} подключился")
        clients.append(conn)
        threading.Thread(target=hendle_recive, args=(conn,addr), daemon=True).start()


def hendle_recive(conn,addr):
    while True:
        message = conn.recv(1024).decode().strip()
        print(addr, message)
        if message == "bye":
            conn.sendall(b"Server off\n")
            conn.close()
            sys.exit(0)
        for client in clients:
            if client != conn:
                client.sendall(f"{addr}: {message}\n".encode())


def hendle_send():
    while True:
        if clients:
            message = input("\nSERVER: ").strip()
            if message.lower() == "bye":
                print("Сервер завершает работу...")
                # посылаем клиентам уведомление и выходим
                for client in clients:
                    client.sendall(b"Server is shutting down...\n")
                    client.close()
                break
            # рассылаем серверное сообщение всем клиентам
            for client in clients:
                client.sendall(f"[SERVER]: {message}\n".encode())
            sys.exit(0)

if __name__ == "__main__":
    server_start()

