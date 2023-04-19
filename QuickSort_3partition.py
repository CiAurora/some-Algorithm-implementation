import numpy as np
import random
import pandas as pd
import time
from data_structure1 import Solution
import sys
sys.setrecursionlimit(5000)

class Solution_3:

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

    # 划分
    def partition(self,nums,left,right,pivot):
        p = left
        q = right-1
        i = left
        j = right-1
        v = pivot
        while 1:
            while i<right and nums[i]<=v:
                if nums[i]==v:
                    nums[i],nums[p] = nums[p],nums[i]
                    p+=1
                i+=1
            while left<=j and nums[j]>=v:
                if nums[j]==v:
                    nums[j],nums[q] = nums[q],nums[j]
                    q-=1
                j-=1
            if i>=j:
                break
            nums[i],nums[j] = nums[j],nums[i]
            i+=1
            j-=1
        i-=1
        p-=1
        while p>=left:
            nums[i],nums[p] = nums[p],nums[i]
            i-=1
            p-=1
        j+=1
        q+=1
        while q<=right:
            nums[j],nums[q] = nums[q],nums[j]
            j+=1
            q+=1
        #print(nums)
        return i,j

    def quicksort_3(self, nums,left,right):
        pivot_index = self.findpivot(left, right, nums)  # 可以随机，也可以用上面的findpivot函数（三值取中）

        # print("left:",left,"  right:",right)
        #print("pivot:", pivot_index, "值为:", nums[pivot_index])

        nums[right], nums[pivot_index] = nums[pivot_index], nums[right]
        i,j = self.partition(nums, left, right, nums[right])
        #print("i,j:",i,j)
        # print(nums)
        #print("--------------------------------------------------------------------------------")
        if i - left > 1:
            self.quicksort_3(nums, left, i)
        if right - j > 1:
            self.quicksort_3(nums, j, right)

    def sortArray(self,nums):
        self.quicksort_3(nums, 0, len(nums) - 1)
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

    data = []
    rate = np.arange(0.1,1.1,0.1)
    for r in rate:
        data.append(generateData(100000,r))

    sort_model1 = Solution_3()
    sort_model2 = Solution()

    Y1 = elapsedtime(sort_model1.sortArray,data)
    Y2 = elapsedtime(sort_model2.sortArray_original,data)
    Y3 = elapsedtime(sort_model2.sortArray_optimized,data)
    Y = [Y1,Y2,Y3]
    Y_value = pd.DataFrame(Y)
    Y_value.to_csv('Y_value_1_3.csv')
