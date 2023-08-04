#Indexing by the length of the string
class Node:
    def __init__(self,val,key):
        self.data=val
        self.Key=key
        self.next=None
class Table:
    def __init__(self,size,name):
        self.arr=[None]*size #Creating the table 
        self.size=size 
        self.Name=name # Naming the table
    def add(self,key,val):
        s=len(key)
        m=s%self.size # finding the index by the length of the key[or we can find by other methods]
        newnode=Node(val,key)   # creating the node
        if self.arr[m]==None:    # check whether the index is empty, 
            self.arr[m]=newnode  # if it is then keep the node at the index
            
        else:
           temp=self.arr[m]    
           while temp.next!=None:#checking the last node and add the newnode at last position
                temp=temp.next
           temp.next=newnode
           return self.arr     
            
    def delete(self,key):
        m=len(key)
        d=m%self.size
        if self.arr[d]==None: # to check whether the index is empty or not
            print("There is no element")
            
        else:
            temp=self.arr[d]
            if temp.Key==key:# if the first element is the value then we can delete
               temp=temp.next
            else: 
                
                while temp.next!=None: # iterate till None eg.,a->b->c
                    # if a's next data is the value then point a's next as c
                    if temp.next.Key==key:
                        temp.next=temp.next.next
                        break
                    temp=temp.next    
                else:
                     print("There is no ",key)   
                            
        return self.arr
    def search(self,key):
        m=len(key)
        d=m%self.size
        if self.arr[d]==None: # to check whether the index is empty or not
            print("There is no element")
              
        else:
            temp=self.arr[d]
            
            while temp!=None: # iterate till None eg.,a->b->c
                    # if a's next data is the value then point a's next as c
                if temp.Key==key:
                    print("Key Found")
                    break
                temp=temp.next    
            else:
                print("There is no ",key)   
                            
        return self.arr
    
    def printe(self,size):
       for x in self.arr:
           if x==None:
               print(x)
           else:
               print(x.Key,"=",x.data)
               while x.next!=None:
                   print(x.next.Key,"=",x.next.data)
                   x=x.next 
                     
    def getitem(self,key):
        m=len(key)
        d=m%self.size
        if self.arr[d]==None: # to check whether the index is empty or not
            print("There is no element")
              
        else:
            temp=self.arr[d]
            
            while temp!=None: # iterate till None eg.,a->b->c
                    # if a's next data is the value then point a's next as c
                if temp.Key==key:
                    return temp.data
                temp=temp.next    
            else:
                print("There is no ",key)   
                            
                            
                     
                     
f=Table(4,"Sangeetha")
f.add("Tamil",99)
f.add("English",97)
f.add("Maths",94)
f.add("Science",90)
f.add("Social",100)
f.add("Moral Science",89)
f.delete("Science")
f.delete("Science")
f.delete("MoralScience")
f.search("Maths")  
f.printe(4)
print(f.getitem("Moral Science"))
