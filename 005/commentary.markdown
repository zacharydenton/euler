The critical insight of this problem is this:

$$divisibleto(x) = n \times divisibleto(x-1)$$

This means that when searching for the smallest number divisible to 20,
we can increment by the smallest number divisible to 19 each time (since the 
smallest number divisible to 19 is inherently a factor of the smallest number
divisible to 20).

This insight is used in the python solution on line 14:

	step = divisible_to(x-1)

This is a recursive solution to the problem, and yields incredible performance. It can calculate
the smallest number divisible to 500 in a fraction of a second.
