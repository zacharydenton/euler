#!/usr/bin/env python
print(sum(1 for i in range(1,100) for x in range(1,100) if len(str(i**x)) == x))
