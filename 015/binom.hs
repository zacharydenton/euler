factorial ::  Integer -> Integer
factorial n = foldr (*) 1 [1..n]

choose ::  Integer -> Integer -> Integer
choose n k = (factorial n) `div` ((factorial k) * (factorial (n - k)))

main ::  IO ()
main = print $ choose 40 20
