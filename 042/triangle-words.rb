#!/usr/bin/env ruby
triangles = (1..1000).map { |n| (n*(n+1))/2 }.to_a
puts File.read(File.dirname(__FILE__) + '/words.txt').scan(/\w+/).select { |word|
  triangles.include? word.each_byte.reduce(0) {|s,v| s+(v-64) }
}.count

