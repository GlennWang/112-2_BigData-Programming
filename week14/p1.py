import pandas as pd
import matplotlib.pyplot as plt
import ssl

# 設置字體以顯示中文
plt.rc('font', family='Microsoft JhengHei')

# 避免下載資料時出現SSL錯誤
ssl._create_default_https_context = ssl._create_unverified_context

# 讀取CSV檔案
url = 'https://stats.moe.gov.tw/files/detail/112/112_student.csv'
df = pd.read_csv(url)

# 六都名稱
six_cities = ['新北市', '臺北市', '桃園市', '臺中市', '臺南市', '高雄市']

# 去重以獲取唯一的大專院校
df_unique = df.drop_duplicates(subset=['學校名稱'])

# 計算每個城市的大專院校數目
uni_counts = {}
for city in six_cities:
    city_uni_count = df_unique[df_unique['縣市名稱'].str.contains(city)]['學校名稱'].nunique()
    uni_counts[city] = city_uni_count

# 獲取大專院校數目最多的城市，用於在圖表中突出顯示
# max_city = max(uni_counts, key=uni_counts.get)

# 生成爆炸設定，用於突出顯示最多的大專院校數目的城市
# explode = [0.2 if city == max_city else 0 for city in six_cities]

# 繪製環狀圖
fig, ax = plt.subplots(figsize=(8, 8))
wedges, texts, autotexts = ax.pie(
    uni_counts.values(), 
    # explode=explode, 
    labels=uni_counts.keys(), 
    autopct='%1.1f%%', 
    startangle=140, 
    colors=plt.cm.Paired(range(len(uni_counts))),
    wedgeprops=dict(width=0.3)
)

# 設置圖表標題
ax.set_title('六都區域內的大專院校數目佔比分析')

# 顯示圖表
plt.show()
