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

# print("每個六都區域的大專院校數目:")
# for city, count in uni_counts.items():
#     print(f"{city}: {count}")

uni_counts_df = pd.DataFrame(list(uni_counts.items()), columns=['縣市名稱', '大專院校數目'])

plt.figure(figsize=(10, 6))
plt.bar(uni_counts_df['縣市名稱'], uni_counts_df['大專院校數目'], color='skyblue')
plt.title('六都區域內的大專院校數目')
plt.xlabel('縣市名稱')
plt.ylabel('大專院校數目')
plt.xticks(rotation=45)

plt.show()
