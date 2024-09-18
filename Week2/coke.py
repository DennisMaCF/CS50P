def main():
    due = int(50)
    print(f"Amount due:{due}   please enter 5, 10, 25 cent! ")
    while True:
        try:
            coin = int(input("Insert coin: "))
            if coin in [5, 10, 25,]:
                due -= coin
                if due <= 0:
                    change = -due
                    break
            else:
                print("Invalid input. Please enter a valid coin amount.")
        except ValueError:
            print("Invalid input. Please enter a valid coin amount.")

        print(f"Amount due:{due}")
    print(f"Change owed:{change}")
    print("Thank you! Your amount has been paid! You can geta coke. ")

main()