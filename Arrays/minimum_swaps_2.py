def minimumSwaps(arr):
    swaps = 0
    n = len(arr)
    for i in range(0, n - 1):
        while arr[i] != i + 1:
            t = arr[arr[i] - 1]
            arr[arr[i] - 1] = arr[i]
            arr[i] = t
            swaps += 1

    return swaps
