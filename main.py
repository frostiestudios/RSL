import socket
import os
from http.server import HTTPServer, SimpleHTTPRequestHandler
from appJar import gui
import webbrowser
import threading



def save(btn):
    link = app.getEntry("Add Link")
    with open("/htdocs/content.html", "a") as file:
        file.write(link)
    with open("/htdocs/info.html", "a") as file:
        file.write(link)


# Function to start the server
def server(btn):
    if btn == "Start":
        host_name = socket.gethostbyname(socket.gethostname())
        port_number = 5151
        # Create an HTTP server
        httpd = HTTPServer((host_name, port_number), SimpleHTTPRequestHandler)
        # Start the server in a separate thread
        server_thread = threading.Thread(target=httpd.serve_forever)
        server_thread.start()
        app.setLabel("SL", f"Server: http://{host_name}:{port_number}")
        app.setLabel("SS", "Online")
        print("Server started at http://{}:{}/htdocs".format(*httpd.socket.getsockname()))
    if btn == "Stop":
        host_name = socket.gethostbyname(socket.gethostname())
        port_number = 5151
        httpd = HTTPServer((host_name, port_number), SimpleHTTPRequestHandler)
        server_thread = threading.Thread(target=httpd.serve_forever)
        httpd.shutdown()
        httpd.server_close()
        server_thread.join()
        app.setLabel("SL", "Server: Offline")
        app.setLabel("SS", "Server: Offline")
        print("Server stopped.")
        app.infoBox("Server stopped", "Server has been stopped successfully")
    if btn == "Kill":
        print("BYE")
        app.stop()


def openbrowser(btn):
    print(f"Opening server in browser")
    host_name = socket.gethostbyname(socket.gethostname())
    port_number = 5151
    webbrowser.open(f"http://{host_name}:{port_number}/htdocs")


def move_file(btn):
    file_path = app.getEntry("File")
    file_name = app.getEntry("File Name")
    destination = 'htdocs/files'
    os.rename(file_path, f"{destination}/{os.path.basename(file_path)}")

    with open('htdocs/content.html', "a") as f:
        f.write(f"<div style='background-color: lightblue;'>")
        f.write(f"<b>{file_name}</b><br>\n")
        f.write(f"<form method='get' action='files/{os.path.basename(file_path)}'>")
        f.write(f"<label>{os.path.basename(file_path)}</label><br>\n")
        f.write(f"<button type='submit'>Download</button>\n")
        f.write(f"</div>\n")
        f.write(f"<br><br>\n")
    app.infoBox("Success", "File moved successfully.")

app = gui()

app.setToolbarPinned(pinned=True)
# Add a button to start the server

app.startTabbedFrame("Tabs")
app.startTab("Controls")
app.startLabelFrame("Server", 1, 1)
app.setLabelFont(20)
app.addButton("Start", server)
app.addButton("Stop", server)
app.addButton("Kill", server)
app.addButton("Open In Browser", openbrowser)
app.stopLabelFrame()

# AddFiles
app.startLabelFrame("File Controls", 2, 1)
app.addFileEntry("File")
app.addLabelEntry("File Name")
app.addButton("Move File", move_file)
app.stopLabelFrame()

# Set Store Location
app.startLabelFrame("Location", 2, 2)
app.stopLabelFrame()

app.startLabelFrame("Status", 1, 2)
app.addLabel("SL", "---.---.-.--")
app.setLabelFont(20)
app.addLabel("SS", "Offline")
app.stopLabelFrame()
app.stopTab()

app.startTab("Settings")
app.startLabelFrame("Customization")
app.addLabelEntry("Server Name")
app.stopLabelFrame()
app.stopTab()

app.go()
