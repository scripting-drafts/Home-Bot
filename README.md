# Home-Bot
Remote Appliances Control with pyTelegramBotAPI

Get a Token from Bot_Father and paste it 'TELEGRAM_TOKEN = here'.

This bot uses urllib2 to flick web controlled switches within your local network. Therefore the URLs you need are probably raw IP's with subdomains like /number_of_gpio/on_or_off.

In order to check wether your appliances are on or off, the script fetches the text of the switch URL and looks for text referencing the name of the appliance and its state. I.e. to tell the script those keywords you will have to write them at lines 23 and 25.

To make sure you're the only one talking to your home bot you can write your user chat_id at line 48. Or else comment lines 48, 50, 51 and unindent line 49.
