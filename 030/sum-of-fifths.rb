#!/usr/bin/env ruby
puts (2..500000).select { |i|
  i == i.to_s.each_char.map { |d| d.to_i**5 }.reduce(:+)
}.reduce(:+)
