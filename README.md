# Home-Bot
Remote Appliances Control with pyTelegramBotAPI

Get a Token from @Bot_Father and paste it 'TELEGRAM_TOKEN = here'.

This bot uses urllib2 to flick web controlled switches within your local network. Therefore the URLs you need are probably raw IP's (lines 22, 30 and 38) with subdomains like /number_of_gpio (lines 27, 35 and 43) and /on_or_off. The later is given automatically when the following part is properly configured.

In order to check wether your appliances are on or off, the script fetches text from the switches URLs and looks for references to the name of the appliance and its state. Tell the script those keywords writing them at lines 23 and 25. E.g. "Instant Noodles are ON" and "Instant Noodles are OFF".

Then the bot stores the current state of the appliance, sends an on/off command accordingly and prints a message for the user to notice the change of state.

To make sure you're the only one talking to your home bot you can write your user chat_id at line 48. Or else comment lines 48, 50, 51 and unindent line 49.

This works terribly well with web servers hosted on GPIO capable microprocessors. I.e. Arduino/ESP8266/ESP32...
