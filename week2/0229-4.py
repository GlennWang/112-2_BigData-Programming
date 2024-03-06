def month_calendar(chinese_year, month):
    import calendar

    calendar.setfirstweekday(calendar.SUNDAY)
    # 將民國年轉換為西元年
    year = chinese_year + 1911

    # 取得該月的日曆資訊
    cal = calendar.monthcalendar(year, month)

    # 列印表頭
    print("日  一  二  三  四  五  六")

    # 遍歷日曆，進行列印
    for week in cal:
        for day in week:
            if day == 0:
                print("   ", end=" ")
            else:
                print(f"{day:2d} ", end=" ")
        print()

# test
month_calendar(113, 2)
