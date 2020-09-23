#!/usr/bin/env python3
# -*- coding: utf-8 -*-
n = int(input())
num_list = [int(input()) for i in range(n)]
num_set = set(num_list)
print(len(num_set))