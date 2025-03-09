from aiogram import types, Router
from aiogram.filters import Command

router = Router()

@router.message(Command("mute"))
async def mute_user(message: types.Message):
    if message.reply_to_message:
        user_id = message.reply_to_message.from_user.id
        await message.bot.restrict_chat_member(message.chat.id, user_id, types.ChatPermissions(can_send_messages=False))
        await message.reply("🔇 User has been muted.", parse_mode="HTML")

def register_handlers(dp):
    dp.include_router(router)
