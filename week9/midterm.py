"""
題目：5
有文字字串資料如下，
捐款的名單:
1) Godly Liu $2,500
2) Well-Born Chen $12,000
3) Ferris Wang $500
4) Maurice Lee $1,200
5) Fern Chang $3,000
6) Belinda Pai $4,500
7) Estra Tai $33,580
8) Ernestine Tong $4,200
9) Amanda Kao $25,000
10) Jesse Lin $10,000

請使用 Regular Expression 來完成下列指定的任務:
請從捐款的名單中找出所有的金額部分，並計算其總和。
"""
import re

data = """
捐款名錄
張雅劭,$4
張嘉文 7
林若屏 307516
陳茜宇 41228282643
劉孟哲,$79陳惠琴 $51,964,192,074
王佳靜,92胡美任 $4
陳宗翰:708875006呂蘭琇:$926,788,079,089
常芝菱=>56681
劉惠萍,33519764567
羅素卉:520陳雅婷=>$389,217,645,991
洪廷岳:6
高冠宇=>844541832383鄭璇岳=>$1
吳維哲=>7915826782
張佳月 $8
郭秉蘋 9159559
王雅惠,$588755謝嘉桓=>$67,592,757,646
陳剛蘭 311
陳致真=>6932704325
林雅茹 $55黃玉禾 $454,738,551,590倪珊瑩=>$333
游宜靜,$9527275
黃聖文:$801
王聖松=>$539620004
徐美寶:$87758
游杰薇 7903
吳紋侑:$69
陳信欣=>22
高玉玄=>6759
李盈如,82266816962
黃雅音,51
陳曉盛,329574623王志育,$7,349,310,154郭函誠,$785
黃則生=>204劉馨儀=>$5
張廖振延 4
陳紫安,$5233844088
楊雅辰=>34772689
蔡宛儒 60228
李孟蓮,3695625281
林佳佩,9,433,502
陳奇筠 $1
李家賢,$1968401721
李瓊文,4,302
陳昆漢 $5陳軍妮 $722,592,328
陳君坤=>$1815391759陳克群=>$39
黃惠玟,$10王琦雨:$9,170曹姵郁,$5,924,706
汪冠廷,91188098261
藍心春,176,775
鄭鈺筠=>32,344李朝瑞 $652,696,183
王鈺婷 $17989225
丁雅琳 496030
蔡思賢:2
謝真慧:645
陳怡剛,11,568,605
吳博名=>864
李志明 $4768
陳榮穎:5339591
竇柔修,37,255,005
孫靜怡=>$874602879597陳永杰=>$9,517,709,134陳家潔=>$338,369,939
陳弘海=>3399823徐白音 $3,368
陳傑琪=>$3792668王志婷:$445,374,364,287林建豪=>$4,316
周樂蓉,17林睿姍=>$80,276
吳雅芳 328
林淑娟=>$75
林美玲=>604,791,717,856陳俞萱,$9,201,616
唐曉雯:$9
李宗生:9081586黃文辛:$37,770
張惠皓:$3
張家榮 $8林宇翔=>$652,027,079劉家凱 $787
唐菁學=>45,462,448
孫名誠,840姚淑君,$55,663,383
曾昀邦=>68015935646
吳冠廷:664938365
侯秀慧:11,357,273李志忠:$76,067,916
張雅筑 $9694268485
李盛薇:464,503
張志凱 466
葉豪綸=>88
羅雯方=>$5452045白勳新:$457,947
洪展偉,454
王怡夫,$85589
涂怡文:80,219,829
王耀文,7,025朱政勳:$9,726
陳家弘 691
劉雅雯,$9238蘇安寶 $974,611,047,713
陳美君 56,648藍合綺:$393,931,389,162
劉佩琪=>$89933353669張明蓉 $911
蔡明良 $207050403
許怡君=>9王佩芸 $763,875,724,427
陳婕妤,70,348
林仲倩,485055700
鄭世昌=>561,543,068王文依,$374,090
汪麗萍=>79132148
錢俊宏=>49982
鍾明其 933,400,975,394
丁正威:35
戴育廷:332黃怡君 $446
何世杰:$1
林敬原,5,717,943,827陳子傑:$747蔡俊宏=>$7,809,054,352
李淑如 8
陳雅婷,623,265,622
史俊凱=>$120陳怡君,$9,252王善佐=>$247,877,951
黃政儒,$1
杜詩蘭,32,122,976
宣宇軒:$30363
王冠友 623157007320侯淑慧:$747,791
陳雅云 21,477
張秀妹 374618755898
張雅娟=>40,250,088
李威玲,7927
黃思卿,4
陳韋雄,4,219
周淑惠,5
賴家慶:22375陳威廷 $727,166,332
賴邦亮=>4689740146詹佳雯:$4,592
陳淑群 65,403,806,715
李瑩成:879694159665
林雅婷:$5570077張家幸=>$65,988,964
連修昇:$1
張彥志 $5
劉鴻希:528,278,229,143
林正齊:$279699033馮秀琴 $8
蔡友民 1
陳冠珮:410
錢雅娟=>3122
張政娥=>36,769賴家弘=>$104,177,985,366
張家銘 $44
邱家維 960陳秀慧:$8
王原均:$79230790822王為如,$699
翁杰柏,$24392937061
陳麗美:$94756454269
黃偉義:$489000272743
陳華易:37652
倪靜如=>2,919,805
陳麗珠,$57001152672
葉詠瑤,$289443
陳竣虹,3,718,286蔡湘月,$43
陳英銘:81,012,003,915陳瑤芳:$25
葉俞祥:$2
劉玉孜 596156王思迪:$10,488,378,943
陳建孜=>$275041428林江雯 $60,369
艾月妮,5
黃國明,141602483
蔡緯冰 $36372246
單健豪 93,216,969
顏恩瑜,$9393
蔡瑩亨,$4393黃淑敏=>$346,334,636
陳順儀=>$758899
李承映,4121
傅珮君,44
王之玲:$5863605199陳慧芸=>$40,874,046,160
畢家綺=>49,480
林子仁=>$16043
陳巧為,4715123
林欣怡=>30彭東吉:$47,174,477,302
張佩君,2,117
李得侑:920
吳杰勳=>22,403,584,456
賴紹維,796,723
王麗美=>9
黃雅琪 675,003,725
楊佳福:610446
楊怡如=>994,900,112
蔡淑玲 $2355
趙建宇:1
馮嘉雯=>$87
林慧玲 2642039王心怡=>$3,788
林嘉芸=>$587392
郭彥君,64,559,639,322
劉和威:$2725490464
施俊凱 45
黃夙天,8
林敬富=>$65565
黃心彬,$87509605陳嘉恩,$8,719,851蔡慧君=>$5陳韻齊,$761,124,601
錢台旺,$44923771
張奕君:$9
陳鈺容:5,709,277,172
陳建宏,927035
汪佳蓉=>$26356567665
許淑惠,42
張恒其:124林于雲=>$414,726,995,451
倪人民 66387吳靜定 $8
金坤為:62,493,259,521許淑東=>$859,620
姜佩琪=>5,591,821羅世昌=>$3,374,804,740葉江亞,$97吳宏虹:$6,871,274,505
陳彥蓮 165,879,764
陳麗甫,$7王桂迪=>$557
林家福 $903248
廖嘉惠:$6
陳俊堅:$89
蔡勇志 1
張家孜,90200黃博威=>$81,434,068
陳雅婷:$3239125538
陳明杰,4,081
陳冠宏=>$539332808
鄭宇君:2,375,878,121
高少然 1,684,008張珮瑜:$51,681
陳彥行 643,449,483,227
陳美玲,1,661,456
鐘美君 6886453006
何淑娟,4,995胡佳燕,$2,793陳佑霖,$147,401
林琬婷,690儲雅玲=>$982,442,595,787
楊文青 8450476
劉明瑩:$3
阮博文:55井柏翰=>$957,330,725
張志剛,$2783347031
宋耀學:62991556
陸俊廷=>$53886
陳伊苓=>633
蔡盈枝:$834532872544
賴彥元:$743
蔡怡璇:1014681
蘇立偉=>61579
林家慶=>$3
崔淑敏,261614
陳庭瑋,8
謝千慧=>89135845
張中然,1黎佩珊=>$696,182
許文麟:13
黃偉為 78陳淑婷,$29
張志成,$9100552
黃柏源=>211王文沛 $155,785
張博孝,$639257
黃儀善:6701419
汪依婷:2000432
賴怡靜 695,263,885,884
陳立南:8,604,981
邱俊廷 $445550
魏巧如 82786915569
潘盈如 $4678430030
蔡雲昆,551,797,604,190
林昱雅=>$28532
王堯漢,5
倪芝希 $898944
葉展欣=>72934838744
孫佩芳 95,783,715,377
黃淑玲:857,406,044,232
藍彥璋 2631366345
賴瑞柏=>6828郭明慧 $82,447,358
賴剛順:57478933
柯邦筠 9312
謝惠美:965555
黃淑美:5,474陳玉士,$7
錢雅茹,$6
謝意英=>578866331442
葉夢鴻=>69,728林佳霖 $246,056,699
江秋燕:$85793宋凱元:$2,276,476,652
黃麗雯,9501401
蔡雅婷 $336427
黃淑華=>99,888,759,850汪偉智:$4,804,498
張陽偉:$11821
黃珮昆=>$227094
施伯雄,253112905594
黃培倫=>$594550
許信豪:64,307,635王怡君=>$2,704,128,326
周佳芳,$2張美奇:$9,154,858
何俊嘉,6
蔡依伯=>$534014445
王仁韻=>$9169楊玫啟=>$95,664,795,006張家妏:$8,557,712
陳冠宇,46,229,657
林慧群=>454,672,036,259
黃淑士:$65409
沈平以:3,393,734,786許秀美,$80,693,531,090
方至宸,8,228,182,941
柳文豪 87701784
王倫霞:2
林奕映:4,565,654,302林瑞妍,$976,056
黃雅心 $997088637
林立洋,$92042395088袁常順=>$3
彭靜怡,84610
顏士哲:548,745,255
許靜如=>7
黃詩虹:$3傅哲豪:$955,490,011
彭建中=>84080521
陳金博=>$75陳惠玲:$71林冠伶:$10,606,074,742
陳憶龍,74,480,082
吳詠裕 237,077
張以倫,$670845186涂秀玲,$7,834
蔡韋雄 $439156076
許佳燕 8林彥柏:$227
陳孟倫 $8730414
翁文賢:$543
黃凡桂,63971
胡平辰,2518229
陳佳玲,2
許子映,98220794315
陳麗仲,$83726065341
黃惠和,81693558戴哲維 $5,075,150,544
侯淑惠:778,662,689,507
許怡辛:$8952559
許姵來 158,878,806,453
李佳東:926,254,657,595
王惠忠=>714
賴俊剛:$3694751
吳俊良,7,769
游思賢 211290869
王岱辛,1656614
林婷婷:73447
杜欣潔:642663903109
宋孟哲:802654215191
王詩婷,905304268
莊雅泉,$4伊祥皓=>$219,244
卓佳宏:432,208,362,615
郭政勳 2069312
黃添凌 $81972鄭智妍,$61
黃阿智,$5853386
戴家瑋:$122029陳筱芸:$648
蔡其志,$9
張則博=>982
袁建謙=>96,474
吳孟英 $9973
陳智和,4,711,248
富淑芬=>$7118769531
毛柏宏:$1313592
張博恩,698葉士盈=>$516,237
陳致齊 63,618,614
黃善紋=>3576王嘉谷:$955,238,406,179
白明妍=>6,386,788庾思賢,$940,128,542,665許胤中=>$56,102,482張富倩=>$9,981,966,640
張瑞和 $861
蔡政麟,$2馬昶吉=>$674,908,679黃佳其,$5,987,413,853
謝勳岑=>1,537,591
連怡伶:$4048428204
黃彥愛:113793954蔡佳喜,$9
張軒盛,$6116129817林嘉祥 $463袁琪芸:$76
林家弘 554,771
葉靜雯 552吳怡伶 $107,587
施淑萍:76019772793
杜曉萍:6
許育儒 962,473
陳孝岑:$495380649663
林雅萍=>$857524蔡秀娟:$83,719,612
賴韋尹=>751,304,566,362
張家鑫=>24827746
洪亦韋=>69崔振玫 $9,923
李欣正=>4,855,476,387
馮思穎,33
曹雅文:3,974
湛正緯 $486733
陳玉珍 $733620李秀珍=>$908
林宛木=>6425
簡志玉 843251236187
林俊安:$24870899637
方士銘 7
鄭淑揚:13,463,703李昌雄:$593,979,672
張翔江:$275064676965
游宏儒,6389892陳俊宏=>$174,685,666,492張嘉幸:$763蔡惠君=>$58,116,309,847
黃人豪=>842645
祁泰玉 368
許力雅:729劉孟倫 $18,120,355
陳玉婷 4,935,788
林佳以=>936662724851
許詩涵=>$9林芳諭 $28,757,801,339
張紋珊,580
李宗玲=>197056林世陽=>$431,861
王明憲=>2
葉雲修,330,596,660
陳原剛 $210764
黃靜雯,291林信宏,$23
林淑華,9032342
羅仰恭=>9642427
溫欣怡 $56061
黃幼琴 362005
張隆青:1,290
趙芃君,24林信雲:$98
陳淑雲 $6132185
黃昆奇,758098
張嘉玲 382,223邱淑雲:$81,679,825
徐怡璇 $4方芝安=>$38,952,893,100
蔡俊毅=>1
翁惠君:2261381982
林士傑:58,967
黃建甫 $125283759504
吳淑順:$624674419545林奕龍=>$717,777,937,263
陳建成:2847866810
邱彥博:46011097727陳俊亦=>$99
張建志,8
陳淑芬:352587195134莊雅恩:$3
馮文賢 $12483808
吳佳俊=>65
施世昌=>$893
"""

lines = data.strip().split("\n")
# sum = 0
lst = []
for line in lines:
    # print(line)
    money = ""
    for char in line:
        if char.isdigit():
            money += char
        if ord(char) >= 0x4E00 and ord(char) <= 0x9FFF:
            # print(money.strip())
            lst.append(money)
            # sum += int(money)
            money = ""
    # sum += int(money)
    lst.append(money)
    money=""
# print(sum)
sum = 0
for i in lst:
    if i:
        sum += int(i)
print(f'sum:{sum}')

# print(f'sum:{sum(lst)}')



# # 使用正則表達式提取金額部分
# amounts = re.findall(r'\$([\d,]+)', data)

# # 將提取的金額部分轉換為整數並加總
# total_amount = sum(int(amount.replace(',', '')) for amount in amounts)

# print("總捐款金額為: ${}".format(total_amount))
