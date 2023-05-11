# задаем исходные таблицы
table1 = [[1, 2, 3], 
          [4, 5, 6], 
          [7, 8, 9]]

table2 = [[9, 8, 7], 
          [6, 5, 4], 
          [3, 2, 1]]

# задаем размер итоговой таблицы
size = len(table1)

# создаем пустую таблицу
result = [[0 for i in range(size)] for j in range(size)]

# проходим по каждому элементу искомой таблицы и считаем сумму элементов на соответствующих позициях
for i in range(size):
  for j in range(size):
    result[i][j] = table1[i][j] + table2[i][j]

# выводим итоговую таблицу
print(result)
