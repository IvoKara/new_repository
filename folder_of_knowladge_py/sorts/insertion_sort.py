def InsertionSort(arr, n):
    '''
    >>> InsertionSort([1, 4, 3, 5, 6, 2], 6)
    [1, 2, 3, 4, 5, 6]
    >>> InsertionSort([3, 2, 9, 8, 1, 10], 6)
    [1, 2, 3, 8, 9, 10]
    '''
    for i in range(1,n):
        for j in range(i,0,-1):
            if arr[j] < arr[j-1]:
                arr[j], arr[j-1] = arr[j-1], arr[j]
    return arr

if __name__ == "__main__":
    import doctest
    doctest.testmod()
