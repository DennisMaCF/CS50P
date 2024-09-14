def main():
    print_greet()



def print_greet():
    # 調用 get_greet 函數來獲得人名
    greet_list = get_greet()
    # 只有一個人名
    if len(greet_list) == 1:
        print(f"Adieu, adieu, to {greet_list[0]}")
    # 只有兩個人名
    elif len(greet_list) == 2:
        print(f"Adieu, adieu, to {greet_list[0]} and {greet_list[1]}")
    # 有三個以上人名
    else:
        print(f"Adieu, adieu, to {", ".join(greet_list[:-1])}, and {greet_list[-1]}")


def get_greet():
    # 建立一個空資料夾儲存人名
    greet_list = []
    # 建立循環直到用戶輸入 control + d
    while True:
        try:
            # 提示用戶輸入人名
            user_input = input("Name: ")
            # 將人名回傳到list
            greet_list.append(user_input)

        # 捕獲用戶輸入 control + d
        except EOFError:
            print("Exiting...")
            # 偵測到 control + d 循環結束
            return greet_list
            break

if __name__ == "__main__":
    main()