choose :: Integer -> Integer -> Integer
choose _ 0 = 1
choose 0 _ = 0
choose n r = choose (n-1) (r-1) * n `div` r

main :: IO ()
main = print $ length $ filter (> 1000000) [n `choose` r | n <- [1..100], r <- [1..n]]
