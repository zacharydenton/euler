main ::  IO ()
main = print $ (s*s) - sqS where
    s = sum [1..100]
    sqS = sum [i * i | i <- [1..100]]
