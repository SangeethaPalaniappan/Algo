# Heap Sorting


def dswap(i,arr,size):#i is the parent node
    left=(2*i)+1
    right=left+1
    
    
    if left<size:
        temp=arr[i]
        if right==size:#Having only left child 
            if arr[i]<arr[left]:
                arr[i]=arr[left]
                arr[left]=temp
            
        else:
            if arr[i]<arr[left] or arr[i]<arr[right]:#to check the root node's children are greater than the parent
                #if the root node is lesser then check whhich child is greater
                if arr[left]<arr[right]:
                    arr[i]=arr[right]
                    arr[right]=temp
                    dswap(right,arr,size-1)
                else:
                    arr[i]=arr[left]
                    arr[left]=temp
                    dswap(left,arr,size-1)
            
    elif left>=size:
        return arr

# Delete is the Top-down approach
    
def delete(arr):
    #swaping the 1st and last  and delete the last element
    #after checking whether it satisfies the binary heap property
    c=len(arr)
    while c>1:
    
        temp=a[0]
        arr[0]=arr[c-1]
        arr[c-1]=temp
        dswap(0,arr,c-1)
        c-=1
    return arr

def Heap(arr,size):
    l=size//2
    while l>=0:
        Heapify(arr,l,size)
        l-=1
    return arr        

def Heapify(arr,i,size):#to check the given array satisfies the BH property else heapify it
    left=(2*i)+1
    right=left+1
    temp=i
    
    if left<size and arr[temp]<arr[left]:
        temp=left
    if right<size and arr[temp]<arr[right]:
        temp=right
    if temp!=i:
        s=arr[temp]
        arr[temp]=arr[i]
        arr[i]=s
        
        Heapify(arr,temp,size)

a=[30,50,10,90,60]
a=Heap(a,len(a))

#for i in a:
#    print(i,end=" ")

delete(a)

for i in a:
    print(i,end=" ")