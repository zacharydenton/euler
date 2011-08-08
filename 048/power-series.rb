#!/usr/bin/env ruby
puts (1..1000).reduce(0) { |s,n| s + n**n }.to_s[-10..-1]
