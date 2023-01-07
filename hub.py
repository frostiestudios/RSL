import socket
import webbrowser
from appJar import gui

HUB_IP = "192.168.1.12"
SERVER_IP = "192.168.1.56"

def receive_message():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((SERVER_IP, 12345))
    s.listen(1)
    print("socket created")
    conn, addr = s.accept()
    print(f"Connection from {addr}")
    # Receive and decode the message
    data = conn.recv(1024).decode()
    print(f"Received: {data}")
    # Call the appropriate function based on the message received
    if data == "Open Link 1":
        open_link_1()
    elif data == "Open Link 2":
        open_link_2()
    # Close the socket
    conn.close()
    receive_message()

def open_link_1():
    webbrowser.open("https://www.example.com/link1")

def open_link_2():
    webbrowser.open("https://www.example.com/link2")

def send_message(button):
    # Create a socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Connect to the server
    s.connect((SERVER_IP, 12345))
    # Send a message to the server
    s.sendall(button.encode())
    # Close the socket
    s.close()

def get_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return s.getsockname()[0]

app = gui("HUB")
print("HUB Running")

# Get the current IP address
ip_address = get_ip_address()

app.addButtons(["Open Link 1", "Open Link 2"], [send_message, send_message])

app.startFrame("IP INFO")
app.addLabel("Your IP", f"Your IP: {ip_address}", 1, 2)
app.addIcon("Connection", iconName="Wi-Fi", row=1, column=1)
app.stopFrame()

app.go()
