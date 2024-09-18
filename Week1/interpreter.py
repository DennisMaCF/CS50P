try:
    expression = input("請輸入您想計算的表達式，例如 3 + 4 或 3**4：\n")
    result = float(eval(expression))

    print(f"結果是: {result} ")
except Exception as e:
    print(f"發生錯誤！{e}")