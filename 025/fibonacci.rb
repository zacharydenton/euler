#!/usr/bin/env ruby
i = 1
t1, t2 = 0, 1
while t2.to_s.length < 1000
  t1, t2 = t2, t1 + t2
  i += 1
end
puts i
