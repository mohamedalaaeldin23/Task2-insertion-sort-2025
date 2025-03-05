def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key


grades = [85, 42, 93, 76, 58, 90, 66]
insertion_sort(grades)
print("الدرجات بعد الترتيب:", grades)