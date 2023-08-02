import telepot
from telepot.loop import MessageLoop

# Replace 'YOUR_BOT_TOKEN' with the actual API token you received from BotFather
bot = telepot.Bot('6544954684:AAFOO7tG48gRFLtAFPVzD1iRguFh0exqaBY')

# This dictionary will store the available stock of vape pens
stock = {
    'Blueberry Kush': 33,
    'Sunset Sherbet': 34,
    'London Pound Cake': 31,
    'Pineapple Express': 32,
    'Royal Jelly': 12
}

def handle_message(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    
    if content_type == 'text':
        command = msg['text']
        if command == '/start':
            bot.sendMessage(chat_id, "Welcome to the Vape Pen Store! Use /help to see available commands.")
        elif command == '/help':
            help_message = "Available commands:\n"
            help_message += "/start - Start the bot and receive a welcome message.\n"
            help_message += "/help - Display this help message.\n"
            help_message += "/stock - View available vape pens and quantities.\n"
            help_message += "/order [pen_name] - Place an order for a specific vape pen.\n"
            help_message += "/dm - Send a direct message to the store owner."
            bot.sendMessage(chat_id, help_message)
        elif command == '/stock':
            stock_message = "Available Vape Pens:\n"
            for pen, quantity in stock.items():
                stock_message += f"{pen}: {quantity} in stock\n"
            bot.sendMessage(chat_id, stock_message)
        elif command.startswith('/order'):
            _, pen_name = command.split(' ', 1)
            if pen_name in stock:
                if stock[pen_name] > 0:
                    stock[pen_name] -= 1
                    bot.sendMessage(chat_id, f"Your order for {pen_name} has been placed. Thank you!")
                else:
                    bot.sendMessage(chat_id, f"Sorry, {pen_name} is currently out of stock.")
            else:
                bot.sendMessage(chat_id, "Vape pen not found. Please check the available pens using /stock.")
        elif command == '/dm':
            bot.sendMessage(chat_id, "You can send a direct message to the store owner by clicking on 'Start' and then 'Message' in the chat with the bot.")
        else:
            bot.sendMessage(chat_id, "Sorry, I don't understand that command. Use /help to see available commands.")

# Start the message loop to continuously listen for incoming messages
MessageLoop(bot, handle_message).run_as_thread()

# Keep the program running
while True:
    pass
