import qualified Data.Set as Set

minus :: [Int] -> [Int] -> [Int]
minus xs@(x:xt) ys@(y:yt) = case compare x y of
    LT -> x : minus xt ys
    EQ ->     minus xt yt
    GT ->     minus xs yt
minus a         _         = a

union :: [Int] -> [Int] -> [Int]
union xs@(x:xt) ys@(y:yt) = case compare x y of
    LT -> x : union xt ys
    EQ -> x : union xt yt
    GT -> y : union xs yt
union a         []        = a
union []        b         = b

uniq :: Ord a => [a] -> [a]
uniq xs = uniq' Set.empty xs where
    uniq' _ [] = []
    uniq' set (y:ys) | Set.member y set = uniq' set ys
                     | otherwise = y : uniq' (Set.insert y set) xs

primes :: [Int]
primes = 2:3:5:7: gaps 11 wheel (fold3t $ roll 11 wheel primes_)
 where
   primes_ = 11: gaps 13 (tail wheel) (fold3t $ roll 11 wheel primes_)     -- separate feed
   fold3t ((x:xs): ~(ys:zs:t)) = x : union xs (union ys zs)
                                      `union` fold3t (pairs t)              -- fold3t: 5% ~ 10% speedup
   pairs ((x:xs):ys:t)         = (x : union xs ys) : pairs t
   wheel = 2:4:2:4:6:2:6:4:2:4:6:6:2:6:4:2:6:4:6:8:4:2:4:2:
           4:8:6:4:6:2:4:6:2:6:6:4:2:4:6:2:6:4:2:4:2:10:2:10:wheel
   gaps k ws@(w:t) cs@ ~(c:u) | k==c  = gaps (k+w) t u              -- (*  better fold, w/ Wheel!   *)
                              | True  = k : gaps (k+w) t cs
   roll k ws@(w:t) ps@ ~(p:u) | k==p  = scanl (\c d->c+p*d) (p*p) ws
                                          : roll (k+w) t u
                              | True  = roll (k+w) t ps

factorize :: Int -> [Int]
factorize n = primeFactors n primes where
    primeFactors 1 _ = []
    primeFactors _ [] = []
    primeFactors m (p:ps) | m < p * p = [m]
                          | r == 0 = p : primeFactors q (p:ps)
                          | otherwise = primeFactors m ps
                          where (q, r) = quotRem m p

totient :: Int -> Double
totient 1 = 1.0
totient n = (fromIntegral n) * product [1.0 - (1.0 / (fromIntegral p)) | p <- uniq $ factorize n]

main :: IO ()
main = print $ snd $ maximum [((fromIntegral n) / (totient n), n) | n <- [1..1000000]]
