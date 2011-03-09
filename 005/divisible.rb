#!/usr/bin/env ruby

class Numeric
    def divisible_to?(x)
        (1..x).each do |i|
            if self % i != 0 
                return false
            end
        end
        return true
    end
end

def divisible_to(x)
    if x < 1
        return false
    elsif x == 1
        return 1
    else
        step = divisible_to(x-1)
        number = 0
        found = false
        while not found
            number += step
            found = number.divisible_to? x
        end
        return number
    end
end

puts divisible_to(20)

