const RPC = require("discord-rpc");
const rpc = new RPC.Client({ transport: 'ipc' });
const config = require('./config.json');

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

        buttons: [{
            label: config.button1,
            url: config.buttonURL1
        }, {
            label: config.button2,
            url: config.buttonURL2
        }]
    })
})

rpc.login({ clientId: config.clientID })
