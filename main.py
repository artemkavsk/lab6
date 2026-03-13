class Building:
    className = "Здание"
    objectsCount = 0

    def __init__(self, area, price_per_meter, residents):
        self._area = area
        self._price = price_per_meter
        self._residents = residents
        Building.objectsCount += 1

    def get_area(self):
        return self._area

    def set_area(self, area):
        if area > 0:
            self._area = area
        else:
            self._area = 1

    def info(self):
        print(f"Тип: {Building.className}")
        print(f"Площадь: {self._area} кв.м.")
        print(f"Стоимость за кв.м.: {self._price}")
        print(f"Проживающих: {self._residents}")


    def total_cost(self):
        cost = self._area * self._price
        print(f"Общая стоимость: {cost}")
        return cost


class VillageHouse(Building):
    className = "Деревенский дом"

    def __init__(self, area, price_per_meter, residents, land_area):
        super().__init__(area, price_per_meter, residents)
        self.land_area = land_area   # уникальное поле

    def info(self):
        super().info()
        print(f"Тип: {VillageHouse.className}")
        print(f"Площадь участка: {self.land_area} соток")


    def cost_per_resident(self):
        cost = self._area * self._price
        result = cost / self._residents
        print(f"Стоимость на человека: {result}")


class ApartmentHouse(Building):
    className = "Многоквартирный дом"

    def __init__(self, area, price_per_meter, residents, floors):
        super().__init__(area, price_per_meter, residents)
        self.floors = floors   # уникальное поле

    def info(self):
        super().info()
        print(f"Тип: {ApartmentHouse.className}")
        print(f"Количество этажей: {self.floors}")

    
    def cost_per_resident(self):
        cost = self._area * self._price
        result = cost / self._residents
        print(f"Стоимость на человека: {result}")


b = Building(120, 50000, 4)
b.info()
b.total_cost()

print()

v = VillageHouse(100, 40000, 3, 12)
v.info()
v.total_cost()
v.cost_per_resident()

print()

a = ApartmentHouse(500, 70000, 50, 9)
a.info()
a.total_cost()
a.cost_per_resident()

print(f"\nКоличество объектов: {Building.objectsCount}")