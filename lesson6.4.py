class Car:

    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f' {self.name} поехала'

    def stop(self):
        return f' {self.name} остановилась'

    def turn_right(self):
        return f' {self.name} повернула направо'

    def turn_left(self):
        return f' {self.name} повернула налево'

    def show_speed(self):
        return f'Скорость {self.name} составляет {self.speed}'


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Скорость   {self.name} составляет {self.speed}')

        if self.speed > 40:
            return f'Скорость  {self.name} выше допустимой'
        else:
            return f'Скорость  {self.name} нормальная'


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        print(f'Скорость {self.name} составляет {self.speed}')

        if self.speed > 60:
            return f'Скорость {self.name} выше допустимой'


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            return f'{self.name} полицейский автомобиль'
        else:
            return f'{self.name} не полицейский автомобиль'


bmw = SportCar(110, 'Red', 'BMW', False)
lada = TownCar(30, 'White', 'LADA', False)
kia = WorkCar(70, 'Black', 'Lada', True)
ford = PoliceCar(110, 'Blue', 'Ford', True)
print(kia.turn_left())
print(f'Когда {lada.turn_right()}, то {bmw.stop()}')
print(f'{kia.go()} со скоростью {kia.show_speed()}')
print(f'{kia.name} is {kia.color}')
print(f'{bmw.name} полицейский автомобиль? {bmw.is_police}')
print(bmw.show_speed())
print(lada.show_speed())
print(ford.police())
print(ford.show_speed())
