#!/usr/bin/env ruby

def cartprod(*args)
  result = [[]]
  while [] != args
    t, result = result, []
    b, *args = args
    t.each do |a|
      b.each do |n|
        result << a + [n]
      end
    end
  end
  result
end

class Integer
    def palindromic?
        digits = self.to_s.split(//)
        return digits == digits.reverse
    end
end

numbers = cartprod((100..999), (100..999))
max = 0
numbers.each do |a, b|
    product = a * b
    if product.palindromic? and product > max
        max = product
    end
end
puts max
