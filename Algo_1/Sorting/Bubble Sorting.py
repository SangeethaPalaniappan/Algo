#Bubble Sorting - swap the maximum elements with its adjacent element , when it reaches the end of the array pop it

#Time complexity - O(n^2) [worst]

# Best case      - O(n)

# The elements are sorted from right to left

# If the length of the array is equal to one then print it is sorted array

# If the length is 0 then print no array exists

s=[50, 20, 30, 10, 5]
o=len(s)

# iterate to check the maximum element with its adjacent element

# If the adjacent element is greater than the element then swap it 

# If there is no swapping occurs , then the array is sorted

for i in range(o-1):
    m=0 # initialise for the loop
    d=len(s)
    swap=0 # this variable is assigning because to check whether the array is sorted or not
    while m!=d-1:
        if s[m]>s[m+1]:
            s[m],s[m+1]=s[m+1],s[m]
            swap=1 # If swaping occurs change swap into 1 else 0 
        m+=1    
    if swap==0: # After the 1st loop still l==0 break the loop
        break
    o-=1    # here reducing the size because the last ele,
           

print(s)