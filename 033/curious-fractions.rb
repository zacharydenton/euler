#!/usr/bin/env ruby
puts ('10'..'99').to_a.product(('10'..'99').to_a).select { |num, den|
  (num[0].to_f / den[1].to_f) == (num.to_f / den.to_f) && num[1] == den[0] && num[1] != den[1]
}.uniq.map { |num, den| [num.to_i, den.to_i] }.reduce([1, 1]) { |p, v|
  f = [p[0] * v[0], p[1] * v[1]]
  [f[0] / f[0].gcd(f[1]), f[1] / f[0].gcd(f[1])]
}[1]
