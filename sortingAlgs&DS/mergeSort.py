# def merge_sort(arr):
#     if len(arr) <= 1:
#         return arr
#
#     mid = len(arr) // 2
#     left = merge_sort(arr[:mid])
#     right = merge_sort(arr[mid:])
#
#     return merge(left, right)
#
# def merge(left, right):
#     result = []
#     i = j = 0
#
#     while i < len(left) and j < len(right):
#         if left[i] < right[j]:
#             result.append(left[i])
#             i += 1
#         else:
#             result.append(right[j])
#             j += 1
#
#     result.extend(left[i:])
#     result.extend(right[j:])
#     return result
#
# # Example usage
# arr = [12, 11, 13, 12, 5, 6, 6 ,7]
# sorted_arr = merge_sort(arr)
# print("Sorted array:", sorted_arr)

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)

def merge(left, right):
    result = []
    while left and right:
        result.append(left.pop(0) if left[0] <= right[0] else right.pop(0))
        # result.append(left.pop(0) if left[0] >= right[0] else right.pop(0))
    return result + left + right

# Example usage
arr = [12, 11, 13, 12, 5, 6, 6 ,7]
sorted_arr = merge_sort(arr)
print("Sorted array:", sorted_arr)
