import socket
import threading

clients = []
clients_name=[]
clients_ip=[]
def handle_client(client_socket, client_address):
    while True:
        message = client_socket.recv(1024).decode('utf-8')
        if not message:
            break
        print(f"Получено сообщение от {client_address}: {message}")
        print(clients_ip )
        i=clients_ip.index(client_address)
        print(clients_name[i])
        message="["+clients_name[i]+"] :"+message
       
        broadcast(message, client_socket)

    client_socket.close()
    clients.remove(client_socket)

def broadcast(message, sender_socket):
    for client in clients:
        if client != sender_socket:
            try:
                client.send(message.encode('utf-8'))
            except:
                client.close()
                clients.remove(client)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip='0.0.0.0'
port=12345

server.bind((ip, port))
server.listen(5)

host=socket.gethostname()
ip=socket.gethostbyname(host)

print(host," ",ip,' ',port)
print("Сервер запущен. Ожидание подключений...")

while True:
    client_socket, client_address = server.accept()
    print(f"Принято соединение от {client_address[0]}:{client_address[1]}")
    clients.append(client_socket)
    message = client_socket.recv(1024).decode('utf-8')
    clients_name.append(message)
    clients_ip.append(client_address)
    client_handler = threading.Thread(target=handle_client, args=(client_socket, client_address))
    client_handler.start()
