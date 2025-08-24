# Description
A simple personal AI assistant project made just for fun.

# Voice Commands
Say "Hello Lathra", and Lathra will run the available commands you say.
Available:
"Say hi"        -> Lathra will introduce herself
"Open browser"  -> Opens a browser
"Play music"    -> Opens YouTube music (You can modify it yourself)
"Ping YouTube"  -> Pinging YouTube (Self Explanatory)
"You may sleep" -> Turn off Lathra

You can modify or create your custom voice commands by configuring the *main.py*, *permissions.json*, and *modules*.
Folder Structure:
Project-Lathra/
├── main.py
├── config/
│   └── permissions.json
├── modules/
│   ├── browser.py
│   ├── media.py
│   └── system.py