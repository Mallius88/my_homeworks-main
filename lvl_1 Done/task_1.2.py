# Задача 1.2.

# Пункт A. 
# Приведем плейлист песен в виде списка списков
# Список my_favorite_songs содержит список названий и длительности каждого трека
# Выведите общее время звучания трех случайных песен в формате
# Три песни звучат ХХХ минут

my_favorite_songs = [
    ['Waste a Moment', 3.03],
    ['New Salvation', 4.02],
    ['Staying\' Alive', 3.40],
    ['Out of Touch', 3.03],
    ['A Sorta Fairytale', 5.28],
    ['Easy', 4.15],
    ['Beautiful Day', 4.04],
    ['Nowhere to Run', 2.58],
    ['In This World', 4.02],
]

# Решение Пункта А и С и D:
from random import randint
import datetime
temp_len = len(my_favorite_songs) - 1
first = my_favorite_songs[(randint(0, temp_len))][1]
second = my_favorite_songs[(randint(0, temp_len))][1]
third = my_favorite_songs[(randint(0, temp_len))][1]
answer = first + second + third
print(f'Три песни звучат {answer} минут')
# Решение D:
answer_sec = answer * 60
first_answer_list = str(datetime.timedelta(seconds = answer_sec))
print(f'Три песни звучат {first_answer_list}')




# Пункт B. 
# Есть словарь песен 
# Распечатайте общее время звучания трех случайных песен
# Вывод: Три песни звучат ХХХ минут.

my_favorite_songs_dict = {
    'Waste a Moment': 3.03,
    'New Salvation': 4.02,
    'Staying\' Alive': 3.40,
    'Out of Touch': 3.03,
    'A Sorta Fairytale': 5.28,
    'Easy': 4.15,
    'Beautiful Day': 4.04,
    'Nowhere to Run': 2.58,
    'In This World': 4.02,
}

# Решение Пункта В и С и D:
temp_len_dict = len(my_favorite_songs_dict) - 1
first_song = my_favorite_songs_dict[list(my_favorite_songs_dict.keys())[(randint(0, temp_len_dict))]]
second_song = my_favorite_songs_dict[list(my_favorite_songs_dict.keys())[(randint(0, temp_len_dict))]]
third_song = my_favorite_songs_dict[list(my_favorite_songs_dict.keys())[(randint(0, temp_len_dict))]]
answer_dict = first_song + second_song + third_song
print(f'Три песни звучат {answer_dict} минут')
answer_dict_sec = answer_dict * 60
# Решение D:
second_answer_dict = str(datetime.timedelta(seconds = answer_dict_sec))
print(f'Три песни звучат {second_answer_dict}')


# Дополнительно для пунктов A и B
# Пункт C.
# Сгенерируйте случайные песни с помощью модуля random
# import random

# Дополнительно 
# Пункт D.
# Переведите минуты и секунды в формат времени. Используйте модуль datetime 





