#!/usr/bin/env ruby
require 'mathn' 

class Integer 
  def divisors
    return [1] if self == 1
    primes, powers = self.prime_division.transpose 
    exponents = powers.map{|i| (0..i).to_a} 
    divisors = exponents.shift.product(*exponents).map do |powers| 
      primes.zip(powers).map{|prime, power| prime ** power}.inject(:*) 
    end 
    divisors.take divisors.length - 1
  end

  def abundant?
    self.divisors.reduce(:+) > self
  end
end

abundants = (1..28213).select { |n| n.abundant? }
i = 0
sums = []
abundants.each do |x|
  abundants[i..abundants.length].each do |y|
    sum = x + y
    sums << sum unless sum > 28213
  end
  i += 1
end
sums.uniq!
puts (1..28213).reject { |n| sums.include? n }.reduce(:+)
