#!/usr/bin/env ruby
puts (0..50000).select { |i|
  i.to_s.length > 1 && i == i.to_s.each_char.map { |d| (1..d.to_i).reduce(1, :*) }.reduce(:+)
}.reduce(:+)
