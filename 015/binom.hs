factorial ::  Integer -> Integer
factorial n = product [1..n]

choose ::  Integer -> Integer -> Integer
choose n k = div (factorial n) $ factorial k * factorial (n - k)

main ::  IO ()
main = print $ choose 40 20
