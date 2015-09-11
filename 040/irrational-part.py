#!/usr/bin/env python
d = [int(digit) for digit in ''.join((str(digit) for digit in range(1, 10000001)))]
print(d[0] * d[9] * d[99] * d[999] * d[9999] * d[99999] * d[999999])
