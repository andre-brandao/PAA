def maxIncreasing(arr):
    maxLength = 1
    maxStart = 0
    curStart = 0
    curLength = 1
    for i in range(1, len(arr)):
        if arr[i] <= arr[i-1]:
            if curLength > maxLength:
                maxLength = curLength
                maxStart = curStart
            curStart = i
            curLength = 1
        else:
            curLength += 1
    if curLength > maxLength:
        maxLength = curLength
        maxStart = curStart
    return (maxLength, maxStart)
