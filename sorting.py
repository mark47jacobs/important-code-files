#selection sort
def selectionSort(l):
    for i in range(len(l)):
        minPos = i
        for j in range(i,len(l)):
            if l[j]< l[minPos]:
                minPos = j
        (l[minPos],l[i])=(l[i],l[minPos])
        print(l)
#insertion sort 
def insertionSort(l):
    for sliceEnd in range(len(l)):
        pos = sliceEnd
        while pos > 0 and l[pos]<l[pos-1]:
            (l[pos],l[pos-1])=(l[pos-1],l[pos])
            pos -=1
        print(l)
#Merge Sort
def merge(A,B):
    (C,m,n)=([],len(A),len(B))
    (i,j)=(0,0)

    # i+j < m+n checks if all the elements of both the list have been put into the list C 
    while i+j< m+n:
        if i == m:#if we have reached the end of list A then append list  B's next element 
            C.append(B[j])
            j+=1
        elif j == n:# if we have reached the end of list B then append list A's next element 
            C.append(A[i])
            i+=1
        # compare A's and B's next element and append the smaller one to list C
        elif A[i]<B[j]:
            C.append(A[i])
            i+=1
        elif A[i]>B[j]:
            C.append(B[j])
            j+=1
    return(C)

def mergeSort(A,left,right):

    if right - left <= 1:#Base Case
        return(A[left:right])
    if right-left > 1:#Recursive Call
        mid = (left+right)//2
        L = mergeSort(A,left,mid)
        R = mergeSort(A,mid,right)
        print(merge(L,R))
        return(merge(L,R))

def quickSort(A,l,r):
    if r - l <= 1:
        return()
    yellow = l+1
 
    for green in range(l+1,r):
        if A[green] <= A[l]:
            (A[yellow],A[green]) = (A[green],A[yellow])
            yellow += 1
    (A[yellow-1],A[l]) = (A[l],A[yellow-1])
    print(A)
    quickSort(A,l,yellow-1)
    quickSort(A,yellow,r)

    

print("enter size of the list")
n = int(input())
print("enter "+str(n)+" elements of a list as space separated values: ",end=" ")
mainList = [int(x) for x in input().split(" ")]
list_merged = mainList[:]
list_inserted = mainList[:]
list_selection = mainList[:]
list_quick = mainList[:]
print("********Selection Sort********")
selectionSort(list_selection)
print("********Insertion Sort********")
insertionSort(list_inserted)
print("**********Merge Sort**********")
mergeSort(list_merged,0,len(list_merged))
print("**********Quick Sort**********")
quickSort(list_quick,0,len(list_quick))

