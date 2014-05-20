palindrome :: String -> Bool
palindrome s = s == reverse s

lychrel :: Int -> Bool
lychrel n = not $ any palindrome $ take 50 $ tail (iterate (\x -> show $ (read x) + (read $ reverse x)) (show n))

main :: IO ()
main = print $ length $ filter lychrel [1..10000]
