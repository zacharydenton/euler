#!/usr/bin/env ruby

names = File.open(File.dirname(__FILE__) + '/names.txt').read.scan(/\w+/).sort
puts names.map { |name| 
  word_score = name.each_byte.map { |c| c - 64 }.reduce(:+)
  (names.index(name) + 1) * word_score
}.reduce(:+)
