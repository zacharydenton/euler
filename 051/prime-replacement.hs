import Data.List (sort, group)

primes :: [Int]
primes = 2 : sieve primes [3,5..] where
    sieve (p:ps) xs = h ++ sieve ps [x | x <- t, rem x p /= 0]
                      where (h, t) = span (< p*p) xs

isPrime :: Int -> Bool
isPrime n | n < 1 = False
          | otherwise = not $ or [n `rem` x == 0 | x <- [2..floor $ sqrt $ fromIntegral n]]

groupFrequency :: Ord a => [a] -> [(Int, a)]
groupFrequency xs = reverse $ sort [(length cs, head cs) | cs <- group $ sort xs]

candidates :: [(Char, String)]
candidates = [(snd $ head g, s) | p <- primes,
                                  let s = show p,
                                  let g = groupFrequency s,
                                  any ((== 3) . fst) g]

replace :: Eq a => a -> a -> [a] -> [a]
replace old new = foldr (\x acc -> (if x == old then new else x) : acc) []

expand :: (Char, String) -> [String]
expand (d, ds) = [new | n <- ['1'..'9'], let new = replace d n ds, isPrime (read new)]

main :: IO ()
main = putStrLn $ snd . head $ filter ((== 8) . length . expand) candidates
