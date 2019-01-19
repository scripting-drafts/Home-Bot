import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import os
import urllib2
import subprocess

TELEGRAM_TOKEN = ''

bot = telebot.TeleBot(TELEGRAM_TOKEN)

def gen_markup():
	markup = InlineKeyboardMarkup()
	markup.row_width = 2
	markup.add(InlineKeyboardButton("Heater", callback_data="cb_heater"),
   	                       InlineKeyboardButton("Air Conditioning", callback_data="cb_air"))
	markup.add(InlineKeyboardButton("Instant Noodles", callback_data="cb_noodles"))
	return markup

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
	if call.data == "cb_heater":
		heaterState = urllib2.urlopen("YOUR SWITCH URL HERE").read()
		if "TEXT IN PAGE WHEN ON" in heaterState:
			heaterState = "off"
		elif "TEXT IN PAGE WHEN OFF" in heaterState:
			heaterState = "on"
		urllib2.urlopen("YOUR SWITCH URL HERE" + heaterState).read()
		bot.answer_callback_query(call.id, "Heater is " + heaterState)
	elif call.data == "cb_air":
		airState = urllib2.urlopen("YOUR SWITCH URL HERE").read()
                if "TEXT IN PAGE WHEN ON" in airState:
                        airState = "off"
                elif "TEXT IN PAGE WHEN OFF" in airState:
                        airState = "on"
                urllib2.urlopen("YOUR SWITCH URL HERE" + airState).read()
                bot.answer_callback_query(call.id, "Air Conditioner is " + airState)
	elif call.data == "cb_noodles":
		noodles = urllib2.urlopen("http://192.168.1.144").read()
		if "instant noodles - It's on." in noodles:
			noodles = "off"
		elif "instant noodles - It's off." in noodles:
			noodles = "on"
		urllib2.urlopen("http://192.168.1.144/27/" + noodles).read()
		bot.answer_callback_query(call.id, "Instant Noodles are " + noodles)

@bot.message_handler (commands=["home"])                                                     #(func=lambda message: True)
def home_handler(message):
	if message.chat.id == UNQUOTED_MESSENGER_ID:
		bot.send_message(message.chat.id, "get by", reply_markup=gen_markup())
	else:
                bot.send_message(message.chat.id, "forbidden", reply_markup="")
