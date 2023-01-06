import socket
from appJar import gui
def receive_message():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("0.0.0.0", 12345))
    s.listen(1)
    print("socket created")
    conn, addr = s.accept()
    print(f"Connection from {addr}")
    # Receive and decode the message
    data = conn.recv(1024).decode()
    print(f"Received: {data}")
    app.setLabel("Message", data)
    # Close the socket
    conn.close()
    receive_message()


app=gui("Listener")
print("App Running")
print("No Server Running Yet")
app.addLabel("Server Manager")
app.addLabel("Message","---")
app.startFrame("IP INFO")
app.addLabel("Your IP","Your IP: 192.168.0.121",1,2)
app.addLabel("Host IP","Host IP: 192.168.0.79",2,2)
app.addIcon("Connection",iconName="Wi-Fi",row=1,column=1,rowspan=2)
app.stopFrame()
app.setLabelFont(20)
app.go()