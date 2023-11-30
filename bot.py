import os
from os.path import join, dirname
from dotenv import load_dotenv
import telebot
import web3

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

BOT_TOKEN = os.environ.get("BOT_TOKEN")

bot = telebot.TeleBot(BOT_TOKEN)

pk = os.environ.get("SECRET_KEY")

w3 = web3.Web3(web3.Web3.HTTPProvider("https://sepolia-rpc.scroll.io/"))

from web3.middleware import geth_poa_middleware
w3.middleware_onion.inject(geth_poa_middleware, layer=0)

account = w3.eth.account.from_key(pk)

@bot.message_handler(commands=['hello'])
def send_welcome(message):
    bot.reply_to(message, "Hi!")

@bot.message_handler(commands=['transact'])
def initial_message_handler(message):
    text = "Enter an address to transact with"
    sent_msg = bot.send_message(message.chat.id, text, parse_mode="Markdown")
    bot.register_next_step_handler(sent_msg, amount_handler)

def amount_handler(message):
    address = message.text
    text = "What amount to you want to send?"
    sent_msg = bot.send_message(
        message.chat.id, text, parse_mode="Markdown")
    bot.register_next_step_handler(
        sent_msg, complete_transaction, address)
    
def complete_transaction(message, address):
    amount = message.text
    
    tx_hash = w3.eth.send_transaction({
        "from": account.address,
        "value": amount,
        "to": address
    })

    bot.send_message(message.chat.id, "Here's transaction hash!")
    bot.send_message(message.chat.id, tx_hash, parse_mode="Markdown")

@bot.message_handler(func=lambda msg: True)
def echo_all(message):
    bot.reply_to(message, message.text)

bot.infinity_polling()