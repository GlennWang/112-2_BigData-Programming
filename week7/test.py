import math



# for i in range(1, 13):
#     print(f'{i}:{math.ceil(12 / i)}')

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

def month_calendar_to_matrix(year, month=1):
    month_matrix = [[0] * 7 for _ in range(6)]
    
    first_day = first_day_of_month(year, month)
    num_days = days_in_month(year, month)
    
    row = 0
    col = first_day
    for day in range(1, num_days + 1):
        month_matrix[row][col] = day
        col += 1
        if col == 7:  
            col = 0
            row += 1
    
    # Print the calendar matrix
    # for row in month_matrix:
    #     for num in row:
    #         if num == 0:
    #             print("   ", end=" ")
    #         else:
    #             print(f"{num:3}", end=" ")
    #     print()
    return month_matrix

# Example usage:
# month_calendar_to_matrix(2024, 5)
print(month_calendar_to_matrix(2024, 1))
print(month_calendar_to_matrix(2024, 2))
print(month_calendar_to_matrix(2024, 3))

def print_calendar_row(year, months):
    for month in months:
        print(f"==== {year}年{month}月 ====", end="\t")

    print()  # 換行

    for week in range(6):
        for month in months:
            calendar_matrix = month_calendar_to_matrix(year, month)
            week_str = " ".join(str(day).rjust(2) if day != 0 else "  " for day in calendar_matrix[week])
            print(week_str, end="\t")
        print()  # 換行

print_calendar_row(2024, [1, 2, 3])

# print(f'2000年2月有{days_in_month(2000, 2)}天')
# print(f'2024年2月有{days_in_month(2024, 2)}天')
# print(f'2024年3月有{days_in_month(2024, 3)}天')
# print(f'2024年4月有{days_in_month(2024, 4)}天')


# month_calendar(2024, 4)
# month_calendar(2002, 1)


list1 = [
    [0, 1, 2, 3, 4, 5, 6],
    [7, 8, 9, 10, 11, 12, 13],
    [14, 15, 16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25, 26, 27],
    [28, 29, 30, 0, 0, 0, 0]
] 

