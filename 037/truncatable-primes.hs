isPrime :: Int -> Bool
isPrime n | n <= 1 = False
          | otherwise = not $ or [n `rem` x == 0 | x <- [2..floor $ sqrt $ fromIntegral n]]

expand :: [Int] -> [Int]
expand ns = [p | n <- ns, k <- [1, 3, 7, 9], let p = 10*n + k, isPrime p]

candidates :: [Int]
candidates = dropWhile (< 10) $ concat $ takeWhile (not . null) (iterate expand [2, 3, 5, 7])

leftTruncatable :: Int -> Bool
leftTruncatable n = all isPrime $ takeWhile (< n) [n `rem` 10^x | x <- [1..]]

main :: IO ()
main = print $ sum $ filter leftTruncatable candidates
