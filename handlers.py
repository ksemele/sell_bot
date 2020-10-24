from main import bot, dp
from aiogram.types import Message
from config import ADMIN_ID, allowed_users


async def ft_send_to_admin(*args):
	await bot.send_message(chat_id=ADMIN_ID, text='Voodoo21Bot started')


@dp.message_handler(commands=['start'])
async def ft_send_welcome(message: Message):
	await message.reply("what do you need?")


@dp.message_handler(commands=['help'])
async def ft_send_help(message: Message):
	await message.reply("u rly need this...? try find something here >> ya.ru")


@dp.message_handler()
async def echo(message: Message):
	text = 'OK'
	if message.text in allowed_users:
		# todo sleep?
		await bot.send_message(chat_id=message.from_user.id, text=text)
		await bot.send_message(chat_id=message.from_user.id, text='run this...')
		# todo send run.sh binary file to user
		return
	await message.answer(f"[{message.text}] not OK")
