primes :: [Int]
primes = 2 : sieve primes [3,5..] where
    sieve (p:ps) xs = h ++ sieve ps [x | x <- t, rem x p /= 0]
                      where (h, t) = span (< p*p) xs

isPrime :: Int -> Bool
isPrime n | n < 1 = False
          | otherwise = not $ or [n `rem` x == 0 | x <- [2..floor $ sqrt $ fromIntegral n]]

filterPairs :: Int -> [Int] -> [Int]
filterPairs p = filter test where
    test x = isPrime (read $ show x ++ show p) && isPrime (read $ show p ++ show x)

candidates :: [[Int]]
candidates = [[a, b, c, d, e] | a <- primes',
                                let bs = filterPairs a $ dropWhile (<= a) primes',
                                b <- bs,
                                let cs = filterPairs b $ dropWhile (<= b) bs,
                                c <- cs,
                                let ds = filterPairs c $ dropWhile (<= c) cs,
                                d <- ds,
                                let es = filterPairs d $ dropWhile (<= d) ds,
                                e <- es]
    where primes' = takeWhile (< 10000) primes

main :: IO ()
main = print $ sum $ head candidates
