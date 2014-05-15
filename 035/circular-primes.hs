import Data.List (union)

pairwise :: (a -> a -> a) -> [a] -> [a]
pairwise f (xs:ys:t) = f xs ys : pairwise f t
pairwise _ t = t

primes :: [Integer]
primes = 2 : _Y ((3 :) . gaps 5 . _U . map (\p-> [p*p, p*p+2*p..]))
    where
        _Y g = g (_Y g)                      -- recursion, Y combinator
        _U ((x:xs):t) = x : (union xs . _U . pairwise union) t   -- ~= nub.sort.concat
        gaps k s@(x:xs) 
            | k < x     = k : gaps (k+2) s    -- ~= [k,k+2..]\\s, when
            | otherwise =     gaps (k+2) xs   --  k <= head s && null(s\\[k,k+2..])

rotate :: [a] -> [a]
rotate [] = []
rotate (x:xs) = xs ++ [x]

rotations :: [a] -> [[a]]
rotations x = take n (iterate rotate x)
    where n = length x

intRotations :: Integer -> [Integer]
intRotations = map read . rotations . show

prime :: Integer -> Bool
prime n = n > 1 && foldr (\p r -> p*p > n || ((n `rem` p) /= 0 && r)) True primes

circular :: Integer -> Bool
circular = all prime . intRotations

candidate :: Integer -> Bool
candidate n | n < 10 = True
            | otherwise = all (`elem` "1379") (show n)

main :: IO ()
main = print $ length . filter circular $ filter candidate $ takeWhile (< 1000000) primes
