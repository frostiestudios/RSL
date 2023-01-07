import socket
from appJar import gui

def send_message(button):
    # Create a socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Connect to the server
    s.connect(("192.168.0.121", 12345))
    # Send a message to the server
    s.sendall(button.encode())
    # Close the socket
    s.close()

def get_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    return s.getsockname()[0]

app = gui("Hub")
ip_address = get_ip_address()
print("App Running")
print("HUB RUNNING AT IP:",ip_address)

app.addButtons(["Open Link 1", "Open Link 2"], [send_message, send_message])

app.startFrame("IP INFO")
app.addLabel("Your IP", f"Your IP: {ip_address}", 1, 2)
app.addIcon("Connection", iconName="Wi-Fi", row=1, column=1)
app.stopFrame()

app.go()
