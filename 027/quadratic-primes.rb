#!/usr/bin/env ruby
require 'mathn'
puts (-999..999).to_a.product((-999..999).to_a).map { |a, b|
  [(0..100).take_while { |n| (n**2 + a*n + b).prime? }.count, a * b]
}.max[1]
