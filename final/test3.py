import pandas as pd
import plotly.express as px

# 讀取CSV文件
df = pd.read_csv('read.csv', encoding='big5')

# 整理數據，選擇需要分析的列
columns_of_interest = df.columns.tolist()  # 使用所有列
print(columns_of_interest)
columns_of_interest.remove('總計人數')

df = df[columns_of_interest]

# 將'教育程度別'中的重複值（例如 '男性', '女性'）去除，僅保留總計行
df = df[df['教育程度別'].isin(['總計', '國小類', '國中類', '高中或高職類', '大專類', '研究所類', '其他或不詳類'])]

# 重新設置索引
df = df.reset_index(drop=True)

# 為每個犯罪類型生成單獨的圖表
for crime_type in columns_of_interest[1:]:
    fig = px.bar(df, x='教育程度別', y=crime_type, title=f'{crime_type} 的犯罪人數', labels={'value': '人數', 'variable': '犯罪類型'})
    fig.show()