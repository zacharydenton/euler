#!/usr/bin/env python

partitions = {}
def partition(n):
    if n < 0: return 0
    if n == 0: return 1
    if n not in partitions:
        # http://mathworld.wolfram.com/PartitionFunctionP.html
        partitions[n] = sum([(-1)**(k+1) * (partition(n - (k * (3 * k - 1) // 2))
            + partition(n - (k * (3 * k + 1) // 2))) for k in range(1, n+1)])
    return partitions[n]

def main():
    print(partition(100) - 1)

if __name__ == "__main__": main()
