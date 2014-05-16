#!/usr/bin/env ruby
require 'set'
p = (1..100000).map { |n| n*(3*n-1)/2 }.to_set
h = (1..100000).map { |n| n*(2*n-1) }.to_set
puts (286..100000).map { |n| n*(n+1)/2 }.detect { |t|
  p.include?(t) and h.include?(t)
}
