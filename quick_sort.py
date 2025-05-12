def quick_sort(array, start, end):
    if start >= end:
        return

    anchor = array[start]
    left = start + 1
    right = end

    print(f"處理區段：{array[start:end+1]}")
    print(f"基準點：{anchor}")

    while left <= right:
        while left <= right and array[right] >= anchor:
            right -= 1
        while left <= right and array[left] <= anchor:
            left += 1
        if left < right:
            print(f"交換：{array[left]} 與 {array[right]}")
            array[left], array[right] = array[right], array[left]
            print(f"目前陣列：{array}\n")

    print(f"交換：{array[start]} 與 {array[right]}")
    array[start], array[right] = array[right], array[start]
    print(f"目前陣列：{array}\n")

    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)

if __name__ == "__main__":
    data = [33, 67, 8, 13, 54, 119, 3, 84, 25, 41]
    print(f"原始陣列：{data}\n")
    quick_sort(data, 0, len(data) - 1)
    print(f"排序後陣列：{data}\n")