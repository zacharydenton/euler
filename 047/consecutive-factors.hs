import Data.List (nub)

primes :: [Int]
primes = 2 : sieve primes [3,5..] where
    sieve (p:ps) xs = h ++ sieve ps [x | x <- t, rem x p /= 0]
                      where (h, t) = span (< p*p) xs

factorize :: Int -> [Int]
factorize n = primeFactors n primes where
    primeFactors 1 _ = []
    primeFactors _ [] = []
    primeFactors m (p:ps) | m < p * p = [m]
                          | r == 0 = p : primeFactors q (p:ps)
                          | otherwise = primeFactors m ps
                          where (q, r) = quotRem m p

uniqueFactors :: Int -> Int
uniqueFactors = length . nub . factorize

chunks :: Int -> [a] -> [[a]]
chunks n l | length chunk < n = []
           | otherwise = chunk : chunks n (tail l)
           where chunk = take n l

candidates :: [[Int]]
candidates = [cons | cons <- chunks 4 [1..], all ((== 4) . uniqueFactors) cons]

main :: IO ()
main = print $ head $ head candidates
