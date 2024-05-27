import pandas as pd
import plotly.express as px
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

url = 'https://stats.moe.gov.tw/files/detail/112/112_students.csv'
df = pd.read_csv(url)

ntu_df = df[(df['學校名稱'] == '國立臺北科技大學') & 
            (df['日間∕進修別'] == 'D 日') & 
            (df['等級別'].isin(['B 四技']))]

ntu_df['學生總數'] = ntu_df['總計']


fig = px.pie(ntu_df, names='科系名稱', values='學生總數', title='國立臺北科技大學各系學生數 (日間部大學部)')
fig.show()
