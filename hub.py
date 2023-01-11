from appJar import gui
import socket
import re
with open("htmlserver/contacts.html", "r") as f:
    contents = f.read()
# Extract the IP addresses using regular expressions


def execute(btn):
    # Get the selected options from the app
    ip_address = app.getOptionBox("PCs")

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
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip_address, 12345))
        s.sendall(data.encode())
        s.close()
    if btn == "Open Sigma":
        data = "SIG"
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip_address, 12345))
        s.sendall(data.encode())
        s.close()
    if btn == "Test":
        data = "TET"
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip_address, 12345))
        s.sendall(data.encode())
        s.close()
    if btn == "Shut Down":
        data = "SHT"
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip_address, 12345))
        s.sendall(data.encode())
        s.close()
    if btn == "Mod":
        data = "MOD"
        car = app.getEntry("Enter Specific Message")
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip_address, 12345))
        s.sendall(data.encode())
        s.close()


app = gui()
ip1="192.168.0.71"
ip2="192.168.0.171"
ip3=""
ip4=""
n1="KGB"
n2=""
n3=""
n4=""

N="SERVER"
print(N)
app.startLabelFrame("PC Commands",1,1) 
app.addOptionBox("PCs",["-options-",f"{ip1}",f"{ip2}",f"{ip3}",f"{ip4}"],1,3)
app.addLabel("Name",f"{N}",1,2)
app.addLabel(f"IP{N}",f"{N}",2,2)
app.addIcon("Wi-Fi","Wi-Fi",1,1,0,2)
app.addIcon("Check","Check",3,1,0,2)
app.addButtons(["Update Drivers","Restart","Custom Shaders Patch"], execute, 3,2,2)
app.addButtons(["Open Sigma","Test","Shut Down","Mod"], execute , 4,2,2)
app.stopLabelFrame()

app.startLabelFrame("History",1,2)
app.addLabel("Status","-")
app.stopLabelFrame()

app.startLabelFrame("Other",2,1,2)
app.addLabel("sade","-")
app.stopLabelFrame()
app.go()