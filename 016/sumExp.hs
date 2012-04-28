sumDigits ::  Integer -> Integer
sumDigits n = sumDigits' n 0
    where sumDigits' 0 acc = acc
          sumDigits' n acc = sumDigits' (div n 10) (acc + (mod n 10))

main ::  IO ()
main = print $ sumDigits $ 2^1000
