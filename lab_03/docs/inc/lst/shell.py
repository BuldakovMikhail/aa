def shell_sort(arr):
    size = len(arr)
    step = size // 2
    while step > 0:
        for i in range(step, size, 1):
            j = i
            delta = j - step
            while delta >= 0 and arr[delta] > arr[j]:
                arr[delta], arr[j] = arr[j], arr[delta]
                j = delta
                delta = j - step
        step //= 2
    return arr
