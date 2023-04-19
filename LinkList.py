import collections
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkList:

    def __init__(self):
        self.size = 0
        self.head = ListNode(0)  #dummy_head
        self.tail = self.head

    def search(self,x): # O(n)
        if self.size==0:
            raise ValueError("list is empty")
        current = self.head.next
        while current.next != None:
            if current.val == x:
                return True
            current = current.next
        return False

    def insert(self,x): # 尾插法 O(1)
        new_node = ListNode(x)
        new_node.next = None
        self.tail.next = new_node
        self.tail = new_node
        self.size += 1

    def delete(self,x): #O(n)
        if self.size==0:
            raise ValueError("list is empty")
        current = self.head
        while current.next is not None:
            if current.next.val==x and current.next != self.tail:
                current.next = current.next.next
                self.size -= 1
                return True
            if current.next.val==x and current.next == self.tail:
                current.next = current.next.next
                self.tail = current
                self.size -= 1
                return True
            current = current.next
        return False

    def successor(self,x): #O(n)
        if self.size==0:
            raise ValueError("list is empty")
        current = self.head.next
        while current.next is not None:
            if current.val==x:
                return current.next.val
            current = current.next
        return -1

    def predecessor(self,x): #O(n)
        if self.size==0:
            raise ValueError("list is empty")
        current = self.head.next
        while current.next is not None:
            if current.next.val==x:
                return current.val
            current = current.next
        return -1

    def minimum(self): #O(n)
        if self.size==0:
            return -1
        else:
            current = self.head.next
            min = current.val
            while current is not None:
                if current.val<min:
                    min=current.val
                current=current.next
            return min

    def maximum(self): #O(n)
        if self.size==0:
            return -1
        else:
            current = self.head.next
            max = current.val
            while current is not None:
                if current.val>max:
                    max=current.val
                current=current.next
            return max

    def KthElement(self,k): #O(k^2+(n-k)*k)=O(kn)=O(n)
        if self.size==0:
            raise ValueError("list is empty")
        if k>self.size:
            raise ValueError("out of index")


        # 维护一个k大小的有序双端队列，保存遍历至当前元素的前k小个元素
        temp = collections.deque()
        current = self.head.next
        # 当temp长度不达到k，来者不拒，每次加入元素时直接插入到合适位置
        while len(temp)<k and current is not None:
            key=current.val
            if len(temp)==0 or key>temp[-1]:
                temp.append(key)
                #print(temp)
            else:
                temp.append(key)
                for i in range(len(temp)-1,0,-1):
                    if temp[i-1]>temp[i]:
                        temp[i-1],temp[i]=temp[i],temp[i-1]
                #print(temp)
            current = current.next
        # 当temp达到k，若新遍历到的元素大于temp所维护的最大值，则抛弃；若小于temp维护的最小值，则右端pop，左端加入新元素
        while current is not None:
            if current.val<temp[0]:
                temp.pop()
                temp.appendleft(current.val)
                current=current.next
                #print(temp)
            elif current.val>temp[-1]:
                current=current.next
                #print(temp)
            # 若新元素值在最大和最小之间，先pop右端，然后插入新元素到合适位置
            elif current.val<temp[-1] and current.val>temp[0]:
                temp.pop()
                temp.append(current.val)
                for i in range(k-1,0,-1):
                    if temp[i-1]>temp[i]:
                        temp[i-1],temp[i]=temp[i],temp[i-1]
                current=current.next
                #print(temp)
        # 返回维护的第k个元素
        return temp[-1]

if __name__ == "__main__":
    # 这个位置可以做一些简单的数据结构测试
    mylist = LinkList()
    mylist.insert(8)
    mylist.insert(3)
    mylist.insert(4)
    mylist.insert(7)
    mylist.insert(10)
    mylist.insert(2)
    mylist.insert(1)
    print("已经向线性表插入8、3、4、7、10、2、1，检查元素3是否存在于线性表：",mylist.search(3))
    print("获取线性表第4小的元素：",mylist.KthElement(4))
    print("获取线性表元素的最小值：",mylist.minimum())
    print("获取线性表元素的最大值：",mylist.maximum())
    print("删除元素3：",mylist.delete(3))
    print("已经从线性表中删除3，检查3是否还存在于元素表中：",mylist.search(3))
    print("删除3之后，检查4的前驱；",mylist.predecessor(4))
    print("检查4的后继：",mylist.successor(4))
    print("已知1是之前插入的最后一个元素，检查它的后继：",mylist.successor(1))
    print("已知8是之前插入的第一个元素，检查它的前驱：",mylist.predecessor(8))
    print("删除元素1：",mylist.delete(1))
    print("删除1之后，获取线性表元素的最小值：",mylist.minimum())
    print("删除元素10：",mylist.delete(10))
    print("删除10之后，获取线性表元素的最大值：",mylist.maximum())