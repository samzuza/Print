def series():
    print("i\t\t\t\t m(i)")

    i = 1
    m = 0
    # range of 1 - 20
    for i in range(1, 21):
        m = m + (i / (i + 1))
        print(i, "\t\t\t\t", round(m, 4))
        i += 1
    return

series()
