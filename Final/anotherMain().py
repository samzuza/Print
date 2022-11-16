def main():
    i = 0
    while i <= 4:
        function1(i)
        i += 1

    print("i is", i)


def function1(i):
    while i >= 1:
        if i % 3 != 0:
            print(i, end=' ')
        i -= 1
        
    print()


main()