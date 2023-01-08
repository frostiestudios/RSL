from appJar import gui
import socket


# Extract the IP addresses using regular expressions


def execute(btn):
    # Get the selected options from the app
    ip_address = "192.168.0.71"

    # Send the content based on the selected type
    if btn == "Update Drivers":
        data = "UPD"
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip_address, 12345))
        s.sendall(data.encode())
        s.close()
    if btn == "Restart":
        # Send a link
        data = "RST"
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip_address, 12345))
        s.sendall(data.encode())
        s.close()
    if btn == "Custom Shaders Patch":
        data = "CSP"
    if btn == "Open Sigma":
        data = "SIG"
    if btn == "Test":
        data = "TET"
    if btn == "Shut Down":
        data = "SHT"
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip_address, 12345))
        s.sendall(data.encode())
        s.close()


app = gui()

ip="192.168.0.71"
name="KGB"

app.startLabelFrame("PC 1",1,1)
app.addLabel("Name",f"{name}",1,2)
app.addLabel("IP2",f"{ip}",2,2)
app.addIcon("Wi-Fi","Wi-Fi",1,1,0,2)
app.addButtons(["Update Drivers","Restart","Custom Shaders Patch","Open Sigma","Test","Shut Down"], execute, 3,2,2,2)
app.stopLabelFrame()


app.go()