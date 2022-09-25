# Discord RPC
This project is using `discord-rpc` (NPM library) and powered by JavaScript (Node.js), it should  run on every common OS (Linux, MacOS, Windows)

#### Make sure you have installed:
- [NodeJS](https://nodejs.org)
- [Discord](https://discord.com)
- [PM2](https://pm2.keymetrics.io/) (Optional - for app background use)
- [Git](https://git-scm.com/) (Optional - you can just use download zip on GitHub
- [Notepad++](https://notepad-plus-plus.org/downloads/) (or some different program what can edit .json files)


## How to set it up?
 - Go to https://discord.com/developers/applications
 - Click on `New Application` and name your app by that what you want **title of your RPC to be!**
 - Click on `OAuth2 --> General` and copy your Client ID and store it somewhere for later
 - Click on `Rich Presence --> Art Assets` and upload some images (2) what you want to use later
 - Run `git clone https://github.com/matejmajny/Discord-RPC` or download [zip file](https://github.com/matejmajny/Discord-RPC/archive/refs/heads/main.zip)
 - Open downloaded folder and execute `run.sh(Linux) or run.bat(Windows)` and **select Install option** or just run `npm i` (recommended)
 - Open config.js with Notepad++ and [configure it](https://github.com/matejmajny/Discord-RPC/edit/main/README.md#configjs-configuration)
 - [Run IT!](https://github.com/matejmajny/Discord-RPC/edit/main/README.md#run-it)
 
## config.js configuration
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

### Run on background:
- Install PM2 if you havent already `npm install pm2 -g`
- Run `pm2 start index.js` in Command Line/Terminal
- Run pm2 list and check if app is running!

### Run on foreground:
#### Option 1:
- Run `run.sh or run.bat` and select Run [R] option.
- P.S: Untested, but should work

#### Option 2: 
- Run `node index.js` in command line/terminal 
- I personally recommend this option
