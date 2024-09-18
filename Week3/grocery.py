def main():
    items = {}
    collect_item(items)
    display_item(items)

def collect_item(items):
    while True:
        try:
            item= input().upper()
            if item in items:
                items[item] += 1
            else:
                items[item] = 1

        except EOFError:
            print()
            break

def display_item(items):
    for item in sorted(items):
        print(f"{items[item]} {item}")

if __name__ == "__main__":
    main()
