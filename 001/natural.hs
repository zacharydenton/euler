main ::  IO ()
main = print $ sum [n | n <- [1..999], or [(n `mod` 3 == 0), (n `mod` 5 == 0)]]
