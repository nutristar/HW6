"""Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты:
 speed, color, name, is_police (булево). А также методы: go, stop, turn(direction),
 которые должны сообщать, что машина поехала, остановилась, повернула (куда).
 Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
  Добавьте в базовый класс метод show_speed, который должен показывать текущую
   скорость автомобиля. Для классов TownCar и WorkCar переопределите метод show_speed.
   При значении скорости свыше 60 (TownCar)
 и 40 (WorkCar) должно выводиться сообщение о превышении скорости."""

class Car:
    def __init__(self,speed,color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police=is_police

    def go(self):
        print(f"{self.name} машина поехала.")

    def stop(self):
        print(f"{self.name} машина остановилась")

    def direction(self, turn):
        a="налево"
        b="направо"
        print(f"{self.name} машина повернула { a  if turn ==0 else  b}.")

    def show_speed(self):
        return f"{self.name}  скорость автомобиля: {self.speed}"

class TownCar(Car):
    def show_speed(self):
        return f"{self.name} скорость автомобиля {self.speed} превышение скорости" if  self.speed> 60 else f"{self.name} скорость автомобиля {self.speed}"

audi100=TownCar(100,"silver", "q5", is_police=False)
print(audi100.show_speed())

class WorckCar(Car):
    def show_speed(self):
        return f"{self.name} скорость автомобиля {self.speed} превышение скорости" if  self.speed> 40 else f"{self.name} скорость автомобиля {self.speed}"


MAN= WorckCar(41, "red", "worck",is_police=False)
print(MAN.show_speed())
MAN.go()
MAN.direction(0)
print(MAN.show_speed())
MAN.direction(10)
MAN.stop()

class PoliceCar(Car):
    """ПОЛИЦЕЙСКИЙ АВТОМОБИЛЬ"""
    def __init__(self, speed,color, name, is_police=True):
        super().__init__(speed,color, name, is_police)

police_car = PoliceCar("Полицаи", "белый",80)
police_car.go()
print(police_car.show_speed())
police_car.direction(1)
police_car.stop()
print()

