def main():
    smth = input()
    x, y, z = smth.split(" ")
    x = float(x)
    z = float(z)
    sayi = interpreter(x, y, z)
    print(sayi)

def interpreter(x, y, z):
    try:
        return {
            '+' : x + z,
            '-' : x - z,
            '*' : x * z,
            '/' : x / z if z!=0 else print("error division by 0", None)
        }.get(y, "invalid operator")
    except ValueError:
        print("value error", None)

main()
