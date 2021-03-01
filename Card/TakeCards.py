# -*- codeing = utf-8 -*-
#@Time: 2021/2/18 11:41
#@Name: TakeCards.py


import random
import xlwt

lis = []    #记录总数
lis5 = []   #记录5*
i = 1       #记录抽卡次数(4*)
j = 1       #记录抽卡次数(5*)
h = 1       #记录抽卡次数(大保底)
r = 0       #记录抽卡次数

a = input("是否开始？（输入‘y’开始）")
if a == "y":
    while a == "y":
        print("1.单抽         2.十连        3.一键小保底")
        b = input()

#单抽
        if b == str(1):
            c = random.randint(1, 403000)
            if c <= 2148 and c >= 1:
                if c >= 1 and c <= 1074:
                    d = "胡桃(5*)"
                    print("\033[1;33m 胡桃(5*)\033[0m")
                    lis.append(d)
                    lis5.append(d)
                    i = 1
                    j = 1
                    h = 1
                    r += 1
                elif c > 1253 and c <= 1432:
                    d = "刻晴(5*)"
                    print("\033[1;33m 刻晴(5*)\033[0m")
                    lis.append(d)
                    lis5.append(d)
                    i = 1
                    j = 1
                    h += 1
                    r += 1
                elif c > 1432 and c <= 1611:
                    d = "莫娜(5*)"
                    print("\033[1;33m 莫娜(5*)\033[0m")
                    lis.append(d)
                    lis5.append(d)
                    i = 1
                    j = 1
                    h += 1
                    r += 1
                elif c > 1611 and c <= 1790:
                    d = "七七(5*)"
                    print("\033[1;33m 七七(5*)\033[0m")
                    lis.append(d)
                    lis5.append(d)
                    i = 1
                    j = 1
                    h += 1
                    r += 1
                elif c > 1790 and c <= 1969:
                    d = "迪卢克(5*)"
                    print("\033[1;33m 迪卢克(5*)\033[0m")
                    lis.append(d)
                    lis5.append(d)
                    i = 1
                    j = 1
                    h += 1
                    r += 1
                elif c > 1969 and c <= 2148:
                    d = "琴(5*)"
                    print("\033[1;33m 琴(5*)\033[0m")
                    lis.append(d)
                    lis5.append(d)
                    i = 1
                    j = 1
                    h += 1
                    r += 1

            # 大保底
            elif h == 180:
                d = "胡桃(5*)"
                print("\033[1;33m 胡桃(5*)\033[0m")
                lis.append(d)
                lis5.append(d)
                i = 1
                j = 1
                h = 1
                r += 1
            # 小保底
            elif j == 90:
                n = random.randint(1, 10)
                if n == 1:
                    d = "刻晴(5*)"
                    print("\033[1;33m 刻晴(5*)\033[0m")
                    lis.append(d)
                    lis5.append(d)
                    i = 1
                    j = 1
                    h += 1
                    r += 1
                elif n == 2:
                    d = "莫娜(5*)"
                    print("\033[1;33m 莫娜(5*)\033[0m")
                    lis.append(d)
                    lis5.append(d)
                    i = 1
                    j = 1
                    h += 1
                    r += 1
                elif n == 3:
                    d = "七七(5*)"
                    print("\033[1;33m 七七(5*)\033[0m")
                    lis.append(d)
                    lis5.append(d)
                    i = 1
                    j = 1
                    h += 1
                    r += 1
                elif n == 4:
                    d = "迪卢克(5*)"
                    print("\033[1;33m 迪卢克(5*)\033[0m")
                    lis.append(d)
                    lis5.append(d)
                    i = 1
                    j = 1
                    h += 1
                    r += 1
                elif n == 5:
                    d = "琴(5*)"
                    print("\033[1;33m 琴(5*)\033[0m")
                    lis.append(d)
                    lis5.append(d)
                    i = 1
                    j = 1
                    h += 1
                    r += 1
                else:
                    d = "胡桃(5*)"
                    print("\033[1;33m 胡桃(5*)\033[0m")
                    lis.append(d)
                    lis5.append(d)
                    i = 1
                    j = 1
                    h = 1
                    r += 1

            elif i == 10:
                s = random.randint(1, 168)
                if s >= 1 and s <= 28:
                    d = "行秋(4*)"
                    print("\033[1;35m 行秋(4*)\033[0m")
                    lis.append(d)
                    i = 1
                    j += 1
                    h += 1
                    r += 1
                elif s > 28 and s <= 56:
                    d = "重云(4*)"
                    print("\033[1;35m 重云(4*)\033[0m")
                    lis.append(d)
                    i = 1
                    j += 1
                    h += 1
                    r += 1
                elif s > 56 and s <= 84:
                    d = "诺艾尔(4*)"
                    print("\033[1;35m 诺艾尔(4*)\033[0m")
                    lis.append(d)
                    i = 1
                    j += 1
                    h += 1
                    r += 1
                elif s > 84 and s <= 87:
                    d = "班尼特(4*)"
                    print("\033[1;35m 班尼特(4*)\033[0m")
                    lis.append(d)
                    i = 1
                    j += 1
                    h += 1
                    r += 1
                elif s > 87 and s <= 90:
                    d = "迪奥娜(4*)"
                    print("\033[1;35m 迪奥娜(4*)\033[0m")
                    lis.append(d)
                    i = 1
                    j += 1
                    h += 1
                    r += 1
                elif s > 90 and s <= 93:
                    d = "芭芭拉(4*)"
                    print("\033[1;35m 芭芭拉(4*)\033[0m")
                    lis.append(d)
                    i = 1
                    j += 1
                    h += 1
                    r += 1
                elif s > 93 and s <= 96:
                    d = "凝光(4*)"
                    print("\033[1;35m 凝光(4*)\033[0m")
                    lis.append(d)
                    i = 1
                    j += 1
                    h += 1
                    r += 1
                elif s > 96 and s <= 99:
                    d = "辛焱(4*)"
                    print("\033[1;35m 辛焱(4*)\033[0m")
                    lis.append(d)
                    i = 1
                    j += 1
                    h += 1
                    r += 1
                elif s > 99 and s <= 102:
                    d = "砂糖(4*)"
                    print("\033[1;35m 砂糖(4*)\033[0m")
                    lis.append(d)
                    i = 1
                    j += 1
                    h += 1
                    r += 1
                elif s > 102 and s <= 105:
                    d = "菲谢尔(4*)"
                    print("\033[1;35m 菲谢尔(4*)\033[0m")
                    lis.append(d)
                    i = 1
                    j += 1
                    h += 1
                    r += 1
                elif s > 105 and s <= 108:
                    d = "北斗(4*)"
                    print("\033[1;35m 北斗(4*)\033[0m")
                    lis.append(d)
                    i = 1
                    j += 1
                    h += 1
                    r += 1
                elif s > 108 and s <= 111:
                    d = "香菱(4*)"
                    print("\033[1;35m 香菱(4*)\033[0m")
                    lis.append(d)
                    i = 1
                    j += 1
                    h += 1
                    r += 1
                elif s > 111 and s <= 114:
                    d = "雷泽(4*)"
                    print("\033[1;35m 雷泽(4*)\033[0m")
                    lis.append(d)
                    i = 1
                    j += 1
                    h += 1
                    r += 1
                elif s > 114 and s <= 117:
                    d = "弓藏(4*)"
                    print("\033[1;35m 弓藏(4*)\033[0m")
                    lis.append(d)
                    i = 1
                    j += 1
                    h += 1
                    r += 1
                elif s > 117 and s <= 120:
                    d = "祭礼弓(4*)"
                    print("\033[1;35m 祭礼弓(4*)\033[0m")
                    lis.append(d)
                    i = 1
                    j += 1
                    h += 1
                    r += 1
                elif s > 120 and s <= 123:
                    d = "绝弦(4*)"
                    print("\033[1;35m 绝弦(4*)\033[0m")
                    lis.append(d)
                    i = 1
                    j += 1
                    h += 1
                    r += 1
                elif s > 123 and s <= 126:
                    d = "西风猎弓(4*)"
                    print("\033[1;35m 西风猎弓(4*)\033[0m")
                    lis.append(d)
                    i = 1
                    j += 1
                    h += 1
                    r += 1
                elif s > 126 and s <= 129:
                    d = "昭心(4*)"
                    print("\033[1;35m 昭心(4*)\033[0m")
                    lis.append(d)
                    i = 1
                    j += 1
                    h += 1
                    r += 1
                elif s > 129 and s <= 132:
                    d = "祭礼残章(4*)"
                    print("\033[1;35m 祭礼残章(4*)\033[0m")
                    lis.append(d)
                    i = 1
                    j += 1
                    h += 1
                    r += 1
                elif s > 132 and s <= 135:
                    d = "流浪乐章(4*)"
                    print("\033[1;35m 流浪乐章(4*)\033[0m")
                    lis.append(d)
                    i = 1
                    j += 1
                    h += 1
                    r += 1
                elif s > 135 and s <= 138:
                    d = "西风秘典(4*)"
                    print("\033[1;35m 西风秘典(4*)\033[0m")
                    lis.append(d)
                    i = 1
                    j += 1
                    h += 1
                    r += 1
                elif s > 138 and s <= 141:
                    d = "西风长枪(4*)"
                    print("\033[1;35m 西风长枪(4*)\033[0m")
                    lis.append(d)
                    i = 1
                    j += 1
                    h += 1
                    r += 1
                elif s > 141 and s <= 144:
                    d = "匣里灭辰(4*)"
                    print("\033[1;35m 匣里灭辰(4*)\033[0m")
                    lis.append(d)
                    i = 1
                    j += 1
                    h += 1
                    r += 1
                elif s > 144 and s <= 147:
                    d = "雨裁(4*)"
                    print("\033[1;35m 雨裁(4*)\033[0m")
                    lis.append(d)
                    i = 1
                    j += 1
                    h += 1
                    r += 1
                elif s > 147 and s <= 150:
                    d = "祭礼大剑(4*)"
                    print("\033[1;35m 祭礼大剑(4*)\033[0m")
                    lis.append(d)
                    i = 1
                    j += 1
                    h += 1
                    r += 1
                elif s > 150 and s <= 153:
                    d = "钟剑(4*)"
                    print("\033[1;35m 钟剑(4*)\033[0m")
                    lis.append(d)
                    i = 1
                    j += 1
                    h += 1
                    r += 1
                elif s > 153 and s <= 156:
                    d = "西风大剑(4*)"
                    print("\033[1;35m 西风大剑(4*)\033[0m")
                    lis.append(d)
                    i = 1
                    j += 1
                    h += 1
                    r += 1
                elif s > 156 and s <= 159:
                    d = "西风剑(4*)"
                    print("\033[1;35m 西风剑(4*)\033[0m")
                    lis.append(d)
                    i = 1
                    j += 1
                    h += 1
                    r += 1
                elif s > 159 and s <= 162:
                    d = "匣里龙吟(4*)"
                    print("\033[1;35m 匣里龙吟(4*)\033[0m")
                    lis.append(d)
                    i = 1
                    j += 1
                    h += 1
                    r += 1
                elif s > 162 and s <= 165:
                    d = "祭礼剑(4*)"
                    print("\033[1;35m 祭礼剑(4*)\033[0m")
                    lis.append(d)
                    i = 1
                    j += 1
                    h += 1
                    r += 1
                elif s > 165 and s <= 168:
                    d = "笛剑(4*)"
                    print("\033[1;35m 笛剑(4*)\033[0m")
                    lis.append(d)
                    i = 1
                    j += 1
                    h += 1
                    r += 1

            elif c > 2148 and c <= 22701:
                s = random.randint(1, 168)
                if s >= 1 and s <= 28:
                    d = "行秋(4*)"
                    print("\033[1;35m 行秋(4*)\033[0m")
                    lis.append(d)
                    i = 1
                    j += 1
                    h += 1
                    r += 1
                elif s > 28 and s <= 56:
                    d = "重云(4*)"
                    print("\033[1;35m 重云(4*)\033[0m")
                    lis.append(d)
                    i = 1
                    j += 1
                    h += 1
                    r += 1
                elif s > 56 and s <= 84:
                    d = "诺艾尔(4*)"
                    print("\033[1;35m 诺艾尔(4*)\033[0m")
                    lis.append(d)
                    i = 1
                    j += 1
                    h += 1
                    r += 1
                elif s > 84 and s <= 87:
                    d = "班尼特(4*)"
                    print("\033[1;35m 班尼特(4*)\033[0m")
                    lis.append(d)
                    i = 1
                    j += 1
                    h += 1
                    r += 1
                elif s > 87 and s <= 90:
                    d = "迪奥娜(4*)"
                    print("\033[1;35m 迪奥娜(4*)\033[0m")
                    lis.append(d)
                    i = 1
                    j += 1
                    h += 1
                    r += 1
                elif s > 90 and s <= 93:
                    d = "芭芭拉(4*)"
                    print("\033[1;35m 芭芭拉(4*)\033[0m")
                    lis.append(d)
                    i = 1
                    j += 1
                    h += 1
                    r += 1
                elif s > 93 and s <= 96:
                    d = "凝光(4*)"
                    print("\033[1;35m 凝光(4*)\033[0m")
                    lis.append(d)
                    i = 1
                    j += 1
                    h += 1
                    r += 1
                elif s > 96 and s <= 99:
                    d = "辛焱(4*)"
                    print("\033[1;35m 辛焱(4*)\033[0m")
                    lis.append(d)
                    i = 1
                    j += 1
                    h += 1
                    r += 1
                elif s > 99 and s <= 102:
                    d = "砂糖(4*)"
                    print("\033[1;35m 砂糖(4*)\033[0m")
                    lis.append(d)
                    i = 1
                    j += 1
                    h += 1
                    r += 1
                elif s > 102 and s <= 105:
                    d = "菲谢尔(4*)"
                    print("\033[1;35m 菲谢尔(4*)\033[0m")
                    lis.append(d)
                    i = 1
                    j += 1
                    h += 1
                    r += 1
                elif s > 105 and s <= 108:
                    d = "北斗(4*)"
                    print("\033[1;35m 北斗(4*)\033[0m")
                    lis.append(d)
                    i = 1
                    j += 1
                    h += 1
                    r += 1
                elif s > 108 and s <= 111:
                    d = "香菱(4*)"
                    print("\033[1;35m 香菱(4*)\033[0m")
                    lis.append(d)
                    i = 1
                    j += 1
                    h += 1
                    r += 1
                elif s > 111 and s <= 114:
                    d = "雷泽(4*)"
                    print("\033[1;35m 雷泽(4*)\033[0m")
                    lis.append(d)
                    i = 1
                    j += 1
                    h += 1
                    r += 1
                elif s > 114 and s <= 117:
                    d = "弓藏(4*)"
                    print("\033[1;35m 弓藏(4*)\033[0m")
                    lis.append(d)
                    i = 1
                    j += 1
                    h += 1
                    r += 1
                elif s > 117 and s <= 120:
                    d = "祭礼弓(4*)"
                    print("\033[1;35m 祭礼弓(4*)\033[0m")
                    lis.append(d)
                    i = 1
                    j += 1
                    h += 1
                    r += 1
                elif s > 120 and s <= 123:
                    d = "绝弦(4*)"
                    print("\033[1;35m 绝弦(4*)\033[0m")
                    lis.append(d)
                    i = 1
                    j += 1
                    h += 1
                    r += 1
                elif s > 123 and s <= 126:
                    d = "西风猎弓(4*)"
                    print("\033[1;35m 西风猎弓(4*)\033[0m")
                    lis.append(d)
                    i = 1
                    j += 1
                    h += 1
                    r += 1
                elif s > 126 and s <= 129:
                    d = "昭心(4*)"
                    print("\033[1;35m 昭心(4*)\033[0m")
                    lis.append(d)
                    i = 1
                    j += 1
                    h += 1
                    r += 1
                elif s > 129 and s <= 132:
                    d = "祭礼残章(4*)"
                    print("\033[1;35m 祭礼残章(4*)\033[0m")
                    lis.append(d)
                    i = 1
                    j += 1
                    h += 1
                    r += 1
                elif s > 132 and s <= 135:
                    d = "流浪乐章(4*)"
                    print("\033[1;35m 流浪乐章(4*)\033[0m")
                    lis.append(d)
                    i = 1
                    j += 1
                    h += 1
                    r += 1
                elif s > 135 and s <= 138:
                    d = "西风秘典(4*)"
                    print("\033[1;35m 西风秘典(4*)\033[0m")
                    lis.append(d)
                    i = 1
                    j += 1
                    h += 1
                    r += 1
                elif s > 138 and s <= 141:
                    d = "西风长枪(4*)"
                    print("\033[1;35m 西风长枪(4*)\033[0m")
                    lis.append(d)
                    i = 1
                    j += 1
                    h += 1
                    r += 1
                elif s > 141 and s <= 144:
                    d = "匣里灭辰(4*)"
                    print("\033[1;35m 匣里灭辰(4*)\033[0m")
                    lis.append(d)
                    i = 1
                    j += 1
                    h += 1
                    r += 1
                elif s > 144 and s <= 147:
                    d = "雨裁(4*)"
                    print("\033[1;35m 雨裁(4*)\033[0m")
                    lis.append(d)
                    i = 1
                    j += 1
                    h += 1
                    r += 1
                elif s > 147 and s <= 150:
                    d = "祭礼大剑(4*)"
                    print("\033[1;35m 祭礼大剑(4*)\033[0m")
                    lis.append(d)
                    i = 1
                    j += 1
                    h += 1
                    r += 1
                elif s > 150 and s <= 153:
                    d = "钟剑(4*)"
                    print("\033[1;35m 钟剑(4*)\033[0m")
                    lis.append(d)
                    i = 1
                    j += 1
                    h += 1
                    r += 1
                elif s > 153 and s <= 156:
                    d = "西风大剑(4*)"
                    print("\033[1;35m 西风大剑(4*)\033[0m")
                    lis.append(d)
                    i = 1
                    j += 1
                    h += 1
                    r += 1
                elif s > 156 and s <= 159:
                    d = "西风剑(4*)"
                    print("\033[1;35m 西风剑(4*)\033[0m")
                    lis.append(d)
                    i = 1
                    j += 1
                    h += 1
                    r += 1
                elif s > 159 and s <= 162:
                    d = "匣里龙吟(4*)"
                    print("\033[1;35m 匣里龙吟(4*)\033[0m")
                    lis.append(d)
                    i = 1
                    j += 1
                    h += 1
                    r += 1
                elif s > 162 and s <= 165:
                    d = "祭礼剑(4*)"
                    print("\033[1;35m 祭礼剑(4*)\033[0m")
                    lis.append(d)
                    i = 1
                    j += 1
                    h += 1
                    r += 1
                elif s > 165 and s <= 168:
                    d = "笛剑(4*)"
                    print("\033[1;35m 笛剑(4*)\033[0m")
                    lis.append(d)
                    i = 1
                    j += 1
                    h += 1
                    r += 1
            else:
                t = random.randint(1, 13)
                if t == 1:
                    d = "弹弓(3*)"
                    print("\033[1;34m 弹弓(3*)\033[0m")
                    lis.append(d)
                    i += 1
                    j += 1
                    h += 1
                    r += 1
                elif t == 2:
                    d = "神射手之誓(3*)"
                    print("\033[1;34m 神射手之誓(3*)\033[0m")
                    lis.append(d)
                    i += 1
                    j += 1
                    h += 1
                    r += 1
                elif t == 3:
                    d = "鸦羽弓(3*)"
                    print("\033[1;34m 鸦羽弓(3*)\033[0m")
                    lis.append(d)
                    i += 1
                    j += 1
                    h += 1
                    r += 1
                elif t == 4:
                    d = "翡玉法球(3*)"
                    print("\033[1;34m 翡玉法球(3*)\033[0m")
                    lis.append(d)
                    i += 1
                    j += 1
                    h += 1
                    r += 1
                elif t == 5:
                    d = "讨龙英雄谭(3*)"
                    print("\033[1;34m 讨龙英雄谭(3*)\033[0m")
                    lis.append(d)
                    i += 1
                    j += 1
                    h += 1
                    r += 1
                elif t == 6:
                    d = "魔导绪论(3*)"
                    print("\033[1;34m 魔导绪论(3*)\033[0m")
                    lis.append(d)
                    i += 1
                    j += 1
                    h += 1
                    r += 1
                elif t == 7:
                    d = "黑缨枪(3*)"
                    print("\033[1;34m 黑缨枪(3*)\033[0m")
                    lis.append(d)
                    i += 1
                    j += 1
                    h += 1
                    r += 1
                elif t == 8:
                    d = "以理服人(3*)"
                    print("\033[1;34m 以理服人(3*)\033[0m")
                    lis.append(d)
                    i += 1
                    j += 1
                    h += 1
                    r += 1
                elif t == 9:
                    d = "沐浴龙血的剑(3*)"
                    print("\033[1;34m 沐浴龙血的剑(3*)\033[0m")
                    lis.append(d)
                    i += 1
                    j += 1
                    h += 1
                    r += 1
                elif t == 10:
                    d = "铁影阔剑(3*)"
                    print("\033[1;34m 铁影阔剑(3*)\033[0m")
                    lis.append(d)
                    i += 1
                    j += 1
                    h += 1
                    r += 1
                elif t == 11:
                    d = "飞天御剑(3*)"
                    print("\033[1;34m 飞天御剑(3*)\033[0m")
                    lis.append(d)
                    i += 1
                    j += 1
                    h += 1
                    r += 1
                elif t == 12:
                    d = "黎明神剑(3*)"
                    print("\033[1;34m 黎明神剑(3*)\033[0m")
                    lis.append(d)
                    i += 1
                    j += 1
                    h += 1
                    r += 1
                elif t == 13:
                    d = "冷刃(3*)"
                    print("\033[1;34m 冷刃(3*)\033[0m")
                    lis.append(d)
                    i += 1
                    j += 1
                    h += 1
                    r += 1

#十连
        elif b == str(2):
            for k in range(0, 10):
                c = random.randint(1, 403000)
                if c <= 2148 and c >= 1:
                    if c >= 1 and c <= 1074:
                        d = "胡桃(5*)"
                        print("\033[1;33m 胡桃(5*)\033[0m")
                        lis.append(d)
                        lis5.append(d)
                        i = 1
                        j = 1
                        h = 1
                        r += 1
                    elif c > 1253 and c <= 1432:
                        d = "刻晴(5*)"
                        print("\033[1;33m 刻晴(5*)\033[0m")
                        lis.append(d)
                        lis5.append(d)
                        i = 1
                        j = 1
                        h += 1
                        r += 1
                    elif c > 1432 and c <= 1611:
                        d = "莫娜(5*)"
                        print("\033[1;33m 莫娜(5*)\033[0m")
                        lis.append(d)
                        lis5.append(d)
                        i = 1
                        j = 1
                        h += 1
                        r += 1
                    elif c > 1611 and c <= 1790:
                        d = "七七(5*)"
                        print("\033[1;33m 七七(5*)\033[0m")
                        lis.append(d)
                        lis5.append(d)
                        i = 1
                        j = 1
                        h += 1
                        r += 1
                    elif c > 1790 and c <= 1969:
                        d = "迪卢克(5*)"
                        print("\033[1;33m 迪卢克(5*)\033[0m")
                        lis.append(d)
                        lis5.append(d)
                        i = 1
                        j = 1
                        h += 1
                        r += 1
                    elif c > 1969 and c <= 2148:
                        d = "琴(5*)"
                        print("\033[1;33m 琴(5*)\033[0m")
                        lis.append(d)
                        lis5.append(d)
                        i = 1
                        j = 1
                        h += 1
                        r += 1

                # 大保底
                elif h == 180:
                    d = "胡桃(5*)"
                    print("\033[1;33m 胡桃(5*)\033[0m")
                    lis.append(d)
                    lis5.append(d)
                    i = 1
                    j = 1
                    h = 1
                    r += 1
                # 小保底
                elif j == 90:
                    n = random.randint(1, 10)
                    if n == 1:
                        d = "刻晴(5*)"
                        print("\033[1;33m 刻晴(5*)\033[0m")
                        lis.append(d)
                        lis5.append(d)
                        i = 1
                        j = 1
                        h += 1
                        r += 1
                    elif n == 2:
                        d = "莫娜(5*)"
                        print("\033[1;33m 莫娜(5*)\033[0m")
                        lis.append(d)
                        lis5.append(d)
                        i = 1
                        j = 1
                        h += 1
                        r += 1
                    elif n == 3:
                        d = "七七(5*)"
                        print("\033[1;33m 七七(5*)\033[0m")
                        lis.append(d)
                        lis5.append(d)
                        i = 1
                        j = 1
                        h += 1
                        r += 1
                    elif n == 4:
                        d = "迪卢克(5*)"
                        print("\033[1;33m 迪卢克(5*)\033[0m")
                        lis.append(d)
                        lis5.append(d)
                        i = 1
                        j = 1
                        h += 1
                        r += 1
                    elif n == 5:
                        d = "琴(5*)"
                        print("\033[1;33m 琴(5*)\033[0m")
                        lis.append(d)
                        lis5.append(d)
                        i = 1
                        j = 1
                        h += 1
                        r += 1
                    else:
                        d = "胡桃(5*)"
                        print("\033[1;33m 胡桃(5*)\033[0m")
                        lis.append(d)
                        lis5.append(d)
                        i = 1
                        j = 1
                        h = 1
                        r += 1

                elif i == 10:
                    s = random.randint(1, 168)
                    if s >= 1 and s <= 28:
                        d = "行秋(4*)"
                        print("\033[1;35m 行秋(4*)\033[0m")
                        lis.append(d)
                        i = 1
                        j += 1
                        h += 1
                        r += 1
                    elif s > 28 and s <= 56:
                        d = "重云(4*)"
                        print("\033[1;35m 重云(4*)\033[0m")
                        lis.append(d)
                        i = 1
                        j += 1
                        h += 1
                        r += 1
                    elif s > 56 and s <= 84:
                        d = "诺艾尔(4*)"
                        print("\033[1;35m 诺艾尔(4*)\033[0m")
                        lis.append(d)
                        i = 1
                        j += 1
                        h += 1
                        r += 1
                    elif s > 84 and s <= 87:
                        d = "班尼特(4*)"
                        print("\033[1;35m 班尼特(4*)\033[0m")
                        lis.append(d)
                        i = 1
                        j += 1
                        h += 1
                        r += 1
                    elif s > 87 and s <= 90:
                        d = "迪奥娜(4*)"
                        print("\033[1;35m 迪奥娜(4*)\033[0m")
                        lis.append(d)
                        i = 1
                        j += 1
                        h += 1
                        r += 1
                    elif s > 90 and s <= 93:
                        d = "芭芭拉(4*)"
                        print("\033[1;35m 芭芭拉(4*)\033[0m")
                        lis.append(d)
                        i = 1
                        j += 1
                        h += 1
                        r += 1
                    elif s > 93 and s <= 96:
                        d = "凝光(4*)"
                        print("\033[1;35m 凝光(4*)\033[0m")
                        lis.append(d)
                        i = 1
                        j += 1
                        h += 1
                        r += 1
                    elif s > 96 and s <= 99:
                        d = "辛焱(4*)"
                        print("\033[1;35m 辛焱(4*)\033[0m")
                        lis.append(d)
                        i = 1
                        j += 1
                        h += 1
                        r += 1
                    elif s > 99 and s <= 102:
                        d = "砂糖(4*)"
                        print("\033[1;35m 砂糖(4*)\033[0m")
                        lis.append(d)
                        i = 1
                        j += 1
                        h += 1
                        r += 1
                    elif s > 102 and s <= 105:
                        d = "菲谢尔(4*)"
                        print("\033[1;35m 菲谢尔(4*)\033[0m")
                        lis.append(d)
                        i = 1
                        j += 1
                        h += 1
                        r += 1
                    elif s > 105 and s <= 108:
                        d = "北斗(4*)"
                        print("\033[1;35m 北斗(4*)\033[0m")
                        lis.append(d)
                        i = 1
                        j += 1
                        h += 1
                        r += 1
                    elif s > 108 and s <= 111:
                        d = "香菱(4*)"
                        print("\033[1;35m 香菱(4*)\033[0m")
                        lis.append(d)
                        i = 1
                        j += 1
                        h += 1
                        r += 1
                    elif s > 111 and s <= 114:
                        d = "雷泽(4*)"
                        print("\033[1;35m 雷泽(4*)\033[0m")
                        lis.append(d)
                        i = 1
                        j += 1
                        h += 1
                        r += 1
                    elif s > 114 and s <= 117:
                        d = "弓藏(4*)"
                        print("\033[1;35m 弓藏(4*)\033[0m")
                        lis.append(d)
                        i = 1
                        j += 1
                        h += 1
                        r += 1
                    elif s > 117 and s <= 120:
                        d = "祭礼弓(4*)"
                        print("\033[1;35m 祭礼弓(4*)\033[0m")
                        lis.append(d)
                        i = 1
                        j += 1
                        h += 1
                        r += 1
                    elif s > 120 and s <= 123:
                        d = "绝弦(4*)"
                        print("\033[1;35m 绝弦(4*)\033[0m")
                        lis.append(d)
                        i = 1
                        j += 1
                        h += 1
                        r += 1
                    elif s > 123 and s <= 126:
                        d = "西风猎弓(4*)"
                        print("\033[1;35m 西风猎弓(4*)\033[0m")
                        lis.append(d)
                        i = 1
                        j += 1
                        h += 1
                        r += 1
                    elif s > 126 and s <= 129:
                        d = "昭心(4*)"
                        print("\033[1;35m 昭心(4*)\033[0m")
                        lis.append(d)
                        i = 1
                        j += 1
                        h += 1
                        r += 1
                    elif s > 129 and s <= 132:
                        d = "祭礼残章(4*)"
                        print("\033[1;35m 祭礼残章(4*)\033[0m")
                        lis.append(d)
                        i = 1
                        j += 1
                        h += 1
                        r += 1
                    elif s > 132 and s <= 135:
                        d = "流浪乐章(4*)"
                        print("\033[1;35m 流浪乐章(4*)\033[0m")
                        lis.append(d)
                        i = 1
                        j += 1
                        h += 1
                        r += 1
                    elif s > 135 and s <= 138:
                        d = "西风秘典(4*)"
                        print("\033[1;35m 西风秘典(4*)\033[0m")
                        lis.append(d)
                        i = 1
                        j += 1
                        h += 1
                        r += 1
                    elif s > 138 and s <= 141:
                        d = "西风长枪(4*)"
                        print("\033[1;35m 西风长枪(4*)\033[0m")
                        lis.append(d)
                        i = 1
                        j += 1
                        h += 1
                        r += 1
                    elif s > 141 and s <= 144:
                        d = "匣里灭辰(4*)"
                        print("\033[1;35m 匣里灭辰(4*)\033[0m")
                        lis.append(d)
                        i = 1
                        j += 1
                        h += 1
                        r += 1
                    elif s > 144 and s <= 147:
                        d = "雨裁(4*)"
                        print("\033[1;35m 雨裁(4*)\033[0m")
                        lis.append(d)
                        i = 1
                        j += 1
                        h += 1
                        r += 1
                    elif s > 147 and s <= 150:
                        d = "祭礼大剑(4*)"
                        print("\033[1;35m 祭礼大剑(4*)\033[0m")
                        lis.append(d)
                        i = 1
                        j += 1
                        h += 1
                        r += 1
                    elif s > 150 and s <= 153:
                        d = "钟剑(4*)"
                        print("\033[1;35m 钟剑(4*)\033[0m")
                        lis.append(d)
                        i = 1
                        j += 1
                        h += 1
                        r += 1
                    elif s > 153 and s <= 156:
                        d = "西风大剑(4*)"
                        print("\033[1;35m 西风大剑(4*)\033[0m")
                        lis.append(d)
                        i = 1
                        j += 1
                        h += 1
                        r += 1
                    elif s > 156 and s <= 159:
                        d = "西风剑(4*)"
                        print("\033[1;35m 西风剑(4*)\033[0m")
                        lis.append(d)
                        i = 1
                        j += 1
                        h += 1
                        r += 1
                    elif s > 159 and s <= 162:
                        d = "匣里龙吟(4*)"
                        print("\033[1;35m 匣里龙吟(4*)\033[0m")
                        lis.append(d)
                        i = 1
                        j += 1
                        h += 1
                        r += 1
                    elif s > 162 and s <= 165:
                        d = "祭礼剑(4*)"
                        print("\033[1;35m 祭礼剑(4*)\033[0m")
                        lis.append(d)
                        i = 1
                        j += 1
                        h += 1
                        r += 1
                    elif s > 165 and s <= 168:
                        d = "笛剑(4*)"
                        print("\033[1;35m 笛剑(4*)\033[0m")
                        lis.append(d)
                        i = 1
                        j += 1
                        h += 1
                        r += 1

                elif c > 2148 and c <= 22701:
                    s = random.randint(1, 168)
                    if s >= 1 and s <= 28:
                        d = "行秋(4*)"
                        print("\033[1;35m 行秋(4*)\033[0m")
                        lis.append(d)
                        i = 1
                        j += 1
                        h += 1
                        r += 1
                    elif s > 28 and s <= 56:
                        d = "重云(4*)"
                        print("\033[1;35m 重云(4*)\033[0m")
                        lis.append(d)
                        i = 1
                        j += 1
                        h += 1
                        r += 1
                    elif s > 56 and s <= 84:
                        d = "诺艾尔(4*)"
                        print("\033[1;35m 诺艾尔(4*)\033[0m")
                        lis.append(d)
                        i = 1
                        j += 1
                        h += 1
                        r += 1
                    elif s > 84 and s <= 87:
                        d = "班尼特(4*)"
                        print("\033[1;35m 班尼特(4*)\033[0m")
                        lis.append(d)
                        i = 1
                        j += 1
                        h += 1
                        r += 1
                    elif s > 87 and s <= 90:
                        d = "迪奥娜(4*)"
                        print("\033[1;35m 迪奥娜(4*)\033[0m")
                        lis.append(d)
                        i = 1
                        j += 1
                        h += 1
                        r += 1
                    elif s > 90 and s <= 93:
                        d = "芭芭拉(4*)"
                        print("\033[1;35m 芭芭拉(4*)\033[0m")
                        lis.append(d)
                        i = 1
                        j += 1
                        h += 1
                        r += 1
                    elif s > 93 and s <= 96:
                        d = "凝光(4*)"
                        print("\033[1;35m 凝光(4*)\033[0m")
                        lis.append(d)
                        i = 1
                        j += 1
                        h += 1
                        r += 1
                    elif s > 96 and s <= 99:
                        d = "辛焱(4*)"
                        print("\033[1;35m 辛焱(4*)\033[0m")
                        lis.append(d)
                        i = 1
                        j += 1
                        h += 1
                        r += 1
                    elif s > 99 and s <= 102:
                        d = "砂糖(4*)"
                        print("\033[1;35m 砂糖(4*)\033[0m")
                        lis.append(d)
                        i = 1
                        j += 1
                        h += 1
                        r += 1
                    elif s > 102 and s <= 105:
                        d = "菲谢尔(4*)"
                        print("\033[1;35m 菲谢尔(4*)\033[0m")
                        lis.append(d)
                        i = 1
                        j += 1
                        h += 1
                        r += 1
                    elif s > 105 and s <= 108:
                        d = "北斗(4*)"
                        print("\033[1;35m 北斗(4*)\033[0m")
                        lis.append(d)
                        i = 1
                        j += 1
                        h += 1
                        r += 1
                    elif s > 108 and s <= 111:
                        d = "香菱(4*)"
                        print("\033[1;35m 香菱(4*)\033[0m")
                        lis.append(d)
                        i = 1
                        j += 1
                        h += 1
                        r += 1
                    elif s > 111 and s <= 114:
                        d = "雷泽(4*)"
                        print("\033[1;35m 雷泽(4*)\033[0m")
                        lis.append(d)
                        i = 1
                        j += 1
                        h += 1
                        r += 1
                    elif s > 114 and s <= 117:
                        d = "弓藏(4*)"
                        print("\033[1;35m 弓藏(4*)\033[0m")
                        lis.append(d)
                        i = 1
                        j += 1
                        h += 1
                        r += 1
                    elif s > 117 and s <= 120:
                        d = "祭礼弓(4*)"
                        print("\033[1;35m 祭礼弓(4*)\033[0m")
                        lis.append(d)
                        i = 1
                        j += 1
                        h += 1
                        r += 1
                    elif s > 120 and s <= 123:
                        d = "绝弦(4*)"
                        print("\033[1;35m 绝弦(4*)\033[0m")
                        lis.append(d)
                        i = 1
                        j += 1
                        h += 1
                        r += 1
                    elif s > 123 and s <= 126:
                        d = "西风猎弓(4*)"
                        print("\033[1;35m 西风猎弓(4*)\033[0m")
                        lis.append(d)
                        i = 1
                        j += 1
                        h += 1
                        r += 1
                    elif s > 126 and s <= 129:
                        d = "昭心(4*)"
                        print("\033[1;35m 昭心(4*)\033[0m")
                        lis.append(d)
                        i = 1
                        j += 1
                        h += 1
                        r += 1
                    elif s > 129 and s <= 132:
                        d = "祭礼残章(4*)"
                        print("\033[1;35m 祭礼残章(4*)\033[0m")
                        lis.append(d)
                        i = 1
                        j += 1
                        h += 1
                        r += 1
                    elif s > 132 and s <= 135:
                        d = "流浪乐章(4*)"
                        print("\033[1;35m 流浪乐章(4*)\033[0m")
                        lis.append(d)
                        i = 1
                        j += 1
                        h += 1
                        r += 1
                    elif s > 135 and s <= 138:
                        d = "西风秘典(4*)"
                        print("\033[1;35m 西风秘典(4*)\033[0m")
                        lis.append(d)
                        i = 1
                        j += 1
                        h += 1
                        r += 1
                    elif s > 138 and s <= 141:
                        d = "西风长枪(4*)"
                        print("\033[1;35m 西风长枪(4*)\033[0m")
                        lis.append(d)
                        i = 1
                        j += 1
                        h += 1
                        r += 1
                    elif s > 141 and s <= 144:
                        d = "匣里灭辰(4*)"
                        print("\033[1;35m 匣里灭辰(4*)\033[0m")
                        lis.append(d)
                        i = 1
                        j += 1
                        h += 1
                        r += 1
                    elif s > 144 and s <= 147:
                        d = "雨裁(4*)"
                        print("\033[1;35m 雨裁(4*)\033[0m")
                        lis.append(d)
                        i = 1
                        j += 1
                        h += 1
                        r += 1
                    elif s > 147 and s <= 150:
                        d = "祭礼大剑(4*)"
                        print("\033[1;35m 祭礼大剑(4*)\033[0m")
                        lis.append(d)
                        i = 1
                        j += 1
                        h += 1
                        r += 1
                    elif s > 150 and s <= 153:
                        d = "钟剑(4*)"
                        print("\033[1;35m 钟剑(4*)\033[0m")
                        lis.append(d)
                        i = 1
                        j += 1
                        h += 1
                        r += 1
                    elif s > 153 and s <= 156:
                        d = "西风大剑(4*)"
                        print("\033[1;35m 西风大剑(4*)\033[0m")
                        lis.append(d)
                        i = 1
                        j += 1
                        h += 1
                        r += 1
                    elif s > 156 and s <= 159:
                        d = "西风剑(4*)"
                        print("\033[1;35m 西风剑(4*)\033[0m")
                        lis.append(d)
                        i = 1
                        j += 1
                        h += 1
                        r += 1
                    elif s > 159 and s <= 162:
                        d = "匣里龙吟(4*)"
                        print("\033[1;35m 匣里龙吟(4*)\033[0m")
                        lis.append(d)
                        i = 1
                        j += 1
                        h += 1
                        r += 1
                    elif s > 162 and s <= 165:
                        d = "祭礼剑(4*)"
                        print("\033[1;35m 祭礼剑(4*)\033[0m")
                        lis.append(d)
                        i = 1
                        j += 1
                        h += 1
                        r += 1
                    elif s > 165 and s <= 168:
                        d = "笛剑(4*)"
                        print("\033[1;35m 笛剑(4*)\033[0m")
                        lis.append(d)
                        i = 1
                        j += 1
                        h += 1
                        r += 1
                else:
                    t = random.randint(1, 13)
                    if t == 1:
                        d = "弹弓(3*)"
                        print("\033[1;34m 弹弓(3*)\033[0m")
                        lis.append(d)
                        i += 1
                        j += 1
                        h += 1
                        r += 1
                    elif t == 2:
                        d = "神射手之誓(3*)"
                        print("\033[1;34m 神射手之誓(3*)\033[0m")
                        lis.append(d)
                        i += 1
                        j += 1
                        h += 1
                        r += 1
                    elif t == 3:
                        d = "鸦羽弓(3*)"
                        print("\033[1;34m 鸦羽弓(3*)\033[0m")
                        lis.append(d)
                        i += 1
                        j += 1
                        h += 1
                        r += 1
                    elif t == 4:
                        d = "翡玉法球(3*)"
                        print("\033[1;34m 翡玉法球(3*)\033[0m")
                        lis.append(d)
                        i += 1
                        j += 1
                        h += 1
                        r += 1
                    elif t == 5:
                        d = "讨龙英雄谭(3*)"
                        print("\033[1;34m 讨龙英雄谭(3*)\033[0m")
                        lis.append(d)
                        i += 1
                        j += 1
                        h += 1
                        r += 1
                    elif t == 6:
                        d = "魔导绪论(3*)"
                        print("\033[1;34m 魔导绪论(3*)\033[0m")
                        lis.append(d)
                        i += 1
                        j += 1
                        h += 1
                        r += 1
                    elif t == 7:
                        d = "黑缨枪(3*)"
                        print("\033[1;34m 黑缨枪(3*)\033[0m")
                        lis.append(d)
                        i += 1
                        j += 1
                        h += 1
                        r += 1
                    elif t == 8:
                        d = "以理服人(3*)"
                        print("\033[1;34m 以理服人(3*)\033[0m")
                        lis.append(d)
                        i += 1
                        j += 1
                        h += 1
                        r += 1
                    elif t == 9:
                        d = "沐浴龙血的剑(3*)"
                        print("\033[1;34m 沐浴龙血的剑(3*)\033[0m")
                        lis.append(d)
                        i += 1
                        j += 1
                        h += 1
                        r += 1
                    elif t == 10:
                        d = "铁影阔剑(3*)"
                        print("\033[1;34m 铁影阔剑(3*)\033[0m")
                        lis.append(d)
                        i += 1
                        j += 1
                        h += 1
                        r += 1
                    elif t == 11:
                        d = "飞天御剑(3*)"
                        print("\033[1;34m 飞天御剑(3*)\033[0m")
                        lis.append(d)
                        i += 1
                        j += 1
                        h += 1
                        r += 1
                    elif t == 12:
                        d = "黎明神剑(3*)"
                        print("\033[1;34m 黎明神剑(3*)\033[0m")
                        lis.append(d)
                        i += 1
                        j += 1
                        h += 1
                        r += 1
                    elif t == 13:
                        d = "冷刃(3*)"
                        print("\033[1;34m 冷刃(3*)\033[0m")
                        lis.append(d)
                        i += 1
                        j += 1
                        h += 1
                        r += 1

#直接保底
        elif b == str(3):
            for m in range(1, 91):
                c = random.randint(1, 403000)
                if c <= 2148 and c >= 1:
                    if c >= 1 and c <= 1074:
                        d = "胡桃(5*)"
                        print("\033[1;33m 胡桃(5*)\033[0m")
                        lis.append(d)
                        lis5.append(d)
                        i = 1
                        j = 1
                        h = 1
                        r += 1
                    elif c > 1253 and c <= 1432:
                        d = "刻晴(5*)"
                        print("\033[1;33m 刻晴(5*)\033[0m")
                        lis.append(d)
                        lis5.append(d)
                        i = 1
                        j = 1
                        h += 1
                        r += 1
                    elif c > 1432 and c <= 1611:
                        d = "莫娜(5*)"
                        print("\033[1;33m 莫娜(5*)\033[0m")
                        lis.append(d)
                        lis5.append(d)
                        i = 1
                        j = 1
                        h += 1
                        r += 1
                    elif c > 1611 and c <= 1790:
                        d = "七七(5*)"
                        print("\033[1;33m 七七(5*)\033[0m")
                        lis.append(d)
                        lis5.append(d)
                        i = 1
                        j = 1
                        h += 1
                        r += 1
                    elif c > 1790 and c <= 1969:
                        d = "迪卢克(5*)"
                        print("\033[1;33m 迪卢克(5*)\033[0m")
                        lis.append(d)
                        lis5.append(d)
                        i = 1
                        j = 1
                        h += 1
                        r += 1
                    elif c > 1969 and c <= 2148:
                        d = "琴(5*)"
                        print("\033[1;33m 琴(5*)\033[0m")
                        lis.append(d)
                        lis5.append(d)
                        i = 1
                        j = 1
                        h += 1
                        r += 1

#大保底
                elif h == 180:
                    d = "胡桃(5*)"
                    print("\033[1;33m 胡桃(5*)\033[0m")
                    lis.append(d)
                    lis5.append(d)
                    i = 1
                    j = 1
                    h = 1
                    r += 1
#小保底
                elif j == 90:
                    n = random.randint(1, 10)
                    if n == 1:
                        d = "刻晴(5*)"
                        print("\033[1;33m 刻晴(5*)\033[0m")
                        lis.append(d)
                        lis5.append(d)
                        i = 1
                        j = 1
                        h += 1
                        r += 1
                    elif n == 2:
                        d = "莫娜(5*)"
                        print("\033[1;33m 莫娜(5*)\033[0m")
                        lis.append(d)
                        lis5.append(d)
                        i = 1
                        j = 1
                        h += 1
                        r += 1
                    elif n == 3:
                        d = "七七(5*)"
                        print("\033[1;33m 七七(5*)\033[0m")
                        lis.append(d)
                        lis5.append(d)
                        i = 1
                        j = 1
                        h += 1
                        r += 1
                    elif n == 4:
                        d = "迪卢克(5*)"
                        print("\033[1;33m 迪卢克(5*)\033[0m")
                        lis.append(d)
                        lis5.append(d)
                        i = 1
                        j = 1
                        h += 1
                        r += 1
                    elif n == 5:
                        d = "琴(5*)"
                        print("\033[1;33m 琴(5*)\033[0m")
                        lis.append(d)
                        lis5.append(d)
                        i = 1
                        j = 1
                        h += 1
                        r += 1
                    else:
                        d = "胡桃(5*)"
                        print("\033[1;33m 胡桃(5*)\033[0m")
                        lis.append(d)
                        lis5.append(d)
                        i = 1
                        j = 1
                        h = 1
                        r += 1
#保底出4*
                elif i == 10:
                    s = random.randint(1, 168)
                    if s >= 1 and s <= 28:
                        d = "行秋(4*)"
                        print("\033[1;35m 行秋(4*)\033[0m")
                        lis.append(d)
                        i = 1
                        j += 1
                        h += 1
                        r += 1
                    elif s > 28 and s <= 56:
                        d = "重云(4*)"
                        print("\033[1;35m 重云(4*)\033[0m")
                        lis.append(d)
                        i = 1
                        j += 1
                        h += 1
                        r += 1
                    elif s > 56 and s <= 84:
                        d = "诺艾尔(4*)"
                        print("\033[1;35m 诺艾尔(4*)\033[0m")
                        lis.append(d)
                        i = 1
                        j += 1
                        h += 1
                        r += 1
                    elif s > 84 and s <= 87:
                        d = "班尼特(4*)"
                        print("\033[1;35m 班尼特(4*)\033[0m")
                        lis.append(d)
                        i = 1
                        j += 1
                        h += 1
                        r += 1
                    elif s > 87 and s <= 90:
                        d = "迪奥娜(4*)"
                        print("\033[1;35m 迪奥娜(4*)\033[0m")
                        lis.append(d)
                        i = 1
                        j += 1
                        h += 1
                        r += 1
                    elif s > 90 and s <= 93:
                        d = "芭芭拉(4*)"
                        print("\033[1;35m 芭芭拉(4*)\033[0m")
                        lis.append(d)
                        i = 1
                        j += 1
                        h += 1
                        r += 1
                    elif s > 93 and s <= 96:
                        d = "凝光(4*)"
                        print("\033[1;35m 凝光(4*)\033[0m")
                        lis.append(d)
                        i = 1
                        j += 1
                        h += 1
                        r += 1
                    elif s > 96 and s <= 99:
                        d = "辛焱(4*)"
                        print("\033[1;35m 辛焱(4*)\033[0m")
                        lis.append(d)
                        i = 1
                        j += 1
                        h += 1
                        r += 1
                    elif s > 99 and s <= 102:
                        d = "砂糖(4*)"
                        print("\033[1;35m 砂糖(4*)\033[0m")
                        lis.append(d)
                        i = 1
                        j += 1
                        h += 1
                        r += 1
                    elif s > 102 and s <= 105:
                        d = "菲谢尔(4*)"
                        print("\033[1;35m 菲谢尔(4*)\033[0m")
                        lis.append(d)
                        i = 1
                        j += 1
                        h += 1
                        r += 1
                    elif s > 105 and s <= 108:
                        d = "北斗(4*)"
                        print("\033[1;35m 北斗(4*)\033[0m")
                        lis.append(d)
                        i = 1
                        j += 1
                        h += 1
                        r += 1
                    elif s > 108 and s <= 111:
                        d = "香菱(4*)"
                        print("\033[1;35m 香菱(4*)\033[0m")
                        lis.append(d)
                        i = 1
                        j += 1
                        h += 1
                        r += 1
                    elif s > 111 and s <= 114:
                        d = "雷泽(4*)"
                        print("\033[1;35m 雷泽(4*)\033[0m")
                        lis.append(d)
                        i = 1
                        j += 1
                        h += 1
                        r += 1
                    elif s > 114 and s <= 117:
                        d = "弓藏(4*)"
                        print("\033[1;35m 弓藏(4*)\033[0m")
                        lis.append(d)
                        i = 1
                        j += 1
                        h += 1
                        r += 1
                    elif s > 117 and s <= 120:
                        d = "祭礼弓(4*)"
                        print("\033[1;35m 祭礼弓(4*)\033[0m")
                        lis.append(d)
                        i = 1
                        j += 1
                        h += 1
                        r += 1
                    elif s > 120 and s <= 123:
                        d = "绝弦(4*)"
                        print("\033[1;35m 绝弦(4*)\033[0m")
                        lis.append(d)
                        i = 1
                        j += 1
                        h += 1
                        r += 1
                    elif s > 123 and s <= 126:
                        d = "西风猎弓(4*)"
                        print("\033[1;35m 西风猎弓(4*)\033[0m")
                        lis.append(d)
                        i = 1
                        j += 1
                        h += 1
                        r += 1
                    elif s > 126 and s <= 129:
                        d = "昭心(4*)"
                        print("\033[1;35m 昭心(4*)\033[0m")
                        lis.append(d)
                        i = 1
                        j += 1
                        h += 1
                        r += 1
                    elif s > 129 and s <= 132:
                        d = "祭礼残章(4*)"
                        print("\033[1;35m 祭礼残章(4*)\033[0m")
                        lis.append(d)
                        i = 1
                        j += 1
                        h += 1
                        r += 1
                    elif s > 132 and s <= 135:
                        d = "流浪乐章(4*)"
                        print("\033[1;35m 流浪乐章(4*)\033[0m")
                        lis.append(d)
                        i = 1
                        j += 1
                        h += 1
                        r += 1
                    elif s > 135 and s <= 138:
                        d = "西风秘典(4*)"
                        print("\033[1;35m 西风秘典(4*)\033[0m")
                        lis.append(d)
                        i = 1
                        j += 1
                        h += 1
                        r += 1
                    elif s > 138 and s <= 141:
                        d = "西风长枪(4*)"
                        print("\033[1;35m 西风长枪(4*)\033[0m")
                        lis.append(d)
                        i = 1
                        j += 1
                        h += 1
                        r += 1
                    elif s > 141 and s <= 144:
                        d = "匣里灭辰(4*)"
                        print("\033[1;35m 匣里灭辰(4*)\033[0m")
                        lis.append(d)
                        i = 1
                        j += 1
                        h += 1
                        r += 1
                    elif s > 144 and s <= 147:
                        d = "雨裁(4*)"
                        print("\033[1;35m 雨裁(4*)\033[0m")
                        lis.append(d)
                        i = 1
                        j += 1
                        h += 1
                        r += 1
                    elif s > 147 and s <= 150:
                        d = "祭礼大剑(4*)"
                        print("\033[1;35m 祭礼大剑(4*)\033[0m")
                        lis.append(d)
                        i = 1
                        j += 1
                        h += 1
                        r += 1
                    elif s > 150 and s <= 153:
                        d = "钟剑(4*)"
                        print("\033[1;35m 钟剑(4*)\033[0m")
                        lis.append(d)
                        i = 1
                        j += 1
                        h += 1
                        r += 1
                    elif s > 153 and s <= 156:
                        d = "西风大剑(4*)"
                        print("\033[1;35m 西风大剑(4*)\033[0m")
                        lis.append(d)
                        i = 1
                        j += 1
                        h += 1
                        r += 1
                    elif s > 156 and s <= 159:
                        d = "西风剑(4*)"
                        print("\033[1;35m 西风剑(4*)\033[0m")
                        lis.append(d)
                        i = 1
                        j += 1
                        h += 1
                        r += 1
                    elif s > 159 and s <= 162:
                        d = "匣里龙吟(4*)"
                        print("\033[1;35m 匣里龙吟(4*)\033[0m")
                        lis.append(d)
                        i = 1
                        j += 1
                        h += 1
                        r += 1
                    elif s > 162 and s <= 165:
                        d = "祭礼剑(4*)"
                        print("\033[1;35m 祭礼剑(4*)\033[0m")
                        lis.append(d)
                        i = 1
                        j += 1
                        h += 1
                        r += 1
                    elif s > 165 and s <= 168:
                        d = "笛剑(4*)"
                        print("\033[1;35m 笛剑(4*)\033[0m")
                        lis.append(d)
                        i = 1
                        j += 1
                        h += 1
                        r += 1

#非保底出四星

                elif c > 2148 and c <= 22701 :
                    s = random.randint(1, 168)
                    if s >= 1 and s <= 28:
                        d = "行秋(4*)"
                        print("\033[1;35m 行秋(4*)\033[0m")
                        lis.append(d)
                        i = 1
                        j += 1
                        h += 1
                        r += 1
                    elif s > 28 and s <= 56:
                        d = "重云(4*)"
                        print("\033[1;35m 重云(4*)\033[0m")
                        lis.append(d)
                        i = 1
                        j += 1
                        h += 1
                        r += 1
                    elif s > 56 and s <= 84:
                        d = "诺艾尔(4*)"
                        print("\033[1;35m 诺艾尔(4*)\033[0m")
                        lis.append(d)
                        i = 1
                        j += 1
                        h += 1
                        r += 1
                    elif s > 84 and s <= 87:
                        d = "班尼特(4*)"
                        print("\033[1;35m 班尼特(4*)\033[0m")
                        lis.append(d)
                        i = 1
                        j += 1
                        h += 1
                        r += 1
                    elif s > 87 and s <= 90:
                        d = "迪奥娜(4*)"
                        print("\033[1;35m 迪奥娜(4*)\033[0m")
                        lis.append(d)
                        i = 1
                        j += 1
                        h += 1
                        r += 1
                    elif s > 90 and s <= 93:
                        d = "芭芭拉(4*)"
                        print("\033[1;35m 芭芭拉(4*)\033[0m")
                        lis.append(d)
                        i = 1
                        j += 1
                        h += 1
                        r += 1
                    elif s > 93 and s <= 96:
                        d = "凝光(4*)"
                        print("\033[1;35m 凝光(4*)\033[0m")
                        lis.append(d)
                        i = 1
                        j += 1
                        h += 1
                        r += 1
                    elif s > 96 and s <= 99:
                        d = "辛焱(4*)"
                        print("\033[1;35m 辛焱(4*)\033[0m")
                        lis.append(d)
                        i = 1
                        j += 1
                        h += 1
                        r += 1
                    elif s > 99 and s <= 102:
                        d = "砂糖(4*)"
                        print("\033[1;35m 砂糖(4*)\033[0m")
                        lis.append(d)
                        i = 1
                        j += 1
                        h += 1
                        r += 1
                    elif s > 102 and s <= 105:
                        d = "菲谢尔(4*)"
                        print("\033[1;35m 菲谢尔(4*)\033[0m")
                        lis.append(d)
                        i = 1
                        j += 1
                        h += 1
                        r += 1
                    elif s > 105 and s <= 108:
                        d = "北斗(4*)"
                        print("\033[1;35m 北斗(4*)\033[0m")
                        lis.append(d)
                        i = 1
                        j += 1
                        h += 1
                        r += 1
                    elif s > 108 and s <= 111:
                        d = "香菱(4*)"
                        print("\033[1;35m 香菱(4*)\033[0m")
                        lis.append(d)
                        i = 1
                        j += 1
                        h += 1
                        r += 1
                    elif s > 111 and s <= 114:
                        d = "雷泽(4*)"
                        print("\033[1;35m 雷泽(4*)\033[0m")
                        lis.append(d)
                        i = 1
                        j += 1
                        h += 1
                        r += 1
                    elif s > 114 and s <= 117:
                        d = "弓藏(4*)"
                        print("\033[1;35m 弓藏(4*)\033[0m")
                        lis.append(d)
                        i = 1
                        j += 1
                        h += 1
                        r += 1
                    elif s > 117 and s <= 120:
                        d = "祭礼弓(4*)"
                        print("\033[1;35m 祭礼弓(4*)\033[0m")
                        lis.append(d)
                        i = 1
                        j += 1
                        h += 1
                        r += 1
                    elif s > 120 and s <= 123:
                        d = "绝弦(4*)"
                        print("\033[1;35m 绝弦(4*)\033[0m")
                        lis.append(d)
                        i = 1
                        j += 1
                        h += 1
                        r += 1
                    elif s > 123 and s <= 126:
                        d = "西风猎弓(4*)"
                        print("\033[1;35m 西风猎弓(4*)\033[0m")
                        lis.append(d)
                        i = 1
                        j += 1
                        h += 1
                        r += 1
                    elif s > 126 and s <= 129:
                        d = "昭心(4*)"
                        print("\033[1;35m 昭心(4*)\033[0m")
                        lis.append(d)
                        i = 1
                        j += 1
                        h += 1
                        r += 1
                    elif s > 129 and s <= 132:
                        d = "祭礼残章(4*)"
                        print("\033[1;35m 祭礼残章(4*)\033[0m")
                        lis.append(d)
                        i = 1
                        j += 1
                        h += 1
                        r += 1
                    elif s > 132 and s <= 135:
                        d = "流浪乐章(4*)"
                        print("\033[1;35m 流浪乐章(4*)\033[0m")
                        lis.append(d)
                        i = 1
                        j += 1
                        h += 1
                        r += 1
                    elif s > 135 and s <= 138:
                        d = "西风秘典(4*)"
                        print("\033[1;35m 西风秘典(4*)\033[0m")
                        lis.append(d)
                        i = 1
                        j += 1
                        h += 1
                        r += 1
                    elif s > 138 and s <= 141:
                        d = "西风长枪(4*)"
                        print("\033[1;35m 西风长枪(4*)\033[0m")
                        lis.append(d)
                        i = 1
                        j += 1
                        h += 1
                        r += 1
                    elif s > 141 and s <= 144:
                        d = "匣里灭辰(4*)"
                        print("\033[1;35m 匣里灭辰(4*)\033[0m")
                        lis.append(d)
                        i = 1
                        j += 1
                        h += 1
                        r += 1
                    elif s > 144 and s <= 147:
                        d = "雨裁(4*)"
                        print("\033[1;35m 雨裁(4*)\033[0m")
                        lis.append(d)
                        i = 1
                        j += 1
                        h += 1
                        r += 1
                    elif s > 147 and s <= 150:
                        d = "祭礼大剑(4*)"
                        print("\033[1;35m 祭礼大剑(4*)\033[0m")
                        lis.append(d)
                        i = 1
                        j += 1
                        h += 1
                        r += 1
                    elif s > 150 and s <= 153:
                        d = "钟剑(4*)"
                        print("\033[1;35m 钟剑(4*)\033[0m")
                        lis.append(d)
                        i = 1
                        j += 1
                        h += 1
                        r += 1
                    elif s > 153 and s <= 156:
                        d = "西风大剑(4*)"
                        print("\033[1;35m 西风大剑(4*)\033[0m")
                        lis.append(d)
                        i = 1
                        j += 1
                        h += 1
                        r += 1
                    elif s > 156 and s <= 159:
                        d = "西风剑(4*)"
                        print("\033[1;35m 西风剑(4*)\033[0m")
                        lis.append(d)
                        i = 1
                        j += 1
                        h += 1
                        r += 1
                    elif s > 159 and s <= 162:
                        d = "匣里龙吟(4*)"
                        print("\033[1;35m 匣里龙吟(4*)\033[0m")
                        lis.append(d)
                        i = 1
                        j += 1
                        h += 1
                        r += 1
                    elif s > 162 and s <= 165:
                        d = "祭礼剑(4*)"
                        print("\033[1;35m 祭礼剑(4*)\033[0m")
                        lis.append(d)
                        i = 1
                        j += 1
                        h += 1
                        r += 1
                    elif s > 165 and s <= 168:
                        d = "笛剑(4*)"
                        print("\033[1;35m 笛剑(4*)\033[0m")
                        lis.append(d)
                        i = 1
                        j += 1
                        h += 1
                        r += 1
                else:
                    t = random.randint(1, 13)
                    if t == 1:
                        d = "弹弓(3*)"
                        print("\033[1;34m 弹弓(3*)\033[0m")
                        lis.append(d)
                        i += 1
                        j += 1
                        h += 1
                        r += 1
                    elif t == 2:
                        d = "神射手之誓(3*)"
                        print("\033[1;34m 神射手之誓(3*)\033[0m")
                        lis.append(d)
                        i += 1
                        j += 1
                        h += 1
                        r += 1
                    elif t == 3:
                        d = "鸦羽弓(3*)"
                        print("\033[1;34m 鸦羽弓(3*)\033[0m")
                        lis.append(d)
                        i += 1
                        j += 1
                        h += 1
                        r += 1
                    elif t == 4:
                        d = "翡玉法球(3*)"
                        print("\033[1;34m 翡玉法球(3*)\033[0m")
                        lis.append(d)
                        i += 1
                        j += 1
                        h += 1
                        r += 1
                    elif t == 5:
                        d = "讨龙英雄谭(3*)"
                        print("\033[1;34m 讨龙英雄谭(3*)\033[0m")
                        lis.append(d)
                        i += 1
                        j += 1
                        h += 1
                        r += 1
                    elif t == 6:
                        d = "魔导绪论(3*)"
                        print("\033[1;34m 魔导绪论(3*)\033[0m")
                        lis.append(d)
                        i += 1
                        j += 1
                        h += 1
                        r += 1
                    elif t == 7:
                        d = "黑缨枪(3*)"
                        print("\033[1;34m 黑缨枪(3*)\033[0m")
                        lis.append(d)
                        i += 1
                        j += 1
                        h += 1
                        r += 1
                    elif t == 8:
                        d = "以理服人(3*)"
                        print("\033[1;34m 以理服人(3*)\033[0m")
                        lis.append(d)
                        i += 1
                        j += 1
                        h += 1
                        r += 1
                    elif t == 9:
                        d = "沐浴龙血的剑(3*)"
                        print("\033[1;34m 沐浴龙血的剑(3*)\033[0m")
                        lis.append(d)
                        i += 1
                        j += 1
                        h += 1
                        r += 1
                    elif t == 10:
                        d = "铁影阔剑(3*)"
                        print("\033[1;34m 铁影阔剑(3*)\033[0m")
                        lis.append(d)
                        i += 1
                        j += 1
                        h += 1
                        r += 1
                    elif t == 11:
                        d = "飞天御剑(3*)"
                        print("\033[1;34m 飞天御剑(3*)\033[0m")
                        lis.append(d)
                        i += 1
                        j += 1
                        h += 1
                        r += 1
                    elif t == 12:
                        d = "黎明神剑(3*)"
                        print("\033[1;34m 黎明神剑(3*)\033[0m")
                        lis.append(d)
                        i += 1
                        j += 1
                        h += 1
                        r += 1
                    elif t == 13:
                        d = "冷刃(3*)"
                        print("\033[1;34m 冷刃(3*)\033[0m")
                        lis.append(d)
                        i += 1
                        j += 1
                        h += 1
                        r += 1


        print("")
        print("已抽卡次数：%d"%(int(r)))
        print("共消耗原石：%d"%(int(r) * 160))
        print("")
        e = input("是否展示抽卡记录？")
        if e == "y":
            for m in lis:
                print(m)
        p = input("展示获得5*？")
        if p == "y":
            for q in lis5:
                print(q)

        print("")
        a = input("再来？")
else:
    print("好吧")
print("溜了！")