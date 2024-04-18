"""
題目：4
請寫一個 Python 程式，
def month_calendar(chinese_year, month):
	...
	
當呼叫時給定民國年與月份時，會印出是年該月份的月曆內容。
例如，當呼叫 month_calendar(113, 2)，會得到如下的輸出結果，請觀察並完全依照下列的格式印出結果。
日 一 二 三 四 五 六
             1  2  3
 4  5  6  7  8  9 10
11 12 13 14 15 16 17
18 19 20 21 22 23 24
25 26 27 28 29
"""
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
