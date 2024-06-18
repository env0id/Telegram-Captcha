import telebot
import time

 
token =  "YOUR_BOT_TOKEN"
button_text = "I'm not a robot"
verification_time = 30

#HTML parse mode
text =  '''Welcome, {}! '''


bot = telebot.TeleBot(token)
verification_status = {}

@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    bot.answer_callback_query(call.id, "Verification successful!")
    verification_status[(call.message.chat.id, call.from_user.id)] = True
    bot.restrict_chat_member(call.message.chat.id, call.from_user.id, can_send_messages=True)
    bot.delete_message(call.message.chat.id, call.message.id)


@bot.message_handler(content_types=['new_chat_members'])
def handle_new_member(message):
    for new_member in message.new_chat_members:
        user_id = new_member.id
        bot.restrict_chat_member(message.chat.id, user_id, can_send_messages=False)
        msg = bot.send_message(message.chat.id,
                            text.format(new_member.first_name), 
                            parse_mode='HTML', 
                            reply_markup=create_verify_button(),
                            disable_web_page_preview=True
                            )
        verification_status[(message.chat.id, user_id)] = False
        time.sleep(verification_time)
        if not verification_status[(message.chat.id, user_id)]:
            bot.kick_chat_member(message.chat.id, user_id)
            bot.delete_message(message.chat.id, msg.message_id)
            time.sleep(3)
            bot.unban_chat_member(message.chat.id, user_id)


def create_verify_button():
    markup = telebot.types.InlineKeyboardMarkup()
    verify_button = telebot.types.InlineKeyboardButton(text=button_text, callback_data="verify")
    markup.add(verify_button)
    return markup


bot.polling(non_stop=True)
