import Data.Ratio (denominator)

fraction :: Int -> Int -> Rational
fraction n d = fromIntegral n / fromIntegral d

curious :: Int -> Int -> Bool
curious n d | f > 1 = False
            | d1 == 0 || d2 == 0 = False
            | n == d = False
            | n2 /= d1 = False
            | otherwise = fraction n1 d2 == f
            where f = fraction n d
                  (n1, n2) = quotRem n 10
                  (d1, d2) = quotRem d 10

main :: IO ()
main = print $ denominator $ product [fraction n d | n <- [10..99], d <- [10..99], curious n d]
