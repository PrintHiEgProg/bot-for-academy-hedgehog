import asyncio
import logging

import yookassa


from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton
from aiogram import Router, types, F
from aiogram import Bot, types
from aiogram import Router, types, F
from aiogram.client import bot
from aiogram.enums import ContentType
from aiogram.filters import Command, StateFilter
from aiogram import types
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram import Bot, Dispatcher, types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils.deep_linking import create_start_link, decode_payload
import time
from aiogram.utils.markdown import hlink
import uuid
from aiogram import Router, types, F
from aiogram.client import bot
from aiogram.enums import ContentType
from aiogram.filters import Command
from aiogram import types
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State

from yookassa import Configuration, Payment

from payment import create
from aiogram.fsm.state import StatesGroup, State
import logging
import asyncio
import os
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram import Router, types, F
from aiogram.client import bot
from aiogram.enums import ContentType
from aiogram.filters import Command
from aiogram import types
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
import random

logging.basicConfig(level=logging.INFO)
storage = MemoryStorage()
router = Router()
Configuration.account_id = "390758"
Configuration.secret_key = "test_1Dl-vG5-vhngjfudno_K8O1-O41JVjKyOmzNteUEYHU"
ACCOUNT_ID = "390758"
SECRET_KEY = "test_1Dl-vG5-vhngjfudno_K8O1-O41JVjKyOmzNteUEYHU"
PRICE = "1.00" 
bot = Bot(token="6444012828:AAF-LBFaKiR9OBLIuBO2KPXWCJHNmE3fQJQ")
link_group = ""
PRICE_LIST = ["6000.00","7000.00","6000.00","6000.00","6000.00"]
SMALL_PROGERS_PRICE=PRICE_LIST[0]
PROGERS_PRICE=PRICE_LIST[1]
WEB_DESIGNER_PRICE=PRICE_LIST[2]
GAME_DEVELOPER_PRICE=PRICE_LIST[3]
BLOGGER_PRICE=PRICE_LIST[4]

GROUP_LIST = ["https://t.me/+ONDmCM7vaBwxZWMy","https://t.me/+5LVy696K_almNTYy","https://t.me/+3rkagsqO-ecwYTky","https://t.me/+UwBWMt99A4RiODI6","https://t.me/+lPJOJBc6H-VmNmMy"]
SMALL_PROGERS_GROUP = GROUP_LIST[0]
PROGERS_GROUP = GROUP_LIST[1]
WEB_DESIGNER_GROUP = GROUP_LIST[2]
GAME_DEVELOPER_GROUP = GROUP_LIST[3]
BLOGGER_GROUP = GROUP_LIST[4]

joinedFile = open("joined.txt", "r")
joinedUsers = set ()
for line in joinedFile:
    joinedUsers.add(line.strip())
joinedFile.close()


@router.message(Command("start"))
async def cmd_start(message: types.Message) -> None:

    global username
    global userlastname
    global user_id
    username = message.from_user.first_name
    userlastname = message.from_user.full_name
    nickname = message.from_user.username
    user_id = message.from_user.id
    chat_id = message.chat.id
    if not str(message.chat.id) in joinedUsers:
        joinedFile = open("joined.txt", "a")
        joinedFile.write(str(message.chat.id) + "\n")
        joinedUsers.add(message.chat.id)

    main_menu = [
        [
            types.KeyboardButton(text="Информация")],[
            types.KeyboardButton(text="Купить курсы")],[
            types.KeyboardButton(text="Техподдержка")]



        ]

    keyboard = types.ReplyKeyboardMarkup(keyboard=main_menu, resize_keyboard=True)
    await message.answer(f"Привет {username}!\nМы ИТ-академия Хечхог.\nХечхог - это ИТ-школа где дети изучают не только программирование, но и другие востребованные навыки в сфере ИТ. Такие как работу с нейросетями, создание игр, 3D-моделирование, web-дизайн и блогинг." , reply_markup=keyboard)
    print("first name:",username)
    print("last name:",userlastname)
    print("nickname:",nickname)
    print("user id:", user_id)
    print("бот запущен!")

class Form(StatesGroup):
    priceSMALL_PROGGERS = State()
    pricePROGGERS = State()
    priceWEB_DESIGNER = State()
    priceGAME_DEVELOPER = State()
    priceBLOGGER = State()
    groupSMALL_PROGGERS = State()
    groupPROGGERS = State()
    groupWEB_DESIGNER = State()
    groupGAME_DEVELOPER = State()
    groupBLOGGER = State()
    end = State()


@router.message(F.text == "Купить курсы")
async def buyLoot(message: types.Message, state: FSMContext) -> None:
    if message.text == 'Купить курсы':
        main_menu = [
        [
            types.KeyboardButton(text="Младший программист")],[
            types.KeyboardButton(text="Разработчик игр")],[
            types.KeyboardButton(text="Web-дизайнер")],[
            types.KeyboardButton(text="Программист")
            ],[types.KeyboardButton(text="Блогер")],
            [types.KeyboardButton(text="Назад")]



        ]

        keyboard = types.ReplyKeyboardMarkup(keyboard=main_menu, resize_keyboard=True)
        await message.answer(f"Выберите интересующий курс:", reply_markup=keyboard)

#тут обработка курсов и их описания с кнопкой оплатить

@router.message(F.text == "Младший программист")
async def buyLoot(message: types.Message, state: FSMContext) -> None:
    global PRICE
    global link_group
    global SMALL_PROGERS_PRICE
    global SMALL_PROGERS_GROUP
    PRICE = SMALL_PROGERS_PRICE
    link_group=SMALL_PROGERS_GROUP 
    payment_url, payment_id = create(PRICE, message.chat.id)
    builder = InlineKeyboardBuilder()
    builder.row(types.InlineKeyboardButton(
        text="✅ОПЛАТИТЬ", url=payment_url),
    )
    builder.row(types.InlineKeyboardButton(
        text="Проверить оплату", callback_data=f"check_{payment_id}")
    )

    if message.text == 'Младший программист':
        #логика предоставления счёта
        
        
        await message.answer(f'<b>Курс "Младший программист"</b>\n\nПрограмма рассчитана на возраст 7-9 лет\n\nУченики на этом курсе изучат компьютерную грамотность, научаться работать с Искусственным интеллектом, а также будут разрабатывать игру в среде программирования Scratch.\n\nЧему научится ребенок:\n✔ Работе с компьютером и ИИ\n✔ Работать в программе Scratch\n✔Работе и коммуникации в команде\n✔Геймдизайну и созданию своих проектов\n\nУ нас есть гарантия образовательного результата: в конце каждого модуля ребёнок создает свой проект, в противном случае мы возвращаем деньги!\n\nПогружаемся в профессию, создаём, креативим и презентуем!\n\n<b>Цена курса: {PRICE}₽</b>', parse_mode='HTML', reply_markup=builder.as_markup())

@router.message(F.text == "Разработчик игр")
async def buyLoot(message: types.Message, state: FSMContext) -> None:
    global PRICE
    global GAME_DEVELOPER_PRICE
    global GAME_DEVELOPER_GROUP
    PRICE=GAME_DEVELOPER_PRICE
    link_group=GAME_DEVELOPER_GROUP   
    payment_url, payment_id = create(PRICE, message.chat.id)
    builder = InlineKeyboardBuilder()
    builder.row(types.InlineKeyboardButton(
        text="✅ОПЛАТИТЬ", url=payment_url),
    )
    builder.row(types.InlineKeyboardButton(
        text="Проверить оплату", callback_data=f"check_{payment_id}")
    )

    if message.text == 'Разработчик игр':
        #логика предоставления счёта
        
        
        
        await message.answer(f'<b>Курс "Разработчик игр"</b>\n\nПрограмма рассчитана на возраст 10-12 лет\n\nВ игровом и знакомом ребенку формате он с помощью строчного языка Lua создаст свою игру в Roblox и выгрузит её на сервер. Затем уже в среде Blender изучит основы создания 3D моделей, и к концу курса будет уверенно владеть двумя языком программирования и основами гейм-дизайна.\n\nЧему научится ребенок:\n✔ Работать в программах Roblox и Blender\n✔ Работе и коммуникации в команде\n✔ Геймдизайну и созданию своих проектов\n\nУ нас есть гарантия образовательного результата: в конце каждого модуля ребёнок создает свой проект- в противном случае мы возвращаем деньги!\n\nПогружаемся в профессию, создаём, креативим и презентуем!\n\n<b>Цена курса: {PRICE}₽</b>', parse_mode='HTML', reply_markup=builder.as_markup())

@router.message(F.text == "Web-дизайнер")
async def buyLoot(message: types.Message, state: FSMContext) -> None:
    global PRICE
    global link_group
    global WEB_DESIGNER_PRICE
    global WEB_DESIGNER_GROUP
    PRICE=WEB_DESIGNER_PRICE
    link_group=WEB_DESIGNER_GROUP
    payment_url, payment_id = create(PRICE, message.chat.id)
    builder = InlineKeyboardBuilder()
    builder.row(types.InlineKeyboardButton(
        text="✅ОПЛАТИТЬ", url=payment_url),
    )
    builder.row(types.InlineKeyboardButton(
        text="Проверить оплату", callback_data=f"check_{payment_id}")
    )

    if message.text == 'Web-дизайнер':
        #логика предоставления счёта
        
        
        await message.answer(f'<b>Курс "Web-дизайнер"</b>\n\nПрограмма рассчитана на возраст 12-17 лет\n\nУченики познакомятся с профессией дизайнера, изучат Tilda, научатся делать сайты, презентации и визитки. Также ученики спроектируют интерфейс приложения, а затем будут осваивать верстку сайтов на HTML.\n\nЧему научится ребенок:\n✔ Работать в программах Tilda, Figma, HTML.\n✔ Работе и коммуникации в команде\n✔ Сайтостроению и созданию своих проектов\n\nУ нас есть гарантия образовательного результата: в конце каждого модуля ребёнок создает свой проект - в противном случае мы возвращаем деньги!\n\nПогружаемся в профессию, создаём, креативим и презентуем!\n\n<b>Цена курса: {PRICE}₽</b>', parse_mode='HTML', reply_markup=builder.as_markup())

@router.message(F.text == "Программист")
async def buyLoot(message: types.Message, state: FSMContext) -> None:
    global PRICE
    global link_group
    global PROGERS_PRICE
    global PROGERS_GROUP
    PRICE=PROGERS_PRICE
    link_group=PROGERS_GROUP
    payment_url, payment_id = create(PRICE, message.chat.id)
    builder = InlineKeyboardBuilder()
    builder.row(types.InlineKeyboardButton(
        text="✅ОПЛАТИТЬ", url=payment_url),
    )
    builder.row(types.InlineKeyboardButton(
        text="Проверить оплату", callback_data=f"check_{payment_id}")
    )

    if message.text == 'Программист':
        #логика предоставления счёта
        
        
        await message.answer(f'<b>Курс "Программист"</b>\n\nПрограмма рассчитана на возраст 13-17 лет\n\nУченики погрузятся в профессию программиста, изучат язык программирования Python, создадут простое консольное приложение, чат-бота и игру. К концу курса ребенок освоит базово язык программирования, сможет создавать различного уровня приложения, верстать сайты и делать небольшие игры.\n\nЧему научится ребенок:\n✔ Работать в программе Python\n✔ Работе и коммуникации в команде\n✔ Геймдизайну и созданию своих проектов\n\nУ нас есть гарантия образовательного результата: в конце каждого модуля ребёнок создает свой проект - в противном случае мы возвращаем деньги!\n\nПогружаемся в профессию, создаём, креативим и презентуем!\n\n<b>Цена курса: {PRICE}₽</b>', parse_mode='HTML', reply_markup=builder.as_markup())

@router.message(F.text == "Блогер")
async def buyLoot(message: types.Message, state: FSMContext) -> None:
    global PRICE
    global link_group
    global BLOGGER_PRICE
    global BLOGGER_GROUP
    PRICE=BLOGGER_PRICE
    link_group=BLOGGER_GROUP
    
    payment_url, payment_id = create(PRICE, message.chat.id)
    builder = InlineKeyboardBuilder()
    builder.row(types.InlineKeyboardButton(
        text="✅ОПЛАТИТЬ", url=payment_url),
    )
    builder.row(types.InlineKeyboardButton(
        text="Проверить оплату", callback_data=f"check_{payment_id}")
    )

    if message.text == 'Блогер':
        #логика предоставления счёта
        
        
        await message.answer(f'<b>Курс "Блогер"</b>\n\nПрограмма рассчитана на возраст 8-14 лет\n\nУченики узнают основы монтажа и съемки, научатся снимать и монтировать на телефоне, создадут свой блог.\n\nЧему научится ребенок:\n✔ Работать с площадками YouTube, ВКонтакте\n✔ Снимать и монтировать видео на телефоне\n✔ Работе и коммуникации в команде\n✔ Блогингу и созданию своих проектов\n\nУ нас есть гарантия образовательного результата: в конце каждого модуля ребёнок создает свой проект - в противном случае мы возвращаем деньги!\n\nПогружаемся в профессию, создаём, креативим и презентуем!\n\n<b>Цена курса: {PRICE}₽</b>', parse_mode='HTML', reply_markup=builder.as_markup())

def check(payment_id):
    payment = yookassa.Payment.find_one(payment_id)
    if payment.status == "succeeded":
        return payment.metadata
    else:
        return False

@router.callback_query(lambda c: 'check' in c.data)
async def check_handler(callback: types.callback_query, state: FSMContext):
    main_menu = [
        [
            types.KeyboardButton(text="Информация")],[
            types.KeyboardButton(text="Купить курсы")],[
            types.KeyboardButton(text="Техподдержка")]



        ]

    keyboard = types.ReplyKeyboardMarkup(keyboard=main_menu, resize_keyboard=True)
    
    builder = InlineKeyboardBuilder()
    builder.row(types.InlineKeyboardButton(
        text="Перейти в группу", url=link_group),
    )
    
    
    result = check(callback.data.split("_")[-1])
    if result:
        await callback.message.answer("Оплата прошла успешно!", reply_markup=builder.as_markup())
        await callback.message.answer("Переходите в группу дальше вся информация будет там!", reply_markup=keyboard)
        
        
        


    else:
        print(link_group)
        await callback.message.answer("Оплата не прошла или возникла ошибка")
    await callback.answer()


@router.message(F.text == "Техподдержка")
async def tech_help(message: types.Message) -> None:
    if message.text == "Техподдержка":
        await message.answer("С ботом что-то не так?\nНе получается оплатить?\nНапишите -> @egprog")

@router.message(F.text == "Информация")
async def tech_help(message: types.Message) -> None:
    if message.text == "Информация":
        await message.answer("Хечхог - это ИТ-школа где дети изучают не только программирование, но и другие востребованные навыки в сфере ИТ. Такие как работу с нейросетями, создание игр, 3D-моделирование, web-дизайн и блогинг.")

@router.message(F.text == "Назад")
async def tech_help(message: types.Message) -> None:
    main_menu = [
        [
            types.KeyboardButton(text="Информация")],[
            types.KeyboardButton(text="Купить курсы")],[
            types.KeyboardButton(text="Техподдержка")]



        ]

    keyboard = types.ReplyKeyboardMarkup(keyboard=main_menu, resize_keyboard=True)
    if message.text == "Назад":
        await message.answer("Вы вернулись назад", reply_markup=keyboard)

@router.message(Command("admin"))
async def setPrice(message: types.Message, state: FSMContext) -> None:
    main_menu = [
        [
            types.KeyboardButton(text="Изменить цену")],[
            types.KeyboardButton(text="Изменить ссылку на группу")]



        ]

    keyboard = types.ReplyKeyboardMarkup(keyboard=main_menu, resize_keyboard=True)

    await message.answer('Выберите что хотите сделать:', reply_markup=keyboard)
    
#изменение цен

@router.message(F.text == "Изменить цену")
async def tech_help(message: types.Message) -> None:
    if message.text == "Изменить цену":
        main_menu = [
        [
            types.KeyboardButton(text="Цена Младший программист")],[
            types.KeyboardButton(text="Цена Разработчик игр")],[
            types.KeyboardButton(text="Цена Web-дизайнер")],[
            types.KeyboardButton(text="Цена Программист")
            ],[types.KeyboardButton(text="Цена Блогер")],
            [types.KeyboardButton(text="Вернуться")]



        ]

        keyboard = types.ReplyKeyboardMarkup(keyboard=main_menu, resize_keyboard=True)
        await message.answer("Выберите у чего хотите изменить цену:", reply_markup=keyboard)


@router.message(F.text == "Вернуться")
async def tech_help(message: types.Message) -> None:
    if message.text == "Вернуться":
        main_menu = [
        [
            types.KeyboardButton(text="Изменить цену")],[
            types.KeyboardButton(text="Изменить ссылку на группу")]



        ]

        keyboard = types.ReplyKeyboardMarkup(keyboard=main_menu, resize_keyboard=True)
        await message.answer("Вы вернулись", reply_markup=keyboard)



@router.message(F.text == "Цена Младший программист")
async def setPrice(message: types.Message, state: FSMContext) -> None:
    if message.text == "Цена Младший программист":
        await message.answer('Введите новую цену для курса "Младший программист" в формате (1.00)', reply_markup=types.ReplyKeyboardRemove())
        await state.set_state(Form.priceSMALL_PROGGERS)

@router.message(Form.priceSMALL_PROGGERS)
async def setPrice(message: types.Message, state: FSMContext) -> None:
    main_menu = [
        [
            types.KeyboardButton(text="Цена Младший программист")],[
            types.KeyboardButton(text="Цена Разработчик игр")],[
            types.KeyboardButton(text="Цена Web-дизайнер")],[
            types.KeyboardButton(text="Цена Программист")
            ],[types.KeyboardButton(text="Цена Блогер")],
            [types.KeyboardButton(text="Вернуться")]



        ]

    keyboard = types.ReplyKeyboardMarkup(keyboard=main_menu, resize_keyboard=True)
    await state.update_data(priceSMALL_PROGGERS=message.text)
    user_data = await state.get_data()
    priceSMALL_PROGGERS = user_data['priceSMALL_PROGGERS']
    global PRICE_LIST
    global SMALL_PROGERS_PRICE
    PRICE_LIST.pop(0)
    PRICE_LIST.insert(0, priceSMALL_PROGGERS)
    SMALL_PROGERS_PRICE=PRICE_LIST[0]
    await message.answer(f'Цена курса "Младший разработчик" изменена на {SMALL_PROGERS_PRICE}', reply_markup=keyboard)
    await state.set_state(Form.end)

@router.message(F.text == "Цена Программист")
async def setPrice(message: types.Message, state: FSMContext) -> None:
    if message.text == "Цена Программист":
        await message.answer('Введите новую цену для курса "Программист" в формате (1.00)', reply_markup=types.ReplyKeyboardRemove())
        await state.set_state(Form.pricePROGGERS)

@router.message(Form.pricePROGGERS)
async def setPrice(message: types.Message, state: FSMContext) -> None:
    main_menu = [
        [
            types.KeyboardButton(text="Цена Младший программист")],[
            types.KeyboardButton(text="Цена Разработчик игр")],[
            types.KeyboardButton(text="Цена Web-дизайнер")],[
            types.KeyboardButton(text="Цена Программист")
            ],[types.KeyboardButton(text="Цена Блогер")],
            [types.KeyboardButton(text="Вернуться")]



        ]

    keyboard = types.ReplyKeyboardMarkup(keyboard=main_menu, resize_keyboard=True)
    await state.update_data(pricePROGGERS=message.text)
    user_data = await state.get_data()
    pricePROGGERS = user_data['pricePROGGERS']
    global PRICE_LIST
    global PROGERS_PRICE
    PRICE_LIST.pop(1)
    PRICE_LIST.insert(1, pricePROGGERS)
    PROGERS_PRICE=PRICE_LIST[1]
    await message.answer(f'Цена курса "Программист" изменена на {PROGERS_PRICE}', reply_markup=keyboard)
    await state.set_state(Form.end)

@router.message(F.text == "Цена Web-дизайнер")
async def setPrice(message: types.Message, state: FSMContext) -> None:
    if message.text == "Цена Web-дизайнер":
        await message.answer('Введите новую цену для курса "Web-дизайнер" в формате (1.00)', reply_markup=types.ReplyKeyboardRemove())
        await state.set_state(Form.priceWEB_DESIGNER)

@router.message(Form.priceWEB_DESIGNER)
async def setPrice(message: types.Message, state: FSMContext) -> None:
    main_menu = [
        [
            types.KeyboardButton(text="Цена Младший программист")],[
            types.KeyboardButton(text="Цена Разработчик игр")],[
            types.KeyboardButton(text="Цена Web-дизайнер")],[
            types.KeyboardButton(text="Цена Программист")
            ],[types.KeyboardButton(text="Цена Блогер")],
            [types.KeyboardButton(text="Вернуться")]



        ]

    keyboard = types.ReplyKeyboardMarkup(keyboard=main_menu, resize_keyboard=True)
    await state.update_data(priceWEB_DESIGNER=message.text)
    user_data = await state.get_data()
    priceWEB_DESIGNER = user_data['priceWEB_DESIGNER']
    global PRICE_LIST
    global WEB_DESIGNER_PRICE
    PRICE_LIST.pop(2)
    PRICE_LIST.insert(2, priceWEB_DESIGNER)
    WEB_DESIGNER_PRICE=PRICE_LIST[2]
    await message.answer(f'Цена курса "Web-дизайнер" изменена на {WEB_DESIGNER_PRICE}', reply_markup=keyboard)
    await state.set_state(Form.end)

@router.message(F.text == "Цена Разработчик игр")
async def setPrice(message: types.Message, state: FSMContext) -> None:
    if message.text == "Цена Разработчик игр":
        await message.answer('Введите новую цену для курса "Разработчик игр" в формате (1.00)', reply_markup=types.ReplyKeyboardRemove())
        await state.set_state(Form.priceGAME_DEVELOPER)

@router.message(Form.priceGAME_DEVELOPER)
async def setPrice(message: types.Message, state: FSMContext) -> None:
    main_menu = [
        [
            types.KeyboardButton(text="Цена Младший программист")],[
            types.KeyboardButton(text="Цена Разработчик игр")],[
            types.KeyboardButton(text="Цена Web-дизайнер")],[
            types.KeyboardButton(text="Цена Программист")
            ],[types.KeyboardButton(text="Цена Блогер")],
            [types.KeyboardButton(text="Вернуться")]



        ]

    keyboard = types.ReplyKeyboardMarkup(keyboard=main_menu, resize_keyboard=True)
    await state.update_data(priceGAME_DEVELOPER=message.text)
    user_data = await state.get_data()
    priceGAME_DEVELOPER = user_data['priceGAME_DEVELOPER']
    global PRICE_LIST
    global GAME_DEVELOPER_PRICE
    PRICE_LIST.pop(3)
    PRICE_LIST.insert(3, priceGAME_DEVELOPER)
    GAME_DEVELOPER_PRICE=PRICE_LIST[3]
    await message.answer(f'Цена курса "Разработчик игр" изменена на {GAME_DEVELOPER_PRICE}', reply_markup=keyboard)
    await state.set_state(Form.end)

@router.message(F.text == "Цена Блогер")
async def setPrice(message: types.Message, state: FSMContext) -> None:
    if message.text == "Цена Блогер":
        await message.answer('Введите новую цену для курса "Блогер" в формате (1.00)', reply_markup=types.ReplyKeyboardRemove())
        await state.set_state(Form.priceBLOGGER)

@router.message(Form.priceBLOGGER)
async def setPrice(message: types.Message, state: FSMContext) -> None:
    main_menu = [
        [
            types.KeyboardButton(text="Цена Младший программист")],[
            types.KeyboardButton(text="Цена Разработчик игр")],[
            types.KeyboardButton(text="Цена Web-дизайнер")],[
            types.KeyboardButton(text="Цена Программист")
            ],[types.KeyboardButton(text="Цена Блогер")],
            [types.KeyboardButton(text="Вернуться")]



        ]

    keyboard = types.ReplyKeyboardMarkup(keyboard=main_menu, resize_keyboard=True)
    await state.update_data(priceBLOGGER=message.text)
    user_data = await state.get_data()
    priceBLOGGER = user_data['priceBLOGGER']
    global PRICE_LIST
    global BLOGGER_PRICE
    PRICE_LIST.pop(4)
    PRICE_LIST.insert(4, priceBLOGGER)
    BLOGGER_PRICE=PRICE_LIST[4]
    await message.answer(f'Цена курса "Блогер" изменена на {BLOGGER_PRICE}', reply_markup=keyboard)
    await state.set_state(Form.end)

@router.message(F.text == "Изменить ссылку на группу")
async def tech_help(message: types.Message) -> None:
    if message.text == "Изменить ссылку на группу":
        main_menu = [
        [
            types.KeyboardButton(text="Группа Младший программист")],[
            types.KeyboardButton(text="Группа Разработчик игр")],[
            types.KeyboardButton(text="Группа Web-дизайнер")],[
            types.KeyboardButton(text="Группа Программист")
            ],[types.KeyboardButton(text="Группа Блогер")],
            [types.KeyboardButton(text="Вернуться")]



        ]

        keyboard = types.ReplyKeyboardMarkup(keyboard=main_menu, resize_keyboard=True)
        await message.answer("Выберите у чего хотите изменить ссылку на группу:", reply_markup=keyboard)

#изменение ссылок на группу

@router.message(F.text == "Группа Младший программист")
async def setPrice(message: types.Message, state: FSMContext) -> None:
    if message.text == "Группа Младший программист":
        await message.answer('Введите новую новую ссылку на группу для курса "Младший программист" в формате (https://...)', reply_markup=types.ReplyKeyboardRemove())
        await state.set_state(Form.groupSMALL_PROGGERS)

@router.message(Form.groupSMALL_PROGGERS)
async def setPrice(message: types.Message, state: FSMContext) -> None:
    main_menu = [
        [
            types.KeyboardButton(text="Группа Младший программист")],[
            types.KeyboardButton(text="Группа Разработчик игр")],[
            types.KeyboardButton(text="Группа Web-дизайнер")],[
            types.KeyboardButton(text="Группа Программист")
            ],[types.KeyboardButton(text="Группа Блогер")],
            [types.KeyboardButton(text="Вернуться")]



        ]

    keyboard = types.ReplyKeyboardMarkup(keyboard=main_menu, resize_keyboard=True)
    await state.update_data(groupSMALL_PROGGERS=message.text)
    user_data = await state.get_data()
    groupSMALL_PROGGERS = user_data['groupSMALL_PROGGERS']
    global GROUP_LIST
    global SMALL_PROGERS_GROUP
    GROUP_LIST.pop(0)
    GROUP_LIST.insert(0, groupSMALL_PROGGERS)
    SMALL_PROGERS_GROUP=GROUP_LIST[0]
    await message.answer(f'Группа курса "Младший разработчик" изменена на {SMALL_PROGERS_GROUP}', reply_markup=keyboard)
    await state.set_state(Form.end)

@router.message(F.text == "Группа Программист")
async def setPrice(message: types.Message, state: FSMContext) -> None:
    if message.text == "Группа Программист":
        await message.answer('Введите новую новую ссылку на группу для курса "Программист" в формате (https://...)', reply_markup=types.ReplyKeyboardRemove())
        await state.set_state(Form.groupPROGGERS)

@router.message(Form.groupPROGGERS)
async def setPrice(message: types.Message, state: FSMContext) -> None:
    main_menu = [
        [
            types.KeyboardButton(text="Группа Младший программист")],[
            types.KeyboardButton(text="Группа Разработчик игр")],[
            types.KeyboardButton(text="Группа Web-дизайнер")],[
            types.KeyboardButton(text="Группа Программист")
            ],[types.KeyboardButton(text="Группа Блогер")],
            [types.KeyboardButton(text="Вернуться")]



        ]

    keyboard = types.ReplyKeyboardMarkup(keyboard=main_menu, resize_keyboard=True)
    await state.update_data(groupPROGGERS=message.text)
    user_data = await state.get_data()
    groupPROGGERS = user_data['groupPROGGERS']
    global GROUP_LIST
    global PROGERS_GROUP
    GROUP_LIST.pop(1)
    GROUP_LIST.insert(1, groupPROGGERS)
    PROGERS_GROUP=GROUP_LIST[1]
    await message.answer(f'Группа курса "Программист" изменена на {PROGERS_GROUP}', reply_markup=keyboard)
    await state.set_state(Form.end)

@router.message(F.text == "Группа Web-дизайнер")
async def setPrice(message: types.Message, state: FSMContext) -> None:
    if message.text == "Группа Web-дизайнер":
        await message.answer('Введите новую новую ссылку на группу для курса "Web-дизайнер" в формате (https://...)', reply_markup=types.ReplyKeyboardRemove())
        await state.set_state(Form.groupWEB_DESIGNER)

@router.message(Form.groupWEB_DESIGNER)
async def setPrice(message: types.Message, state: FSMContext) -> None:
    main_menu = [
        [
            types.KeyboardButton(text="Группа Младший программист")],[
            types.KeyboardButton(text="Группа Разработчик игр")],[
            types.KeyboardButton(text="Группа Web-дизайнер")],[
            types.KeyboardButton(text="Группа Программист")
            ],[types.KeyboardButton(text="Группа Блогер")],
            [types.KeyboardButton(text="Вернуться")]



        ]

    keyboard = types.ReplyKeyboardMarkup(keyboard=main_menu, resize_keyboard=True)
    await state.update_data(groupWEB_DESIGNER=message.text)
    user_data = await state.get_data()
    groupWEB_DESIGNER = user_data['groupWEB_DESIGNER']
    global GROUP_LIST
    global WEB_DESIGNER_GROUP
    GROUP_LIST.pop(2)
    GROUP_LIST.insert(2, groupWEB_DESIGNER)
    WEB_DESIGNER_GROUP=GROUP_LIST[2]
    await message.answer(f'Группа курса "Web-дизайнер" изменена на {WEB_DESIGNER_GROUP}', reply_markup=keyboard)
    await state.set_state(Form.end)

@router.message(F.text == "Группа Разработчик игр")
async def setPrice(message: types.Message, state: FSMContext) -> None:
    if message.text == "Группа Разработчик игр":
        await message.answer('Введите новую новую ссылку на группу для курса "Разработчик игр" в формате (https://...)', reply_markup=types.ReplyKeyboardRemove())
        await state.set_state(Form.groupGAME_DEVELOPER)

@router.message(Form.groupGAME_DEVELOPER)
async def setPrice(message: types.Message, state: FSMContext) -> None:
    main_menu = [
        [
            types.KeyboardButton(text="Группа Младший программист")],[
            types.KeyboardButton(text="Группа Разработчик игр")],[
            types.KeyboardButton(text="Группа Web-дизайнер")],[
            types.KeyboardButton(text="Группа Программист")
            ],[types.KeyboardButton(text="Группа Блогер")],
            [types.KeyboardButton(text="Вернуться")]



        ]

    keyboard = types.ReplyKeyboardMarkup(keyboard=main_menu, resize_keyboard=True)
    await state.update_data(groupGAME_DEVELOPER=message.text)
    user_data = await state.get_data()
    groupGAME_DEVELOPER = user_data['groupGAME_DEVELOPER']
    global GROUP_LIST
    global GAME_DEVELOPER_GROUP
    GROUP_LIST.pop(3)
    GROUP_LIST.insert(3, groupGAME_DEVELOPER)
    GAME_DEVELOPER_GROUP=GROUP_LIST[3]
    await message.answer(f'Группа курса "Разработчик игр" изменена на {GAME_DEVELOPER_GROUP}', reply_markup=keyboard)
    await state.set_state(Form.end)

@router.message(F.text == "Группа Блогер")
async def setPrice(message: types.Message, state: FSMContext) -> None:
    if message.text == "Группа Блогер":
        await message.answer('Введите новую новую ссылку на группу для курса "Блогер" в формате (https://...)', reply_markup=types.ReplyKeyboardRemove())
        await state.set_state(Form.groupBLOGGER)

@router.message(Form.groupBLOGGER)
async def setPrice(message: types.Message, state: FSMContext) -> None:
    main_menu = [
        [
            types.KeyboardButton(text="Группа Младший программист")],[
            types.KeyboardButton(text="Группа Разработчик игр")],[
            types.KeyboardButton(text="Группа Web-дизайнер")],[
            types.KeyboardButton(text="Группа Программист")
            ],[types.KeyboardButton(text="Группа Блогер")],
            [types.KeyboardButton(text="Вернуться")]



        ]

    keyboard = types.ReplyKeyboardMarkup(keyboard=main_menu, resize_keyboard=True)
    await state.update_data(groupBLOGGER=message.text)
    user_data = await state.get_data()
    groupBLOGGER = user_data['groupBLOGGER']
    global GROUP_LIST
    global BLOGGER_GROUP
    GROUP_LIST.pop(4)
    GROUP_LIST.insert(4, groupBLOGGER)
    BLOGGER_GROUP=GROUP_LIST[4]
    await message.answer(f'Группа курса "Блогер" изменена на {BLOGGER_GROUP}', reply_markup=keyboard)
    await state.set_state(Form.end)

@router.message(Command("sendall"))
async def mess(message: types.Message, state: FSMContext):
    for user in joinedUsers:
        await bot.send_message(chat_id = user, text=message.text[message.text.find(' '):])

@router.message(Form.end)
async def setPrice(message: types.Message, state: FSMContext) -> None:
    print("success")

async def main():
    dp = Dispatcher(storage=MemoryStorage())
    dp.include_routers(router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())
if __name__ == "__main__":
    asyncio.run(main())
