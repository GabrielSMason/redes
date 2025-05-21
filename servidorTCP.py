import socket

servidor_host = 'localhost'  
servidor_porta = 12000

servidor_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

servidor_socket.bind((servidor_host, servidor_porta))
servidor_socket.listen(1)

print("Servidor aguardando conexao...")

conn, endereco = servidor_socket.accept()

try:
    while True:
        mensagem = conn.recv(1024)
        if not mensagem:
            break
        print(f"Recebido de {endereco}: {mensagem.decode()}")
        conn.send(b'pong')

except KeyboardInterrupt:
    print("\nServidor encerrado pelo usuário.")

finally:
    conn.close()
    servidor_socket.close()
