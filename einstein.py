def main():
    print_ans()

def get_ans():
    while True:
        try:
            m = int(input("請以整數輸入一個質量。 \n"))
            if m > 0:
                return m
            print("請輸入正數。 ")
        except ValueError:
            pass

def print_ans():
    m = get_ans()
    print(m * 90000000000000000)

main()