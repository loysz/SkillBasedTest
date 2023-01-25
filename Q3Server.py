import random
import socket
import threading

# Quotes array
QUOTES = [
    "Agama tidak pernah mengecewakan manusia. Tetapi manusia yang selalu mengecewakan agama.",
    "Hati yg terluka umpama besi bengkok walau diketuk sukar kembali kepada bentuk asalnya.",
    "Keikhlasan itu umpama seekor semut hitam di atas batu yang hitam di malam yang amat kelam. Ianya wujud tapi amat sukar dilihat.",
    "Harta akan habis digunakan tanpa ilmu tetapi sebaliknya ilmu akan berkembang jika ia digunakan.",
    "Reaksi emosi  jangan dituruti kerana implikasinya tidak seperti yang diimaginasi."
]

# Function to handle client 
def handle_client(client_socket):
    global threadcount
    # Randomize quote from array
    quote = random.choice(QUOTES)
    print("[*] Randomizing quotes")

    # Send quote to client
    client_socket.send(quote.encode())
    print("[*] Packet sent")

    # Close client's socket
    client_socket.close()
    threadcount -= 1
    print("[*] Disconnected")
    print(f"[*] Active thread:{threadcount}\n")

# Create socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("[*] Socket created")

# Define port
port = 8888

# Bind the socket to the IP address 0.0.0.0 and port 8888
server_socket.bind(("0.0.0.0", port))
print(f"[*] Socket bind to port:{port}")

# Listen for incoming connections
server_socket.listen(5)
print("[*] Waiting for incoming connection...")

# Trying gethostbyname function (Not neccessary)
hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)

# Define threadcount
threadcount = 0

while True:
    # Accept connection
    client_socket, client_address = server_socket.accept()
    print(f"[*] Accept connection from {hostname}:{ip_address}")

    # Create new thread to handle client's request
    client_thread = threading.Thread(target=handle_client, args=(client_socket,))
    threadcount += 1

    # Start new thread
    client_thread.start()
    print(f"[*] Active thread:{threadcount}")


