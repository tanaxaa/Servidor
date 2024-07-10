import socket

# Configura el servidor
host = '0.0.0.0'  # Escucha en todas las interfaces de red
port = 12345  # Puerto en el que escuchará el servidor

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((host, port))
server_socket.listen(1)

print(f"Servidor escuchando en {host}:{port}")

# Espera una conexión
client_socket, client_address = server_socket.accept()
print(f"Conexión recibida desde {client_address}")

try:
    while True:
        data = client_socket.recv(1024)
        
        if not data:
            break 
        
        print(f"Datos recibidos: {data.decode()}")
finally:
    client_socket.close()
    server_socket.close()
    print("Conexión cerrada.")
