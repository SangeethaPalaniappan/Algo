# Selection Sort - Array of ascending order

#Time Complexity of this sorting is O(n^2)

# The elements are sorted from left to right 

# If the length of the array is equal to one then print it is sorted array

# If the length is 0 then print no array exists

s=[90,120,40,230,80]
m=len(s)

# Check the element of the 1st position with the other elements in the array
# After placing the element in the 1st position now check for the second element
# Do this till the last's before element of the array , because when we check for the last's before element 
# we place the correct element for the last position 

for i in range(m-1): 
    # Here we check from the next of i , so the reange starts from i+1
   
    
    for j in range(i+1,m):
        # If the current position's element is greate then swap it with the compared element
        
        if s[i]>s[j]:
            s[i],s[j]=s[j],s[i]
    
print(s)            