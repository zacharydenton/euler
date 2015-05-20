#!/usr/bin/env ruby
puts ((1..100).inject(0) {|s,v| s += v})**2 - ((1..100).collect {|x| x**2}.inject(0) { |s,v| s += v})
