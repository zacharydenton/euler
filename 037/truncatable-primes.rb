#!/usr/bin/env ruby
require 'mathn'
puts (10..1000000).select { |i|
  (0..i.to_s.length-1).all? { |j|
    i.to_s[0..j].to_i.prime? && i.to_s[j..-1].to_i.prime?
  }
}.reduce(:+)
