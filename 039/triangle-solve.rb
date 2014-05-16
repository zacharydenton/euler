#!/usr/bin/env ruby
solutions = {}
(1..500).each do |a|
  (a..500).each do |b|
    (b..500).each do |c|
      if a**2 + b**2 == c**2
        solutions[a+b+c] ||= 0
        solutions[a+b+c] += 1
      end
    end
  end
end
puts solutions.max { |a,b| a[1] <=> b[1] }[0]
