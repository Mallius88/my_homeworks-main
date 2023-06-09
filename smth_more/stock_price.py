# Дан массив целых чисел, где price[i], цена каждой акции на i-ый день

# цены: [7, 1, 5, 3,  6 ]
# дни:   1й 2й 3й 4й, 5й

# Найдите максимальную прибыль, которой вы можете достичь, если
#   - в каждый из дней вы можете принять решение о покупке и/или продаже акции;
#   - в любой момент вы можете владеть не более чем одной акцией;
#   - тем не менее, вы можете купить акцию, а затем немедленно продать в тот же день.

# Примеры:
# Ввод: prices = [7, 1, 5, 3, 6]
# Вывод: 7
# Объяснение: 
# Купили в день 2 (цена = 1) и продали в день 3 (цена = 5), прибыль = 5-1 = 4.
# Затем купили в день 4 (цена = 3) и продали в день 5 (цена = 6), прибыль = 6-3 = 3.
# Общая прибыль равна 4 + 3 = 7.

# Ввод: prices = [1, 2, 3, 4, 5]
# Вывод: 4
# Объяснение: 
# Купили в день 1 (цена = 1) и продали в день 5 (цена = 5), прибыль = 5-1 = 4.
# Общая прибыль равна 4.

# Ввод: prices = [7, 6, 4, 3, 1]
# Вывод: 0
# Объяснение: 
# Невозможно получить прибыль, следовательно, не покупаем акции, чтобы достичь прибыли 0.
# Общая прибыль равна 0.
