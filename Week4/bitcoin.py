import requests
import sys


def main():
    get_bitcoin_amount()


def get_response():
    try:
        # 另response來儲存返回的比特幣價格資料
        response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        # 提取JSON資料，轉換為dict格式
        data = response.json()
        # 從字典中提取比特幣兌美金的值（float）
        current_price = data["bpi"]["USD"]["rate_float"] # float 
        # 返回比特幣單價
        return current_price
    # 使用RequestException來捕獲request模塊中的異常
    except requests.RequestException:
        # 退出
        sys.exit()



def get_bitcoin_amount():

    try:
        amount = float(sys.argv[1])
    # 如果遇到ValueError，打印提示
    except ValueError:
        sys.exit("Command-line argument is not a number")
    # 如果遇到IndexError，打印提示
    except IndexError:
        sys.exit("Missing command-line argument")
    # 打印比特幣總價
    print(f"${amount * get_response():,.4f}", end = "")


if __name__ =="__main__":
    main()