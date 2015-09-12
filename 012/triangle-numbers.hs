import Data.List (group)

triangles :: [Int]
triangles = scanl1 (+) [1..]

primes :: [Int]
primes = sieve [2..] where
    sieve [] = []
    sieve (p:xs) = p : sieve [x | x <- xs, x `mod` p > 0]

factorize :: Int -> [Int]
factorize n = primeFactors n primes where
    primeFactors 1 _ = []
    primeFactors _ [] = []
    primeFactors m (p:ps) | m < p * p = [m]
                          | r == 0 = p : primeFactors q (p:ps)
                          | otherwise = primeFactors m ps
                          where (q, r) = quotRem m p

primePowers :: Int -> [(Int, Int)]
primePowers n = [(head x, length x) | x <- group $ factorize n]

numDivisors :: Int ->  Int
numDivisors n = product [k + 1 | (_, k) <- primePowers n]

main :: IO ()
main = print $ head $ dropWhile (\n -> numDivisors n <= 500) triangles
