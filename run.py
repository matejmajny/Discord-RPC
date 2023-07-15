from nicegui import ui, app
import json, os, subprocess, atexit, sys

sys.stdout = open('logs.txt', 'w')

def loadSettings():
    jsonCfgRead = open("config.json").read()
    cfgRead = json.loads(jsonCfgRead)

    ui.notify("Loading from config.json")
    ClientID.set_value(cfgRead.get("clientID"))
    lrgImgName.set_value(cfgRead.get("largeImage"))
    lrgImgText.set_value(cfgRead.get("largeImageText"))
    smlImgName.set_value(cfgRead.get("smallImage"))
    smlImgText.set_value(cfgRead.get("smallImageText"))
    details.set_value(cfgRead.get("details"))
    state.set_value(cfgRead.get("state"))
    btnLbl1.set_value(cfgRead.get("button1"))
    btnUrl1.set_value(cfgRead.get("buttonURL1"))
    btnLbl2.set_value(cfgRead.get("button2"))
    btnUrl2.set_value(cfgRead.get("buttonURL2"))

def saveSettings():
    ui.notify("Saved to config.json")
    cfgWrite = {}
    cfgWrite.update({"clientID": ClientID.value})
    cfgWrite.update({"largeImage": lrgImgName.value})
    cfgWrite.update({"largeImageText": lrgImgText.value})
    cfgWrite.update({"smallImage": smlImgName.value})
    cfgWrite.update({"smallImageText": smlImgText.value})
    cfgWrite.update({"details": details.value})
    cfgWrite.update({"state": state.value})
    cfgWrite.update({"button1": btnLbl1.value})
    cfgWrite.update({"buttonURL1": btnUrl1.value})
    cfgWrite.update({"button2": btnLbl2.value})
    cfgWrite.update({"buttonURL2": btnUrl2.value})

    with open("config.json", "w") as f:
        f.write(json.dumps(cfgWrite, indent=4))


def run():
    statusLabel.set_content("**Status:** Running")
    statusLabel.update()
    global p
    try:
        poll = p.poll()
        if poll is None:
            ui.notify("RPC is running, cant be started.")
        else:
            if os.path.isdir("node_modules"):
                p = subprocess.Popen("node index.js")
            else:
                os.system("npm install")
                p = subprocess.Popen("node index.js")
            atexit.register(lambda: p.terminate())
    except:
        if os.path.isdir("node_modules"):
            p = subprocess.Popen("node index.js")
        else:
            os.system("npm install")
            p = subprocess.Popen("node index.js")
        atexit.register(lambda: p.terminate())

def stop():
    statusLabel.set_content("**Status:** Not Running")
    statusLabel.update()

    try:
        poll = p.poll()
        if poll is None:
            p.terminate()
        else:
            ui.notify("RPC is not running, cant be stopped.")
    except:
        ui.notify("RPC is not running, cant be stopped.")

def close():
    try:
        poll = p.poll()
        if poll is None:
            ui.notify("To return back to editor, stop the RPC.")
        else:
            dialog3.close()
    except:
        dialog3.close()

# dialogs
with ui.dialog() as dialog1, ui.card():
        ui.markdown("**1.** Go to the [Discord Developer Portal](https://discord.com/developers/applications).")
        ui.markdown("**2.** Create new application.")
        ui.markdown("**3.** After you have created your application, copy *Client ID* from OAuth2 tab.")
        ui.button('Close', on_click=dialog1.close)

with ui.dialog() as dialog2, ui.card():
        ui.markdown("**1.** Go to the [Discord Developer Portal](https://discord.com/developers/applications).")
        ui.markdown("**2.** Open your application.")
        ui.markdown("**3.** Upload your images (max. 2) in the Rich Presence Assets Tab.")
        ui.markdown("**4.** Then use the filenames as *Image Names*")
        ui.markdown("**P.S.** Image Text is text which displays when somebody hovers over the image with their mouse.")
        ui.button('Close', on_click=dialog2.close)

with ui.dialog().props("persistent") as dialog3, ui.card():
        ui.label("RPC menu").style("font-size: 180%; font-weight: 500; font-family: 'Segoe UI Black';")

        ui.markdown("**Note:** Running application for first time can take a bit longer because it needs to install dependencies.")
        statusLabel = ui.markdown("**Status:** Not Running")

        with ui.row():
            ui.button("Start", on_click=lambda: run())
            ui.button("Stop", on_click=lambda: stop())
            ui.button("Close", on_click=lambda: close())


ui.label('Discord-RPC GUI').style('color: #6E93D6; font-size: 230%; font-weight: 900')
ui.label("This program will help set up and run your custom Discord-RPC.").style("font-size: 115%")

with ui.row():
    ui.button("Save your settings.", on_click=lambda: saveSettings())
    ui.button("Load previous settings.", on_click=lambda: loadSettings())
    ui.button("Run.", on_click=dialog3.open)
ui.label("\n \n \n ")

# client ID
with ui.row():
    ui.label("ClientID").style("font-size: 180%; font-weight: 500; font-family: 'Segoe UI Black';")
    with ui.button(on_click=dialog1.open).style(f'background-color:#0a0909!important'):
        ui.icon("help")
        
ClientID = ui.input("ClientID")
    

# images
with ui.row():
    ui.label("Images").style("font-size: 180%; font-weight: 500; font-family: 'Segoe UI Black';")
    with ui.button(on_click=dialog2.open).style(f'background-color:#0a0909!important'):
        ui.icon("help")

with ui.row():
    lrgImgName = ui.input("Large Image Name")
    lrgImgText = ui.input("Large Image Text")

with ui.row():
    smlImgName = ui.input("Small Image")
    smlImgText = ui.input("Small Image Text")


# labels
ui.label("Labels").style("font-size: 180%; font-weight: 500; font-family: 'Segoe UI Black';")
details = ui.input("Details")
state = ui.input("State")


# buttons
ui.label("Buttons").style("font-size: 180%; font-weight: 500; font-family: 'Segoe UI Black';")
with ui.row():
    btnLbl1 = ui.input("Button Label 1")
    btnUrl1 = ui.input("Button URL 1")

with ui.row():
    btnLbl2 = ui.input("Button Label 2")
    btnUrl2 =  ui.input("Button URL 2")

ui.run(native=True, window_size=(720,720), reload=False, title="Discord-RPC GUI")