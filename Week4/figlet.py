from pyfiglet import Figlet
import random
import sys


def main():
    font_type = get_font()
    input_text = input("Input: ")
    print(print_font(font_type, input_text))

def get_font():

    figlet = Figlet()
    available_fonts = figlet.getFonts()
    # 使用者沒有加上任何提示
    if len(sys.argv) == 1: # 檢查使否沒有加上任何提示
        # figlet,getFonts 來獲取藝術字 使用random.choice隨機他
        font = random.choice(figlet.getFonts()) 
        return font

    # 使用者在.py 後加上-f or --font 以及指定字體
    # 判斷是否輸入了： -f or --font 以及指定字體
    elif len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font"):
        # figlet,getFonts 來獲取指定藝術字 
        font = sys.argv[2]
        if font in available_fonts:
            return font
        else:
            print("Invalid usage")
            sys.exit(1)
    
    # 如果用法錯誤
    else:
        print("Invalid usage")
        sys.exit(1) # 退出 


def print_font(font_tpye, input_text):
    # 使用try excpet 來偵錯
    try:
        # 把搜尋到的藝術子類型賦值給 figlet
        figlet = Figlet(font = font_tpye)
        # 把藝術字類型轉成藝術字，並賦值給 output
        output = figlet.renderText(input_text)
        return f"Output: \n {output}"

    except Exception as e:
        return f"Error: {e}"

if __name__ == "__main__":
    main()
