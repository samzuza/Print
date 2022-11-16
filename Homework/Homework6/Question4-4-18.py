def convertMillis(millis):
    # finds how many hours
    hours = (millis // (1000 * 60 * 60))
    # finds how many minutes but mods 60
    # so you don't have more than 59 minutes
    minutes = (millis // (1000 * 60)) % 60
    # finds how many minutes but mods 60
    # so you don't have more than 59 seconds
    seconds = (millis // 1000) % 60

    print(str(hours) + ":" + str(minutes) + ":" + str(seconds))
    return


millis = int(input("Enter time in milliseconds: "))

convertMillis(millis)
