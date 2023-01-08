import socket
from appJar import gui

def receive_message():
    # Create a socket and listen for incoming connections
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("0.0.0.0", 12345))
    s.listen(1)

    # Accept a connection
    conn, addr = s.accept()
    print(f"Connection from {addr}")
    # Receive and decode the message
    data = conn.recv(1024).decode()
    print(f"Received: {data}")

    # Open a message window with the received message
    app = gui("Message")
    app.infoBox("Message Received", data)
    # Close the socket
    conn.close()
    receive_message()
    
def receive_file():
    # Create a socket and listen for incoming connections
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("0.0.0.0", 12345))
    s.listen(1)

    # Accept a connection
    conn, addr = s.accept()
    print(f"Connection from {addr}")

    # Receive and save the file
    with open("received_file.bin", "wb") as f:
        f.write(conn.recv(1024))

    # Close the socket
    conn.close()
# Create a loop to continuously listen for incoming connections
while True:
    receive_message()
    receive_file()