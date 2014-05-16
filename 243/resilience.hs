import Data.List (union)
import qualified Data.Set as Set

pairwise :: (a -> a -> a) -> [a] -> [a]
pairwise f (xs:ys:t) = f xs ys : pairwise f t
pairwise _ t = t

primes :: [Int]
primes = 2 : _Y ((3 :) . gaps 5 . _U . map (\p-> [p*p, p*p+2*p..]))
    where
        _Y g = g (_Y g)                      -- recursion, Y combinator
        _U ((x:xs):t) = x : (union xs . _U . pairwise union) t   -- ~= nub.sort.concat
        gaps k s@(x:xs) 
            | k < x     = k : gaps (k+2) s    -- ~= [k,k+2..]\\s, when
            | otherwise =     gaps (k+2) xs   --  k <= head s && null(s\\[k,k+2..])

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

totient :: Int -> Double
totient 1 = 1.0
totient n = (fromIntegral n) * product [1.0 - (1.0 / (fromIntegral p)) | p <- uniq $ factorize n]

resilience :: Int -> Double
resilience d = (totient d) / (fromIntegral (d - 1))

primorials :: [Int]
primorials = scanl1 (*) primes

candidates :: [Int]
candidates = expand 1 primorials where
    expand m ps@(x:y:_) | m * x < y = m * x : expand (m+1) ps
                        | otherwise = expand 1 (tail ps)

main :: IO ()
main = print $ head [d | d <- candidates, resilience d < 15499 / 94744]
