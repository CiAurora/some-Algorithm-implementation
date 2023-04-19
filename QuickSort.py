import random
import time
import sys
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

sys.setrecursionlimit(3000)

class Solution:

    # 划分
    def partition(self, nums, left, right, pivot):
        # print(nums)
        border = left
        count = 0
        left -= 1
        while 1:
            while 1:
                left += 1
                if nums[left] >= pivot:
                    break
            while 1:
                if right == 0:  # 可以是border也可以是0，因为在左界非0的区间，上一层的pivot也会让right停下来
                    break
                right -= 1
                if nums[right] <= pivot:
                    break
            nums[left], nums[right] = nums[right], nums[left]
            count += 1
            if left >= right:
                break
        nums[left], nums[right] = nums[right], nums[left]
        count -= 1
        print('交换次数:',count)
        # print(nums)
        return left

    # 选择轴值
    def findpivot(self, left, right, nums):
        middle = left + (right - left) // 2
        #print("left,middle,right:",left,middle,right)
        candidate = [nums[left], nums[middle], nums[right]]
        #print("candidate:",candidate)
        candidate_sort = sorted(candidate)
        #print("candidate_sort:",candidate_sort)
        index = candidate.index(candidate_sort[1])
        #print("index:",index)
        if index == 0:
            return left
        elif index == 1:
            return middle
        else:
            return right

    # 直接插入排序
    def insertionsort(self, nums, left, right):
        for i in range(left, right+1, 1):
            key = nums[i]
            j = i-1
            while j>left and nums[j]>key:
                nums[j+1] = nums[j]
                j -= 1
            nums[j+1] = key



    def quicksort_original(self, nums, left, right):
        pivot_index = self.findpivot(left,right,nums)  # 可以随机，也可以用上面的findpivot函数（三值取中）

        #print("left:",left,"  right:",right)
        print("pivot:",pivot_index,"值为:",nums[pivot_index])


        nums[right], nums[pivot_index] = nums[pivot_index], nums[right]
        k = self.partition(nums, left, right, nums[right])
        nums[k], nums[right] = nums[right], nums[k]
        # print(nums)
        print("--------------------------------------------------------------------------------")
        if k - left > 1:
            self.quicksort_original(nums, left, k - 1)
        if right - k > 1:
            self.quicksort_original(nums, k + 1, right)


    def quicksort_optimized(self, nums, left, right):
        pivot_index = self.findpivot(left,right,nums)  # 可以随机，也可以用上面的findpivot函数（三值取中）
        print("pivot:", pivot_index, "值为:", nums[pivot_index])
        nums[right], nums[pivot_index] = nums[pivot_index], nums[right]
        k = self.partition(nums, left, right, nums[right])
        nums[k], nums[right] = nums[right], nums[k]
        print("--------------------------------------------------------------------------------")
        if k - left > 64:
            self.quicksort_optimized(nums, left, k - 1)
        else:
            self.insertionsort(nums, left, k-1)
        if right - k > 64:
            self.quicksort_optimized(nums, k + 1, right)
        else:
            self.insertionsort(nums, k+1, right)

    def sortArray_original(self, nums):
        self.quicksort_original(nums, 0, len(nums) - 1)
        return nums

    def sortArray_optimized(self, nums):
        self.quicksort_optimized(nums, 0, len(nums) - 1)
        return nums

# 生成数据with重复率参数
def generateData(scale,repetitionRate):
    dataSet = scale - int(repetitionRate*scale)
    if dataSet == 0:
        return [0]*scale
    data = [0]*scale
    for i in range(dataSet):
        data[i] = i
    startIndex = dataSet
    while startIndex < scale:
        for i in range(dataSet):
            data[startIndex] = random.randrange(0,dataSet)
            startIndex += 1
            if startIndex == scale:
                break
    random.shuffle(data) # 将数据随机打乱
    return data

# 适用于第一题第一问的生成数据函数，按要求规模每次给出三组数据
def generate_data_1(scale):
    data1 = np.arange(0,scale,1) #when scale=100, data1=[0,1,2,...,99]
    data2 = np.arange(scale-1,-1,-1) # when scale=100,data2=[99,98,97,...,0]
    data3 = np.random.randint(0,scale,scale)  # random int with scale
    return data1,data2,data3

def elapsedtime(function, data_set):
    elapsedtime = []
    for data in data_set:
        startTime = time.time_ns()
        function(data)
        endTime = time.time_ns()
        elapsedtime.append(endTime-startTime)
    return elapsedtime



if __name__ == "__main__":

    data_asc = []
    data_desc = []
    data_random = []
    for scale in range(100, 10100, 100):
        data = generate_data_1(scale)
        data_asc.append(data[0])
        data_desc.append(data[1])
        data_random.append(data[2])

    sort_model = Solution()
    # sort_model.sortArray_optimized(generate_data_1(7000)[1])
    #
    # 测试原始快排函数
    elapsedtime_asc = elapsedtime(sort_model.sortArray_original, data_asc)
    elapsedtime_desc = elapsedtime(sort_model.sortArray_original, data_desc)
    elapsedtime_random = elapsedtime(sort_model.sortArray_original, data_random)

    # 测试优化后的快排函数
    elapsedtime_asc_optimized = elapsedtime(sort_model.sortArray_optimized, data_asc)
    elapsedtime_desc_optimized = elapsedtime(sort_model.sortArray_optimized, data_desc)
    elapsedtime_random_optimized = elapsedtime(sort_model.sortArray_optimized, data_random)

    elapasedtime_6 = [elapsedtime_asc,
                      elapsedtime_desc,
                      elapsedtime_random,
                      elapsedtime_asc_optimized,
                      elapsedtime_desc_optimized,
                      elapsedtime_random_optimized]
    Y_value = pd.DataFrame(elapasedtime_6)
    Y_value.to_csv('Y_value.csv')









