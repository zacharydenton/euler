#!/usr/bin/env ruby
require 'set'
require 'mathn'
primes = (2..10000).select { |n| n.prime? }.to_set
composites = (2..10000).reject { |n| n.prime? }.to_set
twicesquares = (0..100).map { |n| 2*(n**2) }.to_set
sums = primes.to_a.product(twicesquares.to_a).map { |a,b| a+b }.to_set
puts composites.select { |n| !sums.include?(n) and n.odd? }.min
