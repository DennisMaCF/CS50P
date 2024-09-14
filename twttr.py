def main():
    text_process()

def text_process():
    text = str(input("Input: "))
    result = ""
    for char in text:
        if char in ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]:
            continue
        else:
            result += char
    print(f"Output: {result}")

main()