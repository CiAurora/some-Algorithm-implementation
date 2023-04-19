import numpy as np
import collections
import os
import sys

# 得到某个数字指定位的值
def getBitValue(num,i):
    num_str = str(num)
    if len(str(num)) < i:
        return 0
    else:
        return int(num_str[-i])

# 基于队列实现基数排序
def RadixSort(nums):
    if len(nums)==0:
        return []
    if isinstance(nums[0],int):
        # 检查最大数字的位数
        max_num = max(nums)
        max_bit = len(str(max_num))
        # 创建10个队列
        all_buckets = []
        for i in range(10):
            all_buckets.append(collections.deque())
        # 用于暂存每一轮结果
        temp = collections.deque()
        # 将初始序列加入队列
        for elem in nums:
            temp.append(elem)
        for i in range(1,max_bit+1):
            while len(temp) != 0:
                num = temp.popleft()
                bit_value = getBitValue(num,i)
                all_buckets[bit_value].append(num)
            for bucket in all_buckets:
                while len(bucket) != 0:
                    num = bucket.popleft()
                    temp.append(num)
            #print(list(temp))
        return list(temp)
    if isinstance(nums[0],str):
        max_bit = len(nums[0])
        # 创建字符->数字映射;优先级：A-Z a-z
        reflect = {'A': 0, 'B': 1, 'C': 2, 'D': 3, 'E': 4, 'F': 5, 'G': 6, 'H': 7,
                   'I': 8, 'J': 9, 'K': 10, 'L': 11, 'M': 12, 'N': 13, 'O': 14,
                   'P': 15, 'Q': 16, 'R': 17, 'S': 18, 'T': 19, 'U': 20, 'V': 21,
                   'W': 22, 'X': 23, 'Y': 24, 'Z': 25, 'a': 26, 'b': 27, 'c': 28, 'd': 29, 'e': 30,
                   'f': 31, 'g': 32, 'h': 33, 'i': 34, 'j': 35, 'k': 36, 'l': 37, 'm': 38, 'n': 39, 'o': 40, 'p': 41,
                   'q': 42,
                   'r': 43, 's': 44, 't': 45, 'u': 46, 'v': 47, 'w': 48, 'x': 49, 'y': 50, 'z': 51, }
        # 创建52个队列
        all_buckets = []
        for i in range(52):
            all_buckets.append(collections.deque())
        # 用于暂存每一轮结果
        temp = collections.deque()
        # 将初始序列加入队列
        for elem in nums:
            temp.append(elem)
        for i in range(max_bit - 1, -1, -1):
            while len(temp) != 0:
                num = temp.popleft()
                bit_value = reflect[num[i]]
                all_buckets[bit_value].append(num)
            for bucket in all_buckets:
                while len(bucket) != 0:
                    num = bucket.popleft()
                    temp.append(num)
            # print(list(temp))
        return list(temp)

# 数据预处理
data1 = []
with open('radixSort1.txt','r') as f:
    for line in f.readlines():
        line = line.split(' ')
        line = line[:-1]
        data1.append(line)
for i in range(40):
    for j in range(100):
        data1[i][j] = int(data1[i][j])

data2 = []
with open('radixSort2.txt','r') as f:
    for line in f.readlines():
        line = line.split(' ')
        line = line[:-1]
        data2.append(line)


# 开始测试对数字排序效果
flag = 0
print('进入数字数据测试：----------------------------------------------')
for elem in data1:
    print('待排数据：',list(elem))
    temp1 = RadixSort(elem)
    print('基数排序结果：',temp1)
    elem.sort()
    print('使用内置函数排序结果：',elem)
    print('对比基数排序结果与内置函数排序结果：')
    if (temp1==elem):
        print('结果一致，基数排序结果正确！')
    else:
        print('基数排序结果错误！')
        flag += 1
    print('-----------------------------------------------------')
if flag == 0:
    print('所有数字数据测试正确！')
else:
    print('有错误！')
print()
print('进入字符数据测试：----------------------------------------------')
# 开始测试对字符排序效果
flag = 0
for elem in data2:
    print('待排数据：',list(elem))
    temp1 = RadixSort(elem)
    print('基数排序结果：',temp1)
    elem.sort()
    print('使用内置函数排序结果：',elem)
    print('对比基数排序结果与内置函数排序结果：')
    if (temp1==elem):
        print('结果一致，基数排序结果正确！')
    else:
        print('基数排序结果错误！')
        flag += 1
    print('-----------------------------------------------------')
if flag == 0:
    print('所有字符数据测试正确！')
else:
    print('有错误！')