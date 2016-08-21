
class CoinSum:
    def __init__(self):
        pass

    def Sum(self, v, s):
        min = [9999] * (s + 1)
        min[0] = 0

        for i in range(1, s + 1):
            for j in v:
                if (j <= i) and ((min[i-j] + 1) <= min[i]):
                    min[i] = min[i-j] + 1

        return min[s]


def main():
    CS = CoinSum()

    print (CS.Sum([1, 2, 5], 9))


main()

