# Insertion Sort - Keep the first element fixed , check from the 2nd element , check from the current index to the 0th index ,check with the before adjacent element if it is maximum swap it 

#Time complexity - O(n^2)

# Best case      - O(n)

# If the length of the array is equal to one then print it is sorted array

# If the length is 0 then print no array exists

a=[30,21,43,12,9]
l=len(a)
for i in range(1,l):
    m=i
    # Here checking the value is maximum or not because if it sorted array the previous element will be smaller than the current index element
    while m!=0 and a[m-1]>a[m]:
        a[m],a[m-1]=a[m-1],a[m]
        m-=1
print(a)        