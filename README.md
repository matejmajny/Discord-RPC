# Discord RPC
This project is using `discord-rpc` (NPM library) and powered by JavaScript (Node.js), it should  run on every common OS (Linux, MacOS, Windows)

#### Make sure you have installed:
- [NodeJS](https://nodejs.org)
- [Discord](https://discord.com)
- [PM2](https://pm2.keymetrics.io/) (Optional - for app background use)
- [Notepad++](https://notepad-plus-plus.org/downloads/) (Optional - you can choose different program and is not required for GUI)


## How to set it up?
 - Go to https://discord.com/developers/applications
 - Click on `New Application` and name your app by that what you want **title of your RPC to be!**
 - Click on `OAuth2 --> General` and copy your Client ID and store it somewhere for later
 - Click on `Rich Presence --> Art Assets` and upload some images (2) what you want to use later
 - Download version of your choice from release
 - Edit [config.js](https://github.com/matejmajny/Discord-RPC/edit/main/README.md#configjs-configuration) or use built-in editor in GUI editions.
 - [Run IT!](https://github.com/matejmajny/Discord-RPC/edit/main/README.md#run-it)
 
## config.js configuration
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

## Run IT!

### Run with GUI
- Download GUI version for your OS based on your system.
- App is pretty simple so this doesnt need further information ig
- Note: This does not support background running

### Background mode:
- Install PM2 if you havent already `npm install pm2 -g`
- Run `pm2 start index.js` in Command Line/Terminal
- Run `pm2 list` and check if app is running!
- Note: This makes app run fully on background, kill it with `pm2 stop <name>`

### Command line mode (foreground):

- Run `node index.js` in command line/terminal
- Note: I guess this requires more of tech skill?
