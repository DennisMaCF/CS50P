def main():
    gricery_process()

def gricery_process():
    gricery_list = {
    }

    while True:
        try:
            item = input("請輸入一個項目： ").upper().strip()#接收輸入並轉換大小寫
            if item:
                gricery_list[item] = gricery_list.get(item, 0) + 1

        except EOFError:
            for item in sorted(gricery_list):
                print(f"{gricery_list[item]} {item} ")
            print("Exiting...")
            break

main()