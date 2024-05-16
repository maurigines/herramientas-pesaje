from pymodbus.client import ModbusTcpClient
import time

def interpret_as_signed_16bit(value):
    if value > 32767:
        value -= 65536
    return value

# Configuración MODBUS TCP/IP
client = ModbusTcpClient('192.168.1.124', port=502)  # Reemplazar IP y puerto del Indicador de peso

connection = client.connect()

if connection:
    try:
        while True:
            try:
                
                address = 30008 - 30001  
                result = client.read_input_registers(address, 2, unit=1)  

                if not result.isError():
                    
                    low_word = result.registers[0]  
                    # Interpretar el valor como entero de 16 bits con signo
                    raw_value = interpret_as_signed_16bit(low_word)     

                    weight = raw_value * 0.1  # Ajuste del factor de escala balanza
                    formatted_weight = f"{weight:.1f}" # Formatear el peso con un decimal

                    print(f"Peso: {formatted_weight} kg")
                   
                    
                else:
                    print("Error al leer los registros")

                time.sleep(0.1)  # Ajuste de velocidad de consultas en segundos

            except Exception as e:
                print(f"Excepción al leer los registros: {e}")

    except KeyboardInterrupt:
        print("Interrupción del teclado detectada. Terminando el programa de manera segura...")

    finally:
       
        client.close()
else:
    print("No se pudo conectar al cliente MODBUS")
