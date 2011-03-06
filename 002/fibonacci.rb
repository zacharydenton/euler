#!/usr/bin/env ruby
sum = 0
t1 = 1
t2 = 2
while t2 < 4000000
	if t2 % 2 == 0
		sum += t2
	end
	t1, t2 = t2, t1 + t2
end
puts sum
