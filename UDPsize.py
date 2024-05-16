import socket

def recibir_paquetes_udp(puerto):
    # Crea un socket UDP
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    # Asocia el socket al puerto especificado
    sock.bind(('192.168.1.183', puerto))

    print(f"Escuchando en el puerto UDP {puerto}...")

    while True:
        # Recibe un paquete UDP y la dirección del remitente
        data, address = sock.recvfrom(1024)  # Tamaño del búfer para recibir datos

        # Imprime la cantidad de bytes recibidos en el paquete
        print(f"Recibido {len(data)} bytes de {address[0]}:{address[1]}")

# Define el puerto en el que se desea escuchar
puerto_udp = 1024

# Inicia la función para recibir paquetes UDP
recibir_paquetes_udp(puerto_udp)
