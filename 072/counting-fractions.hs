farey :: Int -> Int
farey = (map f [0..] !!) where
    f n = (n*(n + 3)) `quot` 2 - sum [farey (n `quot` k) | k <- [2..n]]

main :: IO ()
main = print $ farey 1000000 - farey 1
