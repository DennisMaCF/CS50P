def main():
    process_ans()

def process_ans():
    while True:
        try:
            #接收用戶輸入之值
            fraction = input("Fraction: ")
            #將x/y分成a b 
            (a, b) = fraction.split("/")
            (a) = int(a)
            (b) = int(b)
            ans = a / b * 100
            if 1<  ans < 99:
                print(f"{ans:.0f}% ")
            elif 99 <= ans <= 100:
                print("F")
            elif 0 <= ans <= 1:
                print("E")
            break
        except (ValueError, ZeroDivisionError):
            print("請以x/y數入,x,y為整數,y不得為0。 ")

main()
