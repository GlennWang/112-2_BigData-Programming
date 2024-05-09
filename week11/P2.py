"""
題目：2
請前往 政府資料開放平台，以關鍵字搜尋 "大專院校校別學生數"，
並請找到 "112學年大專院校校別學生數（CSV檔）" 的連結，透過此連結以 pandas 將檔案讀取回來。
請列出在台北市的所有大學中，人數前五名的學校。 
"""
import pandas as pd

url = 'https://stats.moe.gov.tw/files/detail/112/112_student.csv'
df = pd.read_csv(url)


df2 = df[['學校名稱', '總計', '縣市名稱']]
taipei_uni = df2[df2['縣市名稱'].str.contains('臺北市')]
top5 = taipei_uni.groupby('學校名稱').sum().nlargest(5, '總計')[['總計']]

print(top5)