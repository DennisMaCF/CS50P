def main():
    percentage = convert(input("Fraction: "))
    text = gauge(percentage)
    print(text)


# 轉換數字
def convert(fraction):
    while True:
        try:
            a, b = fraction.split("/")
            a = int(a)
            b = int(b)
            percentage = (a / b ) * 100
            return percentage
        
        except (ValueError, ZeroDivisionError):
            pass


# 規格轉成百分比
def gauge(percentage):
    if percentage <= 1:
        return "E"

    elif percentage >= 99:
        return "F"

    else:
        return f"{percentage:.0f}%"


if __name__ == "__main__":
    main()