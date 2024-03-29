import re

def mark_number(number, digit=4):
    return re.sub(r'^(\d{%d})' % digit, '*' * digit, number)

# 測試函式
number = "1234567890"
print(mark_number(number))  # Output: ****567890
print(mark_number(number, 5))  # Output: *****67890
