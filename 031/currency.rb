#!/usr/bin/env ruby
count = 0
200.step(0, -200) do |a|
  a.step(0, -100) do |b|
    b.step(0, -50) do |c|
      c.step(0, -20) do |d|
        d.step(0, -10) do |e|
          e.step(0, -5) do |f|
            f.step(0, -2) do
              count += 1
            end
          end
        end
      end
    end
  end
end
puts count
