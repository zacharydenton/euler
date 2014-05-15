primes :: [Integer]
primes = 2 : sieve primes [3,5..] where
    sieve (p:ps) xs = h ++ sieve ps [x | x <- t, rem x p /= 0]
                      where (h, t) = span (< p*p) xs

main :: IO ()
main = print $ sum $ takeWhile (< 2000000) primes
