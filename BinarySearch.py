def search(arr, target):
    min, max = 0, len(arr) - 1
    while min <= max:
        mid = int((min + max) / 2)
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            max = mid - 1
        else:
            min = mid + 1