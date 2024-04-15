import socket
import threading
import queue

class Client:
    def __init__(self, conn, address, name):
        self.conn = conn
        self.address = address
        self.name = name

    def handle_connection(self, message_queue):
        try:
            while True:
                msg = self.conn.recv(1024).decode('utf-8')
                if not msg:
                    print(f"{self.address} disconnected")
                    return
                message_queue.put(f"({self.address}): {msg}")
        except Exception as e:
            print("Error reading message:", e)
        finally:
            self.conn.close()

def main():
    print("Start server...")
    clients = []
    message_queue = queue.Queue()

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('localhost', 8000))
    server_socket.listen()

    def broadcast_messages():
        while True:
            msg = message_queue.get()
            for client in clients:
                client.conn.sendall(msg.encode('utf-8'))

    broadcast_thread = threading.Thread(target=broadcast_messages)
    broadcast_thread.start()

    while True:
        conn, address = server_socket.accept()
        print(f"Connected with {address}")
        client = Client(conn, address, "")
        clients.append(client)
        threading.Thread(target=client.handle_connection, args=(message_queue,)).start()

if __name__ == "__main__":
    main()
