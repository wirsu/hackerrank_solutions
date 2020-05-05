def hourglassSum(arr):
    max_hourglass_sum = - 63
    for i in range(1,5):
        for j in range(1,5):
            sumx = 0
            sumx += arr[i-1][j-1]
            sumx += arr[i-1][j]
            sumx += arr[i-1][j+1]
            sumx += arr[i][j]
            sumx += arr[i+1][j-1]
            sumx += arr[i+1][j]
            sumx += arr[i+1][j+1]
            current_hourglass_sum = sumx
            if current_hourglass_sum > max_hourglass_sum:
                max_hourglass_sum = current_hourglass_sum

    return max_hourglass_sum