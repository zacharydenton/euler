#!/usr/bin/env ruby
puts 100.downto(1).inject(:*).to_s.each_char.inject(0) {|s,v|s+v.to_i}
