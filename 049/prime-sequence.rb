#!/usr/bin/env ruby
require 'mathn'
primes = (1488..9999).select { |n| n.prime? }
primes.each do |a|
  primes.select { |b| b > a }.each do |b|
    primes.select { |c| c > b }.each do |c|
      if c-b == b-a &&
        a.to_s.split('').sort == b.to_s.split('').sort &&
        b.to_s.split('').sort == c.to_s.split('').sort &&
        c.to_s.split('').sort == a.to_s.split('').sort
        puts a.to_s + b.to_s + c.to_s; exit
      end
    end
  end
end
