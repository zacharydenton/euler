cycles :: Eq a => [a] -> [[a]]
cycles xs = map fst $ dropWhile (\(a, b) -> a ++ a /= b) $ zip cs (tail cs)
    where cs = [left | n <- [1..], let (left, right) = splitAt n xs, left == take n right]

isSquare :: Int -> Bool
isSquare n = root == fromIntegral (round root)
    where root = sqrt (fromIntegral n)

isPrime :: Int -> Bool
isPrime n | n < 1 = False
          | otherwise = not $ or [n `rem` x == 0 | x <- [2..floor $ sqrt $ fromIntegral n]]

expansion :: Int -> [Int]
expansion s | isSquare s = []
            | isSquare (s-1) = [fromIntegral $ 2 * (floor $ sqrt $ fromIntegral (s-1))]
            | otherwise = head $ dropWhile (all (== first)) cs
            where cs = cycles $ map a [1..]
                  first = (head . head) cs
                  m = (map m' [0..] !!)
                  m' 0 = 0
                  m' n = (d (n-1))*(a (n-1)) - (m (n-1))
                  d = (map d' [0..] !!)
                  d' 0 = 1
                  d' n = (s - (m n)^2) `quot` (d (n-1))
                  a = (map a' [0..] !!)
                  a' 0 = floor $ sqrt $ fromIntegral s
                  a' n = floor $ (fromIntegral ((a 0) + (m n))) / (fromIntegral (d n))

main :: IO ()
main = print $ length $ filter (\x -> odd $ length $ expansion x) [2..10000]
