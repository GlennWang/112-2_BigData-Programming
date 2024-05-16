import pandas as pd
import matplotlib.pyplot as plt
import ssl

plt.rc('font', family='Microsoft JhengHei')
ssl._create_default_https_context = ssl._create_unverified_context

url = 'https://stats.moe.gov.tw/files/detail/112/112_student.csv'
df = pd.read_csv(url)

six_cities = ['新北市', '臺北市', '桃園市', '臺中市', '臺南市', '高雄市']
df_unique = df.drop_duplicates(subset=['學校名稱'])

uni_counts = {}
for city in six_cities:
    city_uni_count = df_unique[df_unique['縣市名稱'].str.contains(city)]['學校名稱'].nunique()
    uni_counts[city] = city_uni_count

print("每個六都區域的大專院校數目:")
for city, count in uni_counts.items():
    print(f"{city}: {count}")

uni_counts_df = pd.DataFrame(list(uni_counts.items()), columns=['縣市名稱', '大專院校數目'])

fig, ax = plt.subplots(figsize=(8, 8))
ax.pie(uni_counts.values(), labels=uni_counts.keys(), autopct='%1.1f%%', startangle=140, colors=plt.cm.Paired(range(len(uni_counts))))

ax.set_title('六都區域內的大專院校數目佔比分析')
plt.show()

max_city = max(uni_counts, key=uni_counts.get)
print(f"佔比最多的市: {max_city} ({uni_counts[max_city]} 所大專院校)")
