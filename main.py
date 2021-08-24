import statistics


def new_func_2():
    return 1 + 1


def new_func():
    pass


def err(data):
    mean = statistics.mean(data)
    res = 0
    for i in data:
        res += abs(i-mean)
    res = res / mean / len(data) * 100
    return res


if __name__ == '__main__':
    values = [120, 95, 90, 85, 85]
    p = [0.2 for i in range(5)]
    std = 0
    mean = statistics.mean(values)
    for i in range(5):
        std += values[i]**2*p[i]
    std -= mean**2
    std2 = statistics.stdev(values)
    print(mean, std**0.5, err(values))

