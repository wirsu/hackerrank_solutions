def maxSubsetSum(arr):
    #dynamic table to fill
    n = len(arr)
    v = [0] * n

    for i in range(n):
        if i < 2:
            v[i] = max(arr[i], 0)
            continue
        elif i == 2:
            v[i] = v[i - 2] + max(arr[i], 0)
            continue

        v[i] = max(v[i-2], v[i-3]) + max(arr[i], 0)

    return (max(v[-1], v[-2]))