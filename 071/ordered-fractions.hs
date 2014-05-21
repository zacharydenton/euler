prevFrac :: Int -> Int -> Int -> (Int, Int)
prevFrac num den limit = inner 1 limit 1 where
    inner n d i | i == limit = (n, d)
                | den*m < num*i && m*d > n*i = inner m i (i+1)
                | otherwise = inner n d (i+1)
                where m = num*i `quot` den

main :: IO ()
main = print $ fst $ prevFrac 3 7 1000000
