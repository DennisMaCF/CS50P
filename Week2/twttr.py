def main():
    word = input("Input: ")
    result = shorten(word)
    print(f"Output: {result}")

def shorten(word):
    result = ""
    for char in word:
        if char.lower() in ["a", "e", "i", "o", "u"]:
            continue
        else:
            result += char
    return result

if __name__ == "__main__":
    main()