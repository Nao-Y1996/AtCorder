#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n = int(input())
num_list = list(map(int, input().split(' ')))
alice = 0
bob = 0
while (len(num_list) > 0):
    try:
        alice += max(num_list)
        num_list.remove(max(num_list))
    except:
        break
    try:
        bob += max(num_list)
        num_list.remove(max(num_list))
    except:
        break
print(alice - bob)
