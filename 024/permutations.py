#!/usr/bin/env python
from itertools import islice, permutations
print ''.join(next(islice(permutations(map(str, range(10))), 999999, None)))
