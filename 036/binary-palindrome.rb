#!/usr/bin/env ruby
class String
  def palindrome?
    self == self.reverse
  end
end

puts (1..1000000).select { |i| i.to_s.palindrome? && i.to_s(2).palindrome? }.reduce(:+)
