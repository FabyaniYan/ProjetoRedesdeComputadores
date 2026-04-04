import socket

TCP_IP = "127.0.0.1"   #para a mesma maquina
TCP_PORTA = 10431      #numero RA
TAMANHO_BUFFER = 1024
COMANDO_SAIR = "QUIT"


def main():
    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        cliente.connect((TCP_IP, TCP_PORTA))
        print("Conectado ao servidor com sucesso.")

        while True:
            msg = input("Cliente: ")
            cliente.send(msg.encode("utf-8"))

            if msg.upper() == COMANDO_SAIR:
                print("Cliente solicitou o encerramento do chat.")
                break

            resposta = cliente.recv(TAMANHO_BUFFER).decode("utf-8")

            if not resposta:
                print("Servidor encerrou a conexão.")
                break

            print(f"Servidor: {resposta}")

            if resposta.upper() == COMANDO_SAIR:
                print("Servidor solicitou o encerramento do chat.")
                break

    finally:
        cliente.close()
        print("Cliente finalizado.")


if __name__ == "__main__":
    main()
