#!/usr/bin/env python
import itertools
print len(set(a**b for a,b in itertools.product(range(2,101), repeat=2)))
