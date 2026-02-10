def maxRequestInWindow(timestamp, windowSize):
    timestamp.sort()
    left = 0
    max_requests = 0

    for right in range(len(timestamp)):
        while timestamp[right] - timestamp[left] >= windowSize:
            left += 1

        current_window = right - left + 1
        max_requests = max(max_requests, current_window)

    return max_requests


timestamp = [1,3,7,5]
windowSize = 4
print(maxRequestInWindow(timestamp, windowSize))
# Answer should be 2