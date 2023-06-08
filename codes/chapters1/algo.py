# !/usr/bin/env python
# -*- coding:utf-8 -*-　
# @Time : 2023/6/8 11:04 
# @Author : sanmaomashi
# @GitHub : https://github.com/sanmaomashi
# @Summary : 算法

print("="*30 + "算法引入-第一次尝试" + "="*30)
import time

start_time = time.time()

# 注意是三重循环
# for a in range(0, 1001):
#     for b in range(0, 1001):
#         for c in range(0, 1001):
#             if a**2 + b**2 == c**2 and a+b+c == 1000:
#                 print("a, b, c: %d, %d, %d" % (a, b, c))
#
# end_time = time.time()
# print("elapsed: %f" % (end_time - start_time))
# print("complete!")
print("="*30 + "算法引入-第一次尝试" + "="*30)

print("="*30 + "算法引入-第二次尝试" + "="*30)
import time

start_time = time.time()

# 注意是两重循环
for a in range(0, 1001):
    for b in range(0, 1001-a):
        c = 1000 - a - b
        if a**2 + b**2 == c**2:
            print("a, b, c: %d, %d, %d" % (a, b, c))

end_time = time.time()
print("elapsed: %f" % (end_time - start_time))
print("complete!")
print("="*30 + "算法引入-第二次尝试" + "="*30)