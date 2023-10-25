def counting_sort(arr):
    max_value = max(arr)
    min_value = min(arr)
    range_of_values = max_value - min_value + 1
    count = [0] * range_of_values
    output = [0] * len(arr)

    for num in arr:
        count[num - min_value] += 1

    for i in range(1, len(count)):
        count[i] += count[i - 1]

    for num in reversed(arr):
        output[count[num - min_value] - 1] = num
        count[num - min_value] -= 1

    return output
