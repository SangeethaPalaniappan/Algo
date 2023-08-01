
#Inserting
def hashing(val,size):
    s=val%size
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
a=hashing(val,size)    

val=int(input("val:"))
a=hashing(val,size)    

val=int(input("val:"))
a=hashing(val,size)    

 