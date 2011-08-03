#!/usr/bin/env ruby
require 'date'
puts Date.new(1901,1,1).upto(Date.new(2000,12,31)).find_all { |d| d.mday == 1 && d.wday == 0 }.count
