def get_index(scores, subject_no):
    # 複製一份原始資料的索引
    original_index = list(range(len(scores)))

    # 依指定欄位進行排序，並取得排序後的索引
    sorted_index = sorted(original_index, key=lambda i: scores[i][subject_no])

    return sorted_index

# 原始成績資料
scores = [
    ["駱俊翔", 35, 29, 72, 136, 0],
    ["陳佳玲", 97, 0, 91, 188, 0],
    ["鄭志丹", 17, 71, 60, 148, 0],
    ["鄭淑玲", 57, 18, 75, 150, 0],
    ["藍婉菁", 52, 70, 50, 172, 0],
    ["李仰夫", 48, 85, 93, 226, 0],
    ["王美華", 50, 99, 29, 178, 0],
    ["霍秀蓉", 14, 45, 91, 150, 0],
    ["陳建佑", 51, 38, 93, 182, 0],
    ["林俊賢", 33, 14, 49, 96, 0],
    ["馮惠雯", 16, 62, 68, 146, 0],
]

# 對總分進行排序
total_score_index = get_index(scores, 4)

# 更新原始資料的倒數分數排名
for i, index in enumerate(total_score_index, start=1):
    scores[index][-1] = i

# 列印結果
print(f"學生姓名 國文\t英文\t數學\t總分")
for student in scores:
    print('\t'.join(map(str, student)))
