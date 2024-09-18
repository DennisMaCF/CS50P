from plates import is_valid


"""
    驗證車牌號是否符合以下規則：
    1. 車牌長度必須在 2 到 6 個字符之間。
    2. 車牌的前兩個字符必須是字母。
    3. 車牌中的數字不能以 '0' 開頭。
    4. 一旦車牌號中出現數字，數字之後不能再有字母。
    “不允許使用句點、空格或標點符號。
"""

def test_is_valid():
    assert is_valid("CS50") == True
    assert is_valid("CS05") == False
    assert is_valid("A") == False
    assert is_valid("CSCSCS50") == False
    assert is_valid("50CS") == False
    assert is_valid("CS50C") == False
    assert is_valid("ANGRY") == True
    assert is_valid("ANT10") == True
    assert is_valid("ANT1-,") == False
    assert is_valid("123456") == False
    assert is_valid("PI4.14") == False