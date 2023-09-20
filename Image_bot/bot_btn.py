from aiogram import types

pillow_filters = [
    "BLUR", "CONTOUR", "DETAIL", "EDGE ENHANCE",
    "EDGE ENHANCE MORE", "EMBOSS", "FIND EDGES",
    "SHARPEN", "SMOOTH", "SMOOTH MORE"
]

async def start_menu_btn():
    btn = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    btn.add(
        types.KeyboardButton("🖼 Effectlar"),
        types.KeyboardButton("👤 Admin bilan bog`lanish"),
    )
    return btn


async def effects_btn():
    btn = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    btn.add(
        *[types.KeyboardButton(f"{item}") for item in pillow_filters],
        types.KeyboardButton("🔙 Ortga")
    )
    # for item in pillow_filters:
    #     btn.add(types.KeyboardButton(f"{item}"))
    return btn


