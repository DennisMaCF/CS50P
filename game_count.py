import random


def main():
    # 執行嵌套過後的guess_num函數
    guess_num()

def get_level():
    # 使用循環來重複提示輸入Level
    while True:
        try:
            # 把用戶輸入之值轉成整數
            level = int(input("Level: "))
            # Level大於1且沒有報錯的話回傳它
            if 1 <= level:
                return level
            else:
                continue

        # ValueError 時代表輸入了字串或是浮點數，忽略繼續提示輸入Level
        except ValueError:
            pass

def get_num():
    # 從get_level函數拿到數字的上限
    level = get_level()
    # 在1 ~ 用戶輸入之 level 中隨機選擇一個目標數字
    num = random.randint(1, level)
    # 返回目標數字
    return num

def guess_num():
    # 從get_num函數得到目標數字
    num = get_num()
    # 初始化times
    times = 0
    # 使用循環來重複
    while True:
        try:
            # 提示用戶輸入他猜測的數字
            user_input = int(input("Guess: "))
            # 使用count_time函數來計算次數
            times = count_times(times)
            # 如果用戶輸入之數字大於1
            if 1 <= user_input:
                # 如果用戶輸入大於目標數字
                if num < user_input:
                    print("Too large!")
                # 如果用戶輸入小於目標數字
                elif user_input < num:
                    print("Too small!")
                # 如果用戶輸入等於目標數字
                else:
                    print("Just right!")
                    print(f"你總共花了{times}次完成!")
                    break
            else:
                continue

        # 偵測到字串或是小數，繼續回到主循環
        except ValueError:
            pass

def count_times(times):
    times += 1
    return times



# 執行主函數
if __name__ == "__main__":
    main()