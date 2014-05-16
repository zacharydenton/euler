#!/usr/bin/env ruby
i = 1
sum = i
step = 2
until i >= 1001**2
  4.times { sum += i += step }
  step += 2
end
puts sum
