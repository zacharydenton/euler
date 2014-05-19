import Data.List (sort)

primes :: [Int]
primes = 2 : sieve primes [3,5..] where
    sieve (p:ps) xs = h ++ sieve ps [x | x <- t, rem x p /= 0]
                      where (h, t) = span (< p*p) xs

isPrime :: Int -> Bool
isPrime n | n < 1 = False
          | otherwise = not $ or [n `rem` x == 0 | x <- [2..floor $ sqrt $ fromIntegral n]]

candidates :: [[Int]]
candidates = tail [ps | p <- dropWhile (< 1000) primes,
                        let ps = [p, p + 3330, p + 6660],
                        all isPrime ps,
                        let sorted = map (sort . show) ps,
                        all (== head sorted) sorted]

main :: IO ()
main = putStrLn $ concatMap show $ head candidates
