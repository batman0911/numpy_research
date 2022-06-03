if __name__ == '__main__':
    n = int(input("enter n: "))
    test = [3, 5, 6, 2, 4, 3, 2]
    res = []

    for ori in range(1, n + 1):
        if ori not in test:
            res.append(ori)

    print(res)
