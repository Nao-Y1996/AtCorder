#!/usr/bin/env python3
# -*- coding: utf-8 -*-
input_list = list(map(int, input().split(' ')))
n = input_list[0]
a = input_list[1]
b = input_list[2]

ans = 0
for i in range(1, n + 1):
    str_i = str(i)

    #格桁の和を計算
    digits_list = []
    for j in str_i:
        digits_list.append(int(j))
        sum_digits = sum(digits_list)

    #総和の計算
    if (a <= sum_digits) and (sum_digits <= b):
        ans += int(i)
print(ans)