import os
import requests
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

TELEGRAM_TOKEN = '7517291871:AAGnspgcSDIvJE5LdlV-58UDjghnk5Ec3ZI'
WEATHER_API_KEY = ''


def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text(
        'Привіт! Я чат-бот для прогнозу погоди. Використовуйте команду /weather <місто> для отримання прогнозу.')


def weather(update: Update, context: CallbackContext) -> None:
    if not context.args:
        update.message.reply_text('Будь ласка, вкажіть місто. Використовуйте команду /weather <місто>.')
        return

    city = ' '.join(context.args)
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={WEATHER_API_KEY}&units=metric'

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        temperature = data['main']['temp']
        weather_description = data['weather'][0]['description']
        update.message.reply_text(f'Погода в {city}: {temperature}°C, {weather_description}.')
    else:
        update.message.reply_text('Місто не знайдено. Будь ласка, спробуйте ще раз.')


def main():
    updater = Updater('7517291871:AAGnspgcSDIvJE5LdlV-58UDjghnk5Ec3ZI')
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CommandHandler('weather', weather))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
