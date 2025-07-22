import asyncio
from telebot.async_telebot import AsyncTeleBot
from config import TELEGRAM_TOKEN
from ai.openrouter import sendAi
from ai.neuroimg import free_generate

bot = AsyncTeleBot(TELEGRAM_TOKEN)

print("Приложение запущено!")

@bot.message_handler(commands=['start', 'help'])
async def start(message):
    await bot.reply_to(message, 'Привет! Ты попал в самый креативный чат бот телеграма!\n/start - помощь\n/help - помощь\n/draw [промпт] - сгенерировать изображение')

@bot.message_handler(commands=['draw'])
async def generate(message):
    str = message.text.split(' ')
    str.remove(str[0])
    await bot.send_message(message.chat.id, " ".join(str))

    await bot.send_message(message.chat.id, 'Генерирую изображение')
    await bot.send_chat_action(message.chat.id, 'upload_photo')
    image_url = await free_generate(message.text)
    await bot.send_photo(message.chat.id, image_url)

async def subscribe(message):
    print("Вызов функции subscribe()")
    await bot.send_message(message.chat.id, "Подписка оформлена!")

@bot.message_handler(content_types=['text'])
async def echo(message):
    await bot.send_chat_action(message.chat.id, 'typing')
    response = await sendAi(f"{message.text}")
    responseAi = response['choices'][0]['message']['content']

    print(responseAi) # проверяем работу параметров

    if responseAi.lower() == "подписка" and responseAi.lower() == "подписка.":
        print("Условие с подпиской сработало")
        await subscribe(message)
    else:
        await bot.send_message(message.chat.id, response['choices'][0]['message']['content'])


asyncio.run(bot.polling())
