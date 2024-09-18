import random

# 主函數
def main():
    level = get_level()
    generate_problems(level)

# 儲存用戶輸入之level
def get_level() -> int:
    # 使用循環已重複提示用戶輸入
    while True:
        try:
            # 提示用戶輸入level，並轉成整數
            level = int(input("Level: "))
            # 將level控制在1 ~ 3 之間
            if 1 <= level <=3 :
                # 將level回傳
                return level
        #識別錯誤
        except ValueError:
            # 繼續回到循環
            pass

# 隨機輸出範圍內數字
def generate_integer(level):

    # level = 1，數字為一位數
    if level == 1:
        return random.randint(0, 9)
    # level = 2，數字為二位數
    elif level == 2:
        return random.randint(10, 99)
    # level = 3，數字三位數
    else:
        return random.randint(100, 999)

# 處理問題
def generate_problems(level):
    # 設定答對題數初值
    correct_answers = 0
    
    # 設定十個問題
    for _ in range(10):
        # 隨機生成x, y
        x = generate_integer(level)
        y = generate_integer(level)
        # xy相加為答案
        correct_answer = x + y
        # 設定答案正確性初值
        answer_correctly = False
        
        # 給予用戶三次輸入機會
        for _ in range(3):
            try:
                # 提示用戶輸入答案
                user_answer = int(input(f"{x} + {y} = "))
                # 如果輸入等於答案
                if correct_answer == user_answer:
                    # 輸入正確，答對題數加一
                    correct_answers += 1
                    # 如果正確就返回True
                    answer_correctly = True
                    # 離開循環
                    break
                else:
                    # 輸入錯誤，給予提示
                    print("EEE")

            except ValueError:
                # ValueError，繼續回到主循環
                pass
        # 如果輸入三次後仍是False，那就反轉成True，進入if循環
        # range(3) 生成的是 [0, 1, 2]
        if not answer_correctly:
            # 打印算式及答案
            print(f"{x} + {y} = {correct_answer}")
    # 運行完十個問題後輸出分數
    print(f"Score: {correct_answers}")

# 避免誤執行主函數
if __name__ == "__main__":
    main()