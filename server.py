import socket
import threading

port = 8888
server_ip = socket.gethostbyname(socket.gethostname())
server_addres = (server_ip, port)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(server_addres)
header = 1024
format = "ascii"
exit = "exit()"
server.listen()
clients = []

def server_recv(cli , addr):
    while True:
        try:
            message = cli.recv(header).decode(format).strip()
            server_send(message)
        except:
            continue

def server_send(message):
    for client in clients:
        try:    
            client.send(message.encode(format))
        except:
            client.close()
            clients.remove(client)

def start():
    while True:    
        cli, addr= server.accept()
        clients.append(cli)
        thread_revc = threading.Thread(target=server_recv, args=(cli,addr))
        thread_revc.start()

start()