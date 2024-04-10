import math

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
    return month_matrix

def year_calendar(year, months_per_row=3, chinese=True):
    """
    思路:
        如果用P2的方式，直接想要把它改成年曆，感覺大腦會燒沒，所以改成回傳一個二維list。
        然後就可以用那個list來印。
    """
    weekdays = "Sun Mon Tue Wed Thr Fri Sat"
    month_names_chinese = ["一月", "二月", "三月", "四月", "五月", "六月", "七月", "八月", "九月", "十月", "十一月", "十二月"]
    month_names_english = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    
    month_name = month_names_chinese if chinese else month_names_english
    month_name_width = 25 if chinese else 27  

    cols = months_per_row
    rows = math.ceil(12 / months_per_row)
    index_of_month_name = 0
    
    for row in range(rows):
        for col in range(cols):
            if index_of_month_name < 12:
                print(f"{month_name[index_of_month_name]:^{month_name_width}}", end='   ')
                index_of_month_name += 1
        print()

        for col in range(cols):
            print(weekdays, end='   ')
        print()

        for week in range(6):
            for col in range(cols):
                if index_of_month_name - cols + col < 12:
                    calendar_matrix = month_calendar_to_matrix(year, index_of_month_name - cols + col + 1)
                    for day in calendar_matrix[week]:
                        if day != 0:
                            print(f"{day:2d} ", end=" ")
                        else:
                            print('   ', end=' ')
                    print("  ", end='')
            print()
        print()

year_calendar(2024, 3, False)