#!/usr/bin/env ruby
require 'mathn'
puts (1..1000000).each_cons(4).detect { |nums| 
  nums.all? { |n| n.prime_division.length == 4 } 
}[0]
