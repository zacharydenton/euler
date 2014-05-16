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
    divisors.sort.take divisors.length - 1
  end

  def amicable?(n=self.divisors.reduce(:+))
    n != self && n.divisors.reduce(:+) == self
  end
end

puts (1..10000).find_all { |n| n.amicable? }.reduce(:+)
