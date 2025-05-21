import socket

servidor_host = 'localhost'
servidor_porta = 12000

servidor_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

servidor_socket.bind((servidor_host, servidor_porta)) 
print("Servidor pronto para receber...")

try:
    while True:
        mensagem, endereco = servidor_socket.recvfrom(1024)
        if not mensagem:
            break
        print(f"Recebido de {endereco}: {mensagem.decode()}")
        servidor_socket.sendto(b'pong', endereco)

except KeyboardInterrupt:
    print("\nServidor encerrado.")

finally:
    servidor_socket.close()
