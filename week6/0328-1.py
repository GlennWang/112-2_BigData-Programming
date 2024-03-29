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