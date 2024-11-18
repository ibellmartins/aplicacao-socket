import socket

def server(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    s.listen(5)
    print(f"Servidor iniciado e aguardando conexões em {host}:{port}...")

    while True:
        client_socket, client_address = s.accept() #aceita conexao
        print(f"Conexão recebida de {client_address}")

        file_name = client_socket.recv(1024).decode() #recebe nome do file 
        print(f"Recebendo arquivo: {file_name}")

        if not file_name:
            print("Nome do arquivo inválido ou não recebido.")
            client_socket.close()
            continue

        with open(file_name, 'w', encoding='utf-8') as f: #abre o arquivo para gravar
            while True:
                data = client_socket.recv(1024)
                if not data:
                    break  #quando não houver mais dados, sai do loop
                f.write(data.decode())  #decodifica e retorna o conteúdo no arquivo

        print(f"Arquivo {file_name} recebido com sucesso!")

        # Exibe o conteúdo do arquivo recebido
        with open(file_name, 'r', encoding='utf-8') as f:
            file_content = f.read()  # Lê o conteúdo do arquivo
            print(f"\nConteúdo do arquivo {file_name}:\n")
            print(file_content)
            
        client_socket.close()

if __name__ == "__main__":
    host = '192.168.0.118'  
    port = 10420
    server(host, port)
