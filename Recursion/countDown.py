def countDown(num):
    if num == 0:
        print("Time ends")
        return

    print("time left", num)

    return countDown(num - 1)

countDown(5)