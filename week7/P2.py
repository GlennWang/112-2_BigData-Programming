def is_leap(year: int) -> bool:
    return (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0))

def days_per_month(year: int) -> list:
    leap = 1 if is_leap(year) else 0
    return [31, 28 + leap, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def days_in_month(year: int, month: int) -> int:
    return days_per_month(year)[month - 1]

def first_day_of_month(year: int, month: int) -> int:
    """
    思路:
        1900年1月1號是星期一，所以就從那天開始一直把經過的每年加上去。
        然後再把指定的月份之前的月份的天數給加上去。
        然後因為1900/01/01是星期一所以要(days + 1) % 7
        星期日是一個禮拜的第一天是0
        星期一是1
        以此類推
        星期六是6
    """
    days = 0
    for y in range(1900, year):
        days += 365 + is_leap(y)
    for m in range(1, month):
        days += days_in_month(year, m)
    return (days + 1) % 7

def month_calendar(year, month=1, chinese=True):
    weekdays = "Sun Mon Tue Wed Thr Fri Sat"
    
    month_names_chinese = ["一月", "二月", "三月", "四月", "五月", "六月", "七月", "八月", "九月", "十月", "十一月", "十二月"]
    month_names_english = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    
    month_name = month_names_chinese[month - 1] if chinese else month_names_english[month - 1]
    
    print(f"{month_name:^25}")
    print(weekdays)
    
    first_day = first_day_of_month(year, month)
    num_days = days_in_month(year, month)
    
    print("    " * first_day, end="")
    for day in range(1, num_days + 1):
        print(f"{day:3}", end=" ")
        first_day = (first_day + 1) % 7
        if first_day == 0:
            print()
    print()


print(f'2000年2月有{days_in_month(2000, 2)}天')
print(f'2024年2月有{days_in_month(2024, 2)}天')
print(f'2024年3月有{days_in_month(2024, 3)}天')
print(f'2024年4月有{days_in_month(2024, 4)}天')


month_calendar(2024, 4)
month_calendar(2002, 1)
