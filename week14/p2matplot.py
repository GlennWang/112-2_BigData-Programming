import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import ssl

# 設置字體以顯示中文
plt.rc('font', family='Microsoft JhengHei')

ssl._create_default_https_context = ssl._create_unverified_context

# 讀取所有年份的 CSV 文件
urls = [
    'https://stats.moe.gov.tw/files/detail/109/109_student.csv',
    'https://stats.moe.gov.tw/files/detail/110/110_student.csv',
    'https://stats.moe.gov.tw/files/detail/111/111_student.csv',
    'https://stats.moe.gov.tw/files/detail/112/112_student.csv'
]

# 下載並讀取 CSV 文件
dfs = [pd.read_csv(url) for url in urls]

# 在109年的資料中新增一列"學年度"，並設置為109
dfs[0]['學年度'] = 109

# 重命名列名
dfs[0] = dfs[0].rename(columns={
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
})

dfs[0]['學校名稱'] = dfs[0]['學校名稱'].replace('亞東技術學院', '亞東科技大學')

# 合併所有數據框
df = pd.concat(dfs)

# 篩選出特定學校的日間部大學一年級數據
schools = ['國立臺北科技大學', '長庚科技大學', '龍華科技大學', '德明財經科技大學', '亞東科技大學']
df_filtered = df[(df['學校名稱'].isin(schools)) & 
                 (df['日間∕進修別'] == 'D 日') & 
                 (df['等級別'] == 'B 四技')]

# 保留所需的列
df_filtered = df_filtered[['學年度', '學校名稱', '一年級男', '一年級女']]

# 填充缺失值为0，并将人数列转换为整数类型
df_filtered['一年級男'] = df_filtered['一年級男'].astype(str).str.replace(',', '').astype(int)
df_filtered['一年級女'] = df_filtered['一年級女'].astype(str).str.replace(',', '').astype(int)

# 將數據按學年度和學校名稱分組
grouped = df_filtered.groupby(['學年度', '學校名稱']).sum().reset_index()

# 分列柱狀圖
fig1, axs1 = plt.subplots(1, len(schools), figsize=(25, 5), sharey=True)
fig1.suptitle('各學年度各學校日間部大學一年級男女生人數（分列）', fontsize=20)

for i, school in enumerate(schools):
    school_data = grouped[grouped['學校名稱'] == school]
    x = school_data['學年度'].astype(str)
    y1 = school_data['一年級男']
    y2 = school_data['一年級女']

    indices = np.arange(len(x))
    bar_width = 0.35

    axs1[i].bar(indices - bar_width/2, y1, bar_width, label='一年級男', color='b', alpha=0.7)
    axs1[i].bar(indices + bar_width/2, y2, bar_width, label='一年級女', color='r', alpha=0.7)
    axs1[i].set_title(f'{school}')
    axs1[i].legend()
    axs1[i].set_xticks(indices)
    axs1[i].set_xticklabels(x)

plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()

# 堆疊柱狀圖
fig2, axs2 = plt.subplots(1, len(schools), figsize=(25, 5), sharey=True)
fig2.suptitle('各學年度各學校日間部大學一年級男女生人數（堆疊）', fontsize=20)

for i, school in enumerate(schools):
    school_data = grouped[grouped['學校名稱'] == school]
    x = school_data['學年度'].astype(str)
    y1 = school_data['一年級男']
    y2 = school_data['一年級女']

    axs2[i].bar(x, y1, label='一年級男', color='b', alpha=0.7)
    axs2[i].bar(x, y2, label='一年級女', color='r', alpha=0.7, bottom=y1)
    axs2[i].set_title(f'{school}')
    axs2[i].legend()

plt.tight_layout(rect=[0, 0.03, 1, 0.95])
plt.show()
