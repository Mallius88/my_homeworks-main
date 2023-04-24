# Задача 1.1.

# Есть строка с перечислением песен

my_favorite_songs = 'Waste a Moment, Staying\' Alive, A Sorta Fairytale, Start Me Up, New Salvation'

# Выведите на консоль с помощью индексации строки, последовательно: первый трек, последний, второй, второй с конца
# Нельзя переопределять my_favorite_songs и запятая не должна выводиться.


# Решение:

print(my_favorite_songs.split(',')[0], my_favorite_songs.split(',')[-1], my_favorite_songs.split(',')[1],
      my_favorite_songs.split(',')[-2])

# Отлично, ну только единственное что, можно немного сократить запись и написать списковое включение

print([my_favorite_songs.split(', ')[i] for i in [0, -1, 1, -2]])
