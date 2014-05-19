import Data.List (permutations)

isPrime :: Int -> Bool
isPrime n | n <= 1 = False
          | otherwise = not $ or [n `rem` x == 0 | x <- [2..floor $ sqrt $ fromIntegral n]]

candidates :: [Int]
candidates = filter isPrime $ concatMap (\n -> map (read . concatMap show) $ permutations [1..n]) [1..7]

main :: IO ()
main = print $ maximum candidates
