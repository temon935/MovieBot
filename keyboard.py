from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton

btnPrp = InlineKeyboardButton('Что ты умеешь?', callback_data='2')
btnStart = InlineKeyboardButton('Новый поиск', callback_data='1')
btnAdventure = InlineKeyboardButton('Приключения', callback_data='Adventure')
btnDrama = InlineKeyboardButton('Драма', callback_data='Drama')
btnFantasy = InlineKeyboardButton('Фэнтази', callback_data='Fantasy')
btnBiography = InlineKeyboardButton('Биография', callback_data='Biography')
btnRomance = InlineKeyboardButton('Романтика', callback_data='Romance')
btnHistory = InlineKeyboardButton('История', callback_data='History')
btnCrime = InlineKeyboardButton('Криминал', callback_data='Crime')
btnMystery = InlineKeyboardButton('Мистика', callback_data='Mystery')
btnHorror = InlineKeyboardButton('Ужасы', callback_data='Horror')
btnAction = InlineKeyboardButton('Экшен', callback_data='Action')
btnComedy = InlineKeyboardButton('Комедия', callback_data='Comedy')
btnFamily = InlineKeyboardButton('Семейный', callback_data='Family')
btnThriller = InlineKeyboardButton('Триллер', callback_data='Thriller')
btnWestern = InlineKeyboardButton('Вестерн', callback_data='Western')
btnSci_Fi = InlineKeyboardButton('Фантастика', callback_data='Sci-Fi')
btnClear = InlineKeyboardButton('Очистить', callback_data='чистка')
btnNext = InlineKeyboardButton('Далее', callback_data='далее')
greet_kb = InlineKeyboardMarkup(resize_keyboard=True, row_width=2).add(btnStart, btnPrp)
search_kb = InlineKeyboardMarkup(resize_keyboard=True, row_width=3).add(
    btnAdventure,
    btnDrama,
    btnFantasy,
    btnBiography,
    btnRomance,
    btnHistory,
    btnCrime,
    btnMystery,
    btnHorror,
    btnAction,
    btnComedy,
    btnFamily,
    btnThriller,
    btnWestern,
    btnSci_Fi)
search_kb.add(btnClear)
search_kb.add(btnNext)

btnS = InlineKeyboardButton('Следующий', callback_data='следующий')
pagination_kb = InlineKeyboardMarkup(resize_keyboard=True, row_width=2).add(btnS, btnStart)