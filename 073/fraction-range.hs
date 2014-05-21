import qualified Data.Set as Set

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

uniq :: Ord a => [a] -> [a]
uniq xs = uniq' Set.empty xs where
    uniq' _ [] = []
    uniq' set (y:ys) | Set.member y set = uniq' set ys
                     | otherwise = y : uniq' (Set.insert y set) xs

mobius :: Int -> Int
mobius n | not squarefree = 0
         | otherwise = (-1)^r
         where factors = factorize n
               uniqFactors = uniq factors
               r = length uniqFactors
               squarefree = r == length factors

f :: Int -> Int
f m = sum [((n - 1) `quot` 2) - (n `quot` 3) | n <- [1..m]]

r :: Int -> Int
r limit = sum [(mobius m) * f (limit `quot` m) | m <- [1..limit]]

main :: IO ()
main = print $ r 12000
