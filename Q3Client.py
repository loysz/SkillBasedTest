import socket

# Function to get quote from server
def get_quote():
    # Create socket
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to server 
    client_socket.connect(("172.104.177.86", 8888))

    # Receive quote from server
    quote = client_socket.recv(4096).decode()

    # Close socket
    client_socket.close()
    return quote

# Call get_quote function
quote = get_quote()

# Print quote
print(f"{quote}\n")
