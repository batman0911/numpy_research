import numpy as np

if __name__ == "__main__":
    print("---------- basic ------------")

    a: np.ndarray = np.array([1, 2, 3])

    print(type(a))

    print(a.ndim)
    print(a.shape)
    print(a.itemsize)
    print(a.size)
    print(a.data)

    print("---------- util function ----------")

    zeros = np.ndarray = np.zeros((1, 5), dtype=np.int16)
    print(zeros.itemsize)
    print(zeros)

    ones = np.ndarray = np.ones((2, 3), dtype=np.int32)
    print(ones.itemsize)
    print(ones)

    range_1: np.ndarray = np.arange(10, 30, 2)
    print(range_1)

    range_2: np.ndarray = np.linspace(0, 5, 9)
    print(range_2)




