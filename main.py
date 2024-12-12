with open("text.txt", "r") as myfile: #открыть файл для чтения
    text = myfile.read() #чтение текстового файла
unique = [] #создание пустого списка для уникальных слов
words = text.split() #разделяем на слова
for word in words: #проход по каждому слову
    if word not in unique: #если нет повтор слова
        unique.append(word) #добавление

with open("output.txt", "w") as file: #открывать файл output.txt
    for word in unique: #разделяем на слова
        file.write(word + ' ') #записываем
