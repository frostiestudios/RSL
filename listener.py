import socket
import webbrowser
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
    conn.close()
    receive_message()

def receive_link():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("0.0.0.0", 12345))
    s.listen(1)

    # Accept a connection
    conn, addr = s.accept()
    print(f"Connection from {addr}")
    data = conn.recv(1024).decode()
    print(f"Received: {data}")
    webbrowser.open_new_tab(f"{data}")
    
# Create a loop to continuously listen for incoming connections
while True:
    receive_message()
    receive_file()