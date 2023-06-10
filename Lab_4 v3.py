#Создайте класс и поля соответствующему вашему варианту (поля статические и динамические). 
#Создайте три метода (класса, объекта и статический). 
#Выберете поле или метод для реализации инкапсуляции. 
#Пропишите запись и считывание (get, set) инкапсулированных полей. 
class House:
    id = 0 # Статическое поле
    def __init__(self, num_flat, square, floor, num_rooms, street, building_type, lifetime):
        self.__num_flat = num_flat # Инкапсулируемое поле
        self.square = square # Динамическое поле
        self.floor = floor # Динамическое поле
        self.num_rooms = num_rooms # Динамическое поле
        self.street = street # Динамическое поле
        self.building_type = building_type # Динамическое поле
        self.lifetime = lifetime # Динамическое поле
        House.id += 1
    
    @classmethod #метод класса id_increase, который увеличивает статическое поле id на заданное число
    def id_increase(cls, num_houses): 
        cls.id += num_houses
    
    def get_num_flat(self): #метод объекта get_num_flat который возвращает значение инкапсулированного поля __num_flat
        return self.__num_flat
    
    def set_num_flat(self, num_flat): #метод объекта set_num_flat, который устанавливает новое значение для инкапсулированного поля __num_flat
        if num_flat < 1:
            print("Ошибка! Номер квартиры должен быть больше 0")
        else:
            self.__num_flat = num_flat
    
    @staticmethod #это декоратор для метода, который позволяет определить метод как статический (т.е. не связанный с объектом класса)
    def calculate_age(lifetime): #статический метод, который принимает дату постройки здания и вычисляет возраст здания на текущий год, который закодирован в методе (2023)
        return 2023 - lifetime
    
    def __str__(self): #метод класса, который возвращает строковое представление объекта
        return f"{self.__num_flat} квартира, {self.num_rooms} комнат, {self.square} кв. м, {self.floor} этаж, " \
               f"ул. {self.street}, {self.building_type}, {self.lifetime} г. постройки"


# Создаем список объектов
houses = [ House(1, 45, 5, 2, "Ленина", "Кирпичный", 1987),
           House(2, 65, 2, 3, "Красная", "Панельный", 1994),
           House(3, 36, 4, 1, "Советская", "Кирпичный", 2000),
           House(4, 78, 10, 4, "Победы", "Монолитный", 2010),
           House(5, 60, 8, 3, "Ленина", "Кирпичный", 1979) ]

# список квартир, имеющих заданное число комнат
def find_flat_by_room(num_rooms):
    flat_list = []
    for house in houses:
        if house.num_rooms == num_rooms:
            flat_list.append(house)
    return flat_list

# список квартир, имеющих заданное число комнат и расположенных на этаже, который находится в заданном промежутке
def find_flat_by_room_and_floor(num_rooms, floor_range):
    flat_list = []
    min_floor, max_floor = floor_range
    for house in houses:
        if house.num_rooms == num_rooms and min_floor <= house.floor <= max_floor:
            flat_list.append(house)
    return flat_list

# Пример использования
print("Список квартир с 3 комнатами")
for house in find_flat_by_room(3):
    print(house)

print("\nСписок квартир с 2 комнатами и этаж от 2 до 5")
for house in find_flat_by_room_and_floor(2, (2, 5)):
    print(house)
