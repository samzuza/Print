def total(i1, i2):
    result = 0
    for i in range(i1, i2 + 1):
        result += i

    return result


def main():
    print("Sum of integers from 1 to 10 is,", total(1, 10))
    print("Sum of integers from 20 to 37 is,", total(20, 37))
    print("Sum of integers from 35 to 50 is,", total(35, 49))


main()
