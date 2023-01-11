import socket
import webbrowser
import pyautogui
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
    if data == "UPD":
        webbrowser.open_new_tab("https://us.download.nvidia.com/Windows/528.02/528.02-desktop-win10-win11-64bit-international-dch-whql.exe")
    if data == "CSP":
        pyautogui.hotkey('win')
        pyautogui.sleep(1)
        pyautogui.typewrite('content manager')
        pyautogui.press('enter')
    elif data == "RST":
        print("Ressetting PC")
        pyautogui.hotkey('win')
        pyautogui.sleep(4) 
        pyautogui.typewrite('restart pc')
        pyautogui.press('enter')
    if data == "SIG":
        pyautogui.hotkey('win')
        pyautogui.sleep(1)
        pyautogui.typewrite('sigma simulation')
        pyautogui.press('enter')
    if data == "TET":
        print("This is A System Test Please Do Not Worry")
        webbrowser.open("https://www.youtube.com/watch?v=0JcM8jLAfdo")
    if data == "SHT":
        pyautogui.hotkey('win')
        pyautogui.sleep(4) 
        pyautogui.typewrite('shutdown pc')
        pyautogui.press('enter')
    # Open a message window with the received message
    app=gui()
    app.setLabel("From",f"Server:{addr}")
    app.setLabel("Data",f"Sent:{data}")
    app.go()
    receive_message()

# Create a loop to continuously listen for incoming connections
while True:
    receive_message()
