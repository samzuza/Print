def selectionSort(lst):
    for i in range(len(lst) - 1):
        currentMin = min(lst[i: ])
        currentMinIndex = i + lst[i: ].index(currentMin)

        if currentMinIndex != 1:
            lst[currentMinIndex], lst[i] = lst[i], currentMin

def main():
    lst = [4.5, 5, -2, 1, 2, -3.3]
    selectionSort(lst)
    print(lst)

main()