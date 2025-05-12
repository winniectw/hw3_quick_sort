swap_count = 0
ascending = True

def quick_sort(array, start, end):
    global swap_count, ascending

    if start >= end:
        return

    anchor = array[start]
    left = start + 1
    right = end

    print(f"處理區段：{array[start:end+1]}")
    print(f"基準點：{anchor}")

    while left <= right:
        if ascending:
            while left <= right and array[right] >= anchor:
                right -= 1
            while left <= right and array[left] <= anchor:
                left += 1
        else:
            while left <= right and array[right] <= anchor:
                right -= 1
            while left <= right and array[left] >= anchor:
                left += 1

        if left < right:
            print(f"交換：{array[left]} 與 {array[right]}")
            array[left], array[right] = array[right], array[left]
            swap_count += 1
            print(f"目前陣列：{array}")
            input("按Enter繼續...\n")

    print(f"交換：{array[start]} 與 {array[right]}")
    array[start], array[right] = array[right], array[start]
    swap_count += 1
    print(f"目前陣列：{array}")
    input("按Enter繼續...\n")

    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)

if __name__ == "__main__":
    default_data = [33, 67, 8, 13, 54, 119, 3, 84, 25, 41]
    user_input = input("請輸入數字(以逗號分隔)，或按Enter使用預設陣列：\n")

    try:
        if user_input.strip() == "":
            data = default_data.copy()
        else:
            str_items = [item.strip() for item in user_input.split(',')]
            if "" in str_items:
                raise ValueError("有空白值或重複逗號")
            for item in str_items:
                if not item.lstrip("-").isdigit():
                    raise ValueError(f"有非整數項目「{item}」")
            data = [int(item) for item in str_items]

        order_input = input("請選擇排序方式：a表示升序，或d表示降序：\n").strip().upper()
        if order_input == "d":
            ascending = False
        elif order_input == "a" or order_input == "":
            ascending = True
        else:
            raise ValueError("只能輸入a(升序)或d(降序)")

        print(f"原始陣列：{data}\n")
        quick_sort(data, 0, len(data) - 1)
        print(f"排序後陣列：{data}")
        print(f"總交換次數：{swap_count}\n")

    except ValueError as VE:
        print(f"輸入錯誤：{VE}")