#Bubble Sorting

s=[50,10,30,20,5]
o=len(s)

for i in range(o-1):
   m=0
   d=len(s)
   l=0
   while m!=d-1:
        if s[m]>s[m+1]:
            s[m],s[m+1]=s[m+1],s[m]
            l==1 
        if l==0:
            break
        m+=1
   s.pop()         
print("Popped element:",s.pop())
print(s)