isPrime :: Int -> Bool
isPrime n | n < 1 = False
          | otherwise = not $ or [n `rem` x == 0 | x <- [2..floor $ sqrt $ fromIntegral n]]

primeCorners :: Int -> Int
primeCorners n = sum [1 | x <- [1..3], isPrime $ n^2 - x*(n - 1)]

expansion :: [(Int, Int)]
expansion = scanl (\(p, t) x -> (p + primeCorners x, t + 4)) (0, 1) [3,5..]

main :: IO ()
main = print $ 3 + 2 * (length $ takeWhile id $ tail [10*p >= t | (p, t) <- expansion])
