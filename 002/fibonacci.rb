#!/usr/bin/env ruby
sum, a, b = 0, 1, 2
while b < 4000000
	sum += b if b % 2 == 0
	a, b = b, a + b
end
puts sum
