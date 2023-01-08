from appJar import gui
import socket


# Extract the IP addresses using regular expressions


def send_content(btn):
    # Get the selected options from the app
    content_type = app.getOptionBox("Content Type")
    ip_address = app.getOptionBox("IP Address")

    # Send the content based on the selected type
    if content_type == "Link":
        # Send a link
        link = app.getEntry("Link")
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip_address, 12345))
        s.sendall(link.encode())
        s.close()
    elif content_type == "Command":
        # Send a command
        command = app.getEntry("Command")
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip_address, 12345))
        s.sendall(command.encode())
        s.close()
    elif content_type == "File":
        # Send a file
        file_path = app.getEntry("File")
        with open(file_path, "rb") as f:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip_address, 12345))
            s.sendfile(f)
            s.close()
    elif content_type == "Message":
        # Send a message
        message = app.getEntry("Message")
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((ip_address, 12345))
        s.sendall(message.encode())


app = gui()
app.addLabelEntry("Message")
app.addLabelEntry("Link")
app.addFileEntry("File")
app.addButton("Send", send_content)
app.addOptionBox("Content Type",["Message","File","Command","Link"])
app.addOptionBox("IP Address",["192.168.1.56"])
app.go()