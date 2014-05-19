lastN :: Int -> [a] -> [a]
lastN n xs = foldl (const . drop 1) xs (drop n xs)

main :: IO ()
main = putStrLn $ lastN 10 $ show $ sum [x^x | x <- [1..1000]]
