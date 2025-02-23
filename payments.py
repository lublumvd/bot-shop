import requests
from config import CRYPTOBOT_API_KEY

def create_payment(amount):
    url = "https://pay.crypt.bot/api/createInvoice"
    data = {
        "asset": "USDT",
        "amount": amount,
        "description": "Покупка в магазине",
        "hidden_message": "Спасибо за покупку!",
        "paid_btn_name": "openBot",
        "paid_btn_url": "https://t.me/ТВОЙ_БОТ",
        "allow_comments": False,
        "allow_anonymous": False
    }
    headers = {"Authorization": f"Bearer {CRYPTOBOT_API_KEY}"}
    response = requests.post(url, json=data, headers=headers)
    return response.json()["result"]["pay_url"]