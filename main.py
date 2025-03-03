import telebot
import os
from dotenv import load_dotenv
import requests

load_dotenv("D:\Weather bot tg\.venv\BOT_TOKEN.env")
TOKEN = os.getenv("BOT_TOKEN")
bot = telebot.TeleBot(TOKEN)
API = 'b64ca373efc8ab8ff37161bcca0a3fc5'



@bot.message_handler(commands=['start'])
def start_command(message):
    bot.send_message(message.chat.id, "Hello, send city name...")
    bot.register_next_step_handler(message, get_weather)

@bot.message_handler(content_types = ['text'])
def get_weather(messege):
    city = messege.text.strip().lower()
    weather = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric")
    data = weather.json()

    if data["cod"] == 200:
        weather_main = data["weather"][0]["main"]
        temperature_main = data["main"]["temp"]
        feels_like = data["main"]["feels_like"]
        temperature_minimal = data["main"]["temp_min"]
        temperature_max = data["main"]["temp_max"]
        wind_speed = data["wind"]["speed"]
        bot.send_message(messege.chat.id, f"City: {city}\nWeather: {weather_main}\nTemperature: {temperature_main}\nFeels like: {feels_like}\n"
                                            f"Temperature minimum: {temperature_minimal}\nTemperature max: {temperature_max}\nWind speed: {wind_speed}")
    else:
        bot.send_message(messege.chat.id, "City not found")
bot.polling(none_stop = True)