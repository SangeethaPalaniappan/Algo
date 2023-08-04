class Table:
    def __init__(self,size):
        self.arr=[None]*self.size
class Node:
    def __init__(self,val):
        self.data=val
        self.next=None
class Head:
    def __init__(self):
        self.head=None
    def add(self,key,val,size):
        s=len(key)
        m=s%size
        if self.arr[m]==None:
            self.arr[m]=val
        else:
            newnode=Node(val)
            temp=self.head
            if temp==None:
                self.head=newnode
            else:
                while temp.next!=None:
                    temp=temp.next
                temp.next=newnode
            
    def delete(self,key,val,size):
        self.d=len(key)%size
        if self.arr[m]==None:
            print("There is no element")
        else:
            temp=self.head
            while temp!=val:
                temp=temp.next
            temp.next=temp.next.next
            