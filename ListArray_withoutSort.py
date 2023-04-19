import copy
class ListArray_withoutSort:
    def __init__(self, size=10):
        self.mSize = size
        self.numInList = 0
        self.listArray = [None] * size
        self.min = -1 # 维护数组最小值，减少查找min的时间复杂度
        self.max = -1

    def search(self,x): #O(n)
        for i in range(self.numInList):
            if self.listArray[i] == x:
                return True
        return False

    def insert(self, x): #O(1)
        if not (self.numInList < self.mSize):
            raise ValueError("List is Full.")
        self.listArray[self.numInList] = x
        self.numInList += 1
        if x<self.min or self.min==-1:
            self.min = x
        if x>self.max:
            self.max = x

    def delete(self,x): #O(n)
        if self.numInList==0:
            raise ValueError("Can't delete from empty list.")
        i=0
        while i<self.numInList:
            if self.listArray[i]==x:
                for j in range(i,self.numInList-1):
                    self.listArray[j]=self.listArray[j+1]
                self.numInList -= 1
                # 维护min和max两个数据成员
                if self.numInList == 0:
                    self.min = self.max = -1
                else:
                    if x == self.min:
                        self.min=self.listArray[0]
                        for e in range(self.numInList):
                            if self.listArray[e] < self.min:
                                self.min = self.listArray[e]
                    if x == self.max:
                        self.max = self.listArray[0]
                        for e in range(self.numInList):
                            if self.listArray[e] > self.max:
                                self.max = self.listArray[e]
                return True
            i += 1
        return False

    def successor(self,x): #O(n)
        if self.numInList==0:
            raise ValueError("list is empty")
        for i in range(self.numInList-1): #防止x位于最后一个元素，搜索停止于倒数第二个元素
            if self.listArray[i]==x:
                return self.listArray[i+1]
        return -1

    def predecessor(self,x): #O(n)
        if self.numInList==0:
            raise ValueError("list is empty")
        for i in range(1,self.numInList): # 从第二个元素开始搜索，因为第一个元素没有前驱
            if self.listArray[i]==x:
                return self.listArray[i-1]
        return -1

    def minimum(self): #O(1)
        return self.min

    def maximum(self): #O(1)
        return self.max

    def KthElement(self,k): #O(n)
        if self.numInList==0:
            raise ValueError("list is empty")
        if k>self.numInList:
            raise ValueError("out of index")
        # 直接插入排序
        nums=copy.deepcopy(self.listArray)
        def insertionsort(nums, left, right):
            for i in range(left, right + 1, 1):
                key = nums[i]
                j = i - 1
                while j > left and nums[j] > key:
                    nums[j + 1] = nums[j]
                    j -= 1
                nums[j + 1] = key

        # 找到每个区间的中位数，集中放在最前面
        def median(nums, left, right):
            inx = left
            i = left
            while i + 4 < right:
                insertionsort(nums, i, i + 4)
                nums[i], nums[inx] = nums[inx], nums[i]
                inx += 1
                i += 5
            end = (inx - left) * 5 + left
            if end < right:
                insertionsort(nums, end, right)
                nums[inx], nums[(right + end) // 2] = nums[(right + end) // 2], nums[inx]
            return inx

        # 找到中位数的中位数
        def selectMedian(nums, left, right):
            if right - left > 0:
                inx = median(nums, left, right)
                selectMedian(nums, left, inx)

        # 划分,返回主元下标
        def partition(nums, left, right):
            inx = left
            if left < right:
                i = left
                j = right
                x = nums[left]
                while i < j:
                    while i < j and nums[j] > x:
                        j -= 1
                    if i < j:
                        nums[i] = nums[j]
                        i += 1

                    while i < j and nums[i] <= x:
                        i += 1
                    if i < j:
                        nums[j] = nums[i]
                        j -= 1

                nums[i] = x
                inx = i

            return inx

        # 主算法
        def select(nums, left, right, key):
            selectMedian(nums, left, right)
            k = partition(nums, left, right)
            if k > key:
                return select(nums, left, k - 1, key)
            elif k < key:
                return select(nums, k + 1, right, key)
            return nums[k]


        k -= 1
        return select(nums, 0, self.numInList-1, k)


if __name__ == "__main__":
    # 这个位置可以做一些简单的数据结构测试
    mylist = ListArray_withoutSort(10)
    mylist.insert(8)
    mylist.insert(3)
    mylist.insert(4)
    mylist.insert(7)
    mylist.insert(10)
    print("已经向线性表插入8、3、4、7、10，检查元素3是否存在于线性表：",mylist.search(3))
    print("获取线性表第3小的元素：",mylist.KthElement(3))
    print("获取线性表元素的最小值：",mylist.minimum())
    print("获取线性表元素的最大值：",mylist.maximum())
    print("删除元素3：",mylist.delete(3))
    print("已经从线性表中删除3，检查3是否还存在于元素表中：",mylist.search(3))
    print("检查4的前驱；",mylist.predecessor(4))
    print("检查4的后继：",mylist.successor(4))
    print("已知10是之前插入的最后一个元素，检查它的后继：",mylist.successor(10))
    print("已知8是之前插入的第一个元素，检查它的前驱：",mylist.predecessor(8))
    print("删除3之后，获取线性表元素的最小值：",mylist.minimum())
    print("删除元素10：",mylist.delete(10))
    print("删除10之后，获取线性表元素的最大值：",mylist.maximum())





