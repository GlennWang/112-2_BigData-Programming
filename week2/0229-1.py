"""
題目：1
name_str = "駱俊翔、陳佳玲、鄭志丹、鄭淑玲、藍婉菁、李仰夫、王美華、霍秀蓉、陳建佑、林俊賢、馮惠雯"
請將上述的字串 name_str 拆解，做為成績資料的學生人名部分。
再為每個人名資料附加三個科目(國文、英文、數學)的成績，每科的成績範圍 0 ~ 99，則請以隨機方式生成。
最後，請計算三科的總分，將其附加在成績資料的後面，再把所有資料以如下圖的形式輸出。

參考輸出如下:(其中各列(row)的資料間，均以tab分隔，且分數部分的則是讓個位數對齊。)
學生姓名	國文	英文	數學	總分
駱俊翔	 92	 68	  2	162	
陳佳玲	 50	 79	 22	151	
鄭志丹	 92	 54	 23	169	
鄭淑玲	 78	 93	 37	208	
藍婉菁	 73	 35	  1	109	
李仰夫	 67	 56	 58	181	
王美華	 73	 65	 54	192	
霍秀蓉	  5	 34	 12	 51	
陳建佑	 88	 54	 90	232	
林俊賢	 72	 49	  5	126	
馮惠雯	 10	 45	 43	 98
"""
import random

name_str = "駱俊翔、陳佳玲、鄭志丹、鄭淑玲、藍婉菁、李仰夫、王美華、霍秀蓉、陳建佑、林俊賢、馮惠雯"
names = name_str.split("、")

# 印表標頭
print(f"學生姓名 國文\t英文\t數學\t總分")

for name in names:
    # 生成隨機成績
    chinese_score = random.randint(0, 99)
    english_score = random.randint(0, 99)
    math_score = random.randint(0, 99)

    # 計算總分
    total_score = chinese_score + english_score + math_score

    # 輸出資料
    print(f"{name}\t {chinese_score:2}\t{english_score:2}\t{math_score:2}\t{total_score:3}")
