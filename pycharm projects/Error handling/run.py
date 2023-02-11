class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model
        self.name = 'camry'

    def __repr__(self):
        return f'<<{self.name}: {self.make}{self.model}>>'


class Garage:
    def __init__(self):
        self.cars = []

    def __len__(self):
        return len(self.cars)

    def __getitem__(self, i):
        return self.cars[i]

    def add_car(self, car):
        if not isinstance(car, Car):
            raise TypeError(f'You try adding `{car.__class__.__name__}` but you can only add `Car` objects')
        self.cars.append(car)
        print(f'{car} added sucessfully!')


camry = Car('fiesta', 'focus')
venza = Car('toyota', '2020')
ford = Garage()
ford.add_car(camry)
ford.add_car(venza)
print(len(ford))
print(ford[1])


