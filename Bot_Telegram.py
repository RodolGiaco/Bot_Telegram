from telegram.ext import (Updater, CommandHandler,MessageHandler, Filters)


def start(update,context):
	userid1 = str(update.message.chat_id)
	print(userid1)
	context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Hola soy Rodo"
    )
    
start_handler = CommandHandler('start', start)

# def echo(update,context):	
#   context.bot.send_message(
#        chat_id=update.effective_chat.id,
#        text=update.message.text
#   )
#   exit(0)
	
# echo_handler = MessageHandler(Filters.text & (~Filters.command),echo)

def hola(update, context):
	myStr = update.message.text
	print(type(myStr))
	myStrArray = myStr.split(' ')
	print(myStrArray)

hola_handler = MessageHandler(Filters.text & (~Filters.command),hola)
    
def main():
	TOKEN="5216494523:AAEBoEjXbtMC771QLyVKNlmoU9xaJvUNp18"
	updater=Updater(TOKEN, use_context=True)

	dp=updater.dispatcher
	dp.add_handler(start_handler)
	#dp.add_handler(echo_handler)
	dp.add_handler(hola_handler)

	updater.start_polling()
	updater.idle()

if __name__ == '__main__':
	main()


