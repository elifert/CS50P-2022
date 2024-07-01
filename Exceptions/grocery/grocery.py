def main():
    grocery_list = {}
    while True:
        try:
            item = input().strip().lower()            
            if item in grocery_list:
                grocery_list[item] += 1
            else:
                grocery_list[item] = 1
        
        except EOFError:
            print_grocery_list(grocery_list)
            break

def print_grocery_list(grocery_list):
    sorted_items = sorted(grocery_list)

    for item, count in sorted_items:
        print(f"{count} {item.upper()}")


if __name__ == "__main__":
    main()
