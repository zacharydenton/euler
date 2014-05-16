import Data.List (maximumBy)
import Data.Function (on)

cycleLength :: Integer -> Integer
cycleLength n | even n = 0
              | n `rem` 5 == 0 = 0
              | otherwise = head [p | p <- [1..], (10^p - 1) `rem` n == 0]

main :: IO ()
main = print $ maximumBy (compare `on` cycleLength) [1,3..1000]
