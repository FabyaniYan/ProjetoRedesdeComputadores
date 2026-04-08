import socket
import os

TCP_IP = '127.0.0.1'
TCP_PORTA = 10441

def menu():
    print("\n" + "=" * 35)
    print("      MENU DE TRANSFERÊNCIA")
    print("=" * 35)
    print("1. Digitar o nome de um arquivo para enviar")
    print("2. Sair")
    print("=" * 35)
    return input("Escolha uma opção: ")

def main():
    while True:
        opcao = menu()
        
        if opcao == '1':
            nome_arquivo = input("Digite o nome exato do arquivo (ex: arquivo_teste.txt): ")
            
            # Verifica se o arquivo existe na pasta
            if not os.path.exists(nome_arquivo):
                print(f"\n[ERRO] O arquivo '{nome_arquivo}' não foi encontrado nesta pasta.")
                continue

            cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            try:
                cliente.connect((TCP_IP, TCP_PORTA))
                print("\nConectado ao servidor!")

                # Abre o arquivo escolhido e envia
                with open(nome_arquivo, 'rb') as arquivo:
                    pedacos = arquivo.read(1024)
                    while pedacos:
                        cliente.send(pedacos)
                        pedacos = arquivo.read(1024)
                        
                print(f"[SUCESSO] Arquivo '{nome_arquivo}' enviado com sucesso!")
            except ConnectionRefusedError:
                print("\n[ERRO] Não foi possível conectar. O ServidorArquivo.py está rodando?")
            finally:
                cliente.close()
            
            break # Sai do loop após enviar, agora com o alinhamento correto!
            
        elif opcao == '2':
            print("\nEncerrando o programa...")
            break
        else:
            print("\n[AVISO] Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()