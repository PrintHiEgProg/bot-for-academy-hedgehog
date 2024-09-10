import yookassa
from yookassa import Payment
import uuid

def create(amount, chat_id):
    id_key = str(uuid.uuid4())
    payment = Payment.create({
        "amount": {
            "value": amount,
            "currency": "RUB"
        },
        "paymnet_method_data":{
            "type" : "bank_card"
        },
        "confirmation": {
            "type": "redirect",
            "return_url": "https://t.me/hedgehog_academy_bot"
        },
        "capture": True,
        "metadata": {
          "chat_id": chat_id
        },
        "description": 'Покупка курса'
    }, id_key)

    return payment.confirmation.confirmation_url, payment.id