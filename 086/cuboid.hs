isSquare :: Int -> Bool
isSquare x = let x' = truncate $ sqrt (fromIntegral x :: Double) in x'*x' == x

solutions :: Int -> Int
solutions m = length [1 | a <- [1..m], b <- [a..m], isSquare((a + b)^2 + m^2)]

main :: IO ()
main = print $ length $ takeWhile (<= 1000000) $ scanl1 (+) $ map solutions [0..]
