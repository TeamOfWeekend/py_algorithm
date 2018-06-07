#!/usr/bin/python
# -*- coding:utf-8 -*-
"""
@author:dingxiaojie
@contact:dingxiaojie@huahuan.com
@file:algo_binary_watch
@time:2018/6/4 10:41
@desc:
"""

#二进制手表：4个Led表示小时，6个Led表示分钟
#给定一个非负整数 n 代表当前 LED 亮着的数量，返回所有可能的时间。
#输出的顺序没有要求。
#小时不会以零开头，比如 “01:00” 是不允许的，应为 “1:00”。
#分钟必须由两位数组成，可能会以零开头，比如 “10:2” 是无效的，应为 “10:02”。

class BinaryWatch:
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        if num > 10:
            return False

        res_time = []

        for num_in_hour in (0, num + 1):
            if num_in_hour > 3:
                break
            num_in_minute = num - num_in_hour

            if 1 == num_in_hour:
                res_hour = self.getHourByNum(num_in_hour)
                res_minute = self.getMinuteByNum(num_in_minute)
            elif 2 == num_in_hour:
                res_minute = 0

    def getHourByNum(self, num):
        base_hours = [1, 2, 4, 8]
        res_hours = []

        if (num < 1) or (num > 3):
            return None
        elif 1 == num:
            res_hours = base_hours[:]
        elif 2 == num:
            for i in range(0, len(base_hours)):
                for j in range(i+1, len(base_hours)):
                    hour_calc = base_hours[i] + base_hours[j]
                    if hour_calc > 12:
                        continue
                    res_hours.append(hour_calc)
        elif 3 == num:
            for i in range(0, len(base_hours)):
                for j in range(i+1, len(base_hours)):
                    for k in range(j+1, len(base_hours)):
                        hour_calc = base_hours[i] + base_hours[j] + base_hours[k]
                        if hour_calc > 12:
                            continue
                        res_hours.append(hour_calc)

        return res_hours


    def getMinuteByNum(self, num):
        base_minutes = [1, 2, 4, 8, 16, 32]
        res_minutes = []
        if num > 5:
            return None
        elif 0 == num:
            return [0]
        elif 1 == num:
            return base_minutes
        elif 2 == num:
            for i in range(0, len(base_minutes)):
                for j in range(i+1, len(base_minutes)):
                    minute_calc = base_minutes[i] + base_minutes[j]
                    if minute_calc > 59:
                        continue
                    res_minutes.append(minute_calc)
            #return [3, 5, 9, 17, 33, 6, 10, 18, 34, 12, 20, 36, 24, 40, 48]
        elif 3 == num:
            for i in range(0, len(base_minutes)):
                for j in range(i+1, len(base_minutes)):
                    for k in range(j + 1, len(base_minutes)):
                        minute_calc = base_minutes[i] + base_minutes[j] + base_minutes[k]
                        if minute_calc > 59:
                            continue
                        res_minutes.append(minute_calc)
            #return [7, 11, 19, 35, 13, 21, 37, 25, 41, 49, 14, 22, 38, 26, 42, 50, 28, 44, 52, 56]
        elif 4 == num:
            for i in range(0, len(base_minutes)):
                for j in range(i+1, len(base_minutes)):
                    for k in range(j + 1, len(base_minutes)):
                        for m in range(k + 1, len(base_minutes)):
                            minute_calc = base_minutes[i] + base_minutes[j] + base_minutes[k] + base_minutes[m]
                            if minute_calc > 59:
                                continue
                            res_minutes.append(minute_calc)
            #return [15, 23, 39, 27, 43, 51, 29, 45, 53, 57, 30, 46, 54, 58]
        elif 5 == num:
            for i in range(0, len(base_minutes)):
                for j in range(i+1, len(base_minutes)):
                    for k in range(j + 1, len(base_minutes)):
                        for m in range(k + 1, len(base_minutes)):
                            for n in range(m + 1, len(base_minutes)):
                                minute_calc = base_minutes[i] + base_minutes[j] + base_minutes[k] + base_minutes[m] \
                                              + base_minutes[n]
                                if minute_calc > 59:
                                    continue
                                res_minutes.append(minute_calc)
            #return [31, 47, 55, 59]

        return res_minutes


    def getAllBinaryTime(self, num_bit):
        time_list = []
        if (num_bit < 0) or (num_bit > 10):
            return None
        for hour_bit in range(num_bit+1):
            minute_bit = num_bit - hour_bit
            hours = self.getHourByNum(hour_bit)
            minutes = self.getMinuteByNum(minute_bit)
            if (hour_bit < 1) or (hour_bit > 3):
                continue
            if (minute_bit > 5):
                continue
            for hour in hours:
                for minute in minutes:
                    time_get = "%d:%02d" % (hour, minute)
                    time_list.append(time_get)
        return time_list



s = BinaryWatch()
# print(s.getHourByNum(1))
# print(s.getHourByNum(2))
# print(s.getHourByNum(3))
# print(s.getHourByNum(4))
# print(s.getMinuteByNum(0))
# print(s.getMinuteByNum(1))
# print(s.getMinuteByNum(2))
# print(s.getMinuteByNum(3))
# print(s.getMinuteByNum(4))
# print(s.getMinuteByNum(5))
# print(s.getMinuteByNum(6))
# print(s.getTimeByHourMinute(1,2))
print(s.getAllBinaryTime(8))