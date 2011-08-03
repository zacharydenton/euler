#!/usr/bin/env ruby
require 'linguistics' # gem install linguistics
Linguistics::use( :en )
puts (1..1000).map { |i| i.en.numwords.gsub(/[ -]/, '').length }.reduce(:+)
