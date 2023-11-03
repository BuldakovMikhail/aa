def gnome_sort(arr):
    size = len(arr)
    i = 0
    while i < size:
        if i == 0 or arr[i] >= arr[i - 1]:
            i += 1
        else:
            arr[i], arr[i - 1] = arr[i - 1], arr[i]
            i -= 1

    return arr
