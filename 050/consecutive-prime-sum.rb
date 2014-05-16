#!/usr/bin/env ruby
require 'mathn'
primes = Prime.each(10000).to_a
longest = []
primes[0..10].each_with_index { |p, i|
  j = i
  begin
    j += 1
    cons = primes[i..j]
    sum = cons.reduce(:+)
    if sum.prime? && cons.length > longest.length
      longest = cons
    end
  end while sum < 1000000
}
puts longest.reduce(:+)
