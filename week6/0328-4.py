"""
題目：4
請寫 Python 函式，限用 RE(Regular Expression) 的方式來進行星號的替換。
def mark_number(number, digit=4):
    pass
    
可以將給定數字字串內容的前 digit 位，以星號取代。
例如，number = "1234567890"，則
mark_number(number)    => ****567890 <-- 預設4位。
mark_number(number, 5) => *****67890 <-- 指定5位。
"""
import re

def mark_number(number, digit=4):
    return re.sub(r'^(\d{%d})' % digit, '*' * digit, number)

# 測試函式
number = "1234567890"
print(mark_number(number))  # Output: ****567890
print(mark_number(number, 5))  # Output: *****67890
