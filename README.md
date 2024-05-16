# TCP - UDP Leer Peso

Este repositorio contiene un script en Python para leer datos de pesaje de una balanza utilizando el protocolo MODBUS TCP/IP y UDP. EL fin es para utilizarlo como herramienta de pruebas y control.

## Descripción

El script se conecta a un dispositivo de pesaje utilizando MODBUS TCP/IP y lee registros de entrada para obtener el peso medido. Luego, interpreta y formatea el valor del peso, y lo imprime en la consola.
En el caso de leer UDP se crea un socket UDP, donde el indicador envia paquetes de 100 bytes con lecturas de peso empaquetadas, se formatea y se imprime por consola.

## Requisitos

- Python 3.x
- Librería `pymodbus`, `socket`
