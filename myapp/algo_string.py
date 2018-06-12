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

    #删除字符串中的重复字符
    @staticmethod
    def delete_duplicate_words(str):
        str_new = ''
        str_new += str[0]
        for i in range(1, len(str)):
            for j in range(len(str_new)):
                if str_new[j] == str[i]:
                    break
                if j == (len(str_new) - 1):
                    str_new += str[i]

        return str_new


print(Algo_string.delete_duplicate_words('jflksdjfldsj'))