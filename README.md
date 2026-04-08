# Projeto 1 - Analise Programação de Socket UDP e TCP

Redes de Computadores

| Aluno | RA |
| :--- | :--- |
| Fabyani Tiva Yan | 10431835 |
| Rafael Araujo Cabral Moreira | 10441919 |


# Chat TCP e Transferência de Arquivos em Python

## Descrição

Este projeto apresenta duas aplicações utilizando sockets TCP em Python:

- um chat cliente-servidor para troca de mensagens;
- um sistema simples de transferência de arquivos.

## Arquivos do projeto

- `ClienteChatTCP.py`: conecta ao servidor e permite enviar e receber mensagens no chat.
- `ServidorChatTCP.py`: cria o servidor de chat, aguarda a conexão do cliente e responde às mensagens.
- `ClienteArquivo.py`: exibe um menu, permite escolher um arquivo da pasta local e envia esse arquivo ao servidor.
- `ServidorArquivo.py`: recebe os dados enviados pelo cliente e salva o conteúdo em um novo arquivo.
- `arquivo_teste.txt`: arquivo de exemplo utilizado para teste de envio.
- `arquivo_recebido.txt`: arquivo gerado pelo servidor após o recebimento.

## Funcionamento

### Chat TCP

O servidor de chat fica aguardando conexão na porta `10431`.  
Quando o cliente se conecta, a comunicação é feita pelo terminal, com envio e recebimento de mensagens entre os dois lados.  
A conversa é encerrada quando cliente ou servidor envia o comando `QUIT`.

### Transferência de arquivos

O servidor de arquivos fica aguardando conexão na porta `10441`.  
O cliente exibe um menu com a opção de digitar o nome de um arquivo da pasta local.  
Se o arquivo existir, ele é aberto em modo binário e enviado ao servidor em blocos de 1024 bytes.  
O servidor recebe os dados e grava o conteúdo no arquivo `arquivo_recebido.txt`.

## Conceitos utilizados

- comunicação cliente-servidor;
- protocolo TCP;
- sockets em Python;
- criação de conexão com `connect()`;
- espera de conexão com `bind()`, `listen()` e `accept()`;
- envio e recebimento de dados com `send()` e `recv()`;
- leitura e escrita de arquivos em modo binário.

## Como executar

### 1. Chat TCP

No terminal 1:

```bash
python ServidorChatTCP.py

No terminal 2:

```bash
python ClienteChatTCP.py

Para encerrar a conversa:

QUIT

### 2. Transferência de arquivos

No terminal 1:

```bash
python ServidorArquivo.py
```

No terminal 2:

```bash
python ClienteArquivo.py
```

Escolher o nome do arquivo.
