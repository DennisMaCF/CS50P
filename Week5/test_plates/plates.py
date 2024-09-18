def main():
    # Get the Plate
    plate = input("Plate: ")

    # use the is_vaild function to check the plate
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")

def is_valid(s_):
    """
    驗證車牌號是否符合以下規則：
    1. 車牌長度必須在 2 到 6 個字符之間。
    2. 車牌的前兩個字符必須是字母。
    3. 車牌中的數字不能以 '0' 開頭。
    4. 一旦車牌號中出現數字，數字之後不能再有字母。
    """

    # 檢查代碼長度在2 到 6 個字符之間。
    if not 2 <= len(s_) <= 6:
        return False
    
    # 車牌的前兩位必須為字母（數字不行）
    if not s_[:2].isalpha():
        return False
    
    # 初始化標誌位
    digit_found = False # 紀錄是否遇到數字
    
    # 車牌中的數字不能以 '0' 開頭。
    for char in s_:
        if char.isdigit():
            if char == "0" and  not digit_found:
                return False
            digit_found = True
        # 一旦車牌號中出現數字，數字之後不能再有字母。
        elif digit_found and char.isalpha():
            return False
    
    # “不允許使用句點、空格或標點符號。
    # isalnum函數為判斷是否全部都為數字及字母
    if not s_.isalnum():
        return False

    return True

if __name__ == "__main__":
    main()