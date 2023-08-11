# Pivot element  - the central element which balances both side 

# But I haven't written in O(nlogn) {Time Complexity} even in the best case

# Best time complexity - O(nlogn)

# Worst case Time complexity - O(n^2)

# If the length of the array is equal to one then print it is sorted array

# If the length is 0 then print no array exists


def Quick_sort(i,j,pivot,a):
    # It will be used for the recursive function
    start=i
    end=j
      
    while i<j:
        while a[i]<=a[pivot]: # To get the maximum element position
            i+=1
        while a[j]>a[pivot]: # To get the minimum element position
            j-=1
        if j==start: # If the given array is already sorted
            return "The array is already sorted"    
        if i<j: # If the max and min elements are mixed it will stop at certain at that point I have to 
                # change the min elements in front and max elements in back 
            a[i],a[j]=a[j],a[i]
           
        else:# If i>j i.e., i and j crossed so the elements after j are maximum and before i are minimum
             # if we swap  j and pivot and making the jth index as pivot so that the before elements of pivot 
             # are minimum and after the pivot are maximum
            a[j],a[pivot]=a[pivot],a[j]
            pivot=j
       
                   
    j=i
    i=pivot        
    if i<j:
        Quick_sort(start,pivot-1,start,a) # Before the pivot element  {to sort}
        Quick_sort(pivot+1,end,pivot+1,a) # After the pivot element   {to sort}
    return a
arr=[10,30,9,50,4,60] 
print(len(arr))
i=0
j=len(arr)-1

arr=Quick_sort(i,j,i,arr)
print(arr)
    