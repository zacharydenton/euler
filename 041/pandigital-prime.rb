#!/usr/bin/env ruby
require 'mathn'
puts (1..9).flat_map { |n|
  ('1'..n.to_s).to_a.permutation.map { |p|
    p.join('').to_i
  }.select { |i| i.prime? }
}.max
