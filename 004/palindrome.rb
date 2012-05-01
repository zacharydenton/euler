#!/usr/bin/env ruby

class Integer
  def palindromic?
    digits = self.to_s.split('')
    return digits == digits.reverse
  end
end

max = 0
(100..999).each do |a|
  (a..999).each do |b|
    product = a * b
    if product > max and product.palindromic?
      max = product
    end
  end
end
puts max
