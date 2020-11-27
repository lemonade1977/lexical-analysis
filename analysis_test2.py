# -*-codeing = utf-8 -*-
# @Time:2020/11/2515:14
# @Author : lemonade1977
# @File : analysis_test2.py
# @software : PyCharm
import sys
import string
# 存放需要识别的关键字符或字符串的字典
key_word = {'main': 1, 'int': 2, 'if': 4, 'char': 3, 'else': 5, 'return': 8, 'void': 9, 'while': 7}
special_word = {'*': 24, '/': 25, ';': 34, ':': 33, ',': 32, '{': 30, '}': 31, '[': 28, ']': 29, '(': 26, ')': 27}
operate_word = {'=': 21, '+': 22, '-': 23, '<': 36, '>': 35, '!': 40}
oprate_two = {'>=': 37, '<=': 38, '==': 29, '!=': 40}
def process(file_name):
    try:
        fp_read = open(file_name, 'r')  # 打开文件，只读
        fp_write = open('result.txt', 'w')  # 打开文件，只写
        read = fp_read.read()
        length = len(read)  # 获取 read的长度
        i = -1
        notes1 = 0  # /*的标志，当notes1为1时，/*后面的字符都跳过直到遇到*/
        notes2 = 0  # //的标志，当notes2为1时，//后面的字符都跳过知道遇到\n（换行）
        j = 0  # 起始切片标志，当遇到 " 时，将read[i+1]当前的i+1赋给j。在第二次遇到 " 时就用read[j:i]将双引号中的字符串提取出来
        sign = 0  # 双引号的标志，当sign为1时，说明前面以读过的是左引号，为0则表示前面读过右引号
        while i < length - 1:  # 逐个读取字符
            i += 1
            # 忽略注释
            if read[i] == '/' and read[i + 1] == '*':
                notes1 = 1
                i += 1
            elif read[i] == '*' and read[i + 1] == '/':
                notes1 = 0
                i += 1
            elif read[i] == '/' and read[i + 1] == '/':
                notes2 = 1
                i += 1
            elif read[i] == '\n':
                if notes2 == 1:
                    notes2 = 0
            elif notes1 == 1 or notes2 == 1:
                continue
            # 读取到 "
            elif read[i] == '"':
                if sign == 0:
                    sign = 1
                    j = i + 1
                else:
                    sign = 0
                    temp = read[j:i]
                    print('(', temp, ':', 50, ')', file=fp_write)  # file=fp_write可以将print的内容输入到文件中
            # 遇到空格、换行、制表符同样跳过
            elif read[i] == ' ' or read[i] == '\n' or read[i] == '\t':
                continue
            # 如果读到的是字母，如果其后面接的是数字或是字母则将其一起读取出来，匹配为变量
            elif sign == 0 and read[i].isalpha():
                temp = ''
                while i != length:
                    if read[i].isalpha() or read[i].isdigit():
                        temp = temp + read[i]
                        i += 1
                    else:
                        i -= 1
                        break
                if temp in key_word:
                    # 如果匹配到在关键字字典中，则匹配为关键字
                    print('(', temp, ':', key_word.get(temp), ')', file=fp_write)
                else:
                    print('(', temp, ':', 10, ')', file=fp_write)
            # 如果读到的是数字则将其后面的数字一起读取出来，匹配为整数
            elif sign == 0 and read[i].isdigit():
                temp = ''
                while i != length:
                    if read[i].isdigit():
                        temp = temp + read[i]
                        i += 1
                    else:
                        i -= 1
                        break
                print('(', temp, ':', 20, ')', file=fp_write)
            # 将剩余的字符跟字典进行匹配
            elif sign == 0 and read[i] in special_word:
                # 如果匹配到在边界符中，则匹配为边界符
                print('(', read[i], ':', special_word.get(read[i]), ')', file=fp_write)
            elif sign == 0 and read[i] in operate_word:
                # 如果匹配为运算符，如果其紧接的下一个也为运算符，则匹配为双目运算符，否则为单目运算符
                if read[i + 1] in operate_word:
                    temp = ''
                    temp = read[i] + read[i + 1]
                    print('(', temp, ':', oprate_two.get(temp), ')', file=fp_write)
                else:
                    print('(', read[i], ':', operate_word.get(read[i]), ')', file=fp_write)
            else:
                # 其余没有匹配到的字符则将其种别码置为-1，表示不在关键字符表中
                if sign == 0:
                    print('(', read[i], ':', -1, ')', file=fp_write)
    except Exception:
        print("ERROR !")
def main():
    process('test.txt')
if __name__ == '__main__':
    main()
