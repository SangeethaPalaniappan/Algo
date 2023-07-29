size=int(input("size:"))
a=[-1]*size
print(a)

def hashing(val,size):
    s=val%size
    print(s)
    if a[s]!=-1:
        while a[s]!=-1:
            s=s+1
            if s==size:
                s=0
        a[s]=val  
    else:
        a[s]=val
    print(a)
    
for x in range(size):
    val=int(input("val:"))
    hashing(val,size)    