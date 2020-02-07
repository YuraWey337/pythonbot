import pyowm
import telebot

owm = pyowm.OWM('dc63a5f9017da1ef8335f79ffb2c62b7', language = "ua")
bot = telebot.TeleBot("958511697:AAH73VZ6_gmlAGm75JylK0zSbuim3Ed3CG4")

@bot.message_handler(content_types=['text'])
def send_echo(message):
	observation = owm.weather_at_place( message.text )
	w = observation.get_weather()
	temp = w.get_temperature('celsius')["temp"]

	answer = "В місті " + message.text + " зараз " + w.get_detailed_status() + "\n"
	answer += "Температура зараз близько " + str(temp) + " Градусів" "\n\n"
	
	if temp < 5:
		answer += "Зараз ппц як холодно, одягайся як танк!" 
	elif temp < 10:
		answer += "Зараз не дуже холодно, але одягайся тепліше!" 
	else:
		answer += "Температура норм, одягай, що захочеш!"

	bot.send_message(message.chat.id, answer)

bot.polling( none_stop = True )
