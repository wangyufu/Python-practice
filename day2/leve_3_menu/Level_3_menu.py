#!/usr/bin/env python
menu = {
    '英雄联盟':
        {
            '网通区': {
                '比尔吉沃特': {},
                '德玛西亚': {},
                '无畏先锋': {},
            },
            '电信区': {
                '艾欧尼亚': {},
                '祖安': {},
                '诺克萨斯': {},
            }
        },
    'FIFA_Online3':
        {
            '网通区': {
                '华北网通': {},
            },
            '电信区': {
                '华东电信': {},
                '华南电信': {},
                '西南电信': {},
            }
        },
    'NBA2K_Online':
        {
            '网通区': {
                '玫瑰花园': {},
            },
            '电信区': {
                '联合中心': {},
                '美航球馆': {},
                '斯台普斯': {},
            }
        },
}

print('Input information view to the next level,\
 type b or B back at the next higher level, the input q or Q from the menu.\n')
# 当前状态
current_layer = menu
# 每选择一级都存在这个列表里
layers = [menu]

while True:
    for x in current_layer:
        print(x)
    choice = input('>>: ').strip()
    if choice in current_layer:
        layers.append(current_layer)
        current_layer = current_layer[choice]
    elif choice == 'b' or choice == 'B':
        # 列表中只有一个值时，提示已经在最上级
        if len(layers) > 1:
            current_layer = layers[-1]
            layers.pop()
        else:
            print('\nThere is no at the next higher level\n')
    elif choice == 'q' or choice == 'Q':
        break
    else:
        print('\nPlease enter the correct information\n')