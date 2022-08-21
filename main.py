# Задание 1
import string

def task1():
    with open('task1_text1.txt', 'w+') as file1:
        file1.write('Киев - столица и крупнейший город Украины, город со специальным статусом. Расположен на реке Днепр, является центром Киевской агломерации. Отдельная административно-территориальная единица Украины; культурный, политический, социально-экономический, транспортный, научный и религиозный центр страны.')
    with open('task1_text2.txt', 'w+') as file2:
        file2.write('Харьков - второй по численности населения город Украины, важный промышленный и научный центр страны, центр Харьковской области, Харьковского района и Харьковской городской общины. С 6 марта 2022 Город-герой Украины.')
    with open('task1_text1.txt') as file1:
        # удаляем знаки препинания
        text1 = file1.read().translate(str.maketrans('', '', string.punctuation))
        print(text1)
        list_file1 = set(text1.split())
        with open('task1_text2.txt') as file2:
            # удаляем знаки препинания
            text2 = file2.read().translate(str.maketrans('', '', string.punctuation))
            print(text2)
            list_file2 = set(text2.split())
    # проверяем совпадения
    intersection = list_file1.intersection(list_file2)

    if len(intersection) > 0:
        print('Совпадения в тексте:', intersection)
    else:
        print('Совпадения не найдены')


print('Задание 1.', end='\n\n')
task1()
print()


# Задание 2

def task2():
    with open('task1_text2.txt') as file2:
        list = [i for i in file2.read()]
        # text = file2.read().lower()
        # print(len(list))
        # print(list)

    # определяем количество строк
    count_line = sum(1 for line in open('task1_text2.txt', 'r'))

    vowels = set('аяуюоеёэиы')
    nums = set('123456790')
    symbols = set(',. ?!-:;\'"(){}[]@#$%^&*_+<>/|')
    # print(symbols)

    count_vowels = sum(1 for i in list if i in vowels)
    # print(count_vowels)
    count_num = sum(1 for i in list if i in nums)
    # print(count_num)
    count_consonants = sum(1 for i in list if i not in vowels and i not in nums and i not in symbols)
    # print(count_consonants)
    lines = [line for line in open('task3_text1.txt', 'r')]
    print(f'Текст файла:\n{lines}')
    print(f'Всего символов в тексте: {len(list)}')
    print(f'Всего строк в тексте: {count_line}')
    print(f'Всего цифр в тексте: {count_num}')
    print(f'Всего согласных в тексте: {count_consonants}')
    print(f'Всего гласных в тексте: {count_vowels}')


print('Задание 2.', end='\n\n')
task2()
print()


# Задание 3

def task3():
    # Файл - task3_text1.txt задан. определяем все строки в файле
    lines = [line for line in open('task3_text1.txt', 'r')]
    print(f'Строки исходного файла:\n{lines}\n')
    # удаляем последнюю
    lines = lines[:-1]
    # print(lines)
    # Файл - task3_text2.txt создаем и записываем данные без последней строки
    with open('task3_text2.txt', 'w+') as file:
        file.writelines(lines)
    with open('task3_text2.txt', 'r') as file:
        print('Проверяем данные в новом файле: ')
        print(file.read())


print('Задание 3.', end='\n\n')
task3()
print()


# Задание 4

def task4():
    # текст по умолчанию взял из 3 задания
    lines = [line for line in open('task3_text1.txt', 'r')]
    print(f'Строки в файле:\n {lines}')
    # определяем длины каждой строки в файле
    lines_lenght = [len(line) for line in open('task3_text1.txt', 'r')]
    line = [line for line in open('task3_text1.txt', 'r') if len(line) == max(lines_lenght)]
    print(f'Длины всех строк в файле: {lines_lenght}')
    print(f'Максимальная длина строки в файле: {max(lines_lenght)}\n'
          f'Строка: {line}')


print('Задание 4.', end='\n\n')
task4()
print()


# Задание 5

def task5():
    # текст по умолчанию взял из 3 задания
    with open('task3_text1.txt', 'r') as file:
        list_word = file.read().lower().split()
    # список из полученного текста
    print(list_word, end='\n\n')
    word = input('Введите слово: ')
    count_word = sum(1 for i in list_word if i == word)
    if count_word > 0:
        print(f'Слово "{word}" встречается в тексте файла - {count_word} раз(а)')
    else:
        print(f'Слово "{word}" в тексте файла не найдено')


print('Задание 5.', end='\n\n')
task5()
print()

# Задание 6

def task6():
    with open('task5_text1.txt', 'w') as file:
        file.write('London is the capital of Great Britain, its political, economic and cultural centre. '
                   'It\'s one of the largest cities in the world. Its population is more than million people. '
                   'London is situated on the river Thames. The city is very old and beautiful. '
                   'It was founded more than two thousand years ago. '
                   'Traditionally London is divided into several parts: the City, the West End, the East End and Westminster. '
                   'The City is the oldest part of London, its financial and business centre. The heart of the City is the Stock Exchange. '
                   'Westminster is the most important part of the capital. '
                   'It\'s the administrative centre. '
                   'The Houses of Parliament, the seat of the British Government, are there. '
                   'It\'s a very beautiful building with two towers and a very big clock called Big Ben. '
                   'Big Ben is really the bell which strikes every quarter of an hour. Opposite the Houses of Parliament is Westminster Abbey. '
                   'It\'s a very beautiful church built over 900 years ago. The tombs of many great statesmen, scientists and writers are there.')
    with open('task5_text1.txt', 'r') as file:
        text = file.read()
        # print(text)
        # Вводил исходное слово - London, слово на замену - Киев
    word_origin = input('Введите слово которое надо заменить: ')
    word_replace = input('Введите слово на которое произвести замену: ')
    new_text = text.replace(word_origin, word_replace)
    print(new_text)
    with open('task5_text1.txt', 'w') as file:
        file.write(new_text)

print('Задание 6.', end='\n\n')
task6()






