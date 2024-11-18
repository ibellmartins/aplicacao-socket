import socket
import os

def file(folder_name, file_name, host, port): 
    user_path = os.path.expanduser('~')
    file_path = os.path.join(user_path, folder_name, file_name)

    if not os.path.exists(file_path): #validacao da existencia do arquivo
        print(f"O arquivo {file_path} não foi encontrado.")
        return

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #criacao do socket e conexao com o server
    s.connect((host, port))  
    print(f"Conectado ao servidor {host}:{port}")


    s.send(file_name.encode()) #envia o nome do arquivo
    with open(file_path, 'rb') as f: #abre o arquivo e faz a leitura
        while True:
            leitura = f.read(1024)
            if not leitura:
                break
            s.send(leitura)
            
    print(f"Arquivo {file_name} enviado com sucesso!")
    
    s.close()

if __name__ == "__main__":
    host = '192.168.0.118' #endereço do servidor
    port = 10420  

    folder_name = input("Digite o nome da pasta em que o arquivo está: ")
    file_name = input("Digite o nome do arquivo (com a extensão .txt): ")

    file(folder_name, file_name, host, port)
