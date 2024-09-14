def main():
    greet = input("Please enter your greet : ").lower().strip()
    greeting(greet)

def greeting(greet):
    if greet[0:5] == "hello":
        print("$: 0")
    elif greet[0:1] == "h":
        print("$: 20")
    else:
        print("$: 100")

if __name__ == "__main__":
    main()