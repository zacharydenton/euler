#!/usr/bin/env ruby
require 'set'

def factorize(orig)
  factors = {}
  factors.default = 0 # return 0 instead nil if key not found in hash
  n = orig
  i = 2
  sqi = 4 # square of i
  while sqi <= n do
    while n.modulo(i) == 0 do
      n /= i
      factors[i] += 1
    end
    # we take advantage of the fact that (i +1)**2 = i**2 + 2*i +1
    sqi += 2 * i + 1
    i += 1
  end

  if (n != 1) && (n != orig)
    factors[n] += 1
  end
  factors
end

def totient(n)
  n * factorize(n).each_key.map { |p| 1 - 1.0 / p }.reduce(1, :*)
end

puts (2..1000000).map { |n| [n / totient(n), n] }.max[1]
