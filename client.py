import socket
import threading
import time
def receive_messages(client_socket):
    while True:
        message = client_socket.recv(1024).decode('utf-8')
        time.sleep(1)
        print(message)

server_ip = '192.168.100.248'  # IP-адрес сервера
server_port = 12345  # Порт сервера

print(f"Подключаемся к {server_ip} {server_port}")
try:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((server_ip, server_port))
    receive_thread = threading.Thread(target=receive_messages, args=(client,))
    receive_thread.start()
except ValueError:
    print("ошибка")
    input()
print("успешно")
print("Первое собщение будет твоим ником ")
while True:
    
    message = input("Сообщение :")
    client.send(message.encode('utf-8'))
