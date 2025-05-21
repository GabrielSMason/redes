import socket
import time

servidor_host = 'localhost'
servidor_porta = 12000

cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
cliente_socket.settimeout(1)

for i in range(10):
    mensagem = f'ping {i + 1}'
    tempo_envio = time.time()

    try:
        cliente_socket.sendto(mensagem.encode(), (servidor_host, servidor_porta))
        resposta, endereco = cliente_socket.recvfrom(1024)
        tempo_recebimento = time.time()

        rtt = tempo_recebimento - tempo_envio
        print(f"Resposta recebida: {resposta.decode()} | RTT = {rtt:.10f} segundos")

    except socket.error:
        print("Erro ao enviar ou receber dados.")

cliente_socket.close()
