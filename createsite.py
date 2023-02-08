import subprocess
import webbrowser
import json
from appJar import gui
import os

settings_file = 'settings.json'
folder_path = None
project_name = None

def server(button):
    if button == "Start":
        print("Starting Server")
        with open(settings_file, 'r') as file:
                data = json.load(file)
                folder_path = data['folder_path']
                project_name = data['project_name']
        os.chdir(os.path.join(folder_path, project_name))
        subprocess.run(['mkdocs', 'serve'])
    if button == "Open":
        webbrowser.open("http://127.0.0.1:8000/")
        
def create(button):
    global folder_path, project_name
    if button == "Cancel":
        app.stop()
    elif button == "Submit":
        folder_path = app.directoryBox("Select Folder")
        project_name = app.getEntry("Project Name")
        if folder_path and project_name:
            os.chdir(folder_path)
            subprocess.run(['mkdocs', 'new', project_name])
            os.chdir(os.path.join(folder_path, project_name))
            with open(os.path.join('docs', 'index.md'), 'w') as file:
                file.write('')
            with open(os.path.join('info.yml'), 'w') as file:
                file.write('')
            with open(settings_file, 'w') as file:
                data = {
                    'folder_path': folder_path,
                    'project_name': project_name
                }
                json.dump(data, file)
            app.infoBox("Success", "Folder and files created successfully")
        else:
            app.errorBox("Error", "Both Folder Path and Project Name are required")
    elif button == "Start":
        if folder_path and project_name:
            os.chdir(os.path.join(folder_path, project_name))
            subprocess.run(['mkdocs', 'serve'])
        else:
            app.errorBox("Error", "Both Folder Path and Project Name are required")
        if os.path.exists(settings_file):
            with open(settings_file, 'r') as file:
                data = json.load(file)
                folder_path = data['folder_path']
                project_name = data['project_name']

app = gui("Create Project Folder", useTtk=True)
app.startTabbedFrame("Tabs")
app.startTab("Dash")
app.setTtkTheme("alt")
app.addLabel("title", "Create Project Folder")
app.addLabelEntry("Project Name")
app.addOptionBox("Select Server",[f"{folder_path}"])
app.addButtons(["Submit", "Cancel"], create)
app.addButtons(["Start","Open"], server)
app.stopTab()

app.startTab("Settings")
app.stopTab()
app.go()
