import Data.List (tails, transpose)

parse :: String -> [[Int]]
parse = map (map read . words) . lines

chunks :: Int -> [a] -> [[a]]
chunks n l | length chunk < n = []
           | otherwise = chunk : chunks n (tail l)
           where chunk = take n l

horizontal :: [[Int]] -> [[Int]]
horizontal = concatMap (chunks 4)

vertical :: [[Int]] -> [[Int]]
vertical = horizontal . transpose

diagonal :: [[Int]] -> [[Int]]
diagonal = vertical . zipWith drop [0..]

southEast :: [[Int]] -> [[Int]]
southEast = concatMap diagonal . tails

southWest :: [[Int]] -> [[Int]]
southWest = southEast . map reverse

largestProduct :: [[Int]] -> Int
largestProduct = maximum . map product

main :: IO ()
main = do
        str <- readFile "/home/zach/code/euler/011/grid.txt"
        let grid = parse str
        print $ largestProduct $ concatMap ($grid) [horizontal, vertical, southEast, southWest]

