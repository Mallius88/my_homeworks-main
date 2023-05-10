# Задача 2.3.

# Напишите функцию, которая принимает цифры от 0 до 9 и возвращает значение прописью.
# Например,
# switch_it_up(1) -> 'One'
# switch_it_up(3) -> 'Three'
# switch_it_up(10000) -> None
# Использовать условный оператор if-elif-else нельзя!

# Решение:

def switch_it_up(number:int):
    match number:
        case 0:
            print('Null')
        case 1:
            print('One')
        case 2:
            print('Two')
        case 3:
            print('Three')
        case 4:
            print('Four')
        case 5:
            print('Five')
        case 6:
            print('Six')
        case 7:
            print('Seven')
        case 8:
            print('Eight')
        case 9:
            print('Nine')
        case _:
            print('None')
            
# Ну конечно здорово что инструкцию с case использовали, но все таки можно использовать простые типы данных и записать это решение лаконичнее)
def switch_it_up(number):
    return {0: 'Zero', 1: 'One', 2: 'Two', 3: 'Three', 4: 'Four', 5: 'Five',
            6: 'Six', 7: 'Seven', 8: 'Eight', 9: 'Nine'}.get(number)
