import os
import time
import csv
import Brain
import config
import logging
import asyncio
import random
import keyboard as kb
from aiogram import Bot, Dispatcher, executor, types


# задаем уровень логов
logging.basicConfig(level=logging.INFO)

# инициализируем бота
bot = Bot(token=config.API_TOKEN)
dp = Dispatcher(bot)

bot_property = Brain.bot_property()
bot_search = Brain.search()
country_list = ['USA', 'Australia', 'UK', 'France', 'Russia']
search_metrics = []
movies = []
showed_results = []


@dp.message_handler(commands=['start'])
async def any_msg(message: types.Message):
    await bot.send_message(message.chat.id, "Чего изволите?", reply_markup=kb.greet_kb)


@dp.callback_query_handler(lambda c: c.data == '1' or c.data == '2')
async def callback_btn1(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    if callback_query.data == '1':
        showed_results.clear()
        movies.clear()
        search_metrics.clear()
        await bot.send_message(callback_query.from_user.id, 'Выберите жанры', reply_markup=kb.search_kb)

    elif callback_query.data == '2':
        await bot.send_message(callback_query.from_user.id, bot_property, reply_markup=kb.greet_kb)


@dp.callback_query_handler(lambda c: c.data in ('Adventure', 'Drama', 'Fantasy', 'Biography', 'Romance', 'History',
                                                'Crime', 'Mystery', 'Horror', 'Action', 'Comedy', 'Family', 'Thriller',
                                                'Western', 'Sci-Fi'))
async def callback_btn2(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    if callback_query.data not in search_metrics:
        search_metrics.append(callback_query.data)
        resp = f'Добавил {callback_query.data}.\nДля продолжения нажмите "Далее"'
        await bot.send_message(callback_query.from_user.id, resp)
    else:
        await bot.send_message(callback_query.from_user.id, 'Этот жанр уже добавлен')


@dp.callback_query_handler(lambda c: c.data == 'чистка')
async def callback_btn3(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    search_metrics.clear()
    await bot.send_message(callback_query.from_user.id, 'Список жанров очищен')


@dp.callback_query_handler(lambda c: c.data == 'далее')
async def callback_btn4(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    if len(search_metrics) == 0:
        await bot.send_message(callback_query.from_user.id, 'Выберите жанры', reply_markup=kb.search_kb)
    else:
        await bot.send_message(callback_query.from_user.id, 'Загрузка...')
        await show_results(search_metrics, callback_query.from_user.id)


@dp.callback_query_handler(lambda c: c.data == 'следующий')
async def callback_btn5(callback_query: types.CallbackQuery):
    await bot.answer_callback_query(callback_query.id)
    await show(callback_query.from_user.id)


async def show_results(metrics, callback_query):
    with open("IMDb_movies.csv", encoding='utf-8') as r_file:
        # Создаем объект reader, указываем символ-разделитель ","
        file_reader = csv.DictReader(r_file, delimiter=",")
        for row in file_reader:
            try:
                s = int(row['year'])
            except ValueError:
                pass
            for x in metrics:
                if s > 1995 and float(row['avg_vote']) > 7.0 and x in row['genre'] and row['country'] in country_list:
                    movies.append({'Название': row['original_title'],
                                   'ID': row['imdb_title_id'],
                                   'Описание': row['description'],
                                   'Рейтинг': row['avg_vote'],
                                   'Жанр': row['genre'],
                                   'Страна': row['country'],
                                   'Год': s,
                                   'Ссылка': f'https://www.imdb.com/title/{row["imdb_title_id"]}/?ref_=tt_mv_close'})
    print(len(movies))
    await show(callback_query)


async def show(callback_query):
    rep = 0
    while rep != 1:
        num = random.randint(1, len(movies))
        if num in showed_results:
            rep = 0
        else:
            showed_results.append(num)
            answer = f"Название: {movies[num]['Название']}\nОписание:\n{movies[num]['Описание']}\nРейтинг: {movies[num]['Рейтинг']}\n" \
                     f"Жанр: {movies[num]['Жанр']}\nСтрана: {movies[num]['Страна']}\nГод: {movies[num]['Год']}"
            answer2 = f"{movies[num]['Ссылка']}"
            return await bot.send_message(callback_query, answer), await bot.send_photo(callback_query, answer2,
                                                                                        reply_markup=kb.pagination_kb)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)