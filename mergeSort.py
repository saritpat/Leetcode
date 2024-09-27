# Merge Sort
array = [2, 4, 3, 5, 1]



def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        # recurion
        merge_sort(L)
        merge_sort(R)
        
        # merge
        # i = L indx 
        # j = R indx
        # k = merge arr indx
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        # case R arr run out first append remaining L
        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        # case L arr run out first append remaining R
        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
    return arr

print(merge_sort(array))







# Bubble sort O(n^2)
# array = [2, 4, 3, 5, 1]

def bubbleSort(arr):
    for i in range(len(arr)):
        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j+1], arr[j] = arr[j], arr[j+1]
    return arr

print(bubbleSort(array))


# Selection sort  O(n^2)
# array = [2, 4, 3, 5, 1]

# def selection_sort(arr):
#     n = len(arr)
#     for i in range(n):
#         min_idx = i
#         for j in range(i+1, n):
#             if arr[j] < arr[min_idx]:
#                 min_idx = j
#         arr[i], arr[min_idx] = arr[min_idx], arr[i]
#     return arr

# print(selection_sort(array))


# Insertion Sort  O(n^2)
# array = [2, 4, 3, 5, 1]

# def insertion_sort(arr):
#     n = len(arr)
#     for i in range(1, n):
#         key = arr[i]
#         j = i-1
#         while j >= 0 and key < arr[j]:
#             arr[j + 1] = arr[j]
#             j -= 1
#         arr[j + 1] = key
#     return arr

# print(insertion_sort(array))
# 
    