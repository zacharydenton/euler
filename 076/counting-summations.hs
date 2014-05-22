import Data.Array

change :: Integer -> Integer -> Integer
change t c = cache ! (t, c) where
    cache = array ((0, 0), (t, c)) [((i, j), f i j) | i <- [0..t], j <- [0..c]]
    f _ 1 = 1
    f t' c' = sum [cache ! (t' - i*c', c' - 1) | i <- [0..t' `quot` c']]

main :: IO ()
main = print $ change 100 99
