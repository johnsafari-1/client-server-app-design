import socket

HOST = '127.0.0.1'      # Localhost
PORT = 5000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

print("Server is running...")
print("Waiting for client connection...")

conn, addr = server.accept()

print(f"Connected by {addr}")

message = conn.recv(1024).decode()
print("Client:", message)

reply = "Hello Client, your message was received successfully!"
conn.send(reply.encode())

conn.close()
server.close()