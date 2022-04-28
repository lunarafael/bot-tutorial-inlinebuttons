import telebot
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

chave_api = "sua chave"
bot = telebot.TeleBot(chave_api)

def botoes_menu():
    markup = InlineKeyboardMarkup()
    markup.row_width = 3
    markup.add(
        InlineKeyboardButton("1", callback_data="botao_1"),
        InlineKeyboardButton("2", callback_data="botao_2"),
        InlineKeyboardButton("3", callback_data="botao_3")
    )
    return markup

@bot.callback_query_handler(func = lambda call:True)
def query(call):
    if call.data == "botao_1":
        botao_1(call.message)
    elif call.data == "botao_2":
        botao_2(call.message)

@bot.message_handler(commands=["botao_1"])
def botao_1(mensagem):
    texto = "Você pressionou o botão 1"

    bot.send_message(mensagem.chat.id, texto)

@bot.message_handler(commands=["botao_2"])
def botao_2(mensagem):
    texto = "Você pressionou o botão 2"

    bot.send_message(mensagem.chat.id, texto)

@bot.message_handler(commands=["menu"])
def menu(mensagem):
    texto = "Este é o menu do bot de botões inline"

    bot.send_message(mensagem.chat.id, texto, reply_markup=botoes_menu())

bot.polling()