#!/usr/bin/env ruby
require 'mathn'
puts Prime.take_while{ |n| n < 2000000 }.reduce(:+)
