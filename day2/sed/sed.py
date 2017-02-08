#!/usr/bin/env python
import argparse, os

parser = argparse.ArgumentParser()
help_i = "edit files in place . ----------------------------- example : python sed.py -i  source_str,dest_str file"
parser.add_argument('-i', help=help_i)
parser.add_argument('file', help="input-file")
args = parser.parse_args()
place = args.i
o_file = args.file
# place传进来的参数以','为分隔符转换成列表
list_str = place.split(',')

# 以读得方式打开目标文件，再以覆盖写入的方式打开一个新的文件
with open(o_file, 'r', encoding='utf-8') as rf:
	#以行缓冲方式打开文件
    with open(o_file+'.new', 'w', encoding='utf-8', buffering=1) as wf:
        for line in rf:
            if list_str[0] in line:
                wf.write(line.replace(list_str[0], list_str[1]))
            else:
                wf.write(line)

# 这个文件存在，先删除，再重命名
if os.path.exists(o_file):
    os.remove(o_file)
    os.rename(o_file + '.new', o_file)
