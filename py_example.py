car_1 = input("Введіть марку автомобіля 1 ")
car_2 = input("Введіть марку автомобіля 2 ")
car_3 = input("Введіть марку автомобіля 3 ")


class Cars:
    # your code goes here
    list_of_cars = []

    def __init__(self, name):
        self.name = name
        """Cars.list_of_cars.append(name)"""

    def add_new_car(new_car):
        Cars.list_of_cars.append(new_car)

        return Cars.list_of_cars


newCar1 = Cars(car_1)
Cars.add_new_car(newCar1)
newCar2 = Cars(car_2)
Cars.add_new_car(newCar2)
newCar3 = Cars(car_3)
Cars.add_new_car(newCar3)


rez = "та".join(Cars.list_of_cars)


print("Список авто: {}".format(rez))
