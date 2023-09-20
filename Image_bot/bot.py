import logging
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage 
from aiogram.dispatcher import FSMContext #
from bot_btn import start_menu_btn, effects_btn, pillow_filters 
from bot_states import UserStates 
from bot_utils import make_img_filter
import os #
import datetime
from database import * 

logging.basicConfig(level=logging.INFO)

BOT_TOKEN = '5939110451:AAHd3BnHchgsazL-111kod9Yab_gKCWoBUY' 
ADMINS = [670607400]

bot = Bot(token=BOT_TOKEN, parse_mode='html')
storage = MemoryStorage()
dp = Dispatcher(bot=bot, storage=storage)


async def on_start_bot(dispatcher):
    await create_table()


@dp.message_handler(commands=['start'])
async def welcome_handler(message: types.Message):
    user_id = message.from_user.id
    username = message.from_user.username
    today = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
    await create_user(user_id, username, today)

    btn = await start_menu_btn()
    await message.answer("Salom men rasimlarga turli xil effectlar beraoladigon bor man!", reply_markup=btn)
    await message.answer(datetime.datetime.now().strftime("%Y.%m.%d %H:%M"))



@dp.message_handler(commands=['admin'])
async def admin_handler(message: types.Message):
    user_id = message.from_user.id
    if user_id in ADMINS:
        all_users = await select_all_users()
        today_users = await select_today_users()
        yesterday_users = await select_yesterday_users()
        await message.answer(f"Bot azolar: {all_users} ta\nBugun kirgan azolar: {today_users} ta\nKecha kirgan azolar: {yesterday_users} ta")
    else:
        await message.answer("Siz admin emasiz!")


@dp.message_handler(commands=['send'])
async def send_msg_all_users(message: types.Message):
    user_id = message.from_user.id
    if user_id in ADMINS:
        await message.answer("Xabaringizni yuboring: ")

        await UserStates.mailing.set()

@dp.message_handler(state=UserStates.mailing, content_types=["text"])
async def mailing_to_users(message: types.Message, state: FSMContext):
    text = message.text
    users = await get_all_users()
    for user in users:
        await bot.send_message(chat_id=user[0], text = text)


@dp.message_handler(state=UserStates.mailing, content_types=["photo"])
async def mailing_to_users(message: types.Message, state: FSMContext):
    photo = types.InputFile("images.png")
    users = await get_all_users()
    for user in users:
        await bot.send_photo(chat_id=user[0], photo = photo)

@dp.message_handler(state=UserStates.mailing, content_types=["video"])
async def mailing_to_users(message: types.Message, state: FSMContext):

    video = types.InputFile("video.mp4")
    users = await get_all_users()
    for user in users:
        await bot.send_video(chat_id=user[0], video = video)

@dp.message_handler(state=UserStates.mailing, content_types=["audio"])
async def mailing_to_users(message: types.Message, state: FSMContext):
    audio = types.InputFile("audio.ogg")
    users = await get_all_users()

    for user in users:
        await bot.send_audio(chat_id=user[0], audio = audio)

@dp.message_handler(state=UserStates.mailing, content_types=["gif"])
async def mailing_to_users(message: types.Message, state: FSMContext):
    animation = types.InputFile("Gif.mp4")
    users = await get_all_users()
    await state.finish()
    for user in users:

        await bot.send_animation(chat_id=user[0], animation = animation)

@dp.message_handler(text="🖼 Effectlar")
async def show_effects_handler(message: types.Message):
    btn = await effects_btn()
    await message.answer("Effectni tanlang:", reply_markup=btn)


@dp.message_handler(text="🔙 Ortga")
async def back_to_menu_handler(message: types.Message):
    await welcome_handler(message)


@dp.message_handler()
async def select_filter_handler(message: types.Message, state: FSMContext):
    text = message.text
    if text in pillow_filters:
        await state.update_data(user_filter=text, info="Burhaniddin")
        await message.answer("Rasim yuboring:")
        await UserStates.get_img.set()


@dp.message_handler(state=UserStates.get_img, content_types=['photo'])
async def get_img_state(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    filename = f"img_{user_id}.png"
    await message.photo[-1].download(destination_file=filename)
    msg_id = await message.answer("⏳")
    data = await state.get_data()
    result_img = await make_img_filter(img=filename, filter_name=data['user_filter'])
    await bot.delete_message(user_id, message_id=msg_id.message_id)
    await message.answer_photo(types.InputFile(result_img), caption="✅")
    await state.finish()
    os.unlink(result_img)


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_start_bot)
