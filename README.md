#Suggestion

If you don't want to install CB yourself, you can ask the existing one to join your server. This way you get automatic updates and instant access to it's creator and what have you. Just join here: https://discord.gg/0iLJFytdVRBR1vgh

**[Please read the terms of service before adding CacoBot to your server.](https://github.com/Orangestar12/cacobot/blob/master/tos.md)**

#Prerequisites

[Install Python 3.](https://www.python.org)

[Install the Async branch of Discord.py.](https://github.com/Rapptz/discord.py/tree/async)

[For YouTube functionality, install the YouTube API Python Library.](https://developers.google.com/api-client-library/python/apis/youtube/v3?hl=en)

#Download

[Download the latest version of CacoBot and place it in a folder by itself.](https://github.com/Orangestar12/cacobot/archive/master.zip)

#Configuration

Create a folder called `configs` with these two files, filling in any necessary information:

`configs/config.json`
```
{
    "token" : "Place your application token here.",
    "client_id" : "Place your application client ID here.",
    "owner_id" : "Place your Discord ID here. Use .myid to get it with the bot.",
    "invoker" : "Place the character or line you want to invoke CB commands. Base CacoBot's is '.'",
    "log_request_limit" : 50,
    "games" : [
        "The Ultimate DOOM",
        "DOOM II: Hell On Earth"
    ],
    "error_messages": [
        "Oh no!",
        "How'd you do that?",
        "Oops..."
    ],
    "youtube" : {
        "DEVELOPER_KEY" : "Put your YouTube developer key here. Change the request limits if you feel like it. ['youtube']['request_limit'] is the max amount of videos that can be recieved. ['log_request_limit'] is the max amount of messages .log can retrieve.",
        "API_SERVICE_NAME" : "youtube",
        "API_VERSION" : "v3",
        "request_limit" : 5
    },
    "pastebin_key" : "Get a Pastebin key from http://pastebin.com/api and put it here. We use it to post the tag list to Pastebin.",
    "git": {
        "repo_author" : "Orangestar12",
        "repo_name" : "cacobot",
        "comment" : "Replace these with your GitHub username and forked CacoBot repo name, or leave them to pull latest changes and source from the default."
    }
}
```

`configs/tags.json`
```
{
  "orangestars-tag": {
      "tag": "This tag belongs to Orangestar in the CacoServer server!",
      "server": "128043020418285568",
      "owner": "88401933936640000"
  },
  "nobodys-tag": {
      "tag": "This is an orphaned tag, and anyone can claim it!",
      "server": "None",
      "owner": "None"
  }
}
```

#Activation

Run `main.py` in Python 3.

Congratulations, you have a CacoBot.
