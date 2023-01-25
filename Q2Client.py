import socket

# create socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect to server 
client_socket.connect(("172.104.177.86", 8000))

# get temperature in Fahrenheit input
temperature_f = input("Enter temperature in Fahrenheit: ")

# send to server
client_socket.sendall(temperature_f.encode())

# receive temperature in Celsius from server
temperature_c = client_socket.recv(1024).decode()

# print temperature in Celsius
print(f"Temperature in Celsius:{temperature_c}\n")

# close socket
client_socket.close()
