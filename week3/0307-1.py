import math

namestr = """
李彥智、張逸凡、劉建岳、李國偉、張淑雯、魏怡伶、王偉妮、黃登秋、許舒婷、陳于婷、
洪致歡、劉海元、謝怡文、林雅雯、黃家靖、魏玉玲、郭于珮、侯惠文、王家瑋、阮禎旺、
張蘭添、魏振豪、林惠婷、曾玫琬、黃佳蓉、王右倩、許卓白、林韋龍、陳哲維、周良松、
洪宇坤、鄭姿伶、楊敬仲、黃靜靖、林榮泉、黃冠伶、林俊雅、李宜雪、葉靜如、陳宥玟、
宋淑君、王蕙妏、駱嘉祥、林舜、郭萱帆、林瑞恭、黃美均、郭志峰、王宛臻、胡木行、
李雅盛、張俊宇、李民易、林志文、陳思光、張行其、鄭怡海、吳心怡
"""

name_list = namestr.replace("、"," ").split()

def show_in_columns(data: list, cols: int):
    data.sort()
    data_len = len(data)
    one_col_len = math.ceil(data_len / cols)
    
    for row in range(one_col_len):
        for col in range(cols):
            index = row + col * one_col_len 
            if index > data_len - 1:
                continue
            else:
                print(f'{data[index]}\t',end = "")
        print()

    return 

show_in_columns(name_list, 4)