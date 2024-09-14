def main():
    ans()

def ans():
    ans = str(input("What is the Answer to the Great Question of Life, the Universe, and Everything? ")).lower()
    if ans in ["42", "forty two", "forty-two"]:
        print("Yes. ")
    else:
        print("No. ")

main()