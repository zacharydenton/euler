#!/usr/bin/env ruby
s = ('1'..'1000000').to_a.join ''
puts (0..6).map { |i|
  s[(10**i)-1].to_i
}.reduce(1, :*)
