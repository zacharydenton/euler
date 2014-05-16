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
    divisors.sort.map{|div| [div, self / div]} 
  end
end

triangles = Enumerator.new do |yielder|
  i = 1
  loop do
    yielder.yield i * (i + 1) / 2
    i += 1
  end
end

puts triangles.detect { |t| t.divisors.count > 500 }
