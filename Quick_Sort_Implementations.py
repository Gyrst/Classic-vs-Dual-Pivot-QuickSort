import sys

#Sentinels --> Just pointers
sentinel = -sys.maxsize-1

def swap(A, i, j):
    temp = A[i]
    A[i] = A[j]
    A[j] = temp

def swap2(A, i, j):
    A[i], A[j] = A[j], A[i]
    return A


def quick_sort(A, left, right):
    if right - left >= 1:
        p = A[right]; i = left-1; j = right

        #Currently it will not run any single interation if j>i is not satisfied.
        while j>i:
            i+=1
            while A[i] < p:
                i+= 1
            
            j-=1
            while A[j] > p:
                j-=1
            if j>i:
                swap2(A, i, j)
        
        swap2(A, i, right)
        quick_sort(A, left, i-1)
        quick_sort(A,i+1,right)
    
    return A



#Alternative version that is not stopped by
def quick_sort2(A, left, right):
    if right - left >= 1:

        p = A[right]; i = left-1; j = right

        #Here it will at least run once before it haults
        while True:
            i+=1
            while A[i] < p:
                i+= 1
            
            j-=1
            while A[j] > p:
                j-=1
            if j>i:
                swap2(A, i, j)
            if j>i:
                break     
        swap2(A, i, right)
        quick_sort2(A, left, i-1)
        quick_sort2(A,i+1,right)

    return A


def classic_quicksort(list):
    return quick_sort(list, 0, len(list)-1)



#Dual-QuickSort

def dual_pivot_quick_sort(A, left, right):
    if right - left >= 1:

        if A[left] > A[right]:
            swap2(A, left, right)
        
        p = A[left]; q= A[right]
        if p>q: swap2(A, p, q)

        l = left + 1; g = right-1; k = l
        
        while k <= g:
            if A[k] < p:
                swap2(A, k, l)
                l+= 1
            else:
                if A[k] > q:
                    while (A[g] > q) & (k < g):
                        g-= 1
                    swap2(A, k, g)
                    g-=1
                    if A[k] < p:
                        swap2(A, k, l)
                        l+= 1
            k += 1
        l-= 1
        g+= 1
        swap2(A, left, l)
        swap2(A, right, g)

        dual_pivot_quick_sort(A, left, l-1)
        dual_pivot_quick_sort(A, l+1, g-1)
        dual_pivot_quick_sort(A, g+1, right)  

    return A

def dual_quicksort(list):
    return dual_pivot_quick_sort(list, 0, len(list)-1)


def standard_lib_sort(list):
    return list.sort()
