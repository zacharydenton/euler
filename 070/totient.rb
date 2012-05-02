#!/usr/bin/env ruby
require 'mathn'

min = [100, 0]
primes = (1..(2*Math.sqrt(1e7))).select { |n| n.prime? }
primes.combination(2).select { |a, b| a * b < 1e7 }.each do |a, b|
  n = a * b
  t = (a - 1) * (b - 1)
  if n.to_s.split('').sort == t.to_s.split('').sort
    if n / t < min[0]
      min = [n / t, n]
    end
  end
end
puts min[1]
