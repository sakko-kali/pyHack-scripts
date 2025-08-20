import socket
import threading

# Список всех клиентов
clients = []


def handle_send():
    while True:
        message = input("SERVER: ").strip()
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

def handle_client(conn, addr):
    print(f"[+] Подключился {addr}")
    clients.append(conn)

    try:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            message = data.decode().strip()
            print(f"{addr}: {message}")

            if message.lower() == "bye":
                conn.send(b"Bye!")
                break

            # Рассылка всем клиентам кроме отправителя
            for client in clients:
                if client != conn:
                    client.sendall(f"{addr}: {message}\n".encode())

    except ConnectionResetError:
        print(f"[-] Клиент {addr} отключился внезапно")

    finally:
        clients.remove(conn)
        conn.close()
        print(f"[-] Отключен {addr}")


def start_server():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.bind(("0.0.0.0", 6001))  # слушаем на всех интерфейсах
    sock.listen(5)
    print("Сервер запущен на порту 6000...")

    threading.Thread(target=handle_send, daemon=True).start()

    while True:
        conn, addr = sock.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.daemon = True
        thread.start()


if __name__ == "__main__":
    start_server()
