#!/usr/bin/env python3
# -*- coding: utf-8 -*-
c_500 = int(input())
c_100 = int(input())
c_50 = int(input())
total = int(input())

count = 0

i,j,k = 0,0,0
for i in range(c_500+1):
  for j in range(c_100+1):
    for k in range(c_50+1):
      if i * 500 + j * 100 + k * 50 == total:
        count += 1
print(count)

