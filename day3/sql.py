#!/usr/bin/env python
import os, sys

staff_list = []
filter_list = []
where_list = []
# 把列表的索引值定义赋值
staff_id, name, age, phone, dept, enroll_date = range(6)
# head元组作用是判断列名是否有效
head = ('staff_id', 'name', 'age', 'phone', 'dept', 'enroll_date')
# operator元组作用是判断操作符是否有效
operator = ('<', '=', '>', 'like')


def where(command):
    # 如果没有where子句，就直接返回原列表
    if (len(sys.argv) == 5 or len(sys.argv) == 7) and (command == 'select' or command == 'update'):
        where_list.extend(staff_list)
        return where_list

    # select和update的命令位置不一样，把列表的索引值定义赋值
    if command == 'select':
        head_arg, operator_arg, str_arg = range(6, 9)
    elif command == 'update':
        head_arg, operator_arg, str_arg = range(8, 11)
    for line in staff_list:
        # select指定列名称时使用下面的判断
        if sys.argv[2] != '*' and command == 'select':
            if sys.argv[7] == '<':
                if int(line[sys.argv[2].split(',').index(sys.argv[6])]) < int(sys.argv[8]):
                    where_list.append(line)
            elif sys.argv[7] == '>':
                if int(line[sys.argv[2].split(',').index(sys.argv[6])]) > int(sys.argv[8]):
                    where_list.append(line)
            elif sys.argv[7] == '=':
                if line[sys.argv[2].split(',').index(sys.argv[6])] == sys.argv[8]:
                    where_list.append(line)
            elif sys.argv[7] == 'like':
                if line[sys.argv[2].split(',').index(sys.argv[6])].find(sys.argv[8]) != -1:
                    where_list.append(line)
        # update和select所有列时使用下面的判断
        else:
            if sys.argv[operator_arg] == '<':
                if int(line[eval(sys.argv[head_arg])]) < int(sys.argv[str_arg]):
                    where_list.append(line)
            elif sys.argv[operator_arg] == '>':
                if int(line[eval(sys.argv[head_arg])]) > int(sys.argv[str_arg]):
                    where_list.append(line)
            elif sys.argv[operator_arg] == '=':
                if line[eval(sys.argv[head_arg])] == sys.argv[str_arg]:
                    where_list.append(line)
            elif sys.argv[operator_arg] == 'like':
                if line[eval(sys.argv[head_arg])].find(sys.argv[str_arg]) != -1:
                    where_list.append(line)
    return where_list


def save_new_file():
    if os.path.exists('staff_table'):
        os.remove('staff_table')
        os.rename('staff_table.new', 'staff_table')


def select():
    global staff_list
    count = 0

    # 如果列名是指定的，需要一条判断，并把列名称的值过滤出来存到filter_list表里
    if sys.argv[2].split(',') == [x for x in sys.argv[2].split(',') if x in head]:
        for line in staff_list:
            filter_list.append([line[eval(field)] for field in sys.argv[2].split(',')])
        # staff_list指向filter_list是为了避免下面的重复代码
        staff_list = filter_list
    elif sys.argv[2] == '*':
        pass
    else:
        print('Please enter the right field')
        sys.exit()

    try:
        if (len(sys.argv) == 5 or len(sys.argv) == 9) \
                and (sys.argv[3] == 'from' and sys.argv[4] == 'staff_table') \
                or (sys.argv[5] == 'where' and sys.argv[6] in head and sys.argv[7] in operator):
            # where函数会返回一个选取后数据列表
            for line in where(sys.argv[1]):
                print(' '.join(line))
                count += 1
            print('\nTotal of %s rows' % count)
        else:
            print('Please enter the right field')
    except:
        print('Please enter the right field')


def delete():
    if len(sys.argv) == 8 and sys.argv[2] == 'from' and sys.argv[4] == 'where' and sys.argv[5] == 'staff_id' and \
            sys.argv[6] == '=':
        with open('staff_table.new', 'w', encoding='utf-8') as wf:
            count = 0
            for line in staff_list:
                # 值不等于这行数据的staff_id
                if sys.argv[7] != line[staff_id]:
                    wf.write(','.join(line) + '\n')
                elif sys.argv[7] == line[staff_id]:
                    count += 1
                    print('Delete the success')
        # count=0，值跟数据的staff_id都不匹配
        if count == 0:
            print('without this data')
        save_new_file()
    else:
        print('Please enter the right field')


def insert():
    if len(sys.argv) == 6 and sys.argv[2] == 'into' and sys.argv[3] == 'staff_table' and sys.argv[4] == 'values':
        with open('staff_table', 'w', encoding='utf-8') as wf:
            # staff_list的所有phone存到phone_list列表中
            phone_list = [x[phone] for x in staff_list]
            # 再把values的phone也添加进来
            phone_list.append(sys.argv[5].split(',')[2])
            # 利用set函数，判断是否重复
            if len(phone_list) == len(set(phone_list)):
                # 找到最后一行的staff_id加1
                wf.write('{0}{1}\n'.format(int(staff_list[-1][staff_id]) + 1, ',' + sys.argv[5]))
                print('Successful writing')
            else:
                print('phone repeat')
    else:
        print('Please enter the right field')


def update():
    try:
        if (len(sys.argv) == 7 or len(sys.argv) == 11) and (sys.argv[2] == 'staff_table' and sys.argv[3] == 'set' \
                and sys.argv[4] in head and sys.argv[5] == '=') or (sys.argv[7] == 'where' and sys.argv[8] in head \
                and sys.argv[9] in operator):
            with open('staff_table.new', 'w', encoding='utf-8') as wf:
                count = 0
                for line in staff_list:
                    # 如果line在where函数返回的列表里，就替换列值
                    if line in where(sys.argv[1]):
                        line[eval(sys.argv[4])] = sys.argv[6]
                        count += 1
                    wf.write(','.join(line) + '\n')
                # where函数返回也可能是空列表，count如果不为0就是已经成功修改了
                if count != 0:
                    print('Successful changed')
                else:
                    print('There is no matching condition')
                save_new_file()
        else:
            print('Please enter the right field')
    except:
        print('Please enter the right field')

with open('staff_table', 'r', encoding='utf-8') as rf:
    # 将staff_table每行逗号分隔转成列表，再每个列表添加到staff_list中
    for line in rf:
        staff_list.append(line.strip().split(','))

if 4 < len(sys.argv) < 12:
    if sys.argv[1] == 'select':
        select()
    elif sys.argv[1] == 'delete':
        delete()
    elif sys.argv[1] == 'insert':
        insert()
    elif sys.argv[1] == 'update':
        update()
else:
    print('Please enter the right field')