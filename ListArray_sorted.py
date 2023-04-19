class ListArray_sorted:
    def __init__(self, size=10):
        self.mSize = size
        self.numInList = 0
        self.listArray = [None] * size

    def search(self,x): #O(logn)
        left = 0
        right = self.numInList - 1  # 左闭右闭
        while left <= right:
            mid = (right + left) // 2
            if self.listArray[mid] == x:
                return True
            elif x > self.listArray[mid]:
                left = mid + 1
            else:
                right = mid - 1
        return False



    def insert(self, x): #O(n)
        if not (self.numInList < self.mSize):
            raise ValueError("List is Full.")
        if self.numInList == 0:
            self.listArray[0] = x
            self.numInList += 1

        elif self.numInList!=0 and x <= self.listArray[0]:
            for i in range(self.numInList,0,-1):
                self.listArray[i] = self.listArray[i-1]
            self.listArray[0] = x
            self.numInList += 1

        elif self.numInList!=0 and x >= self.listArray[self.numInList-1]:
            self.listArray[self.numInList] = x
            self.numInList += 1

        else:
            for i in range(0,self.numInList):
                if x<self.listArray[i] and x>self.listArray[i-1]:
                    for j in range(self.numInList,i,-1):
                        self.listArray[j] = self.listArray[j-1]
                    self.listArray[i] = x
            self.numInList += 1


    def delete(self,x): #O(n)
        if self.numInList==0:
            raise ValueError("Can't delete from empty list.")
        left = 0
        right = self.numInList - 1  # 左闭右闭
        while left <= right:
            mid = (right + left) // 2
            if self.listArray[mid] == x:
                for j in range(mid,self.numInList-1,1):
                    self.listArray[j] = self.listArray[j + 1]
                self.numInList -= 1
                return True
            elif x > self.listArray[mid]:
                left = mid + 1
            else:
                right = mid - 1
        return False

    def successor(self,x): #O(logn)
        if self.numInList==0:
            raise ValueError("list is empty")
        left = 0
        right = self.numInList - 2  # 左闭右闭,同时防止x位于最后一个元素，搜索停止于倒数第二个元素
        while left <= right:
            mid = (right + left) // 2
            if self.listArray[mid] == x:
                return self.listArray[mid+1]
            elif x > self.listArray[mid]:
                left = mid + 1
            else:
                right = mid - 1
        return -1

    def predecessor(self,x): #O(logn)
        if self.numInList==0:
            raise ValueError("list is empty")
        left = 1 #  从第二个元素开始搜索，因为第一个元素没有前驱
        right = self.numInList - 1  # 左闭右闭
        while left <= right:
            mid = (right + left) // 2
            if self.listArray[mid] == x:
                return self.listArray[mid-1]
            elif x > self.listArray[mid]:
                left = mid + 1
            else:
                right = mid - 1
        return -1

    def minimum(self): #O(1)
        if self.numInList != 0:
            return self.listArray[0]
        else:
            return -1

    def maximum(self): #O(1)
        if self.numInList != 0:
            return self.listArray[self.numInList-1]
        else:
            return -1

    def KthElement(self,k): #O(1)
        if self.numInList==0:
            raise ValueError("list is empty")
        if k>self.numInList:
            raise ValueError("out of index")
        return self.listArray[k-1]


if __name__ == "__main__":
    # 这个位置可以做一些简单的数据结构测试
    mylist = ListArray_sorted(10)
    mylist.insert(8)
    mylist.insert(3)
    mylist.insert(4)
    mylist.insert(7)
    mylist.insert(10)
    print("已经向线性表插入8、3、4、7、10，检查元素3是否存在于线性表：",mylist.search(3))
    print("看看现在的线性表：",mylist.listArray[:mylist.numInList])
    print("插入元素大小是无序的，但我们的线性表是有序的！")
    print("获取线性表第3小的元素：",mylist.KthElement(3))
    print("获取线性表元素的最小值：",mylist.minimum())
    print("获取线性表元素的最大值：",mylist.maximum())
    print("删除元素3：",mylist.delete(3))
    print("已经从线性表中删除3，检查3是否还存在于元素表中：",mylist.search(3))
    print("再看看删除3之后的线性表：",mylist.listArray[:mylist.numInList])
    print("依然是有序的！")
    print("检查4的前驱；",mylist.predecessor(4))
    print("检查4的后继：",mylist.successor(4))
    print("已知10是之前插入的最大的元素，检查它的后继：",mylist.successor(10))
    print("删除3之后，获取线性表元素的最小值：",mylist.minimum())
    print("删除元素10：",mylist.delete(10))
    print("删除10之后，获取线性表元素的最大值：",mylist.maximum())
    print("再看看此时的线性表吧！",mylist.listArray[:mylist.numInList])





