import Data.Array
import Data.List (sort)

pentagonals :: [Integer]
pentagonals = sort [n*(3*n - 1) `quot` 2 | n <- [-250..250], n /= 0]

cache :: Array Integer Integer
cache = array (0, 100000) [(x, partition x) | x <- [0..100000]]

partition :: Integer -> Integer
partition n | n <= 1 = 1
            | otherwise = sum [s * (cache ! (n - p)) | (s, p) <- zip (cycle [1, 1, -1, -1]) (takeWhile (<= n) pentagonals)]

main :: IO ()
main = print $ head [i | (i, p) <- assocs cache, p `rem` 1000000 == 0]
