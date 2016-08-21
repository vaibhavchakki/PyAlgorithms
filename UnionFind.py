
class UnionFind:

    def __init__(self, n):
        self._id = list(range(n))
        self._sz = [1] * n


    def _root(self, i):

        while (i != self._id[i]):
            i = self._id[i]

        return i

    def Find(self, p, q):
        return self._root(p) == self._root(q)


    def Union(self, p, q):
        i = self._root(p)
        j = self._root(q)

        if self._sz[i] > self._sz[j]:
            self._id[i]  = j
            self._sz[i] += 1
        else:
            self._id[j]  = i
            self._sz[j] += 1


def main():
    uf = UnionFind(10)
    uf.Union(0, 1)
    uf.Union(1, 3)
    uf.Union(3, 5)
    uf.Union(2, 4)
    uf.Union(4, 6)
    uf.Union(3, 4)
    uf.Union(7, 8)

    print("Found: %d" % uf.Find(3, 6))


main()