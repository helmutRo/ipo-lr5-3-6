file = open("text.txt", 'r') #открывается файл 
x = file.read().split() #читает текст из файла и разделяет текст на слова
s = set(x)#ищет уникальные слова
with open("output.txt", 'w+') as file: #открывает файл с возможностью изменения
    for x in s:
        file.write(x + ' ') #в output.txt записывается изменённая строка 