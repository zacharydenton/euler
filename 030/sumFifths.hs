digits ::  Integer -> [Integer]
digits n = digits' n []
    where digits' 0 acc = acc
          digits' n acc = digits' (div n 10) (mod n 10 : acc)

main = print $ sum [n | n <- [2..500000], sum (map (^5) (digits n)) == n]
