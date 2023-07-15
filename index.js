const RPC = require("discord-rpc");
const config = require('./config.json');

// creating buttons based on config.json
buttonsArray = []
if (typeof config.button1 != "undefined" && typeof config.buttonURL1 != "undefined") { 
    buttonsArray.push({label: config.button1, url: config.buttonURL1});
}

if (typeof config.button2 != "undefined" && typeof config.buttonURL2 != "undefined") { 
    buttonsArray.push({label: config.button2, url: config.buttonURL2});
}


// rpc 
const rpc = new RPC.Client({ transport: 'ipc' });
rpc.on("ready", () => {
    console.log("Rich Presence set!")
    rpc.setActivity({
        largeImageKey: config.largeImage,
        largeImageText: config.largeImageText,
        smallImageKey: config.smallImage,
        smallImageText: config.smallImage,
        state: config.state,
        details: config.details,
        startTimestamp: new Date(),

        buttons: buttonsArray
    })
})

rpc.login({ clientId: config.clientID })
