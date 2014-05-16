#!/usr/bin/env ruby
require 'set'
pentagonals = (1..3000).map { |n| n*(3*n-1)/2 }.to_set
puts pentagonals.to_a.combination(2).select { |a,b|
  pentagonals.include?(a+b) && pentagonals.include?((a-b).abs)
}.map { |a,b| (a-b).abs }.min
