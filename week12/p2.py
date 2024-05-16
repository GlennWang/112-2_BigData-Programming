"""
題目：2
同上題，請使用相同的資料來完成下列指定的任務。。
將"國立臺北科技大學"，日大學部(D 日, B 四技)一到四年級的男女學生的人數資料取出來。
接著以年級為索引(index)，男女學生人數為欄位(column)畫成柱狀圖，其中 併排 與 堆疊 兩種形式都請繪出來。
建議步驟:
1)首先請讀入檔案中資料並進行拆解，找出符合的校名與學制。
2)觀察各個欄位的排列結構，找出日間大學部一到四年級的男、女學生人數，將其轉換成 DataFrame。
3)再針對該 DataFrame 進行柱狀圖的繪製。請參考下圖的輸出。
"""
import pandas as pd
import matplotlib.pyplot as plt

url = 'https://stats.moe.gov.tw/files/detail/112/112_student.csv'
df = pd.read_csv(url)

filtered_df = df[(df['學校名稱'] == '國立臺北科技大學') & (df['日間∕進修別'] == 'D 日') & (df['等級別'] == 'B 四技')]

male_df = filtered_df[['一年級男', '二年級男', '三年級男', '四年級男']].values.flatten()
female_df = filtered_df[['一年級女', '二年級女', '三年級女', '四年級女']].values.flatten()

x = range(1, 5)
x_male = [i - 0.1 for i in x]
x_female = [i + 0.1 for i in x]

plt.rc('font', family='Microsoft JhengHei')
fig, axs = plt.subplots(1, 2, figsize=(8, 4))

# 並排柱狀圖
axs[0].bar(x_male, male_df, color='blue', width=0.2, align='center', label='男')
axs[0].bar(x_female, female_df, color='orange', width=0.2, align='center', label='女')
axs[0].set_xlabel('年級')
axs[0].set_ylabel('人數')
axs[0].set_title('臺北科技大學')
axs[0].set_xticks(x)
axs[0].set_xticklabels(['一年級', '二年級', '三年級', '四年級'])
axs[0].legend(loc='upper right')  

# 堆疊柱狀圖
axs[1].bar(x, male_df, color='blue', width=0.3, label='男')
axs[1].bar(x, female_df, bottom=male_df, color='orange', width=0.3, label='女')
axs[1].set_xlabel('年級')
axs[1].set_ylabel('人數')
axs[1].set_title('臺北科技大學')
axs[1].set_xticks(x)
axs[1].set_xticklabels(['一年級', '二年級', '三年級', '四年級'])
axs[1].legend(loc='upper right')
axs[1].set_yticks(range(0, max(male_df) + max(female_df) + 100, 250))


plt.tight_layout()
plt.show()