def inplace_quick_sort(alist, l, r):
    if r - l <= 1:
        return None
    pivot = alist[r-1]
    i,j = l, l
    patrition = False
    while j < r:
        if alist[j] <= pivot:
            alist[j], alist[i] = alist[i], alist[j]
            i+=1
        j+=1
    for num in alist:
        print(num, end=" ")
    print()
    inplace_quick_sort(alist, l, i-1)
    inplace_quick_sort(alist, i, r)

print(inplace_quick_sort([1,3,9,8,2,7,5],0,7))
