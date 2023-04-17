# Задача 2.4.

# Пункт A.
# Напишите функцию, которая удаляет все восклицательные знаки из заданной строк.
# Например,
# foo("Hi! Hello!") -> "Hi Hello"
# foo("") -> ""
# foo("Oh, no!!!") -> "Oh, no"

# Решение А:
def remove_exclamation_marks(s):
    answer = s.replace('!', '')
    print(answer)


remove_exclamation_marks('Hi! Hello!')

# Пункт B.
# Удалите восклицательный знак из конца строки. 
# remove("Hi!") == "Hi"
# remove("Hi!!!") == "Hi!!"
# remove("!Hi") == "!Hi"


def remove_last_em(s):
    if s[-1] == '!':
        s = s[0:-1]
    print(s)


remove_last_em("Hi!!!")

# Дополнительно

# Пункт С.
# Удалите слова из предложения, если они содержат ровно один восклицательный знак.
# Слова разделены одним пробелом.
# Например,
# remove("Hi!") === ""
# remove("Hi! Hi!") === ""
# remove("Hi! Hi! Hi!") === ""
# remove("Hi Hi! Hi!") === "Hi"
# remove("Hi! !Hi Hi!") === ""
# remove("Hi! Hi!! Hi!") === "Hi!!"
# remove("Hi! !Hi! Hi!") === "!Hi!"


# Решение С:
def remove_word_with_one_em(s):
    answer = []
    for i in s.split():
        if i.count('!') == 1:
            continue
        else:
            answer.append(i)
    print(*answer)
