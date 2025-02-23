import telebot
import json
import payments
from config import TOKEN

bot = telebot.TeleBot(TOKEN)

# Загружаем товары
with open("products.json", "r", encoding="utf-8") as file:
    products = json.load(file)

# Команда /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, "Добро пожаловать! Выберите товар:")
    for product in products:
        bot.send_message(
            message.chat.id,
            f"{product['name']} - {product['price']} USDT\n"
            f"/buy_{product['id']}"
        )

# Обработка покупки
@bot.message_handler(commands=[f"buy_{p['id']}" for p in products])
def buy_product(message):
    product_id = message.text.split("_")[1]
    product = next((p for p in products if p["id"] == product_id), None)

    if product:
        payment_link = payments.create_payment(product["price"])
        bot.send_message(message.chat.id, f"Оплатите по ссылке: {payment_link}")
    else:
        bot.send_message(message.chat.id, "Товар не найден!")

bot.polling()