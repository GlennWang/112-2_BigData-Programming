import pandas as pd
import plotly.express as px
import ssl

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
dfs[0].rename(columns={
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

# 將數據轉換為長格式，以便繪製分列柱狀圖
df_melted = df_filtered.melt(id_vars=['學年度', '學校名稱'], 
                             value_vars=['一年級男', '一年級女'], 
                             var_name='性別', 
                             value_name='人數')


df_melted['人數'] = df_melted['人數'].astype(str).str.replace(',', '').astype(int)


print(df_melted)

# 繪製分列柱狀圖
fig = px.bar(df_melted, 
             x='學年度', 
             y='人數', 
             color='性別', 
             facet_col='學校名稱', 
             barmode='group', 
             title='各學年度各學校日間部大學一年級男女生人數（分列）')
fig.show()

# 繪製堆疊柱狀圖
fig_stacked = px.bar(df_melted, 
                     x='學年度', 
                     y='人數', 
                     color='性別', 
                     facet_col='學校名稱', 
                     barmode='stack', 
                     title='各學年度各學校日間部大學一年級男女生人數（堆疊）')
fig_stacked.show()
