def merge_sort(arr):
    if len(arr) <= 2:
        return sorted(arr)
    mid = int(len(arr)/2)
    begin = merge_sort(arr[:mid])
    end = merge_sort(arr[mid:])
    merge = []
    i,j = 0,0
    while i < len(begin) and j< len(end):
        if begin[i] < end[j]:
            merge.append(begin[i])
            i+=1
        else:
            merge.append(end[j])
            j+=1
    merge.extend(begin[i:])
    merge.extend(end[j:])
    return merge

# def qsort(nums):
#     pivot = random.choice(nums)
#     return qsort(filter(lambda x: x < pivot, qsort(max())))
# print(merge_sort([10,3,20,5]))
# print(merge_sort([3,2,4,2,11,10]))
print(merge_sort([10, 9, 8, 7, 6, 5, 4, 3,2, 1]))