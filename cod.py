# a = '123'

# def rev(str):
#     ans = ''
#     for i in range(len(str)-1, -1, -1):
#         if len(str) <= 1:
#             return str
#         else:
#             ans += str[i]
#     return ans

# print(rev(a))


# b = 'abcbbcba'

# def palin(str):
#     if len(str) <= 1:
#         return True
#     lst1 = list(str)
#     lst2 = []
#     # for i in str:
#     #     lst1.append(i)
    
#     for i in range(len(str)-1, -1, -1):
#         lst2.append(str[i])

#     return lst1 == lst2

# print(palin(b))


# c = '123abc167b'

# def num_in_string(str):
#     num = '1234567890'
#     count = 0
#     ans = 0
#     for i in str:
#         if i in num:
#             count += 1
#             ans += int(i)

#     return count, ans

# print(num_in_string(c))


# c = '123abc167baacbbg'
# cha = 'b'

# def count_char(str, char):
#     count = 0
#     for i in str:
#         if i in char:
#             count += 1

#     return count

# print(count_char(c, cha))


# c = '123abc167baacbbg'

# def uniqe_char(str):
#     sets = set()
#     for i in str:
#         sets.add(i)

#     return sets

# print(uniqe_char(c))


# s1 = 'listen'
# s2 = 'silent'

# def anagram(str1, str2):
#     if len(str1) != len(str2):
#         return False
    
#     dict1 = {}
#     dict2 = {}
    
#     for i in str1:
#         dict1[i] = dict1.get(i, 0) + 1
    
#     for i in str2:
#         dict2[i] = dict2.get(i, 0) + 1
    
#     if dict1 == dict2:
#         return True
    
#     return False

# print(anagram(s1, s2))


# s = 'listen'

# def count_vowel_consonant(str):
#     vowel = 'aeiou'
#     countV = 0
#     countC = 0
#     for i in str:
#         if i in 'vowel':
#             countV += 1
#         else:
#             countC += 1
#     return countV, countC

# print(count_vowel_consonant(s))

# arr= [2,1,2,3,2]

# def find_match_num(arr):
#     dict = {}
#     for i in arr:
#         dict[i] = dict.get(i, 0) + 1

#     return dict

# print(find_match_num(arr))


# arr= ['a','b','c','d','e','f','g']

# def reverse_arr(arr):
#     ans = []
#     for i in range(len(arr)-1, -1, -1):
#         ans.append(arr[i])

#     return ans

# print(reverse_arr(arr))

# arr = [2,1,2,3,2,711,10,99,5]

# def max(arr):
#     ans = 0
#     for i in arr:
#         if i > ans:
#             ans = i

#     return ans

# print(max(arr))

# arr = [2, 4, 3, 5, 1, 2, 9, 7, 4]

# def sort(arr):
#     if len(arr) > 1:
#         mid = len(arr) // 2

#         L = arr[:mid]
#         R = arr[mid:]

#         sort(L)
#         sort(R)

#         # merge
#         i = j = k = 0
#         while i < len(L) and j < len(R):
#             if L[i] < R[j]:
#                 arr[k] = L[i]
#                 i += 1
                
#             else:
#                 arr[k] = R[j]
#                 j += 1
                
#             k += 1

#         while j < len(R):
#             arr[k] = R[j]
#             j += 1
#             k += 1

#         while i < len(L):
#             arr[k] = L[i]
#             i += 1
#             k += 1

#     return arr

# print(sort(arr))


# def fibonacci(num):
#     if num == 0:
#         return 0

#     if num == 1:
#         return 1

#     return fibonacci(num-2) + fibonacci(num-1)

# for i in range(10):
#     print(fibonacci(i))


# def sum(a, b):
#     return a+b

# print(sum(1, 100000))


# def avg(lst):
#     sum = 0
#     for i in lst:
#         sum += i
#     return sum / len(lst)

# print(avg([9,9,9,9,9,9,9]))

# def even_odd(a):
#     if a % 2 == 0:
#         return 'even'
#     return 'odd'

# print(even_odd(200102))



arr = [1, 3, 5, 2, 7]

def merge_sort(arr):
    # divide
    if len(arr) > 1:
        middle = len(arr) // 2
        L = arr[:middle]
        R = arr[middle:]

        # recur
        merge_sort(L)
        merge_sort(R)

        i = 0
        j = 0
        k = 0
        # merge
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                print('if',arr)
                i += 1

            else:
                arr[k] = R[j]
                print('el',arr)
                j += 1
            
            k += 1

        while j < len(R):
            arr[k] = R[j]
            print('R',arr)
            j += 1
            k += 1
        
        while i < len(L):
            arr[k] = L[i]
            print('L',arr)
            i += 1
            k += 1
        
    return arr

print(merge_sort(arr))