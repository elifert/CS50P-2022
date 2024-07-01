def main():
    fuel_percentage = round(fuelgauge())
    print(f"{fuel_percentage}%")

def fuelgauge():
    while True:
        try:
            #map is used to apply a specified function to all items in an input iterable
            #(e.g., a list) and return an iterator of the results.
            x, y = map(int, input("Fraction: ").split('/'))
            if x<=y:
                if (x/y)*100 >= 99:
                    print("F")
                elif (x/y)*100 <= 1:
                    print("E")
                else:
                    return (x/y)*100
            else:
                pass
        except(ValueError, ZeroDivisionError):
            pass

main()