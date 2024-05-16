import pandas as pd
import matplotlib.pyplot as plt

url = 'https://stats.moe.gov.tw/files/detail/112/112_student.csv'
df = pd.read_csv(url)

filtered_df = df[(df['學校名稱'] == '中國文化大學') & (df['日間∕進修別'] == 'D 日') & (df['等級別'] == 'B 學士')]

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
axs[0].set_title('中國文化大學')
axs[0].set_xticks(x)
axs[0].set_xticklabels(['一年級', '二年級', '三年級', '四年級'])
axs[0].legend(loc='upper right')  

# 堆疊柱狀圖
axs[1].bar(x, male_df, color='blue', width=0.3, label='男')
axs[1].bar(x, female_df, bottom=male_df, color='orange', width=0.3, label='女')
axs[1].set_xlabel('年級')
axs[1].set_ylabel('人數')
axs[1].set_title('中國文化大學')
axs[1].set_xticks(x)
axs[1].set_xticklabels(['一年級', '二年級', '三年級', '四年級'])
axs[1].legend(loc='upper right')
# axs[1].set_yticks(range(0, max(male_df) + max(female_df) + 100, 250))


plt.tight_layout()
plt.show()