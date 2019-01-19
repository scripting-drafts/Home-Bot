# Home-Bot
Remote Appliances Control with pyTelegramBotAPI

Get a Token from Bot_Father and paste it 'TELEGRAM_TOKEN = here'.

This bot uses urllib2 to call web controlled appliances within your local network, 
so write your appliances URL's accordingly.

In order to check wether your appliances are on or off, this script fetches the text in the URL and looks for words/sentences contaning ON/OFF and other text referencing the name of the switch and its state. To make the script do that you will have to write that string in the switch URL.
