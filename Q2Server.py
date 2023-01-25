import socket

port = 8000

# function to convert temperature from Fahrenheit to Celsius
def fahrenheit_to_celsius(temp_f):
    temp_c = (temp_f - 32) * 5/9
    return temp_c

# create socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("[*] Socket created")

# bind socket
server_socket.bind(("0.0.0.0", port))
print(f"[*] Socket bind to port:{port}")

# listen for incoming connection
server_socket.listen(5)
print("[*] Waiting for connection...")

while True:
    # accept connection from client
    client_socket, address = server_socket.accept()
    print(f"[*] Accepted Connection from {address[0]}:{address[1]}") 

    # receive temperature in Fahrenheit from client
    temperature_f = client_socket.recv(1024).decode()
    print(f"[*] Receive temperature in Fahrenheit :{temperature_f}") 

    # convert temperature to Celsius
    temperature_c = fahrenheit_to_celsius(float(temperature_f))
    print("[*] Convert temperature to Celcius")

    # send temperature in Celsius back to client
    client_socket.sendall(str(temperature_c).encode())
    print("[*] Packet sent")

    # close client socket
    client_socket.close()
    print("[*] Disconnected\n")
