# No linked-lists


# class Solution(object):
#     def mergeKLists(self, lists):
#         """
#         :type lists: List[ListNode]
#         :rtype: ListNode
#         """
#         lst = []
#         for i in range(len(lists)):
#             for j in lists[i]:
#                 lst.append(j)
        
#         lst.sort()
#         return lst




# s = Solution()
# x = [[1,4,5],[1,3,4],[2,6]]
# print(s.mergeKLists(x))

# lst = [1,2]
# for i in lst[::-1]:
#     print(i)

# lst = [1,1,1,1,2,12]
# lst.remove(1)
# print(lst)




from collections import Counter

lst = ['a','b','c']
c= Counter(lst)
for i in c:
    print(i)



x = 2.0001
print(f"{x:.2f}")








import itertools

lst = [1,2,3]

l = list(itertools.permutations(lst))
c = list(itertools.combinations(lst, 2))

print(l)
print(c)


diff = 7
count = (-(-diff // 2))
print(count)


number = 20
def recursive(number):
    if number <= 1:
        return number

    return recursive(number - 4) + recursive(number - 2)

print(recursive(number))


        #         arr

        #     L          R 
        # 1      1   2       3
        # L      R   L       R







arr = [3,2,5,1,4]

def sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        sort(L)
        sort(R)

        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] > R[j]:
                arr[k] = R[j]
                j+=1
            else:
                arr[k] = L[i]
                i+=1

            k += 1

        while i < len(L):
            arr[k] = L[i]
            i+=1
            k+=1

        while j < len(R):
            arr[k] = R[j]
            j+=1
            k+=1     

    return arr   



print(sort(arr))