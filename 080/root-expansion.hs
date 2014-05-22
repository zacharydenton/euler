isqrt :: Integer -> Integer
isqrt 0 = 0
isqrt 1 = 1
isqrt n = head $ dropWhile (\x -> x*x > n) $ iterate (\x -> (x + n `div` x) `div` 2) (n `div` 2)

digits :: Integer -> [Integer]
digits = map (read . return) . show

sqrtDigits :: Integer -> Integer -> [Integer]
sqrtDigits count x = digits $ isqrt $ x*(10^(2*count))

isSquare :: Integer -> Bool
isSquare n = root * root == n
    where root = round $ sqrt $ fromIntegral n

main :: IO ()
main = print $ sum $ concat [ds | n <- [1..99], not $ isSquare n, let ds = sqrtDigits 99 n]
