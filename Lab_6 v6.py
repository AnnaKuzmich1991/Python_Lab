import re

def main():
    # Открываем файл F1
    with open("F1.txt", "w") as f1:
        # Записываем информацию в файл
        f1.write("Пример строки 1\n")
        f1.write("Это строка 2\n")
        f1.write("Еще одна строка, номер 3\n")
        f1.write("Строка 4\n")
        f1.write("И тут строка 5\n")
        f1.write("Это строка номер 6\n")
        f1.write("А тут строка 7\n")
        f1.write("И это уже строка 8\n")
        f1.write("Номер 9\n")
        f1.write("И наконец, строка 10\n")

    # Открываем файлы F1 и F2
    with open("F1.txt", "r") as f1, open("F2.txt", "w") as f2:
        # Читаем все строки из файла F1
        lines = f1.readlines()
        # Получаем строки от 5 до 8 и записываем их в файл F2
        for line in lines[4:8]:
            f2.write(line)

    # Открываем файл F2
    with open("F2.txt", "r") as f2:
        # Читаем все строки из файла F2
        lines = f2.readlines()
        # Преобразуем все строки в одну строку
        text = "".join(lines)
        # Используем регулярное выражение для подсчета количества согласных букв
        consonants = re.findall(r'[бвгджзйклмнпрстфхцчшщBCDFGHJKLMNPQRSTVWXYZ]', text)
        # Выводим количество найденных согласных букв
        print("Количество согласных букв в файле F2: ", len(consonants))
