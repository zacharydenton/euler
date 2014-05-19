import Data.Function (on)
import Data.List (maximumBy)

solutions :: Int -> [(Int, Int, Int)]
solutions p = [(a, b, c) | a <- [1..p `quot` 4],
                           let b = (p * (p - 2*a)) `quot` (2 * (p - a)),
                           let c = floor $ sqrt $ fromIntegral (a^2 + b^2),
                           a + b + c == p]

main :: IO ()
main = print $ maximumBy (compare `on` (length . solutions)) [2,4..1000]
