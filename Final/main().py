def main():
    i = 1
    while i <= 6:
        function(i, 2)
        i += 1


def function(i, num):
    for j in range(1, i + 1):
        print(num, end=' ')
        num *= 2

    print()


main()
