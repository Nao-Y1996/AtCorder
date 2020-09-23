#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n = int(input())
num_list = list(map(int, input().split(' ')))
count = 0
while (1):
    judge_list = list(map(lambda x: x % 2, num_list))
    if judge_list == [0] * n:
        num_list = list(map(lambda x: x / 2, num_list))
        count += 1
    else:
        break
print(count)
