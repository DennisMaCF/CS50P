def main():
    convert()

def convert():
    n = str(input("請輸入一段文字並配上表情符號:)或是:(\n")).replace(":(", "🙁").replace(":)", "🙂")
    print(n)


main()