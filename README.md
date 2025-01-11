# A simple truly anonymous confessions bot for Discord

This bot is just a fun little project to get more familiar with using webhooks, it probably won't be maintained very actively but it is very lightweight and easy to set up, so if you still want to use it feel free to do so!
The profile picture the Webhook uses is from under the Public Domain sourced from [Wikimedia Commons](https://commons.wikimedia.org/wiki/Category:Anonymous_(group)#/media/File:Anonymous_emblem.svg)

## Setup Instructions

To get started with the bot, you just need to follow a couple easy steps:

1. **Clone the repository**:

   ```bash
   git clone https://github.com/itzminey/dcAnonBot.git
   
   cd cdAnonBot
   ```

2. **Create a virtual environment**

   - On Windows:
     ```bash
     python -m venv venv
     ```
   - On macOS/Linux:
     ```bash
     python3 -m venv venv
     ```


3. **Activate the vitual environment:**
   - On Windows:
     ```bash
     .\venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```bash
     source venv/bin/activate
     ```

4. **Get your Bot Token**:
   
   Visit the [Discord Developer Portal](https://discord.com/developers/applications) to make an Application, then go to the **Bot** tab of your application and click on "Reset Token" to generate your Bot Token.


5. **Make a Webhook for your Confession Channel**
   
   The bot works very simple by just utilizing a webhook and posting to it, for this to work you need to make a channel for your confessions and go to it's settings, where you can add a new Webhook to it.

6. **Set up the .env**
 
   First, copy the example .env file:
   - On Windows:
     ```bash
     copy example.env .env
     ```
   - On macOS/Linux:
     ```bash
     cp example.env .env
     ```

   After that, simply open the .env file with a text editor and replace the example values with your Bot Token and Webhook URL that you created earlier.
   And that easily, the setup is done!

## Start the bot

   Before you can start using the bot, you'll need to invite it to your server.
   
1. Invite the bot to your server:
   Go to the [Discord Developer Portal](https://discord.com/developers/applications) again.
        In your application, open the **Installation** tab.
        Search for a box labeled "Install Link" and copy the generated link
        Then open the copied link in your browser to invite the bot to your server.

2. Run the bot:
   
   Open a terminal window in the bot's folder and run the following command to start the bot:

   - On Windows:
     ```bash
     python main.py
     ```

   - On Linux/macOS:
     ```bash
     python3 main.py
     ```

  Your bot should now be ready and working! It should work just fine without needing any Permission Grants or Gateway Intents at all, since it simply posts what you put in the slash command to a Webhook URL, but if it for some reason doesn't work, you can first try enabling all intents in the Bot tab on the Discord Developer Portal.
