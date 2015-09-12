#!/usr/bin/env python
from itertools import islice, permutations
print(''.join(next(islice(permutations(list(map(str, list(range(10))))), 999999, None))))
