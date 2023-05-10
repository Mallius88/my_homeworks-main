# Задача 2.2. 

# Напишите функцию, которая возвращает номер квартал по номеру месяца
# Например: 
# месяц 2 (февраль) является частью первого квартала; 
# месяц 6 (июнь) является частью второго квартала; 
# месяц 11 (ноябрь) является частью четвертого квартала.

def quarter_of(month):
    data = ["январь", "февраль", "март", "апрель", "мaй", "июнь", "июль",
              "август", "сентябрь", "октябрь", "ноябрь", "декабрь"]
    if 1 <= month <= 3:
        print(f'месяц {month} ({data[month-1]}) является частью первого квартала')
    elif 4 <= month <= 6:
        print(f'месяц {month} ({data[month - 1]}) является частью второго квартала')
    elif 7 <= month <= 9:
        print(f'месяц {month} ({data[month - 1]}) является частью третьего квартала')
    elif 7 <= month <= 9:
        print(f'месяц {month} ({data[month - 1]}) является частью четвертого квартала')
    else:
        print('Некорректный ввод, используйте диапазон 1 - 12')



quarter_of(1)

# Да, можно! Но лучше покороче
def quarter_of(month):
    q = {1: (1,3), 2:(4,6), 3:(7,9), 4:(10,12)}
    return [k for k,v in q.items() if v[0] <= month <= v[1]][0]
