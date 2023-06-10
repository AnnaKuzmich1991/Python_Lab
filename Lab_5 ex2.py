#класс House с пятью магическими методами

class House:
    id = 0
    
    def __init__(self, num_flat, square, floor, num_rooms, street, building_type, lifetime):
        self.__num_flat = num_flat
        self.square = square
        self.floor = floor
        self.num_rooms = num_rooms
        self.street = street
        self.building_type = building_type
        self.lifetime = lifetime
        House.id += 1
        
    def __str__(self):
        return f"{self.__num_flat} квартира, {self.num_rooms} комнат, {self.square} кв. м, {self.floor} этаж, " \
               f"ул. {self.street}, {self.building_type}, {self.lifetime} г. постройки"

    def __repr__(self):
        return f"House({self.__num_flat}, {self.square}, {self.floor}, {self.num_rooms}, '{self.street}', " \
               f"'{self.building_type}', {self.lifetime})"
    
    def __eq__(self, other):
        return isinstance(other, House) and self.__num_flat == other.__num_flat and self.square == other.square \
               and self.floor == other.floor and self.num_rooms == other.num_rooms and self.street == other.street \
               and self.building_type == other.building_type and self.lifetime == other.lifetime
    
    def __hash__(self):
        return hash((self.__num_flat, self.square, self.floor, self.num_rooms, self.street,
                     self.building_type, self.lifetime))
    
    @classmethod
    def id_increase(cls, num_houses):
        cls.id += num_houses
    
    def get_num_flat(self):
        return self.__num_flat
    
    def set_num_flat(self, num_flat):
        if num_flat < 1:
            print("Ошибка! Номер квартиры должен быть больше 0")
        else:
            self.__num_flat = num_flat
