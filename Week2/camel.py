def main():
    text = input("camelCase: ")
    symbol = "_"
    s = text_process(text, symbol)
    print(f"snake_case:{s}")

def text_process(text, symbol):
    result = ""
    for char in text:
        if char.isupper():
            result += symbol + char
        else:
            result += char
    return result
    

main()