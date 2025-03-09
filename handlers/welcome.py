from aiogram import types, Router
from aiogram.filters import Command

router = Router()

@router.message(Command("welcome"))
async def welcome_cmd(message: types.Message):
    await message.reply("👋 <b>Welcome to the group!</b>
Please follow the rules.", parse_mode="HTML")

def register_handlers(dp):
    dp.include_router(router)
