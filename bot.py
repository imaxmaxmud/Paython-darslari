import asyncio
import logging
import re
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.filters import ChatMemberUpdatedFilter, MEMBER, ChatMemberUpdated
from aiogram.utils.keyboard import InlineKeyboardBuilder

TOKEN = "7346072064:AAGuNBqUQWBayBz7LJtkoUEiiEFzOvtfWWo"
ADMIN_ID = 6947353  # Admin ID (Sizning Telegram ID)
SOURCE_CHANNELS = ["@Kunvideolari24", "@Qoraxabar","@shopirlar"]  # Manba kanallar
TARGET_CHANNEL = "@Uznew_yangiliklar"  # Xabar yuboriladigan kanal

bot = Bot(token=TOKEN)
dp = Dispatcher()

def replace_links(text: str) -> str:
    return re.sub(r'https?://\S+', '@Uznew_yangiliklar', text)

@dp.chat_member(ChatMemberUpdatedFilter(member_status_changed=MEMBER))
async def new_member(update: ChatMemberUpdated):
    if update.new_chat_member.status == "member":
        await bot.send_message(update.chat.id, "Xush kelibsiz!")

@dp.channel_post()
async def forward_news(message: Message):
    if message.chat.id in SOURCE_CHANNELS:
        try:
            modified_text = replace_links(message.text) if message.text else message.caption
            keyboard = InlineKeyboardBuilder()
            keyboard.button(text="✅ Tashash", callback_data=f"approve_{message.chat.id}_{message.message_id}")
            keyboard.button(text="❌ Rad etish", callback_data=f"deny_{message.chat.id}_{message.message_id}")
            
            await bot.copy_message(chat_id=ADMIN_ID, from_chat_id=message.chat.id, message_id=message.message_id)
            await bot.send_message(ADMIN_ID, "Xabarni kanalga tashashni xohlaysizmi?", reply_markup=keyboard.as_markup())
            logging.info(f"Xabar admin tasdig'iga yuborildi: {message.message_id}")
        except Exception as e:
            logging.error(f"Xatolik yuz berdi: {e}")

@dp.callback_query()
async def handle_callback(call: types.CallbackQuery):
    data = call.data.split("_")
    action, chat_id, message_id = data[0], int(data[1]), int(data[2])
    
    if action == "approve":
        message = await bot.forward_message(ADMIN_ID, chat_id, message_id)
        modified_text = replace_links(message.text) if message.text else message.caption
        await bot.send_message(chat_id=TARGET_CHANNEL, text=modified_text)
        await bot.send_message(ADMIN_ID, "✅ Xabar kanalga tashlandi!")
    elif action == "deny":
        await bot.send_message(ADMIN_ID, "❌ Xabar rad etildi!")
    
    await call.message.delete()

async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
