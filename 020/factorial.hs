sumDigits ::  Integer -> Integer
sumDigits n = sumDigits' n 0
    where sumDigits' 0 acc = acc
          sumDigits' n acc = sumDigits' (div n 10) (acc + (mod n 10))

factorial ::  Integer -> Integer
factorial n = foldr (*) 1 [1..n]

main = print $ sumDigits $ factorial 100
