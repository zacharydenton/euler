#!/usr/bin/env ruby
puts (2..100).to_a.product((2..100).to_a).map { |a,n| a**n }.uniq.count
