#!/usr/bin/env python
import itertools
print(len(set(a**b for a,b in itertools.product(list(range(2,101)), repeat=2))))
