def is_leap(year: int) -> bool:
    return (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0))

def days_per_month(year: int) -> list:
    leap = 1 if is_leap(year) else 0
    return [31, 28 + leap, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def days_in_month(year: int, month: int) -> int:
    return days_per_month(year)[month - 1]

def first_day_of_month(year: int, month: int) -> int:
    days = 0
    for y in range(1900, year):
        days += 365 + is_leap(y)
    for m in range(1, month):
        days += days_in_month(year, m)
    return (days + 1) % 7

year = 2024
month = 9
print("第一天是星期:", first_day_of_month(year, month))

