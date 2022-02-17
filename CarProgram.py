import CarClass as cc

def main():
    car = cc.CarClass(2020,"Toyota")

    for count in range(5):
        car.accelerate()
        print(car.get_speed())
    for count in range(5):
        car.brake()
        print(car.get_speed())

main()