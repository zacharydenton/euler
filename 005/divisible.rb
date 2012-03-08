#!/usr/bin/env ruby

class Numeric
  def divisible_to?(x)
    self > 0 and x.downto(1).all? { |i| self % i == 0 }
  end
end

def divisible_to(x)
  if x < 1
    return false
  elsif x == 1
    return 1
  else
    n = 0
    step = divisible_to(x-1)
    until n.divisible_to? x
      n += step
    end
    return n
  end
end

puts divisible_to(20)
