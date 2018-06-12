#!/usr/bin/python
# -*- coding:utf-8 -*-
"""
@author:Leo
@contact:lipf0627@163.com
@file:algo_string
@time:2018/6/12 11:02
@desc:
"""


class Algo_string:

    @staticmethod
    def delete_duplicate_words(str):
        '''删除字符串中的重复字符'''
        str_new = ''
        str_new += str[0]
        for i in range(1, len(str)):
            for j in range(len(str_new)):
                if str_new[j] == str[i]:
                    break
                if j == (len(str_new) - 1):
                    str_new += str[i]

        return str_new


    @staticmethod
    def get_rolling_str(str):
        '''获取字符串中的回文，如abcab中包含的回文：abca、bcab，即首末字符相同'''
        str_list = []

        for i in range(len(str)):
            str_new = ''
            str_new += str[i]
            for j in range(i+1, len(str)):
                str_new += str[j]
                if str_new[0] == str[j]:
                    str_list.append(str_new)
                    break

        return str_list






print(Algo_string.delete_duplicate_words('jflksdjfldsj'))
print(Algo_string.get_rolling_str('abcadb'))