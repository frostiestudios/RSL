from appJar import gui
import socket


# Extract the IP addresses using regular expressions


def send_content(btn):
    # Get the selected options from the app
    content_type = app.getOptionBox("Content Type")
    ip_address = app.getOptionBox("IP Address")

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
   


app = gui()
app.startLabelFrame("PreGeneratedCommands",1,1)
app.addButton("Update Drivers", send_content)
app.addButton("Restart", send_content)
app.addButton("Shut Down", send_content)
app.addButton("Run Sigma", send_content)
app.addOptionBox("IP Address",["192.168.1.56"])
app.go()