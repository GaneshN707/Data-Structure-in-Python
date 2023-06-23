
def binary_search(a, size, key):
    i = 0
    j = size - 1
    flag = 0
    while i <= j and flag == 0:
        mid = (i + j) // 2
        if a[mid] == key:
            position = mid
            flag = 1
        elif a[mid] > key:
            j = mid - 1
        else:
            i = mid + 1

    if flag == 1:
        print(f"{key} found at position {position}.")
    else:
        print("Number not found.")
a = []
size = int(input("Enter size of the list: "))
for i in range(size):
    val = int(input("Enter a number: "))
    a.append(val)
print(a)
key = int(input("Enter the number to search: "))
binary_search(a, size, key)

