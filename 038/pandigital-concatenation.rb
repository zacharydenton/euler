#!/usr/bin/env ruby
p (1..9999).flat_map { |i|
  (1..9).map { |j|
    (1..j).map { |k|
      i * k
    }.reduce('') { |s,v| s + v.to_s }
  }
}.select { |s|
  s.length == 9 && s.split('').sort.join('') == '123456789'
}.map { |s| s.to_i }.max

