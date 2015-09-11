#!/usr/bin/env python
def recurring_cycle(n, d):
    # solve 10^s % d == 10^(s+t) % d
    # where t is length and s is start
    for t in range(1, d):
        if 1 == 10**t % d:
            return t
    return 0

longest = max(recurring_cycle(1, i) for i in range(2,1001))
print([i for i in range(2,1001) if recurring_cycle(1, i) == longest][0])
