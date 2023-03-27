import aiogram
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from main import vehicles_array

# Replace YOUR_TOKEN with your bot token
bot = Bot(token='6259190488:AAEd7AIeuGz59EqFzDIqB2FHWNvy-CVX_Hs')
dp = Dispatcher(bot)

# Define your function to handle the button click
@dp.callback_query_handler(lambda c: c.data == 'show_array')
async def process_callback_show_array(callback_query: types.CallbackQuery):

    array_string = "ITEM\tPRICE\n"
    # Format each element in the array as a string in the desired format
    array_string = '\n'.join([f"{elem[0]}: {elem[1]}" for elem in vehicles_array])
    # Send the array string as a message
    await bot.send_message(callback_query.from_user.id, array_string)
# Define your function to handle the button click
@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    # Create the inline keyboard with the "Show Array" button
    keyboard = types.InlineKeyboardMarkup()
    show_array_button = types.InlineKeyboardButton(text="Show Prices", callback_data="show_array")
    keyboard.add(show_array_button)
    # Send the start message with the inline keyboard
    await bot.send_message(message.chat.id, "Click the button to show Prices:", reply_markup=keyboard)

# Start the bot
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

