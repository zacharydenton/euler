fibs ::  [Integer]
fibs = 0 : 1 : zipWith (+) fibs (tail fibs)

main ::  IO ()
main = print $ head [i | i <- [1..], (==1000) . length . show $ fibs !! i]
