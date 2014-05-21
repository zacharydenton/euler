import Data.Function (on)
import Data.List (maximumBy)

isInteger :: Double -> Bool
isInteger f = f - (fromIntegral (floor f)) < 0.0000001

isSquare :: Integer -> Bool
isSquare n = isInteger (sqrt $ fromIntegral n)

rationalize :: [Integer] -> (Integer, Integer)
rationalize = foldr (\x (n, d) -> (x*n + d, n)) (1, 0)

convergents :: Integer -> [Integer]
convergents s | isSquare s = []
              | isSquare (s-1) = (a 0) : repeat (fromIntegral $ 2 * (floor $ sqrt $ fromIntegral (s-1)))
              | otherwise = map a [0..]
              where m = (map m' [0..] !!)
                    m' 0 = 0
                    m' n = (d (n-1))*(a (n-1)) - (m (n-1))
                    d = (map d' [0..] !!)
                    d' 0 = 1
                    d' n = (s - (m n)^2) `quot` (d (n-1))
                    a = (map a' [0..] !!)
                    a' 0 = floor $ sqrt $ fromIntegral s
                    a' n = floor $ (fromIntegral ((a 0) + (m n))) / (fromIntegral (d n))

solve :: Integer -> Integer
solve d = head $ [x | n <- [1..], let (x, y) = rationalize $ take n $ convergents d, x^2 - d*y^2 == 1]

main :: IO ()
main = print $ maximumBy (compare `on` solve) $ [1..1000]
