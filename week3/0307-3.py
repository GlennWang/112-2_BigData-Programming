import random

# 特別獎號碼
special_prize_number = "63603594"

# 產生一萬筆發票號碼
invoice_numbers = [str(random.randint(10000000, 99999999)) for _ in range(10000)]

# 中獎統計
prizes = {
    "Special Prize": [],
    "Second Prize": [],
    "Third Prize": [],
    "Fourth Prize": [],
    "Fifth Prize": [],
    "Sixth Prize": [],
}

for number in invoice_numbers:
    if number == special_prize_number:
        prizes["Special Prize"].append(number)
    elif number[-7:] == special_prize_number[-7:]:
        prizes["Second Prize"].append(number)
    elif number[-6:] == special_prize_number[-6:]:
        prizes["Third Prize"].append(number)
    elif number[-5:] == special_prize_number[-5:]:
        prizes["Fourth Prize"].append(number)
    elif number[-4:] == special_prize_number[-4:]:
        prizes["Fifth Prize"].append(number)
    elif number[-3:] == special_prize_number[-3:]:
        prizes["Sixth Prize"].append(number)

# 計算百分比
total_invoices = len(invoice_numbers)
percentages = {key: (len(value) / total_invoices) * 100 for key, value in prizes.items()}

# 列印結果
for key, value in prizes.items():
    print(f"{key}: {len(value)} 組，佔 {percentages[key]:.2f}%")
    print(f"中獎號碼: {', '.join(value)}")
    print()
