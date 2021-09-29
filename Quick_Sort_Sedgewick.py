# # 1) 3-way partitioning
# # 2) Needs to swap <=  only!
# # 3) here we use >= and <= for both side partitions so it takes the equal element in account



# #Quicksort - Sedgewick version
# test = [2,4,6,1,4,3,19,4,5]

# def exchange(list, i, j):
#     temp = list[i]
#     list[i] = j
#     list[j] = temp
#     return list

# def is_sorted(list, lo, hi):
#     i = lo+1
#     for i in range(hi):
#         if (list[i-1] > list[i]): return False
#     return True


# def partition(list, lo, hi):
#     i = lo
#     j = hi
#     v = list[lo]

#     while True:

        
#         while list[i] < v:
#             if i == hi: break
#             i+=1
        
#         while list[j] > v:
#             if j == lo: break
#             j-=1

#         if (i >= j): break

#         exchange(list, i, j)
    
#     exchange(list, lo, j)

#     return j

# def sort(list, lo, hi):
#     if (hi <= lo): return
#     j = partition(list, lo, hi)
#     sort(list, lo, j-1)
#     sort(list, j+1, hi)
#     if is_sorted(list, lo, hi):
#         return list

# def quick_sort(list):
#     sorted_list = sort(list, 0, len(list)-1)
#     return sorted_list


# result = quick_sort(test)
# print(result)

# """ 
# A sentinel is dummy element that we add to the situation.
# we set the first element to be - infinity for instance, so that we don't have to make index tests
# we can simply just see if we reach this sentinel element
# """
