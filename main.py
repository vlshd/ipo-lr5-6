def a(input_file, output_file): # функция
    with open(input_file, 'r', encoding='utf-8') as file: # открывает файл
        text = file.read().lower()  # cчитываем содержимое файла и приводим к нижнему регистру
        words = text.split()  # разделяем текст на слова
        words = [word.strip('.,!;()[]') for word in words]  # убираем знаки препинания
        a_words = set(words)  # находим уникальные слова

    with open(output_file, 'w', encoding='utf-8') as file: # открывает файл
        for word in sorted(a_words):  # записываем уникальные слова в файл, отсортированные по алфавиту
            file.write(word + '\n')

# использование функции
a('text.txt', 'output.txt')