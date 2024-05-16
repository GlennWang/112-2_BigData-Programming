"""
題目：1
請前往 政府資料開放平台，以關鍵字搜尋 "大專院校校別學生數"，
並請找到 "112學年大專院校校別學生數（CSV檔）" 的連結，透過此連結以 pandas 將檔案讀取回來。
請顯示六都區域內的大專院校數目(公私立皆算)。
同時請將獲取的數據，分別以柱狀圖及折線圖，呈現出來。
(*六都: 新北市,臺北市,桃園市,臺中市,臺南市,高雄市。) 
"""
import pandas as pd
import matplotlib.pyplot as plt

plt.rc('font', family='Microsoft JhengHei')

url = 'https://stats.moe.gov.tw/files/detail/112/112_student.csv'
df = pd.read_csv(url)

six_citys = ['新北市', '臺北市', '桃園市', '臺中市', '臺南市', '高雄市']
df_unique = df.drop_duplicates(subset=['學校名稱'])

uni_counts = {}
for city in six_citys:
    city_uni_count = df_unique[df_unique['縣市名稱'].str.contains(city)]['學校名稱'].nunique()
    uni_counts[city] = city_uni_count

print("每個六都區域的大專院校數目:")
for city, count in uni_counts.items():
    print(f"{city}: {count}")


uni_counts_df = pd.DataFrame(list(uni_counts.items()), columns=['縣市名稱', '大專院校數目'])
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))
plt.subplots_adjust(hspace=0.5)

# 柱狀圖
uni_counts_df.plot(kind='bar', x='縣市名稱', y='大專院校數目', color='skyblue', ax=ax1)
ax1.set_title('大專院校數目 - 六都區域')
ax1.set_xlabel('縣市名稱')
ax1.set_ylabel('大專院校數目')
ax1.tick_params(axis='x', rotation=45)

# 折線圖
uni_counts_df.plot(kind='line', x='縣市名稱', y='大專院校數目', marker='o', color='green', ax=ax2)
ax2.set_title('大專院校數目 - 六都區域')
ax2.set_xlabel('縣市名稱')
ax2.set_ylabel('大專院校數目')
ax2.tick_params(axis='x', rotation=45)
ax2.grid(True)

# 顯示圖表
plt.show()