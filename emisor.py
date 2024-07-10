import socket

# Configura el cliente
host = '192.168.43.117'  # Reemplaza 'IP_DEL_SERVIDOR con ip privada'
port = 12345  # Puerto en el que el servidor está escuchando
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((host, port))

try:
    while True:
        message = input("Ingresa el mensaje que deseas enviar al servidor (o 'salir' para terminar): ")
        
        if message.lower() == 'salir':
            break
              
        client_socket.send(message.encode())
finally:
    client_socket.close()
    print("Conexión cerrada.")
