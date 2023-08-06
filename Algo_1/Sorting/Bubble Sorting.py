#Bubble Sorting

s=[50,10,30,20,5]
o=len(s)

for i in range(o-1):
   m=0
   d=len(s)
   while m!=d-1:
        if s[m]>s[m+1]:
            s[m],s[m+1]=s[m+1],s[m]
        m+=1 
   s.pop()         
print("Popped element:",s.pop())
print(s)