import InsectClass as i


def main():
    fly = i.Insect(2,4)
    fly.flight_length()
    print("The insect can fly up to", fly.get_miles(), "miles")

main()