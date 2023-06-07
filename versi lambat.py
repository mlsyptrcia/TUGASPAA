import time

def bubble_sort_slow(arr):
    n = len(arr)
    start_time = time.time()

    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    end_time = time.time()
    execution_time = end_time - start_time
    return execution_time


# Contoh penggunaan
data = [64, 34, 25, 12, 22, 11, 90, 5, 17, 38, 74, 59, 83, 31, 42, 67, 21, 8, 96, 52, 77, 46, 19, 30, 63, 88, 14, 41, 9, 55, 71, 27, 7, 36, 69, 93, 28, 49, 80, 15, 3, 87, 58, 99, 39, 16, 65, 47, 92, 20, 85, 33, 70, 53, 18, 81, 44, 10, 66, 75, 54, 29, 79, 23, 2, 95, 51, 76, 37, 91, 6, 43, 72, 13, 84, 26, 60, 45, 97, 32, 89, 24, 82, 48, 68, 56, 40, 94, 57, 78, 4, 61, 98, 50, 73, 35, 86, 62]
execution_time = bubble_sort_slow(data)
print("Data setelah diurutkan:", data)
print("Waktu eksekusi:", execution_time, "detik")
