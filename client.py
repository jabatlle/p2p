import socket
import threading

def receive_messages(client_socket):
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            print(message)
        except Exception as e:
            print("Error receiving message:", e)
            break
    client_socket.close()

def send_message(client_socket):
    while True:
        try:
            message = input()
            client_socket.send(message.encode('utf-8'))
        except Exception as e:
            print("Error sending message:", e)
            break

def main():
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('localhost', 8000))

    receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
    receive_thread.start()

    send_message(client_socket)

if __name__ == "__main__":
    main()
