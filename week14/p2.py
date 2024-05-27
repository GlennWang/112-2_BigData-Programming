import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import ssl

plt.rc('font', family='Microsoft JhengHei')
ssl._create_default_https_context = ssl._create_unverified_context

urls = [
    'https://stats.moe.gov.tw/files/detail/109/109_student.csv',
    'https://stats.moe.gov.tw/files/detail/110/110_student.csv',
    'https://stats.moe.gov.tw/files/detail/111/111_student.csv',
    'https://stats.moe.gov.tw/files/detail/112/112_student.csv'
]

dfs = [pd.read_csv(url) for url in urls]

for year, df in zip(range(109, 113), dfs):
    df['學年度'] = year

for df in dfs:
    df.rename(columns={
        "一年級男生": "一年級男",
        "一年級女生": "一年級女",
        "二年級男生": "二年級男",
        "二年級女生": "二年級女",
        "三年級男生": "三年級男",
        "三年級女生": "三年級女",
        "四年級男生": "四年級男",
        "四年級女生": "四年級女",
        "五年級男生": "五年級男",
        "五年級女生": "五年級女",
        "六年級男生": "六年級男",
        "六年級女生": "六年級女",
        "七年級男生": "七年級男",
        "七年級女生": "七年級女",
        "延修生男生": "延修生男",
        "延修生女生": "延修生女"
    }, inplace=True)

df = pd.concat(dfs)

df['學校名稱'] = df['學校名稱'].replace('亞東技術學院', '亞東科技大學')

schools = ['國立臺北科技大學', '長庚科技大學', '龍華科技大學', '德明財經科技大學', '亞東科技大學']
df_filtered = df[(df['學校名稱'].isin(schools)) & 
                 (df['日間∕進修別'] == 'D 日') & 
                 (df['等級別'] == 'B 四技')]

df_filtered = df_filtered[['學年度', '學校名稱', '一年級男', '一年級女']]
df_filtered['一年級男'] = df_filtered['一年級男'].astype(str).str.replace(',', '').astype(int)
df_filtered['一年級女'] = df_filtered['一年級女'].astype(str).str.replace(',', '').astype(int)

grouped = df_filtered.groupby(['學年度', '學校名稱']).sum().reset_index()
grouped['學校名稱'] = pd.Categorical(grouped['學校名稱'], categories=schools, ordered=True)
grouped = grouped.sort_values('學校名稱')

fig, ax = plt.subplots(figsize=(12, 8))

bar_width = 0.2
indices = np.arange(len(schools))

for i, year in enumerate(range(109, 113)):
    male_heights = grouped[grouped['學年度'] == year]['一年級男']
    female_heights = grouped[grouped['學年度'] == year]['一年級女']
    
    ax.bar(indices + i * bar_width, male_heights, bar_width, label=f'{year}-男')
    ax.bar(indices + i * bar_width, female_heights, bar_width, bottom=male_heights, label=f'{year}-女')

ax.set_title('109-112 學年度新生入學人數', fontsize=15)
ax.set_xlabel('學校名稱', fontsize=12)
ax.set_ylabel('學生人數', fontsize=12)
ax.set_xticks(indices + bar_width * 1.5)
ax.set_xticklabels(schools, rotation=45, ha='right')

ax.legend()
plt.tight_layout()
plt.show()
