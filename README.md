# Discord RPC
This project is using `discord-rpc` (NPM library) and powered by JavaScript (Node.js), it should  run on every common OS (Linux, MacOS, Windows)

## ❗ Register your RPC on Discord website (mandatory for all) ❗
 - Go to https://discord.com/developers/applications
 - Click on `New Application` and name your app by that what you want **title of your RPC to be!**
 - Click on `OAuth2 --> General` and copy your Client ID and store it somewhere for later
 - Click on `Rich Presence --> Art Assets` and upload some images (2) what you want to use later (optional)

## Run the app 🟢

### 1. Install app with installer and use GUI (Windows) 

#### Make sure you have installed:
- [Discord](https://discord.com)

#### How to set it up?
 - Make sure that you have [registered your RPC](https://github.com/matejmajny/Discord-RPC/edit/main/README.md#register-your-rpc-on-discord-website-mandatory-for-all)
 - Download [WindowsInstaller_GUI.exe](https://github.com/matejmajny/Discord-RPC/releases/latest), it may get flagged as virus but it isn't.
 - Process is pretty straightforward from there so it doesn't need further explanation I think.


### 2. Running raw code files (Linux, MacOS, Windows)

#### Make sure you have installed:
- [Python](https.//python.org) - only if you want to use GUI
- [NodeJS](https://nodejs.org)
- [Discord](https://discord.com)
- [Notepad++](https://notepad-plus-plus.org/downloads/) (Optional - you can choose different program and is not required for GUI)

#### How to set it up?
 - Download [Universal_CLI.zip](https://github.com/matejmajny/Discord-RPC/releases/latest) or `git clone` this repository.
 - Make sure that you have [registered your RPC](https://github.com/matejmajny/Discord-RPC/edit/main/README.md#register-your-rpc-on-discord-website-mandatory-for-all)
 - Edit [config.js](https://github.com/matejmajny/Discord-RPC/edit/main/README.md#configjs-configuration)
 - **CLI:** Run `npm install` and `node index.js` in command line/terminal
 - **GUI:** Run `pip3 install nicegui` and `python3 gui.py` in command line/terminal
 

### 3. Run on background

#### Make sure you have installed:
- [NodeJS](https://nodejs.org)
- [Discord](https://discord.com)
- [PM2](https://pm2.keymetrics.io/) (Optional - for app background use)
- [Notepad++](https://notepad-plus-plus.org/downloads/) (Optional - you can choose different program)

#### How to set it up?:
- Install PM2 if you havent already `npm install pm2 -g`
- Run `pm2 start index.js` in Command Line/Terminal
- Run `pm2 list` and check if app is running!
- Note: This makes app run fully on background, kill it with `pm2 stop <name>`


### config.js configuration (CLI) 🔧
- ***This doesnt need to be done when using GUI.***
- put everything what should be in mentioned line to "putItHere"
```
{
    "clientID": "", // client ID from discord.dev portal
    "largeImage": "", // name of image (big) uploaded on discord.dev
    "largeImageText": "", // comment to display after hovering mouse on large image
    "smallImage": "", // name of image (small) uploaded on discord.dev
    "smallImageText": "", // comment to display after hovering mouse on smal image
    "state": "", // state what you want to display
    "details": "", // details what you want to display
    "button1": "", // button 1 text
    "buttonURL1": "", // button 1 URL
    "button2": "", // button 2 text
    "buttonURL2": "" //button 2 URL
}
```
