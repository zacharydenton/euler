parse :: String -> [Int]
parse = map (read . return) . concat . lines

chunks :: Int -> [a] -> [[a]]
chunks n l | length chunk < n = []
           | otherwise = chunk : chunks n (tail l)
           where chunk = take n l

largestProduct :: [[Int]] -> Int
largestProduct = maximum . map product

main :: IO ()
main = do
        str <- readFile "/home/zach/code/euler/008/numbers.txt"
        print $ largestProduct $ chunks 13 $ parse str
