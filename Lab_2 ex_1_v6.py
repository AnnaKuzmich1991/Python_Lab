# Найдем сумму номеров минимального и максимального элементов
def min_max_sum(array):
    # находим минимальный и максимальный элементы в массиве
    min_element = min(array)
    max_element = max(array)

    # находим индексы минимального и максимального элементов в массиве
    min_index = array.index(min_element)
    max_index = array.index(max_element)

    # возвращаем сумму индексов минимального и максимального элементов
    return min_index + max_index

# определяем, можно ли из данных чисел образовать подмножество, сумма элементов которого делится на n без остатка
def is_divisible(n, array):
    # вычисляем сумму всех элементов массива
    array_sum = sum(array)

    # если сумма элементов делится на n без остатка, возвращаем True
    if array_sum % n == 0:
        return True

    # иначе перебираем все возможные подмножества и проверяем, делится ли их сумма на n без остатка
    for i in range(len(array)):
        for j in range(i+1, len(array)+1):
            subset = array[i:j]
            if sum(subset) % n == 0:
                return True
    
    # если не найдено подходящего подмножества, возвращаем False
    return False

# ищем любое из подходящих подмножеств
def find_subset(n, array):
    # если сумма всех элементов делится на n без остатка, возвращаем весь массив
    if sum(array) % n == 0:
        return array

    # иначе перебираем все возможные подмножества и проверяем, делится ли их сумма на n без остатка
    for i in range(len(array)):
        for j in range(i+1, len(array)+1):
            subset = array[i:j]
            if sum(subset) % n == 0:
                return subset
    
    # если не найдено подходящего подмножества, возвращаем None
    return None
