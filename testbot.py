# Это первая тестовая версия бота для Telegram
import telebot;


# import xlsxwriter;
# # открываем новый файл на запись
# workbook = xlsxwriter.Workbook('journal.xlsx')
# # создаем там "лист"
# worksheet = workbook.add_worksheet()
# # в ячейку A1 пишем текст
# worksheet.write('A1','Журнал обращений к боту')
# # сохраняем и закрываем
# workbook.close()

bot = telebot.TeleBot('1217389131:AAFC6Ow-c2YR1O6fH8nLHKyJoauGmbzIYUc');
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    print(message.text)
    if message.text == "Привет":
         bot.send_message(message.from_user.id, "Привет, чем я могу тебе помочь?")
    elif message.text == "/help":
         bot.send_message(message.from_user.id, "Напиши привет")
    else:
            bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")
bot.polling(none_stop=True, interval=0)
