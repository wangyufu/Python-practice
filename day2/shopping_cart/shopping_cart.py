#!/usr/bin/env python
cart = []
product = [['iphone7', 6500], ['macbook', 12000], ['pythonbook', 66], ['bike', 999], ['coffee', 31]]
# 第二列最长的字符串
two_row = max([len(x[0]) for x in product])

while True:
    gongzi = input('salary>: ').strip()
    # 判断工资输入的是数字还是其它字符
    if gongzi.isdigit():
        gongzi = int(gongzi)
        break
    else:
        print("Please enter the correct salary.")

while True:
    # 表头和列表的第二列以最长字符串左对齐
    print("number", "\t", "product".ljust(two_row), "cost")
    for k, v in enumerate(product):
        print(k, "\t\t", v[0].ljust(two_row), v[1])
    print("Please enter the article number or enter exit.")
    xuanzhe = input('>>: ').strip()
    if xuanzhe != "":
        # 输入负数时isdigit函数用认为‘-’是特殊字符不是输入
        if (xuanzhe.startswith('-') and xuanzhe[1:] or xuanzhe).isdigit():
            xuanzhe = int(xuanzhe)
            if xuanzhe < len(product) and xuanzhe >= 0:
                if product[xuanzhe][1] > gongzi:
                    print('cannot afford this product, need %d' % (product[xuanzhe][1] - gongzi))
                else:
                    gongzi -= product[xuanzhe][1]
                    print('added %s into your shopping cart , your current balance is %d'\
                          % (product[xuanzhe][0], gongzi))
                    cart.append(product[xuanzhe])
            else:
                print("Please enter the correct article number.")
        elif xuanzhe == 'exit':
            total_price = 0
            for c in cart:
                print(c[0], c[1])
                total_price += c[1]
            print('total_price: ', total_price)
            break
    else:
        print("The input value is empty, please enter again.\n")




