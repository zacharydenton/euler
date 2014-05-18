palindrome :: Eq a => [a] -> Bool
palindrome s = s == reverse s

digits :: Int -> Int -> [Int]
digits _ 0 = []
digits base n = r : digits base q
    where (q, r) = quotRem n base

main :: IO ()
main = print $ sum [n | n <- [1..1000000], all palindrome [digits 10 n, digits 2 n]]
