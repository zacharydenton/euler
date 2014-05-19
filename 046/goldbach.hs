isPrime :: Integer -> Bool
isPrime n | n < 1 = False
          | otherwise = not $ or [n `rem` x == 0 | x <- [2..floor $ sqrt $ fromIntegral n]]

isSum :: Integer -> Bool
isSum n = any isPrime [n - 2*s^2 | s <- [0..floor $ sqrt $ fromInteger n]]

candidates :: [Integer]
candidates = [n | n <- [1,3..], not (isPrime n), not (isSum n)]

main :: IO ()
main = print $ head candidates
