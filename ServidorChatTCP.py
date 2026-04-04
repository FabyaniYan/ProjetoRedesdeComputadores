import socket

HOST = '0.0.0.0'
PORTA = 10431  #numero do RA

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.bind((HOST, PORTA))
servidor.listen(1)

print(f"Servidor aguardando conexão na porta {PORTA}...")

conn, addr = servidor.accept()
print(f"Conectado por {addr}")

while True:
    msg_cliente = conn.recv(1024).decode('utf-8')

    if not msg_cliente:
        break

    print(f"Cliente: {msg_cliente}")

    if msg_cliente.upper() == "QUIT":
        print("Cliente encerrou o chat.")
        break

    msg_servidor = input("Servidor: ")
    conn.send(msg_servidor.encode('utf-8'))

    if msg_servidor.upper() == "QUIT":
        print("Servidor encerrou o chat.")
        break

conn.close()
servidor.close()
print("Conexão encerrada.")
