primes :: [Int]
primes = 2 : sieve primes [3,5..] where
    sieve (p:ps) xs = h ++ sieve ps [x | x <- t, rem x p /= 0]
                      where (h, t) = span (< p*p) xs

primePartition :: Int -> Int
primePartition = p primes where
    p _ 0 = 1
    p ks'@(k:ks) m = if m < k then 0 else p ks' (m - k) + p ks m

main :: IO ()
main = print $ fst $ head $ dropWhile ((<= 5000) . snd) [(n, primePartition n) | n <- [1..]]
