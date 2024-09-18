def main():
    process_ans()

def process_ans():
    while True:
        try:
            #接收用戶輸入之值
            fraction = input("Fraction: ")
            #將x/y分成a b c
            (a, c) = fraction.split("/")
            (a) = int(a)
            (c) = int(c)
            ans = a / c * 100
            if 0 < ans < 100:
                print(f"{ans:.0f}% ")
            elif ans == 100:
                print("F")
            elif ans == 0:
                print("E")
            break
        except (ValueError, ZeroDivisionError):
            print("請以x/y數入，x,y為整數，y不得為0。 ")

main()
