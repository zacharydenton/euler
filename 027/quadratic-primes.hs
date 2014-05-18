import Data.Function (on)
import Data.List (maximumBy)

isPrime :: Int -> Bool
isPrime n | n < 1 = False
          | otherwise = not $ or [n `rem` x == 0 | x <- [2..floor $ sqrt $ fromIntegral n]]
 
coefficients :: [(Int, Int)]
coefficients = [(a, b) | a <- [-999..999], b <- filter isPrime [0..999]]

primesProduced :: (Int, Int) -> Int
primesProduced (a, b) = length $ takeWhile isPrime [n^2 + a*n + b | n <- [0..]]

main :: IO ()
main = print $ uncurry (*) $ maximumBy (compare `on` primesProduced) coefficients
