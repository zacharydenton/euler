#!/usr/bin/env ruby
puts (0..1000).map { |d| 
  (1..d).detect(lambda{0}) { |t| (10**t % d) == 1 } 
}.each_with_index.max[1]
