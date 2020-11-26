# -*-codeing = utf-8 -*-
# @Time:2020/11/239:39
# @Author : lemonade1977
# @File : analysis_test.py
# @software : PyCharm
import sys
import string

key_word = {'main': 1, 'int': 2, 'if': 4, 'char': 3, 'else': 5, 'return': 8, 'void': 9, 'while': 7}
special_word = {'*': 24, '/': 25, ';': 34, ':': 33, ',': 32, '{': 30, '}': 31, '[': 28, ']': 29, '(': 26, ')': 27}
operate_word = {'=': 21, '+': 22, '-': 23, '<': 36, '>': 35, '!': 40}
oprate_two = {'>=': 37, '<=': 38, '==': 29, '!=': 40}
p = 0


def filter(file_name):
    try:
        fp_read = open(file_name, 'r')
        fp_write = open('fliter.txt', 'w')
        sign = 0
        notes = 0

        while True:
            read = fp_read.readline()
            if not read:
                break
            length = len(read)
            i = -1
            p = 0
            while i < length - 1:
                i += 1
                if notes == 1:
                    while True:
                        if read[i] == "*" and read[i + 1] == '/':
                            notes = 0
                            break
                        elif i == length - 1:
                            p = 1
                            break
                        i += 1
                    if p == 1:
                        break
                    i += 1
                elif read[i] == '"':
                    if sign == 0:
                        sign = 1
                        fp_write.write(' ')
                        fp_write.write(read[i])
                    else:
                        sign = 0
                        fp_write.write(read[i])
                        fp_write.write(' ')
                elif read[i] == '/' and read[i + 1] == '*':
                    notes = 1
                    i = i + 2
                    while True:
                        if read[i] == "*" and read[i + 1] == '/':
                            notes = 0
                            break
                        elif i == length - 1:
                            p = 1
                            break
                        i += 1
                    if p == 1:
                        break
                    i += 1
                elif read[i] == '/' and read[i + 1] == '/':
                    fp_write.write('\n')
                    break
                elif read[i] in special_word and sign == 0:
                    # print(read[i])
                    fp_write.write(' ')
                    fp_write.write(read[i])
                    fp_write.write(' ')
                    continue
                elif read[i] in operate_word and read[i - 1] not in operate_word and read[
                    i + 1] not in operate_word and sign == 0:
                    # print(read[i])
                    fp_write.write(' ')
                    fp_write.write(read[i])
                    fp_write.write(' ')
                    continue
                elif read[i] in operate_word and read[i + 1] not in operate_word and sign == 0:
                    # print(read[i])
                    fp_write.write(read[i])
                    fp_write.write(' ')
                    continue
                elif read[i] in operate_word and read[i - 1] not in operate_word and sign == 0:
                    # print(read[i])
                    fp_write.write(' ')
                    fp_write.write(read[i])
                    continue
                else:
                    fp_write.write(read[i])

        fp_write.write('#')
    except Exception:
        print("ERROR CODE!")


def word_mate(words):
    if words in key_word:
        print(words, end='')
        print(':', end='')
        print(key_word.get(words))
    elif words in special_word:
        print(words, end='')
        print(':', end='')
        print(special_word.get(words))
    elif words in operate_word:
        print(words, end='')
        print(':', end='')
        print(operate_word.get(words))
    elif words.isdigit():
        print(words, end='')
        print(':', end='')
        print('int')
    elif words in oprate_two:
        print(words, end='')
        print(':', end='')
        print(oprate_two.get(words))
    elif words.isidentifier():
        print(words, end='')
        print(':', end='')
        print('ID')
    else:
        print('qqqqq')



    # else:
    #     i = 0
    #     length = len(words)
    #     if words[i] in operate_word:
    #         if words[i + 1] in operate_word:
    #             p = words[i] + words[i + 1]
    #             if p in oprate_two:
    #                 print(p, end='')
    #                 print(':', end='')
    #                 print(oprate_two.get(p))
    #     elif words[i] == '\"' or '\'':
    #         print(words, end='')
    #         print(':', end='')
    #         print('50')
    #     else:
    #         print(words, end='')
    #         print(':', end='')
    #         print('10')


def process(file_name):
    try:
        fp_read = open(file_name, 'r')
        fp_write = open('result.txt', 'w')
        lines = fp_read.readlines()
        length_lines = len(lines)
        k = -1
        p = 0
        n = 0
        while k < length_lines - 1:
            k += 1
            line = lines[k]
            i = -1
            j = 0
            temp = ''
            sign = 0
            length = len(line)
            while i < length - 1:
                i += 1

                if line[i] == "\"":

                    if n == 0:
                        n = 1
                        j = i + 1
                    else:

                        n = 0
                    if n == 1:
                        continue
                    elif n == 0 and j != 0:
                        temp = line[j:i]
                        print(temp,end='')
                        print(':',end='')
                        print('STRING')
                        # word_mate(temp)
                        continue
                elif line[i] == ' ' or line[i] == '\n':
                    if n == 0:
                        if sign == 1:
                            temp = line[j:i]
                            # print(temp)
                            word_mate(temp)
                            sign = 0
                        else:
                            sign = 0
                        continue
                    else:
                        continue
                elif line[i] != ' ' or line[i] == '\n':
                    if n == 0:
                        if sign == 0:
                            j = i
                            sign = 1
                        else:
                            sign = 1
                    else:
                        continue
                # if line[i] == "\"":
                #     if p == 0:
                #         p = 1
                #     else:
                #         p = 0



    except Exception:
        print("ERROR")

        # for words in line.split():
        #     if words in key_word:
        #         print(words,end='')
        #         print(':', end='')
        #         print(key_word.get(words))
        #     elif words in special_word:
        #         print(words,end='')
        #         print(':', end='')
        #         print(special_word.get(words))
        #     elif words in operate_word:
        #         print(words,end='')
        #         print(':', end='')
        #         print(operate_word.get(words))
        #     elif words.isdigit():
        #         print(words,end='')
        #         print(':', end='')
        #         print('int')
        #     else:
        #         i=0
        #         length = len(words)
        #         if words[i] in operate_word:
        #             if words[i+1] in operate_word:
        #                 p = words[i]+words[i+1]
        #                 if p in oprate_two:
        #                     print(p, end='')
        #                     print(':', end='')
        #                     print(oprate_two.get(p))
        #         elif words[i] == '\"' or '\'':
        #             print(words, end='')
        #             print(':', end='')
        #             print('50')
        #         else:
        #             print(words, end='')
        #             print(':', end='')
        #             print('10')


def main():

    print()
    # filter('test.txt')
    # process('fliter.txt')
    # fp_read = open('test.txt', 'r')
    # read = fp_read.read()
    # lenfth = len(read)
    # i = -1
    # while i<lenfth-1:
    #     i = i+1
    #     print(read[i],end='')




if __name__ == '__main__':
    main()
