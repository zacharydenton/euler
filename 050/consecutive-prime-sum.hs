import Data.Function (on)
import Data.List (maximumBy)

primes :: [Int]
primes = 2 : sieve primes [3,5..] where
    sieve (p:ps) xs = h ++ sieve ps [x | x <- t, rem x p /= 0]
                      where (h, t) = span (< p*p) xs

isPrime :: Int -> Bool
isPrime n | n < 1 = False
          | otherwise = not $ or [n `rem` x == 0 | x <- [2..floor $ sqrt $ fromIntegral n]]

consecutive :: Int -> [Int]
consecutive p = dropWhile (not . isPrime) $ reverse sums where
    sums = takeWhile (< 1000000) $ scanl1 (+) $ dropWhile (< p) primes

main :: IO ()
main = print $ head $ maximumBy (compare `on` length) $ map consecutive $ take 10 primes
