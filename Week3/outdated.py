# 定義主函數，負責使用者輸入及執行
def main():
    while True:
        # 提示使用者輸入並執行韓式格式化輸入
        date = input("請輸入想轉換的日期，請按照 : 9/8/1636 或是 September 8, 1636 的格式輸入！ \n")
        formatted_date = rebuild_date(date)
        # 判斷函式是否執行成，未成功的話不會返回東西
        if formatted_date:
            print(formatted_date)
            break
        # 提示使用者重新輸入
        else:
            print("輸入無效！ 請按照: 9/8/1636 或是 September 8, 1636 的格式輸入！ ")

# 定義重建date函數，負責把使用者輸入格式化
def rebuild_date(date):
    # define a months list to save month
    months = ["January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"]

    # 使用try, except 來確保代碼穩定性
    # 這是使用者輸入的格式 9/8/1636或September 8, 1636 --> 這是我們希望輸出的格式 --> YYYY-MM-DD
    try:
        # September 8, 1636 這是該if 要判斷且格式化的輸入
        if "," in date:
            month_, rest= date.split(",", 1) # --> September 8 and 1636
            month_name, day = month_.split() # --> September and 8
            month_num = months.index(month_name) +1 # 從列表中查找所得到的月份名，並加上1，因為python從0開始計數
            # 下面兩行是要將數值轉為int， 方便之後可以檢查
            years = int(rest.strip()) 
            day = int(day)

        # 9/8/1636 這是該else 要判斷且格式化的輸入
        else:
            month_num, day, years = date.split("/", 3) # 以 "/" 為分割點去分割 
            # 下面三行是轉成int， 方便做檢查
            years = int(years)
            month_num = int(month_num)
            day = int(day)

        # 檢查月份及日期是否超出範圍
        if 1 <= month_num <= 12 and 1 <= day <= 31:
            # 下面兩行讓月份及日期以兩位數形式輸出
            month_num = f"{month_num:02}"
            day = f"{day:02}"
            # 返回格式化後的結果到main
            return f"{years}-{month_num}-{day}"

    # 如果出錯則不返回任何訊息，交給main 中的if判斷句判斷是否執行成功
    except ValueError:
        None

if __name__ == "__main__":
    main()
