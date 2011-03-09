#!/usr/bin/env ruby
puts (2**1000).to_s.each_char.inject(0) {|s,v| s+v.to_i}
