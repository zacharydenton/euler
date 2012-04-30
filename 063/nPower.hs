main ::  IO ()
main = print $ sum $ [1 | i <- [1..99], n <- [1..99], length (show (i^n)) == n]
