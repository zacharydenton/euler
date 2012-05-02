import Data.List (sort, find)

isIncreasing ::  Integer -> Bool
isIncreasing n = show n == sort (show n)

isDecreasing ::  Integer -> Bool
isDecreasing n = show n == reverse (sort (show n))

isBouncy ::  Integer -> Bool
isBouncy n = not (isIncreasing n) && not (isDecreasing n)

bouncy ::  [(Integer, Integer)]
bouncy = b' 1 0 where
    b' n acc | isBouncy n = (n, acc+1) : b' (n+1) (acc+1)
             | otherwise  = (n, acc)   : b' (n+1) acc

main ::  IO ()
main = print $ maybe 0 fst $ find (\(n, b) -> (n * 99) == (b * 100)) bouncy
