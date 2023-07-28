from car import Car
from account import Account

if __name__ == "__main__":
    print("Hola Mundo")
    car = Car("AMD446", Account("Esteban","OLS123"))
    print(vars(car))
    print(vars(car.driver))