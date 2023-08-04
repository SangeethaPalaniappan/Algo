#Inserting
def hashing(val,size):
    s=val%size #position to be added [size divides the value and the value stored in the reminder] 
    start=s
    print(s)
    
    while a[s]!=-1:
        s=s+1
        if s==size:
            s=0
        if s==start:
            print("Hash table is Full")
            return a
    a[s]=val  
    
    return a

#Deleting
def delhashing(val,size):
    d=val%size
    f=d
    while a[f]!=val:
        f+=1
        if f==size:
            f=0
        if f==d:
            print("No element found")
            return a
    a[f]=-1   #deleting the element by giving the value -1 to the element
    return a
    


#Searching
def search_hashing(val,size):
    u=val%size
    m=u
    while a[m]!=val:
        m+=1
        if m==size:
            m=0
        if m==u:
            print("Searched Element not found")
            return a
    else:
        print("Element found")
        return a

size=int(input("size:"))
a=[-1]*size
print(a)    

val=int(input("val:"))
a=hashing(val,size)    

val=int(input("val:"))
a=hashing(val,size)    

val=int(input("val:"))
a=hashing(val,size)    

val=int(input("val:"))
a=search_hashing(val,size)    

val=int(input("val:"))
a=search_hashing(val,size)    

val=int(input("val:"))
a=delhashing(val,size)    

val=int(input("val:"))
a=delhashing(val,size)    

 