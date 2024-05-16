import socket

def procesar_paquete(data):
    resultados = []

    # Buscar el inicio de cada lectura válida
    inicio = data.find(b'\r')
    while inicio != -1:
        if inicio + 8 <= len(data):  # Asegurarse de que hay suficientes bytes para leer
            fragmento = data[inicio + 1:inicio + 8].decode()  # Extraer los 8 bytes siguientes al \r
            try:
                status_byte = ord(fragmento[0])  # Convertir el byte de status a entero
                peso = fragmento[1:]  # El peso no necesita ser convertido a entero
                # Configuracion de indicador de STATUS
                status = []
                if status_byte & 0b00000001:  
                    status.append("N")
                else:
                    status.append("BR")
                if status_byte & 0b00000010:  
                    status.append("ZERO")
                if status_byte & 0b00000100:  
                    status.append("ESTABLE")
                else:
                    status.append("INESTABLE")
                if status_byte & 0b00001000:  
                    status.append("-")
                else:
                     status.append("+")
                if status_byte & 0b00010000 or fragmento.startswith('p'):  
                      status.append("FUERA DE RANGO")
                                 
                status_str = ", ".join(status) if status else "Desconocido"
                # Configuracion de formato de Peso
                if peso == "******":
                    peso_str = "******"
                elif peso == "000000":
                    peso_str = "0,00"
                else:
                    peso_str = f"{int(peso) / 100:.2f}".replace('.', ',')  
                resultados.append(f"{peso_str} kg ({status_str})")

            except Exception as e:
                print(f"Error al procesar la lectura: {e}")
        
        inicio = data.find(b'\r', inicio + 1)  # Buscar el siguiente retorno de carro
    
    return resultados

# Configurar el socket UDP
HOST = '192.168.1.183' #  IP de Host, El Indicador de peso envia datos aqui
PORT = 1024 # Puerto donde envia 
BUFFER_SIZE = 100

with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s:
    s.bind((HOST, PORT))
    print("Escuchando en", (HOST, PORT))
    while True:
        data, addr = s.recvfrom(BUFFER_SIZE)
        resultados = procesar_paquete(data)
        if resultados:
            for resultado in resultados:
                print(resultado)
