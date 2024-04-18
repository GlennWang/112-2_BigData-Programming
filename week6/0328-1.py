"""
題目：1
請寫一 Python 函式: 
def string_length(msg):
	pass
	
用來計算給定的中英夾雜字串資料(msg)，在將該字串列印後，會佔據幾格的空間。
其中，ASCII code 會佔一格，中文或全型內容會佔兩個位置。
例如，
string_length("123abc") => 6
string_length("123中文測試abc") => 14 
"""
def string_length(msg):
    total_length = 0
    for char in msg:
        if ord(char) >= 0x4E00 and ord(char) <= 0x9FFF:  # 檢查是否為中文
            total_length += 2
        else:
            total_length += 1
    return total_length


print(f'123abc:{string_length("123abc")}')
print(f'123中文測試abc:{string_length("123中文測試abc")}')