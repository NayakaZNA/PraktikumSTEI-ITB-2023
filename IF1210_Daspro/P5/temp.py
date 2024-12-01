# FUNGSI revbub_sort(arr)
def revbub_sort(arr: list[int], length: int) -> list[int]:
    for i in range(length):
        for j in range(length - i - 1):
            if arr[j] < arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr