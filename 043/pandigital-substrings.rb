#!/usr/bin/env ruby
primes = [1,2,3,5,7,11,13,17]
puts ('0'..'9').to_a.permutation.select { |digits| 
  (1..7).all? { |i|
    digits[i..i+2].join('').to_i % primes[i] == 0
  }
}.map { |digits| digits.join('').to_i }.reduce(:+)
