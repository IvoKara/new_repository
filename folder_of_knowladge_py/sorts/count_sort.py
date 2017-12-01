def CountSort(n, arr):
    '''
    >>> CountSort(6, [1, 4, 3, 5, 6, 2])
    [1, 2, 3, 4, 5, 6]
    >>> CountSort(6, [3, 2, 9, 8, 1, 10])
    [1, 2, 3, 8, 9, 10]
    '''
    list_len = max(arr) + 1
    listzeros = [0]*(list_len)
    for i in arr:
        listzeros[i] += 1
    arr_sorted = []
    for i in range(list_len):
        if listzeros[i] > 0:
            arr_sorted.extend([i]*listzeros[i])
    return arr_sorted

if __name__ == "__main__":
    import doctest
    doctest.testmod()
