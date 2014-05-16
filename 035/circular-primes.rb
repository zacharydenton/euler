#!/usr/bin/env ruby
require 'mathn'
puts (1..1000000).select { |i|
  (1..i.to_s.length).all? { |j|
    i.to_s.split('').rotate(j).join('').to_i.prime?
  }
}.count
