import socket

HOST = '127.0.0.1'
PORTA = 10441 # Seus 5 primeiros dígitos do RA

servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.bind((HOST, PORTA))
servidor.listen(1)

print(f"Servidor de Arquivos aguardando na porta {PORTA}...")

conn, addr = servidor.accept()
print(f"Conectado por {addr}")

# Abre um novo arquivo em modo de escrita de bytes (wb)
with open('arquivo_recebido.txt', 'wb') as arquivo:
    while True:
        dados = conn.recv(1024)
        if not dados:
            break
        arquivo.write(dados)

print("Arquivo recebido e salvo como 'arquivo_recebido.txt'!")
conn.close()
servidor.close()