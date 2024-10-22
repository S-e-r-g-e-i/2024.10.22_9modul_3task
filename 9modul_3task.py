# Домашнее задание по теме "Генераторные сборки"

first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

# first_result_ = [len(x) - len(y) for x, y in zip(first, second) if len(x) - len(y) != 0]
# print(first_result_) #  создал для себя, списковая сборка

first_result = (len(x) - len(y) for x, y in zip(first, second) if len(x) - len(y) != 0)
print(first_result)
second_result = (len(first[x]) == len(second[x]) for x in range(len(first)))


print(list(first_result))
print(list(second_result))
# print(list(first_result)) # второй раз генераторная сборка не работает
# print(list(second_result)) # второй раз генераторная сборка не работает

